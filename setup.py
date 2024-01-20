from setuptools import setup, find_packages

setup(
    name='clippy64',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
        'pyperclip'
    ],
    entry_points='''
        [console_scripts]
        clippy64=clippy64:cli
    '''
)