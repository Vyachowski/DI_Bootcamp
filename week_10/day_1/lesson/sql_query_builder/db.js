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
// db.select('id', 'name', 'price').from('products')
// .then(rows => {
//   console.log(rows);
// })
// .catch(err => console.log(err))

// !!! Bad example of query !!!
// db('products').select('*')
//   .then(rows => {
//     console.log(rows);
//   })
//   .catch(err => console.log(err))

// Query with conditions
// db('products')
//   .select('id', 'name', 'price').from('products')
//   .where({id: 1})
//   .then(rows => {
//     console.log(rows);
//   })
//   .catch(err => console.log(err))

// Query with conditions
// db('products')
//   .insert(
//     [
//       { name: 'icAr', price: 1000 },
//       { name: 'iBook', price: 300 },
//     ]
//   )
//   .returning('*')
//   .where({id: 1})
//   .then(rows => {
//     console.log(rows);
//   })
//   .catch(err => console.log(err))

// db.raw('select id, name, price from products')
//   .then(rows => {
//     console.log(rows);
//   })
//   .catch(err => console.log(err))

const register = async () => {
  const trx = await db.transaction();
  try {
    const user = await db('products').insert(
      {
        username: 'aaa',
        email: 'aaa@gmail.com'
      },
      ['username', "email"]
    )
      .transacting(trx)
    const hashpwd = await db('hashpwd')
      .insert(
        {
          username: user[0].username,
          password: 123456
        }, ['password', 'username']
      )
    await trx.commit();
  } catch (e) {
    trx.rollback();
    console.log(e);
  }
}
register()