pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/bindhuashokan643/Web-Application-Project-2.git'
            }
        }

        stage('Setup Env') {
            steps {
                bat '''
                "C:\\Users\\Rishu\\AppData\\Local\\Python\\bin\\python.exe" -m pip install --upgrade pip
                "C:\\Users\\Rishu\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                "C:\\Users\\Rishu\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v --alluredir=allure-results --html=report.html --self-contained-html
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                "C:\\Users\\Rishu\\Downloads\\allure-2.42.1\\allure-2.42.1\\bin\\allure.bat" generate allure-results --clean -o allure-report
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            archiveArtifacts artifacts: 'allure-report/**', fingerprint: true
        }
    }
}