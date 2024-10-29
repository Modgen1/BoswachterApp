FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app

# we use 'dev' here so we can sync code changes into the container and
# have the application pick these up without restarting for easy development
CMD ["fastapi", "dev", "app/main.py"]