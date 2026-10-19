# Assignment 4: Docker Networking with Multiple Containers

## Objective
Understand Docker networking and configure multiple containers to communicate through a custom bridge network.

## Tools and Technologies
- Docker
- Python 3.9
- Flask 2.0.1
- Werkzeug 2.0.3
- MySQL
- Redis

## Network Architecture
A custom bridge network named `my-bridge-net` connects three containers:
- **Flask:** Hosts a REST API on port 5001.
- **MySQL:** Database server on port 3306.
- **Redis:** Cache server on port 6379.

## Implementation

### 1. Create the bridge network
```bash
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

### 2. Create and build the Flask application
The Flask application provides a GET endpoint at `/about`, returning the API name, version, and description as JSON.

Build the Docker image:
```bash
docker build -t flask-api .
```

### 3. Launch the containers
```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabRoot123! mysql:latest
docker run -d --name redis --network my-bridge-net redis:latest
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

`Werkzeug==2.0.3` is pinned in `requirements.txt` for compatibility with `Flask==2.0.1`.

### 4. Test the REST API
Open `http://localhost:5001/about` in a browser or run:
```bash
curl http://localhost:5001/about
```

The API returned HTTP status code **200 OK** and the expected JSON response.

### 5. Verify container name resolution
```bash
docker network inspect my-bridge-net
docker exec flask python -c "import socket; print('MySQL IP:', socket.gethostbyname('mysql')); print('Redis IP:', socket.gethostbyname('redis'))"
```

The Flask container successfully resolved:
- `mysql` → `172.18.0.2`
- `redis` → `172.18.0.3`

This confirms Docker's built-in DNS name resolution on the custom bridge network.

## Screenshots
1. `screenshots/network-inspect.png` — custom bridge network and connected containers.
2. `screenshots/flask-api-response.png` — successful Flask API response.
3. `screenshots/container-dns.png` — MySQL and Redis name resolution from Flask.

## Conclusion
The Flask, MySQL, and Redis containers ran on the same custom bridge network. The Flask REST API returned the expected response, and container-name DNS resolution was verified successfully.
