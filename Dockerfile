FROM python:3.9.4-buster
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH=$PATH:/root/.poetry/bin/
# specify your bot key
ENV API_KEY 0000000000:xxx0xxxxx0xxxxx-xxxx00xx0xx0xxxxxx0
WORKDIR /bot
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false &&\
    poetry install
COPY . .
ENTRYPOINT python -m kg3_info_bot.main