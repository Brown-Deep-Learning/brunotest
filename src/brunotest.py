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


def import_solution(package_name: str, import_name: str):
    """
    Import a solution's module and return it.
    Must be compatible with how this works on gradescopes end.
    """

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the directory of the solution's file
    solution_dir = os.path.join(current_dir, "solutions", package_name)

    # Add the solution's directory to the path
    sys.path.append(solution_dir)

    # Import the solution's module
    solution_module = importlib.import_module(import_name)

    # Remove the solution's directory from the path
    sys.path.remove(solution_dir)

    return solution_module


def remove_all(path: str) -> None:
    """
    Removes all files and directories in the given path.
    """
    # Get a list of all files and directories in the path
    files = os.listdir(path)

    # Iterate through the list of files and directories
    for file in files:
        # Get the full path of the file or directory
        full_path = os.path.join(path, file)

        # If the file or directory is a directory
        if os.path.isdir(full_path):
            # Remove the directory
            os.rmdir(full_path)

        # If the file or directory is a file
        else:
            # Remove the file
            os.remove(full_path)


def enter_brunotest_dir():
    """
    Makes a directory called `__brunotest__` in the current working directory and enters it.
    """
    # Make a directory in the current working directory called __brunotest__

    # Enter the directory
    if not os.path.isdir("__brunotest__"):
        os.mkdir("__brunotest__")

    # Remove any existing files in the directory
    remove_all("__brunotest__")

    os.chdir("__brunotest__")


def cleanup_brunotest_dir():
    """
    Deletes the `__brunotest__` directory in the current working directory.
    """
    # Delete the directory
    # Assumes that we are currently in the __brunptest__ directory

    os.chdir("..")
    remove_all("__brunotest__")


def run_brunotest(directory: str, args: list[str]) -> None:
    """
    The core of brunotest. Runs all tests in the current working directory.
    Includes compiling all version of the stencil code as specified in `args`.
    """

    enter_brunotest_dir()

    try:
        pass

    except Exception as e:
        cleanup_brunotest_dir()
