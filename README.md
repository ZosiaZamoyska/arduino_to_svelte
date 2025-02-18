# Arduino To Svelte
Sending Arduino signals through python to svelte web app

Might be particularly useful for:
* sensing with _arduino_
* (ML) processing of data with _python_
* creating web interface with the best front-end framework, _svelte_

# How to run

## Setup
Change the port in arduino.py to your arduino port.
Change the websocket port (default here is 8765) in arduino.py and app/src/lib/App.svelte

## Python Environment
`
python3 -m venv env
source env/bin/activate

pip3 install pyserial
pip3 install websockets
`
## Running

In first terminal, run:
`
python3 arduino.py
`

In second terminal, run:
`
cd app
npm run dev
`