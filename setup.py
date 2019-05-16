from setuptools import setup, find_packages
import sys, os

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README'), encoding='utf-8') as fh:
    long_description = fh.read()

version = '3.0.0.dev1'
setup(
    name='castro',
    version=version,
    description="Screencasting library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pyvnc2swf screencast video',
    author='Jason R. Huggins',
    author_email='jason@jrandolph.com',
    url='http://github.com/hugs/castro',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PyYAML>=5.1',
        'pygame>=2.0.0.dev1',
        'setuptools',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
