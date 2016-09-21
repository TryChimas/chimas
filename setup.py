from setuptools import setup

setup(
    name='chimas',
    version='0.1',
    py_modules=['chimas_server0'],
    #install_requires=[
    #    'Click',
    #],
    entry_points='''
        [console_scripts]
        chimas=app:__main__
    ''',
)
