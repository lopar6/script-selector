FROM python:3.10

# Force stin, stdout, and stderr to be totally unbuffered
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION 1.1.11

# install system dependencies
RUN apt update
RUN apt install -y locales
RUN apt install -y libmagic1
RUN apt install -y libmagickwand-dev

# configure locale
RUN sed -i -e 's/# \(en_US\.UTF-8 .*\)/\1/' /etc/locale.gen && locale-gen

RUN apt install -y \
    postgresql-client \
    exiftool \
    curl \
    build-essential \
    libffi-dev \
    acl

RUN pip install --no-cache-dir --upgrade pip wheel
RUN pip install "poetry==$POETRY_VERSION"

# cleanup
RUN rm -rf /var/lib/apt/lists

# project skeleton
WORKDIR /app/

RUN setfacl -d -m u::rwx /app
RUN setfacl -d -m g::rwx /app
RUN setfacl -d -m o::rwx /app

# COPY pyproject.toml and poetry.lock and RUN poetry install BEFORE adding the rest the code,
# this will cause Docker's caching mechanism to prevent re-installing (all)
# dependencies when there is only a change in the code.
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

RUN echo "alias ll='ls -alF'" >> ~/.bashrc
RUN echo "alias rs='./manage.py runserver 0:8000'" >> ~/.bashrc

