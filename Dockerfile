# Extend the official Rasa SDK image
FROM danyuanwang/xuanwugame:rasa

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

COPY config.yml config.yml
COPY domain.yml domain.yml
COPY endpoints.yml endpoints.yml
COPY credentials.yml credentials.yml

# Create /.cache for spacy model training.
RUN mkdir /.cache && chmod a+rwx /.cache 

# copy models from local if there is any.
RUN mkdir /app/models && chmod a+rwx /app/models
COPY ./models /app/models

# copy data from local if there is any.
RUN mkdir /app/data && chmod a+rwx /app/data
COPY ./data /app/data

# copy test from local if there is any.
RUN mkdir /app/test && chmod a+rwx /app/test
COPY ./tests /app/tests



# Copy actions folder to working directory
COPY ./actions /app/actions
COPY ./actions.py /app/actions

# By best practices, don't run the code with root user
USER 1001

