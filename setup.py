from setuptools import setup, find_packages

INSTALL_REQUIRES = ['pytest',
                    'requests',
                    'beautifulsoup4',
                    'tqdm',
                    'pytz']

setup(
    name='cloud-city',
    version='0.0.1',
    url='https://github.com/LEGO-Han-Solo/cloud-city',
    author='LEGO Han Solo',
    author_email='lego.han.solo.69@gmail.com',
    description='LEGO Search Engine',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
)
