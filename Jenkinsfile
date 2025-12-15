pipeline {
    agent any

    environment {
        VENV = "venv"
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
                    # Install Python if not present (Ubuntu/Debian)
                    if ! command -v python3 &> /dev/null; then
                        apt update && apt install -y python3 python3-venv python3-pip
                    fi

                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install pytest pylint
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Pylint Check') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pylint tests
                '''
            }
        }

        stage('Run Test Cases') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    pytest -v
                '''
            }
        }
    }

    post {
        success { echo 'All checks passed ✅' }
        failure { echo 'Pipeline failed ❌' }
    }
}
