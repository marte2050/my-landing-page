FROM ubuntu:25.04
LABEL maintainer="Jonathan W."

WORKDIR /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadb-dev \
    zlib1g-dev \
    libwebp-dev \
    pipx \
 && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pipx install "gunicorn==20.0.4"
RUN chown -R ubuntu /app

USER ubuntu
RUN pipx install "poetry==2.2"
RUN pipx ensurepath
RUN ~/.local/bin/poetry self add poetry-plugin-shell

COPY src/pyproject.toml .
COPY src/poetry.lock .

RUN ~/.local/bin/poetry install --no-interaction --no-ansi