pipeline {
    agent any

    stages {
        stage('build') {
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
        stage('build container') {
            agent {
                docker { image 'node:alpine3.19' }
            }
            steps {
                sh '''
                pip install requests --break-system-packages
                pip install pytest --break-system-packages
                python3 test_file.py
                '''
            }
        }
    }
}
