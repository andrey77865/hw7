from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='1',
      description='Clean and sort files in folder',
      url='https://github.com/andrey77865/python-hw7',
      author='Andrey',
      author_email='andrey@example.com',
      license='MIT',
      packages=find_namespace_packages(),
          install_requires=['markdown'],
      entry_points={'console_scripts': [
          'clean-folder = clean_folder.clean:sorter']}
      )
