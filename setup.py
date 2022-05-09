from setuptools import setup, find_packages

setup(
    name='pyprofiler',
    version='0.1',
    license='MIT',
    author="Aulia R. Hanifan",
    author_email='auliarahman80@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/auliahanifan/pyprofiler',
    keywords='code profiler',
    install_requires=[
          'decorator',
      ],
)