import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agralogics",
    version="1.0.8",
    author="Agralogics",
    author_email="sumer.johal@agralogics.com",
    description="An Open Source Collection of Agronomic Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agralogics/weather-models",
    packages=setuptools.find_packages(),
    install_requires=[
        'python-dateutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
