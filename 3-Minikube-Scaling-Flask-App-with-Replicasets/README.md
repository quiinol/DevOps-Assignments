
# Assignment 3: Scaling Flask App with ReplicaSets

## Objective
Deploy a Flask flash-sale application on Minikube, scale its ReplicaSet from 3 to 5 Pods, and demonstrate Kubernetes self-healing.

## Application Endpoints
- `/` - Welcomes users and returns the serving Pod name.
- `/buy?user=123` - Simulates a purchase and returns a random product.
- `/health` - Reports application health.

## Technologies Used
- Python and Flask
- Docker and Gunicorn
- Kubernetes and Minikube
- kubectl and YAML

## Implementation
1. Created the Flask application in `app.py`.
2. Created a Dockerfile and built the image `flashsale:1.0`.
3. Loaded the image into Minikube.
4. Created `flashsale-replicaset.yaml` containing a ReplicaSet and ClusterIP Service.
5. Applied the YAML configuration.
6. Tested the homepage, purchase, and health endpoints.
7. Scaled the ReplicaSet from 3 to 5 replicas.
8. Deleted one Pod and observed Kubernetes create a replacement.
9. Inspected Pod distribution across the Minikube node.

## Verification Results
- Initial replicas: 3.
- Final desired/current/ready replicas: 5/5/5.
- All five Pods were running on the single Minikube node.
- All three application endpoints returned HTTP 200.
- Kubernetes replaced the deleted Pod automatically.
- The Service exposed port 80 and forwarded requests to container port 5000.

## Key Learnings
- ReplicaSets maintain the desired number of Pods.
- Kubernetes automatically replaces deleted Pods.
- Readiness and liveness probes monitor application health and readiness.
- Services provide a stable endpoint for accessing matching Pods.

## Project Files
- `app.py` - Flask application.
- `Dockerfile` - Docker image build instructions.
- `flashsale-replicaset.yaml` - ReplicaSet and Service configuration.
- `screenshots/` - Screenshots showing scaling, Pods, and application response.
