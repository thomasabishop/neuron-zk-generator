from setuptools import setup, find_packages

setup(
    name="neuron-zk-generator",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["termcolor", "pyinstaller"],
    entry_points={
        "console_scripts": [
            "neuron-zk-generator=app:main",
        ],
    },
)
