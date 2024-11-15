# Use OpenJDK base image with JDK (not JRE) so javac is available
FROM openjdk:11-jdk-slim

# Set the working directory
WORKDIR /app

# Download the Gson JAR
RUN apt-get update && apt-get install -y wget && \
    wget https://repo1.maven.org/maven2/com/google/code/gson/gson/2.8.8/gson-2.8.8.jar

# Copy source files into the container
COPY TimelineService.java TimelinePost.java .

# Compile Java files, including Gson in the classpath
RUN javac -cp .:gson-2.8.8.jar TimelineService.java TimelinePost.java

# Expose port 3003 for the Timeline Service
EXPOSE 3003

# Run the Timeline Service, adding Gson to the classpath
CMD ["java", "-cp", ".:gson-2.8.8.jar", "TimelineService"]
