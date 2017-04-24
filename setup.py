from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='carrots',
      version='0.1.11',
      description='Library to build RabbitMQ architectures like you were playing with lego blocks',
      url='http://github.com/croccam/carrots',
      author='Croccam',
      author_email='antcarri@gmail.com',
      license='MIT',
      install_requires=required,
      packages=['carrots',
                'carrots.common'],
      zip_safe=False)