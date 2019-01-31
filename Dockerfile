
# Use an official Python runtime as a parent image
FROM python:3.6-slim

# install graphviz pydotplus
RUN apt-get update \
  && apt-get install -y --no-install-recommends graphviz \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir pydotplus

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
# -u to run with unbuffered output
CMD ["python", "-u", "app.py"]
