import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='Invitation',  
     version='0.1',
     scripts=['main'] ,
     author="Priyanka Verma",
     author_email="priyankavermaict@gmail.com",
     description="Interview solution",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/priyankvp/invitation",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
