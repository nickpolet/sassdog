from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='sassdog',
      version='0.1',
      description='Compiles .scss files into .css files when they are changed. Basically glues together watchdog and pyscss.',
      url='http://github.com/npolet/sassdog',
      author='Nick Polet',
      author_email='nickpolet@gmail.com',
      license='MIT',
      packages=['sassdog'],
      install_requires=[
          'watchdog',
          'pyscss',
          'colorama',
          'csscompressor',
      ],
      scripts=['bin/sassdog'],
      zip_safe=False)