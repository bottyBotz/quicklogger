from setuptools import setup, find_packages

setup(
    name="quicklogger",
    version="0.1.0",
    description="A simple and quick logger setup for Python projects",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/quicklogger",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, e.g.:
        # "requests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
