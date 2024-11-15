// user-service/server.js
const express = require("express");
const app = express();
app.use(express.json());

let users = [{ id: 1, username: "user1" }];

app.get("/users", (req, res) => {
  res.json(users);
});

app.post("/register", (req, res) => {
  const user = { id: users.length + 1, username: req.body.username };
  users.push(user);
  res.status(201).json(user);
});

app.listen(3001, () => {
  console.log("User Service running on port 3001");
});
