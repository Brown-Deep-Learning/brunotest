import importlib
import os
import sys
import click
import shutil
import pytest
from core import compiler

BRUNOTEST_DIR = "__brunotest__"


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
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

    # os.rmdir(path)


def create_brunotest_dir():
    """
    Makes a directory called `__brunotest__` in the current working directory and enters it.
    """
    # Make a directory in the current working directory called __brunotest__

    # Enter the directory
    if not os.path.isdir(BRUNOTEST_DIR):
        os.mkdir(BRUNOTEST_DIR)

    # Remove any existing files in the directory
    remove_all(BRUNOTEST_DIR)


def cleanup_brunotest_dir():
    """
    Deletes the `__brunotest__` directory in the current working directory.
    """
    # Delete the directory

    remove_all(BRUNOTEST_DIR)


def find_stencil(directory: str) -> str:
    """
    Attempts to find the stencil file in the main root of the directory.
    """
    entries = os.listdir(directory)
    stencil_entries = [entry for entry in entries if entry.endswith(".stencil")]

    if len(stencil_entries) == 0:
        raise Exception("No stencil file found in the root of the directory.")
    elif len(stencil_entries) > 1:
        raise Exception("Multiple stencil files found in the root of the directory.")

    return os.path.join(directory, stencil_entries[0])


def find_chaff_paths(directory: str) -> list[str]:
    """
    Iterates through the entire subdirectory to find all chaff files.
    """
    chaff_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".chaff"):
                chaff_paths.append(os.path.join(root, file))

    return chaff_paths


def compile_to_directory(
    code_path: str, chaff_path: str, output_directory: str
) -> None:
    """
    Compiles all of the template files from `code_path` to the specified output directory.
    Should maintain folder structure and walk through all subdirectories
    """
    chaff_replacements = compiler.read_chaff_file(chaff_path)

    for root, dirs, files in os.walk(code_path):
        for dir in dirs:
            # Make the directory in the output directory
            os.mkdir(os.path.join(output_directory, dir))
        for file in files:
            compiler.compile_file(
                os.path.join(root, file),
                os.path.join(output_directory, file),
                chaff_replacements,
            )


@click.command()
@click.argument("chaffs", nargs=-1)
@click.option("--directory", "--dir", "-d", type=click.Path(exists=True))
@click.option(
    "compile_dir",
    "-c",
    type=click.Path(),
    help="The directory to compile and output the results to",
)
def brunotest(
    chaffs: list[str],
    directory: str,
    compile_dir: str | None,
):
    """
    The entry point for the brunotest command line executable.
    """

    stencil_path = find_stencil(directory)
    chaff_paths = find_chaff_paths(directory)
    chaff_names = [
        os.path.basename(chaff_path).split(".")[0] for chaff_path in chaff_paths
    ]
    chaff_path_name = list(zip(chaff_paths, chaff_names)) + [(stencil_path, "stencil")]

    # Select only the chaffs we have in chaffs
    chaff_path_name = [
        (chaff_path, chaff_name)
        for chaff_path, chaff_name in chaff_path_name
        if (chaff_name in chaffs or "all" in chaffs)
    ]

    if len(chaff_path_name) == 0:
        raise Exception("No chaffs specified.")

    if compile_dir is not None:
        # Only compile the code, don't run any tests.
        # Compile all of the code to the paths specified in `chaffs`
        os.mkdir(compile_dir)
        for chaff_path, chaff_name in chaff_path_name:
            os.mkdir(os.path.join(compile_dir, chaff_name))
            compile_to_directory(
                os.path.join(directory, "code"),
                chaff_path,
                os.path.join(compile_dir, chaff_name),
            )

        click.echo(
            click.style(
                f"Compiled {len(chaff_path_name)} solutions to '{compile_dir}'",
                fg="green",
            )
        )
        return

    create_brunotest_dir()
    original_dir = os.path.abspath(os.getcwd())
    try:
        # Compile all of the specified chaffs to the testing directory
        for chaff_path, chaff_name in chaff_path_name:
            os.mkdir(os.path.join(BRUNOTEST_DIR, chaff_name))
            compile_to_directory(
                os.path.join(directory, "code"),
                chaff_path,
                os.path.join(BRUNOTEST_DIR, chaff_name),
            )
            # Once it is compiled, run the tests.
            directory_absolute = os.path.abspath(directory)
            current_dir = os.path.abspath(os.getcwd())
            os.chdir(os.path.join(BRUNOTEST_DIR, chaff_name))
            result = pytest.main(
                ["-q", "--color=yes", os.path.join(directory_absolute, "tests")]
            )
            os.chdir(current_dir)
            print(result)
        cleanup_brunotest_dir()
    except Exception as e:
        os.chdir(original_dir)
        cleanup_brunotest_dir()
        raise e


if __name__ == "__main__":
    brunotest()
