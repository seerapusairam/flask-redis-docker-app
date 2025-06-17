pipeline {
    agent any

    options {
        skipDefaultCheckout(true) // <- disables automatic 'checkout scm'
    }

    stages {
        stage('Build and Run with Docker Compose') {
            steps {
                script {
                    // Build and start services defined in docker-compose.yml
                    sh 'docker-compose up --build -d'
                }
            }
        }
    }
}
