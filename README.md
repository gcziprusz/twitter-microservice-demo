
```
twitter-microservices/
├── user-service/
│   ├── Dockerfile
│   ├── server.js
│   ├── package.json
├── tweet-service/
│   ├── Dockerfile
│   ├── server.js
│   ├── package.json
├── timeline-service/
│   ├── Dockerfile
│   ├── server.js
│   ├── package.json
├── docker-compose.yml
```

Running the Microservices
Build and Start the Services: In the terminal, navigate to the project folder and run:

bash
Copy code
docker compose up --build
Access the Services:

User Service: http://localhost:3001
Tweet Service: http://localhost:3002
Timeline Service: http://localhost:3003
Example Usage:

Register a User: Use a POST request to http://localhost:3001/register with JSON { "username": "newuser" }.
Create a Tweet: Use a POST request to http://localhost:3002/tweet with JSON { "userId": 1, "content": "Hello Twitter!" }.
Get Timeline: Use a GET request to http://localhost:3003/timeline to retrieve tweets.

```
curl -X POST http://localhost:3001/register -d'{ "username": "newuser" }'
curl http://localhost:3001/users/

curl -X POST http://localhost:3002/tweets -d'{ "userId": 1, "content": "Hello Twitter!" }'

curl  http://localhost:3003/timeline/posts
curl  http://localhost:3003/timeline/posts -d'{ "userId": 1, "content": "Hello Twitter!" }'
```

You can access the RabbitMQ management UI at http://localhost:15672 using the username and password defined in the environment.