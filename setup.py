from setuptools import setup

setup(
    name='tsv2csv',
    version='0.0.3',
    packages=['tsv2csv'],
    url='',
    license='',
    author='Henry Borchers',
    zip_safe=False,
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'tsv2csv = tsv2csv.__main__:main'
        ]
    }
)
