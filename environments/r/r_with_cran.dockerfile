FROM rocker/tidyverse:4.0.0-ubuntu18.04

# install optparse package
RUN R -e "install.packages('optparse', repos='https://cran.rstudio.com')"

# Install python
RUN apt-get update -qq && \
  apt-get install -y python3
  
# Install pip
RUN apt-get install -y python3-pip

# create link for python
RUN ln -f /usr/bin/python3 /usr/bin/python
RUN ln -f /usr/bin/pip3 /usr/bin/pip

# install azureml-core
RUN pip install azureml-sdk

# install libfuse
RUN apt-get install -y libfuse-dev

