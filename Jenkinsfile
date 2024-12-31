pipeline {
    agent any
    environment {
        PYTHON_PATH = 'C:\\Program Files\\Python311;C:\\Program Files\\Python311\\Scripts'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Coverage Installation') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                pip show coverage
                '''
            }
        }

        stage('Run Unit Tests and Generate Coverage') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Running tests with coverage..."
                coverage run --source=. test_myapp.py || exit /b 1
                coverage xml -o coverage.xml || exit /b 1
                if exist coverage.xml (
                    echo "Coverage report generated successfully."
                ) else (
                    echo "Error: Coverage report not found!"
                    exit /b 1
                )
                '''
            }
        }

        stage('Ensure Correct Working Directory') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                echo "Current working directory: %cd%"
                dir
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner -Dsonar.projectKey=final-coverage ^
                              -Dsonar.sources=. ^
                              -Dsonar.python.coverage.reportPaths=coverage.xml ^
                              -Dsonar.host.url=http://localhost:9000 ^
                              -Dsonar.token=sqp_d33c9ef10ff8d73ae91574190fbc00e4c86c1056
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
        always {
            echo 'This runs regardless of the result.'
        }
    }
}
