'use strict';

module.exports = {
  development: {
    client: 'pg',
    connection: 'postgres://localhost/drawings'
  },

  test: {
    client: 'pg',
    connection: 'postgres://localhost/notesdb_test'
  },

  production: {
    client: 'pg',
    connection: process.env.DATABASE_URL
  }
};
