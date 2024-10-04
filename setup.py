from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Premsai',
    author_email='premsaisahoo@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","huggingface_hub"],
    packages=find_packages()
)





#python setup.py install