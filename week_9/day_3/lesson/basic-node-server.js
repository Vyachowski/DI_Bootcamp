const http = require('http');

const basicNodeServer = http.createServer((req, res) => {
  console.log('Url: ', req.url);
  console.log('Headers: ', req.headers);
  if (req.url === '/') {
    res.end('<h1>Hello, my man!</h1>')
  }
  res.end('hello my first basicNodeServer');
})

basicNodeServer.listen(5002, () => {
  console.log('run on port 5002')
});