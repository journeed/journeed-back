import re
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from services.generator import CodeGenerator
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "email",
            "password"
        )

    # automatic function to receive the user
    def get_user(self):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        return authenticate(email=email, password=password)

    def validate(self, attrs):
        password = attrs.get("password")
        try:
            # getting the appropriate user for e-mail
            user = User.objects.get(email=attrs.get("email"))
        except:
            # error message when user does not exist
            raise serializers.ValidationError({"error": "Bu mail ilə hesab tapılmadı"})

        if not user.check_password(password):
            # checking the password and error message if it is wrong
            raise serializers.ValidationError({"error": "Şifrə yanlışdır"})

        if not user.is_active:
            # checking whether the account is active
            raise serializers.ValidationError({"error": "Hesab aktiv deyil"})

        return attrs

    def create(self, validated_data):
        # create method returns the user
        return self.get_user()

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # preparation and return of user tokens
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            "country",
            "mobile",
            "password",
            "password_confirm"
        )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        full_name = attrs.get("full_name").strip()
        phone_number = attrs.get("mobile")
        password_confirm = attrs.get("password_confirm")
        filter_name = r'^[a-zA-Z ]{1,30}$'

        # checking the existence of e-mail
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Bu mail artıq qeyydiyatdan keçmişdir"})

        # checking the existence of phone number
        if User.objects.filter(mobile=phone_number).exists():
            raise serializers.ValidationError({"error": "Bu nömrə artıq qeyydiyatdan keçmişdir"})

        # password related controls
        if not password == password_confirm:
            raise serializers.ValidationError({"error": "Şifrələr arasında ziddiyət var"})
        if len(password) < 8:
            raise serializers.ValidationError({"error": "Şifrənin uzunluğu 8 dən kiçik ola bilməz"})
        if not any(_.isdigit() for _ in password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})
        if not any(_.isupper() for _ in password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})

        # full name related control
        if len(full_name) < 5:
            raise serializers.ValidationError({"error": "Full name çox qısadır"})
        if not re.match(filter_name, full_name.lower()):
            raise serializers.ValidationError({"error": "Full name yalnız hərif və simvollardan ibarət ola bilər"})

        return attrs

    def create(self, validated_data):
        # creating a new user and storing the password encrypted
        password_confirm = validated_data.pop("password_confirm")
        user = User.objects.create(**validated_data)
        user.set_password(password_confirm)
        user.save()
        return user

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # preparation and return of user tokens
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    # to convert user id to uuid
    uuid = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "uuid"
        )

    def validate(self, attrs):
        email = attrs.get("email")

        try:
            # getting the appropriate user for e-mail
            user = User.objects.get(email=email)
        except:
            # error message when user does not exist
            raise serializers.ValidationError({"error": "Bu mailə bağlı heçbir hesab tapılmadı"})

        if not user.is_active:
            # checking whether the account is active
            raise serializers.ValidationError({"error": "Hesab aktiv deyil"})

        return attrs

    def get_uuid(self, obj):
        # to convert user id to uuid
        uuid = urlsafe_base64_encode(smart_bytes(obj.id))
        return uuid

    def create(self, validated_data):
        user = User.objects.get(email=validated_data.get("email"))
        # preparing a password reset code for the user
        user.activation_code = CodeGenerator().create_user_activation_code(model_=User, size=6)
        user.save()
        # send email to user
        send_mail(
            "JourNeed",
            f"Şifrə yeniləmə kodu: {user.activation_code[:3]}-{user.activation_code[3:]}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True
        )
        return user


class ResetPasswordCheckSerializer(serializers.ModelSerializer):
    activation_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "activation_code",
        )

    def validate(self, attrs):
        user = self.instance
        activation_code = attrs.get("activation_code")

        if not user.activation_code == activation_code:
            # user password reset code check
            raise serializers.ValidationError({"error": "Kod yanlışdır"})

        return attrs

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # to convert user id to uuid
        repr_["uuid"] = urlsafe_base64_encode(smart_bytes(instance.id))
        return repr_


class ResetPasswordCompleteSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    new_password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "new_password",
            "new_password_confirm"
        )

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")

        # password related controls
        if self.instance.check_password(new_password):
            raise serializers.ValidationError({"error": "Bu şifrəni artıq istifadə etmisiniz"})
        if not new_password == new_password_confirm:
            raise serializers.ValidationError({"error": "Şifrələr arasında ziddiyət var"})
        if len(new_password) < 8:
            raise serializers.ValidationError({"error": "Şifrənin uzunluğu 8 dən kiçik ola bilməz"})
        if not any(_.isdigit() for _ in new_password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})
        if not any(_.isupper() for _ in new_password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})

        return attrs

    def update(self, instance, validated_data):
        # storing the new password encrypted
        new_password = validated_data.get("new_password")
        user = self.instance
        user.set_password(new_password)
        # Resetting the user's activation code
        user.activation_code = None
        user.save()
        return user

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # preparation and return of user tokens
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    new_password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})
    new_password_confirm = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = (
            "email",
            "old_password",
            "new_password",
            "new_password_confirm"
        )
        extra_kwargs = {
            "email": {"read_only": True}
        }

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.get("old_password")
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")

        # password related controls
        if not user.check_password(old_password):
            raise serializers.ValidationError({"error": "Köhnə şifrə yanlışdır"})
        if user.check_password(new_password):
            raise serializers.ValidationError({"error": "Bu şifrəni artıq istifadə etmisiniz"})
        if len(new_password) < 8:
            raise serializers.ValidationError({"error": "Şifrənin uzunluğu 8 dən kiçik ola bilməz"})
        if not any(_.isdigit() for _ in new_password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})
        if not any(_.isupper() for _ in new_password):
            raise serializers.ValidationError({"error": "Şifrədə ən az bir rəqəm və bir böyük hərif olmalıdır"})
        if not new_password == new_password_confirm:
            raise serializers.ValidationError({"error": "Şifrələr arasında ziddiyət var"})
        return attrs

    def update(self, instance, validated_data):
        # storing the new password encrypted
        new_password = validated_data.get("new_password")
        instance.set_password(new_password)
        instance.save()
        return instance

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        # preparation and return of user tokens
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return repr_





