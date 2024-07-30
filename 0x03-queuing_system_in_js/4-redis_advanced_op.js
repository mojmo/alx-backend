import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function storeHash() {
  const hashKey = 'HolbertonSchools';
  const hashValues = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [field, value] of Object.entries(hashValues)) {
    client.hset(hashKey, field, value, (err, reply) => {
      if (err) {
        console.error(`Error setting ${field}: ${err.message}`);
      } else {
        redis.print(`Reply: ${reply}`);
      }
    });
  }
}

function displayHash() {
  const hashKey = 'HolbertonSchools';
  client.hgetall(hashKey, (err, object) => {
    if (err) {
      console.error(`Error getting hash: ${err.message}`);
    } else {
      console.log(object);
    }
  });
}

storeHash();
setTimeout(displayHash, 1000); // Delay to ensure all hset operations are completed
