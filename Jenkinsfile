pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image: flask-todo-app'
                    bat 'docker build -t flask-todo-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Checking and stopping existing containers using port 5002...'

                    // Stop and remove any containers using port 5002
                    bat '''
                    FOR /F "tokens=*" %%i IN ('docker ps -q --filter "publish=5002"') DO docker stop %%i
                    FOR /F "tokens=*" %%i IN ('docker ps -a -q --filter "publish=5002"') DO docker rm %%i
                    '''

                    echo 'Starting new container on port 5003...'
                    bat 'docker run -d -p 5003:5002 --name flask-todo-container flask-todo-app'
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
        success {
            echo '✅ Pipeline completed successfully!'
        }
    }
}
