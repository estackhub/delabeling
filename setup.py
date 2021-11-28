from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in delabeling/__init__.py
from delabeling import __version__ as version

setup(
	name="delabeling",
	version=version,
	description="tailor fit",
	author="gross innovate and contributors",
	author_email="spryngmanaged@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
