from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    pass  # Тут можна додати додаткові поля, якщо потрібно


class LoginForm(AuthenticationForm):
    pass  # Кастомізуйте, якщо потрібно
