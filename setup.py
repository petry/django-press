import re
from setuptools import setup, find_packages, findall

version = __import__('publish').__version__


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)
    return requirements


def not_py(file_path):
    return not (file_path.endswith('.py') or file_path.endswith('.pyc'))


core_packages = find_packages()
core_package_data = {}
for package in core_packages:
    package_path = package.replace('.', '/')
    core_package_data[package] = filter(not_py, findall(package_path))

download_url = 'https://github.com/johnsensible/django-publish/archive/v%s.zip#egg=django-publish-%s' % (
    version, version
)

setup(
    name='django-publish',
    version=version,
    description='Handy mixin/abstract class for providing a "publisher workflow" to arbitrary Django models.',
    long_description=open('README.rst').read(),
    author='John Montgomery',
    author_email='john@sensibledevelopment.com',
    url='http://github.com/johnsensible/django-publish',
    download_url=download_url,
    license='BSD',
    packages=core_packages,
    package_data=core_package_data,
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=parse_requirements('requirements.txt'),
    setup_requires=parse_requirements('requirements_test.txt')
)
