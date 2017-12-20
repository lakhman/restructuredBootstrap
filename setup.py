# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
LICENSE = open(os.path.join(here, 'LICENSE')).read()

# rm -rf *.egg-info dist/* && python setup.py sdist
# pip install dist/restructuredBootstrap-0.1.0.tar.gz
# twine upload --repository pypi dist/*
# twine upload --repository pypitest dist/*
setup(
    name='restructuredBootstrap',
    version='1.0.0',
    description="Twitter Bootstrap 3 directives for use with Sphinx.",
    keywords=['sphinx', 'bootstrap', 'restructuredText'],
    author='Anil Lakhman',
    author_email='restructured.bootstrap@anil.io',
    url='https://github.com/lakhman/restructuredBootstrap',
    long_description=README,
    license=LICENSE,
    packages=find_packages('.', exclude=['tests']),
    package_dir={
        'roles': 'restructuredBootstrap',
    },
    data_files=[("", ["LICENSE"])],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'Sphinx >= 1.4', 'six'],
    entry_points={},
    test_suite='tests',
    tests_require=['sphinx-testing'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Documentation',
        'Framework :: Sphinx',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
