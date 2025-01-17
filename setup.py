import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-generators-latest',
    version='0.8.0',

    description='Generate DRF Serializers, Views, and urls for your API application.',
    long_description=README,

    url='https://github.com/SousaPedro11/drf-generators',
    download_url='https://github.com/SousaPedro11/drf-generators/archive/refs/tags/0.8.0.zip',
    author='Sousapedro11',
    author_email='ppls2106@gmail.com',

    license='MIT',

    packages=[
        'drf_generators',
        'drf_generators.templates',
        'drf_generators.management',
        'drf_generators.management.commands'
    ],
    include_package_data=True,
    install_requires=['Django>=1.11'],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
    ],

    keywords='API REST framework generate scaffold',
)
