import express from 'express';

const app = express();
const port = 3001;

app.use(express.json());
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*'); // Разрешить запросы с любых доменов
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.get('/api/hello', (req,res) => {
  res.send('Hello from Express!')
});

app.post('/api/world', (req, res) => {
  const requestBody = req.body;
  const responseText = requestBody.text;
  res.json({ text: responseText });
})
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
