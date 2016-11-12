from setuptools import setup


setup(
    name='Flask-Color',
    version='0.2',
    url='https://github.com/maneyko/flask-color',
    license='MIT',
    author='maneyko',
    author_email='pmaneyko@gmail.com',
    description='flask-color is an extension for Flask that improves the built-in web server with colors when debugging.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
