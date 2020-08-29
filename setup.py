import setuptools
from setuptools import find_packages

build_version = "0.0.4"

if __name__ == "__main__":
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="mutcm", # Replace with your own username
        version=build_version,
        author="Muthupandian",
        author_email="contact@muthupandian.in",
        description="Support for devops",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/muthugit/tcm",
        # packages=setuptools.find_packages(),
        packages=['mutcm'],
        package_dir = {'mutcm': 'src'},
        project_urls={
            "Documentation": "https://mutcm.readthedocs.io/en/latest/",
            "Author": "https://muthupandian.in"
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )