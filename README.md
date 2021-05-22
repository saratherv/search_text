# search_text


This repository contains a simple Django app, **Search Text in the files over cloud**


# DESCRIPTION
This application fetches PDF files from aws s3 bucket, extracts text from the files and then creates indexes for the extracted documents.

# PREREQUISITE
- python 3.6 or above installed
- setup and install elasticsearch https://www.elastic.co/guide/en/elasticsearch/reference/7.12/deb.html#deb-repo




# SETUP & EXECUTION
- create virtal environment using command python3 -m venv environment_name
- activate virtual environment source environment_name/bin/activate
- clone the repository https://github.com/saratherv/search_text.git
- get to root   cd search_text
- run sudo docker-compose up --build, This will start development server on http://0.0.0.0:8000/
