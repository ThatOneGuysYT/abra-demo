pipeline {
    agent any

    stages {
        stage('run test') {
            steps {
                sh '''
                pip install requests --break-system-packages
                pip install pytest --break-system-packages
                python3 test_file.py
                '''
            }
        }
        stage('TestAPI') {
            steps {
                sh '''
                python3 -m pytest
                '''
            }
        }
    }
}
