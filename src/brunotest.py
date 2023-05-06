import importlib
import os
import sys

def import_student(package_name: str, import_name: str):
    """
    Import a student's module and return it.
    Must be compatible with how this works on gradescopes end.
    """

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the directory of the student's file
    student_dir = os.path.join(current_dir, package_name)

    # Add the student's directory to the path
    sys.path.append(student_dir)

    # Import the student's module
    student_module = importlib.import_module(import_name)

    # Remove the student's directory from the path
    sys.path.remove(student_dir)

    return student_module