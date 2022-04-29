import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ysmreg",
    version="0.0.1",
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'ycmd=ycmd:main',
        ],
    },
    author="ysmreg",
    author_email="ysmreg1@gmail.com",
    description="ycmd code runner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ysmservice/ycmd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
