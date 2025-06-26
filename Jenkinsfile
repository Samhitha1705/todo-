pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-todo-app'
        CONTAINER_NAME = 'flask-todo-container'
        PORT = '5002'       // Flask app runs on this port inside container
        HOST_PORT = '5003'  // Mapped port on host (Jenkins/Docker host)
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
                    echo "Checking and removing existing containers by name or using port ${HOST_PORT}..."

                    bat """
                    REM Stop and remove container with same name (if exists)
                    docker stop ${CONTAINER_NAME} || exit 0
                    docker rm ${CONTAINER_NAME} || exit 0

                    REM Stop and remove any container using the same host port (optional cleanup)
                    FOR /F "tokens=*" %%i IN ('docker ps -q --filter "publish=${HOST_PORT}"') DO docker stop %%i
                    FOR /F "tokens=*" %%i IN ('docker ps -a -q --filter "publish=${HOST_PORT}"') DO docker rm %%i

                    REM Run new container
                    docker run -d -p ${HOST_PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}
                    """
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
        success {
            echo '✅ Pipeline executed successfully.'
        }
    }
}
