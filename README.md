
# 🚀 Containerized Web Application with Load Balancing

This project sets up a containerized web application with a PostgreSQL database and Nginx load balancer using Docker and Docker Compose. The web application exposes a simple API to create and fetch user data.

---

## 📋 Table of Contents
1. [📦 Requirements](#-requirements)
2. [🛠️ Setup](#%EF%B8%8F-setup)
3. [🔌 API Endpoints](#-api-endpoints)
4. [⚖️ Scaling and Load Balancing](#%EF%B8%8F-scaling-and-load-balancing)
5. [📜 Logs](#-logs)
6. [🔒 Security](#-security)
7. [🐛 Troubleshooting](#-troubleshooting)

---

## 📦 Requirements

- **🐳 Docker**: Install Docker from [here](https://www.docker.com/get-started).
- **📦 Docker Compose**: Docker Compose is usually included with Docker Desktop. If not, install it from [here](https://docs.docker.com/compose/install/).

---

## 🛠️ Setup

1. **📥 Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/Assignment-2-Advance-Containers.git
   cd Assignment-2-Advance-Containers
   ```

2. **🔨 Build and Run the Containers**:
   ```bash
   docker-compose up --build
   ```
   This will start:
   - The 🌐 web application (API server).
   - The 🗄️ PostgreSQL database.
   - The 🔀 Nginx reverse proxy.

3. **✅ Verify the Containers are Running**:
   ```bash
   docker-compose ps
   ```
   You should see output similar to this:
   ```
   Name                             Command               State           Ports         
   ---------------------------------------------------------------------------------
   assignment-2-advance-containers_db_1    docker-entrypoint.sh postgres    Up      5432/tcp
   assignment-2-advance-containers_web_1   python app.py                   Up      0.0.0.0:5000->5000/tcp
   assignment-2-advance-containers_nginx_1 nginx -g daemon off;            Up      0.0.0.0:8082->80/tcp
   ```

---
## 📸 Screenshot
![Image](https://github.com/user-attachments/assets/32c62f46-95ca-4cc6-836d-999ff8f14f55)
## 🔌 API Endpoints

- **📝 Create a User**  
  Method: `POST`  
  URL: `http://localhost:8082/user`  
  Request Body:
  ```json
  {
    "first_name": "Martin",
    "last_name": "Johny"
  }
  ```
  Response:
  ```json
  {
    "first_name": "Martin",
    "id": 1,
    "last_name": "Johny"
  }
  ```
  ## 📸 Screenshot
  ![Image](https://github.com/user-attachments/assets/6118d9eb-6ecc-4024-bfd5-3d9026cae254)

- **📥 Fetch a User**  
  Method: `GET`  
  URL: `http://localhost:8082/user/{id}`  
  Response:
  ```json
  {
    "first_name": "Martin",
    "id": 1,
    "last_name": "Johny"
  }
  ```
  ## 📸 Screenshot
![Image](https://github.com/user-attachments/assets/43f6fcfa-ed5a-477a-a1dc-0b2811efc24e)
---

## ⚖️ Scaling and Load Balancing

To scale the web application to multiple instances:

1. **📈 Scale the Web Service**:
   ```bash
   docker-compose up --build --scale web=3
   ```

2. **🧪 Test Load Balancing**:  
   Send multiple requests to the API:
   ```bash
   Invoke-WebRequest -Uri http://localhost:8082/user/1 -Method GET
   ```
   Nginx will distribute the requests evenly across the instances.
   ## 📸 Screenshots
![Image](https://github.com/user-attachments/assets/694a9d74-611f-4151-a9f1-5542164a975a)
![Image](https://github.com/user-attachments/assets/dc8d1a4b-7b15-4893-8d93-f34cadf4fdc2)
---

## 📜 Logs

- **📝 Application Logs**:  
  Application logs are saved to the `./app/logs` directory on your host machine. You can view them using:
  ```bash
  cat ./app/logs/app.log
  ```

- **🐳 Container Logs**:  
  To view logs for a specific service, use:
  ```bash
  docker-compose logs <service_name>
  ```
  For example:
  ```bash
  docker-compose logs web
  docker-compose logs nginx
  ```
![Image](https://github.com/user-attachments/assets/29ac47be-0bb7-443f-b563-9dfa8d264557)
---

## 🔒 Security

The following security best practices have been implemented:

- **👤 Non-Root Users**: Containers run as non-root users.
- **📦 Minimized Image Size**: Lightweight base images are used to reduce the attack surface.
- **🔑 Environment Variables**: Sensitive data (e.g., database credentials) is passed via environment variables.
- **🌐 Secure Networking**: Containers communicate over a custom Docker network.

---

## 🐛 Troubleshooting

- **🚫 Port Conflicts**:  
  If port 8082 is already in use, change the port mapping in `docker-compose.yml`:
  ```yaml
  nginx:
    ports:
      - "8083:80"  # Map host port 8083 to container port 80
  ```

- **🔗 Database Connection Issues**:  
  Ensure the database container is running before the web application. Check the logs for errors:
  ```bash
  docker-compose logs db
  ```

- **🔀 Nginx Not Forwarding Requests**:  
  Check the Nginx logs for errors:
  ```bash
  docker-compose logs nginx
  ```

---
