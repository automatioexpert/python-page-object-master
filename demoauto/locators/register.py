class RegistrationPage(object):
    """Represent registration page web element locators."""

    regis_txt: str = "//*[contains(text(), 'basic information')]"
    first_name: str = "//input[@name='firstName']"
    last_name: str = "//input[@name='lastName']"
    phone: str = "//input[@name='phone']"
    email: str = "//input[@name='email']"
    country: str = "//select[@name='country']"
    user_name: str = "//input[@name='userName']"
    password: str = "//input[@name='password']"
    confirm_password: str = "//input[@name='confirmPassword']"
    submit: str = "//input[@name='submit']"
    thank_you: str = "//*[contains(text(), 'Thank you for registering')]"
    post_user: str = "//*[contains(text(), 'Your user name is')]"
