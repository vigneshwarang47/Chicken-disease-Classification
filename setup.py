import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'Chicken-disease-Classification'
AUTHOR_USER_NAME = 'vigneshwarang47'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'vigneshwaran.g47@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app.",
    Long_description=long_description,
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
    
)