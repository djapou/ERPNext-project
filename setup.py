from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in warehouse_management_system/__init__.py
from warehouse_management_system import __version__ as version

setup(
	name="warehouse_management_system",
	version=version,
	description="Warehouse Management System",
	author="Afrikedge",
	author_email="arnold.djapou@afrikedge.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
