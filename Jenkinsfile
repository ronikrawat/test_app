pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code checkout completed'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install pytest pylint
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Pylint Check') {
            steps {
                sh 'pylint tests'
            }
        }

        stage('Run Test Cases') {
            steps {
                sh 'pytest -v'
            }
        }
    }

    post {
        success { echo 'All checks passed ✅' }
        failure { echo 'Pipeline failed ❌' }
    }
}
