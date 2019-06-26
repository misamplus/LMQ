from setuptools import setup
import re


with open('README.md') as f:
    long_description = f.read()

with open('python_library/LMQ/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(
    name='LMQ',
    version=version,
    packages=['LMQ'],
	package_dir={'libs/python': 'LMQ'}
    description='Lightweight Message Queue',
    long_description=long_description,
    author='Misam saki',
    author_email='misamplus@gmail.com',
    url='https://gitlab.ygraphy.ir/misam/LMQ',
    install_requires=['requests'],
    license='Proprietary',
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
    ]
)
