const express = require('express');
const app = express();
const port = 3000; // El puerto en el que correrá la app

// Definir una ruta básica
app.get('/', (req, res) => {
  res.send('¡Hola, mundo!'); // Responde con un mensaje en la raíz
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor escuchando en http://localhost:${port}`);
});