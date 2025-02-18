import asyncio
import serial
import websockets

arduino_port = '/dev/cu.usbmodem11201'  # Update with your port
websocket_port = 8765 # change to port you want to use

baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)


async def handle_websocket(websocket):
    print("Client connected")
    try:
        while True:
            if ser.in_waiting > 0:
                arduino_data = ser.readline().decode('utf-8').strip()
                print(f"Sending data: {arduino_data}")
                await websocket.send(arduino_data)
            await asyncio.sleep(0.1)
    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Error in connection handler: {e}")

async def main():
    print("WebSocket server started...")
    try:
        server = await websockets.serve(handle_websocket, "localhost", websocket_port)
        await asyncio.Future()
    except Exception as e:
        print(f"Failed to start WebSocket server: {e}")

if __name__ == '__main__':
    asyncio.run(main())
