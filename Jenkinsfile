pipeline {
agent any

```
environment {
    VENV_DIR = "venv"
}

stages {

    stage('Checkout') {
        steps {
            echo 'Checking out source code'
        }
    }

    stage('Setup Python Environment') {
        steps {
            sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install pytest pylint
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
            '''
        }
    }

    stage('Pylint Check') {
        steps {
            sh '''
                . ${VENV_DIR}/bin/activate
                pylint tests || exit 1
            '''
        }
    }

    stage('Run Test Cases') {
        steps {
            sh '''
                . ${VENV_DIR}/bin/activate
                pytest -v
            '''
        }
    }
}

post {
    always {
        echo 'Pipeline finished'
    }
    failure {
        echo 'Build failed ❌'
    }
    success {
        echo 'Build successful ✅'
    }
}


}
