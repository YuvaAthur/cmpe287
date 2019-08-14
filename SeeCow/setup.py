import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='seecow',
    version='1.0.0',
    url='http://flask.pocoo.org/docs/tutorial/',
    license='BSD',
    maintainer='Pallets team',
    maintainer_email='yuva.athur@sjsu.edu',
    description='SeeCow application based on basic blog app built in the Flask tutorial.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_login',
        'werkzeug.security',
        'flask_restful',
        'json',
        'sys',
        'sqlite3',
        'flask_sqlalchemy',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)