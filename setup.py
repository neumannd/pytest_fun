from __future__ import with_statement
import versioneer
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


def pip_requirements(fname='requirements.txt'):
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            reqs.append(line)
    return reqs


reqs = [line.strip() for line in open('requirements.txt')]


setup(
    name="pytest-fun",
    version=versioneer.get_version(),
    description="Pytest Training",
    long_description=readme(),
    license='Apache License 2.0',
    author="XXX",
    author_email="xxx@dkrz.de",
    url="https://github.com/neumannd/pytest_fun",
    packages=find_packages(),
    install_requires=pip_requirements(),
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering'
    ],
    cmdclass=versioneer.get_cmdclass(),
)