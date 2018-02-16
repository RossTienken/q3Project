exports.up = function(knex, Promise) {
  return knex.schema.createTable('drawings', table => {
    table.increments('id')
    table.string('name').notNullable()
    table.string('fileName').notNullable()
  })
};

exports.down = function(knex, Promise) {
  return knex.schema.dropTable('drawings')
};
