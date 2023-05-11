from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="brunotest",
    version="0.1",
    author="Robert Scheidegger",
    author_email="robert_scheidegger@brown.edu",
    license="MIT",
    description="<short description for the tool>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<github url where the tool code will remain>",
    py_modules=["brunotest"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        cooltool=my_tool:cli
    """,
)
