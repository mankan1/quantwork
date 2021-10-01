import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='quantwork',
    version='0.0.1',
    author='Manoj Kandlikar',
    author_email='manoj.kandlikar@gmail.com',
    description='Quant work',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mankan1/quantwork.git',
    project_urls = {
        "Bug Tracker": "https://github.com/mankan1/quantwork/issues"
    },
    license='MIT',
    packages=['quantwork'],
    install_requires=['requests'],
)
