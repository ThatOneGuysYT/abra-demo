pipeline {
    agent any

    stages {
        stage('run test') {
            steps {
                sh '''
                pip install requests --break-system-packages
                pip install pytest --break-system-packages
                python3 abra-demo/test_file.py
                '''
            }
        }
        stage('TestAPI') {
            steps {
                sh '''
                cd abra-demo
                python3 -m pytest
                '''
            }
        }
    }
}
