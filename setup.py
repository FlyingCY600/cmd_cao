from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='cao',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cao=cao.cao:main',
        ],
    },
    install_requires=[
        'click',
        'requests',
        'pyyaml',
        'openai',
    ],
    author='FlyingCY',
    author_email='cyf6000@proton.me',
    description='CAO 命令行工具',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cao',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)