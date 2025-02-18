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

Finally, change the route to App.svelte to your local route in _app/src/routes/+page.svelte_.
You can copy path of App.svelte on your local machine from _app/lib/App.svelte_ and paste it in _app/src/routes/+page.svelte_.

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