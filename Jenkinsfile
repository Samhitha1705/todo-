pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-todo-app'
        CONTAINER_NAME = 'flask-todo-container'
        APP_PORT = '5002'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${IMAGE_NAME}"
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Stopping and removing existing container if it exists..."
                    bat "docker rm -f %CONTAINER_NAME% || exit 0"

                    echo "Running new Docker container on port ${APP_PORT}..."
                    bat """
                        docker run -d -p %APP_PORT%:%APP_PORT% ^
                        --name %CONTAINER_NAME% %IMAGE_NAME%
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for more details.'
        }
    }
}
