from setuptools import find_packages, setup

setup(
    name='data-quality-rules',
    packages=find_packages(include = ['src', 'src.*']),
    include_package_data=True,    
    version='0.4.2',
    description='Data Quality Rules for Solvency 2 and FTK',
    author='DeNederlandscheBank',
    license='MIT/X',
    install_requires=[
		'jupyter',
		'pandas==1.1.4',
		'numpy==1.19.3',
		'lxml>=3.4.4',
		'cx_Freeze==6.1',
		'openpyxl==3.0.5',
		'isodate==0.5.4',
		'aniso8601',
		'regex==2018.08.29',
		'requests',
		'tqdm',
		'tabulate',
		'click',
		'python-dotenv>=0.5.1',
		'xlrd>=0.9.0',
		'dnb-arelle',
		'data-patterns',
		'tox==3.20.0'
    ]
)
