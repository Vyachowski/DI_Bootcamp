const knex = require('knex');
require('dotenv').config();

const db = knex({
  client: 'pg',
  connection: {
    host: process.env.DB_HOST,
    port: process.env.DB_HOST,
    user: process.env.DB_HOST,
    password: process.env.DB_HOST,
    database: process.env.DB_HOST,
  }
});

module.exports = { db };