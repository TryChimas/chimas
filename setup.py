from setuptools import setup

import time


version_counter = time.strftime("%Y%m%d%H%M%S")
# https://packaging.python.org/distributing/#setup-args

setup(
    name='chimas',
    version='0.0.6.dev{}'.format(version_counter),
    description='This is Chimas BBS server',
    url='https://github.com/TryChimas/chimas',
    author='Iacchus Mercurius',
    license='GNU GPL v.3',
    classifiers=[
        #https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='chimas bbs forum server',
    #packages=['chimas',''],
     #   '.' :'chimas'},
    #py_modules=['chimas/chimasapp'],
    #packages=['chimas', 'chimas.core'],
    packages=['chimas', 'chimas.core'],
    scripts=['chimas/chimasapp.py'],
    install_requires=[
        'configobj==5.0.6',
        'Flask==0.11.1',
        'Flask-SQLAlchemy==2.1',
        'marshmallow==2.10.0',
        'SQLAlchemy==1.0.15',
        ],

    #include_package_data = True,
    package_data={
        'chimas' : ['requirements.txt','etc/*'],
    },
    #package_dir={'' : '.', 'chimas.core' : 'core/'},
    #package_dir={'' : '.'},
    #py_modules=['chimas_server'],
    #install_requires=[
    #    'Click',
    #],
    entry_points='''
        [console_scripts]
        chimascli=chimasapp:run_chimas
        chimas-server=chimasapp:chimascli
    ''',
)
