import setuptools

setuptools.setup(
    name="MSPCRunnerDAG",
    packages=setuptools.find_packages(exclude=["MSPCRunnerDAG_tests"]),
    install_requires=[
        "dagster==0.13.2",
        "dagit==0.13.2",
        "pytest",
    ],
)
