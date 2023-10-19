const express = require('express');

const app = express();
const port = 1245;

// Définissez une route pour l'endpoint /
app.get('/', (req, res) => {
  res.send('Bonjour Holberton School!');
});

// Écoutez le serveur sur le port 1245
app.listen(port, () => {
  console.log(`Le serveur Express écoute sur le port ${port}`);
});

// Exportez l'application Express
module.exports = app;
