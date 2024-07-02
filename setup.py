import setuptools  # Importing the setuptools library for packaging Python projects

# Reading the long description from the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Defining the version of the package
__version__ = "0.0.0"

# Defining some metadata for the package
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "imaadiiii"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "adityaraj006005@gmail.com"

# Setting up the package configuration
setuptools.setup(
    name=SRC_REPO,  # The name of the package
    version=__version__,  # The version of the package
    author=AUTHOR_USER_NAME,  # The author's username
    author_email=AUTHOR_EMAIL,  # The author's email
    description="A small python package for NLP app",  # A short description of the package
    long_description=long_description,  # A long description of the package read from README.md
    long_description_content="text/markdown",  # The format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # The URL of the project's GitHub repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for the project's bug tracker
    },
    package_dir={"": "src"},  # The directory where the packages are located
    packages=setuptools.find_packages(where="src")  # Automatically find packages in the specified directory
)

