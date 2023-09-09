// 🌟 Exercise 1: Building A RESTful API
// Instructions
// You’re tasked with building a RESTful API for a blog platform.
// Users should be able to create, read, update, and delete blog posts using different endpoints.
// Create a directory named blog-api.
// Inside the blog-api directory, open a terminal and run npm init to initialize a new Node.js project. Follow the prompts to set up your project.
// Install the express package by running npm install express in the terminal.
// Create a file named server.js.
// In server.js, require the express package and set up an Express app.
const express = require('express');
const app = express();
const port = 3000;
app.use(express.json());
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
// Create a data array to simulate a database. Each item in the array should represent a blog post with properties like
// id, title, and content.
const blogArticles = [
  {
    id: 1,
    title: 'First article',
    content: 'Hello, world!'
  },
  {
    id: 2,
    title: 'Second article',
    content: 'Hello, new world!'
  },
  {
    id: 3,
    title: 'Third article',
    content: 'Hello, the newest world!'
  },
]
// Implement the following routes using Express:
// GET /posts/:id: Return a specific blog post based on its id.
app.get('/posts/:id', (req, res) => {
  const id = req.params.id;
  const article = blogArticles.find((article) => article.id === +id);
  res.send(article);
})
// GET /posts: Return a list of all blog posts.
app.get('/posts', (req, res) => {
  res.send(blogArticles);
});
// PUT /posts/:id: Update an existing blog post.
app.put('/posts/:id', (req, res) => {
  const id = req.params.id;
  const { title, content } = req.body;
  const articleIndex = blogArticles.findIndex((article) => article.id === +id);

  blogArticles[articleIndex] = {
    ...blogArticles[articleIndex],
    title,
    content,
  }
  res.json(blogArticles[articleIndex]);
});
// POST /posts: Create a new blog post.
app.post('/posts', (req, res) => {
  const { title, content } = req.body;
  const newPost = {
    id: blogArticles.length + 1,
    title,
    content
  }
  blogArticles.push(newPost);
  res.status(201).json(newPost);
});
// DELETE /posts/:id: Delete a blog post.
app.delete('/posts/:id', (req, res) => {
  const id = req.params.id;
  const articleIndex = blogArticles.findIndex((article) => article.id === +id);

  blogArticles.splice(articleIndex, 1);
  res.json({ message: 'Post deleted successfully' });
  res.status(404).json({ error: 'Post not found' });
});
// Implement error handling for invalid routes and server errors.
app.use((req, res) => {
  res.status(404).json({ error: 'Address not found' });
});
// Start the Express app and listen on a specified port (e.g., 3000).