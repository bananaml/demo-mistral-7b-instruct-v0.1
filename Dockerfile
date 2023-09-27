# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git and wget
RUN apt-get update && apt-get install -y git wget

# Upgrade pip
RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add your model weight files 
ADD download.py .
RUN python3 download.py

ADD . .

EXPOSE 8000

CMD python3 -u app.py