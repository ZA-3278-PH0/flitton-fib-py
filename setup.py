from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flitton_fib_py",
    version=("0.0.1"),
    author=("KKK"),
    author_email=("KKK@ggmail.com"),
    description="Calculates a Fibonacci number",
    long_description= long_description,
    url="...",
    install_requires=[],
    packages=find_packages(exlude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)