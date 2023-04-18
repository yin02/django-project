#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

This script allows users to manage their Django projects by providing
a command-line interface for administrative tasks such as starting a
new app, running the development server, and more.
"""

import os
import sys

def main():
    """Set up the environment for a Django project and run management commands.
    
    This function sets the default value for the DJANGO_SETTINGS_MODULE
    environment variable, imports the execute_from_command_line function
    from Django's management module, and calls it with the command-line
    arguments.
    """

    # Set the default value for the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    
    try:
        # Import the execute_from_command_line function from Django's management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise a more informative error message if Django is not installed or available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # Call the execute_from_command_line function with the command-line arguments
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # If the script is being executed directly, call the main function
    main()
