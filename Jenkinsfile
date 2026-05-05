pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application (Simulate Failure)') {
            steps {
                sh '''
                . venv/bin/activate
                python3 app/broken_code.py || true
                '''
            }
        }

        stage('AI Failure Analysis') {
            steps {
                sh '''
                . venv/bin/activate
                python3 ai_helper.py > ai_output.txt
                '''
                script {
                    def output = readFile('ai_output.txt')
                    echo "${output}"
                }
            }
        }

        stage('Decision Engine') {
            steps {
                echo 'AI-based decision can be implemented here (retry, notify, fix)'
            }
        }
    }
}
