const redis = require('redis');

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.error(`${error}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.error(`${error}`);
    } else {
      console.log(`${reply}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
