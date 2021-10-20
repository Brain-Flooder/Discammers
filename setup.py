import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Discammers",
    version="0.0.1",
    author="Brain-Flooder",
    author_email="brainflooder9985@gmail.com",
    description="A small package for Discord's scammers API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Brain-Flooder/Discammers",
    project_urls={
        "Bug Tracker": "https://github.com/Brain-Flooder/Discammers/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)