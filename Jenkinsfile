pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Build and Run with Docker Compose') {
            steps {
                script {
                    // Force rebuild without cache to pick up latest code
                    sh 'docker-compose down || true' // optional: stop existing containers
                    sh 'docker-compose up --build --no-cache -d'
                }
            }
        }
    }
}
