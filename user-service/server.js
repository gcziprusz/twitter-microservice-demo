// user-service/server.js
const express = require("express");
const messaging = require("./messaging");
const app = express();
app.use(express.json());

let users = [{ id: 1, username: "user1" }];

app.get("/users", (req, res) => {
  messaging.publishMessage(`User-service: All Users ${JSON.stringify(users)} were requested!`);
  res.json(users);
});


app.get('/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: 'User not found' });
  messaging.publishMessage(`User-service: User ${JSON.stringify(user)} was requested!`);
  res.json(user);
});

app.post("/register", (req, res) => {
  console.log('req',req.body,req.params)
  const user = { id: users.length + 1, username: req.body.username };
  users.push(user);
  messaging.publishMessage(`User-service: User ${JSON.stringify(user)} was created!`);
  res.status(201).json(user);
});

app.listen(3001, () => {
  console.log("User Service running on port 3001");
});
