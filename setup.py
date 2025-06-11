from setuptools import setup, find_packages
setup(
    name= "Ayush Saxena",
    version= '0.1',
    author= "Ayush Saxena",
    author_email= "ayushsaxena241195.official@gmail.com",
    install_requires= ['openai',
'langchain',
'langchain_core',
'langchain_community',
'streamlit',
'langchain_openai',
'python-dotenv',
'PyPDF2'],
packages= find_packages()
)