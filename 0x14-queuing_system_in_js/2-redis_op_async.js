const redis = require('redis');
const util = require('util');

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setAsync = util.promisify(client.set).bind(client);
const getAsync = util.promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(`Reply: ${reply}`);
  } catch (error) {
    console.error(`${error}`);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`${reply}`);
  } catch (error) {
    console.error(`${error}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
