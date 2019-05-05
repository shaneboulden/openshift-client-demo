from setuptools import setup, find_packages

setup (
    name = 'ocd',
    version='0.1.0',
    description='OpenShift Client Demo',
    url='https://github.com/shaneboulden/openshift-client-demo',
    author='Shane Boulden',
    author_email='shane.boulden@gmail.com',
    keywords='openshift client api pods',
    include_package_data=True,
    packages=find_packages()
)
