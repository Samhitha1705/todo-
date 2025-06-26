pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-todo-app"
        CONTAINER_NAME = "flask-todo-container"
        PORT = "5002"
        HOST_PORT = "5003" // Change this if needed
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${IMAGE_NAME}"
                    bat "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Checking and stopping existing containers using port ${HOST_PORT}..."
                    bat """
                    FOR /F "tokens=*" %%i IN ('docker ps -q --filter "publish=${HOST_PORT}"') DO docker stop %%i
                    FOR /F "tokens=*" %%i IN ('docker ps -a -q --filter "publish=${HOST_PORT}"') DO docker rm %%i
                    docker run -d -p ${HOST_PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline failed. Check logs for details."
        }
        success {
            echo "✅ Build and deployment successful. App is running on port ${HOST_PORT}."
        }
    }
}
