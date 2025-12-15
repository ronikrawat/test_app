pipeline {
agent any

```
environment {
    VENV = "venv"
    PYTHON = "python"
}

stages {

    stage('Checkout Code') {
        steps {
            git branch: 'main',
                url: 'https://github.com/ronikrawat/test_app.git'
        }
    }

    stage('Setup Virtual Environment') {
        steps {
            bat '''
            %PYTHON% -m venv %VENV%
            %VENV%\\Scripts\\activate
            python --version
            '''
        }
    }

    stage('Install Dependencies') {
        steps {
            bat '''
            %VENV%\\Scripts\\activate
            pip install --upgrade pip
            pip install -r requirements.txt
            '''
        }
    }

    stage('Run Tests') {
        steps {
            bat '''
            %VENV%\\Scripts\\activate
            pytest -v --html=reports/report.html --self-contained-html
            '''
        }
    }
}

post {
    always {
        archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
    }

    success {
        echo '✅ Tests passed successfully!'
    }

    failure {
        echo '❌ Tests failed. Please check reports.'
    }
}
```

}
