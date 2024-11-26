from setuptools import setup, find_packages

setup(
    name='my_image_caption_package',  # The name of your package
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
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_image_caption_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
