// api/index.js
const fastify = require('fastify')();

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
