from setuptools import setup, find_packages

setup(
    name='userdb',
    version='0.1.0',
    url="https://github.com/shon/userdb",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
        ],
    include_package_data=True,
    description='User sessions [WIP]',
    long_description=open("README.rst").read(),
    packages=find_packages(),
    install_requires=[
        'redis'
      ],
    author='Shekhar Tiwatne',
    author_email='pythonic@gmail.com',
    license="http://www.opensource.org/licenses/mit-license.php",
    test_suite="tests",
    )
