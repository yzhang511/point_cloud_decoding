from setuptools import setup

with open("requirements.txt") as f:
    require = [x.strip() for x in f.readlines() if not x.startswith("git+")]

setup(
    name="point_cloud",
    version="0.1",
    packages=["point_cloud"],
)

