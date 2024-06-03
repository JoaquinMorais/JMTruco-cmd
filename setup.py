from setuptools import setup

readme = open("./README.md","r")

setup(
    name='JMTrucoCmd',
    packages=['JMTrucoCmd'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Esta es la descripcion del truco',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Joaquin Morais',
    author_email='joaquinmoraislussary@gmail.com',
    url='https://github.com/JoaquinMorais/JMTrucoCmd', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/JoaquinMorais/JMTrucoCmd/tarball/v0.1', # Te lo explico a continuación
    keywords=['testing','logging','example'], # Palabras que definan tu paquete
    classifiers=[],
)