<script>
    import { onMount } from 'svelte';
  
    let arduinoData = '';
    let websocketPort = 8765; // change to your chosen websocket port
  
    onMount(() => {
      const socket = new WebSocket(`ws://localhost:${websocketPort}`);
  
      socket.onmessage = (event) => {
        arduinoData = event.data;
      };
  
      socket.onopen = () => {
        console.log('WebSocket connected');
      };
  
      socket.onerror = (error) => {
        console.log('WebSocket error: ', error);
      };
    });
  </script>
  
  <main>
    <h1>Arduino Data:</h1>
    <p>{arduinoData}</p>
  </main>
  