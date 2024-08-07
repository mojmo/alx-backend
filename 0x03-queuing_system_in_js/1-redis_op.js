import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting ${schoolName}: ${err.message}`);
    } else {
      redis.print(`Reply: ${reply}`);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting ${schoolName}: ${err.message}`);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
