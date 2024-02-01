pipeline {
    agent any

    stages {
        stage('install requirements')
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        stage('check code')
            steps {
                sh '''
                pylint test_file.py
                '''
            }
        stage('build') {
            steps {
                sh '''
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
