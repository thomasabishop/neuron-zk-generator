from setuptools import find_packages, setup

setup(
    name="neuron-zk-generator",
    version="0.1",
    py_modules=["app"],
    package_dir={"": "src"},
    install_requires=["termcolor", "pyinstaller"],
    entry_points={
        "console_scripts": [
            "neuron-zk-generator=app:main",
        ],
    },
)
