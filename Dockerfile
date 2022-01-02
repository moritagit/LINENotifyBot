FROM python:3.8-slim AS builder

LABEL org.opencontainers.image.source https://github.com/moritagit/LINENotifyBot

ENV DEBIAN_FRONTEND=noninteractive
ENV WORKDIR /workspaces/LINENotifyBot

WORKDIR /opt

# install basic packages
RUN apt-get update && apt-get -yV upgrade && apt-get -yV install \
    git curl vim

# install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH $PATH:/root/.poetry/bin
RUN poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false

WORKDIR ${WORKDIR}
COPY poetry.lock pyproject.toml ${WORKDIR}


FROM builder AS production
RUN poetry install --no-dev --no-root
COPY src ${WORKDIR}/src
RUN poetry install --no-dev


FROM builder AS development
RUN poetry install --no-root
COPY src ${WORKDIR}/src
RUN poetry install
