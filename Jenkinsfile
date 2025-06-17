pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/seerapusairam/flask-redis-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("flask-redis-app")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("-d -p 5000:5000")
                }
            }
        }
    }
}
