pipeline {
    agent any

    options {
        skipDefaultCheckout(true) // <- disables automatic 'checkout scm'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build('flask-redis-app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('flask-redis-app').run('-d -p 5001:5000')
                }
            }
        }
    }
}
