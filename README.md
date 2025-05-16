# Mobilenet Image Classification Web App

GitHub Repository Link:  
[https://github.com/Fatimazahra889/AI-Internship-Test](https://github.com/Fatimazahra889/AI-Internship-Test)

## Project Summary

This project is a lightweight web application that performs image classification using the pre-trained MobileNet model. It allows users to upload an image, and the app returns the top prediction. The model is loaded using TensorFlow and runs inside a Docker container. The web interface is built using Flask.

## Features

- Upload image via web interface
- Predict using MobileNet
- Display prediction result on screen
- Fully containerized with Docker
- Deployable on Kubernetes (Minikube)

## Challenges Faced & Solutions

- **Minikube Docker environment setup:** I faced delays and container issues due to Docker communication problems. Solved it by deleting the cluster and restarting Docker and Minikube cleanly.
- **Slow Docker build process:** The build was freezing due to poor connection and a lot of big files. I optimized the Dockerfile, removed the virtual environment folder using ".dockerignore".
- **TensorFlow model loading slowness:** Cached the model load step and ensured the container has enough memory allocation (increased CPU/memory in Minikube config).

