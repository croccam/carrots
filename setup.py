from setuptools import setup
setup(name='carrots',
      version='0.1.12',
      description='Library to build RabbitMQ architectures like you were playing with lego blocks',
      url='http://github.com/croccam/carrots',
      author='Croccam',
      author_email='antcarri@gmail.com',
      license='MIT',
      install_requires=['pika'],
      packages=['carrots',
                'carrots.common'],
      zip_safe=False)