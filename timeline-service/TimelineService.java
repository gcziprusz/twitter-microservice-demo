import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.List;
import java.io.InputStreamReader;

public class TimelineService {
    
    private static List<TimelinePost> posts = new ArrayList<>();
    private static Gson gson = new Gson();

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(5002), 0);
        server.createContext("/timeline/posts", TimelineService::handlePosts);
        server.setExecutor(null); // creates a default executor
        System.out.println("Timeline Service is running on port 3003...");
        server.start();
    }

    private static void handlePosts(HttpExchange exchange) throws IOException {
        String method = exchange.getRequestMethod();

        if ("GET".equalsIgnoreCase(method)) {
            handleGetPosts(exchange);
        } else if ("POST".equalsIgnoreCase(method)) {
            handleCreatePost(exchange);
        } else {
            exchange.sendResponseHeaders(405, -1); // Method not allowed
        }
    }

    private static void handleGetPosts(HttpExchange exchange) throws IOException {
        String jsonResponse = gson.toJson(posts);
        exchange.sendResponseHeaders(200, jsonResponse.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(jsonResponse.getBytes());
        os.close();
    }

    private static void handleCreatePost(HttpExchange exchange) throws IOException {
        InputStreamReader reader = new InputStreamReader(exchange.getRequestBody(), "utf-8");
        TimelinePost newPost = gson.fromJson(reader, TimelinePost.class);
        posts.add(newPost);

        String response = "Post created";
        exchange.sendResponseHeaders(201, response.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }
}
