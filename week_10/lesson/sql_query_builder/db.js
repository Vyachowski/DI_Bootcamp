const knex = require('knex');

// const db = knex({
//   client: 'pg',
//   connection: {
//     host: 'localhost',
//     port: '5432',
//     user: 'postgres',
//     password: 'root',
//     database: 'dvdrental',
//   }
// })

// db.select('customer_id', 'first_name').from('customer').first()
// .then(rows => {
//   console.log(rows);
// })
// .catch(err => console.log(err))

// Cloud database
const db = knex({
  client: 'pg',
  connection: {
    host: 'lucky.db.elephantsql.com',
    port: '5432',
    user: 'lmhihkwd',
    password: 'IxcVWiofzDn3Hn_Tazo5qGY6WwMCFcXH',
    database: 'lmhihkwd',
  }
})

// Normal example of query
db.select('id', 'name', 'price').from('products')
.then(rows => {
  console.log(rows);
})
.catch(err => console.log(err))

// !!! Bad example of query !!!
// db('products').select('*')
//   .then(rows => {
//     console.log(rows);
//   })
//   .catch(err => console.log(err))
