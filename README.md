# The info bot

## Get started with coding

1. Install poetry to manage dependencies
2. Install project for local development (`poetry install`)

## How to change:
Under the `resources`/*.md should be all pages content.
All the new pages supposed to have simplified `markdown_v2` content.
The `messages.msg_reader` uses the file name w/o ext to read the data.

The `@callback_handler` decorator is required to register callback handlers.

The `keyboard.py` contains the same patter that used in the handler, so pls update it once added new callback handler.

## webhoks
TODO:
Install localtunnel `sudo npm install -g localtunnel`. Than start the app and run proxy on localtunnel using app port: ```lt --port 8000```