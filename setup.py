from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Jithesh Reddy',
    author_email='Jithesh20082002@gmail.com',
    install_requires=[
        "openai==1.16.1",  # Latest version as of 2024-04-02[^1^][22]
        "langchain==0.1.14",  # Latest version as of 5 days ago[^2^][2]
        "streamlit==1.18.0",  # Latest version as of 2023-02-11[^3^][18]
        "python-dotenv==1.0.1",  # Latest version as of 2023-01-22[^4^][7]
        "PyPDF2==3.0"  # Last version of PyPDF2[^5^][10]
    ],
    packages=find_packages()
)
