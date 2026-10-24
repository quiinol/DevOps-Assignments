# Assignment 7: Jenkins CI Automation

## Objective
Understand Continuous Integration (CI), learn Jenkins fundamentals, and install and access Jenkins using Docker.

## 1. Continuous Integration
Continuous Integration is a development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help identify integration errors early and provide feedback.

### Key Features
- Frequent code integration
- Automated builds
- Automated testing
- Immediate feedback

### Benefits
- Early bug detection
- Improved collaboration
- Faster development cycles
- Improved software quality

## 2. Jenkins
Jenkins is an open-source automation server used to automate software building, testing, and delivery.

### Key Concepts
- Job: A task or process executed by Jenkins.
- Build: An execution of a job or pipeline.
- Pipeline: An ordered sequence of automation stages.
- Plugins: Extensions that add Jenkins functionality.
- Nodes: Machines on which Jenkins jobs execute.

## 3. Jenkins Installation Using Docker

The installation command provided in the exercise is:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
