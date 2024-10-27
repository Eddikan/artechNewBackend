// app/api/index.js
const fastify = require('fastify')();
const cors = require('fastify-cors');

// Register the CORS plugin
fastify.register(cors, {
  // Here you can specify the allowed origins
  origin: '*', // Allow all origins. Change to a specific domain if needed
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'], // Specify any headers you need
});

// Example route
fastify.get('/', async (request, reply) => {
  return { message: 'Hello, World!' };
});

// Export the Fastify instance as a serverless function
module.exports = (req, res) => {
  fastify.ready(err => {
    if (err) {
      res.status(500).send(err);
    } else {
      fastify.handleRequest(req, res);
    }
  });
};
