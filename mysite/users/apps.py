from django.apps import AppConfig

# The UsersConfig class configures the 'users' app for a Django project.
class UsersConfig(AppConfig):
    name = 'users'

    # The ready method is called by Django when the app is fully loaded and ready to use.
    def ready(self):
        # Import the 'users.signals' module to load and connect any signals defined for the 'users' app.
        import users.signals
