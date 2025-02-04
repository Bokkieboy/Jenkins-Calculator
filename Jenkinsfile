pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        DOCKER_IMAGE = 'simple-calculator'
        CONTAINER_NAME = 'calculator-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Bokkieboy/UniCalculator.git'
            }
        }

        stage('Build Application') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    sh 'python3 -m unittest discover -s tests'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'docker run -d -p 5050:5050 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
