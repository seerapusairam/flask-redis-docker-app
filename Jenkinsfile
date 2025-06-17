pipeline {
    agent any
        options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }
        
        stage('Build and Run with Docker Compose') {
            steps {
                script {
                    // Stop existing containers if running
                    sh 'docker-compose down || true'

                    // Force rebuild without cache
                    sh 'docker-compose build --no-cache'

                    // Start services in detached mode
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
