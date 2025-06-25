pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-todo-app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Samhitha1705/todo-.git'  // Update this!
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                        docker rm -f flask-todo-container || true
                        docker run -d -p 5002:5002 --name flask-todo-container $IMAGE_NAME
                    '''
                }
            }
        }
    }
}
