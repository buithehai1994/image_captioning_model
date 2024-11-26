from setuptools import setup, find_packages

setup(
    name='image_captioning_model',  # The name of your package
    version='0.1.0',  # Version number
    packages=find_packages(),  # This will automatically discover your package files
    install_requires=[
        'torch',
        'torchvision',
        'Pillow',
    ],
    description='A simple package to generate image captions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='thehaibui',
    author_email='haibt0206@gmail.com',
    url='https://github.com/buithehai1994/image_caption_model',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
