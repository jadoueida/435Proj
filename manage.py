#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    # Set the default port to 8000
    port = 8000

    # Check if a custom port is provided as a command-line argument
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        if len(sys.argv) > 2:
            arg = sys.argv[2]
            # Extract the port from the argument, assuming the format "0.0.0.0:8002"
            _, port_str = arg.split(":")
            port = int(port_str)

        # Modify sys.argv to include only 'runserver' and the extracted port
        sys.argv = ['manage.py', 'runserver', f'0.0.0.0:{port}']

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Run the server with the specified port
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



