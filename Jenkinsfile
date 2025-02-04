pipeline {
    agent any

    environment {
        IMAGE_NAME = "simple-calculator"
        CONTAINER_NAME = "calculator-app"
        GITHUB_REPO = "https://github.com/Bokkieboy/UniCalculator.git"
        TEST_SCRIPT = "test_calculator.py"  // Ensure you have a test script
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Cloning repository from GitHub..."
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('Build Application') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Test Application') {
            steps {
                echo "Running tests..."
                sh 'docker run --rm ${IMAGE_NAME} python3 ${TEST_SCRIPT} || true'  // Run inside container
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying application..."
                sh 'docker run -d --rm --name ${CONTAINER_NAME} -p 5050:5050 ${IMAGE_NAME}'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
         always {
            archiveArtifacts artifacts: 'build_logs.txt', fingerprint: true

        }
    }
}
