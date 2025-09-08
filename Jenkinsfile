pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests with Pytest + Allure') {
            steps {
                bat '''
                    cd C:\\Users\\unforsaken\\Desktop\\temp\\pytest-starter
                    call venv\\Scripts\\activate.bat
                    pytest --alluredir=reports
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        failure {
            echo 'Build failed! 請檢查測試結果'
        }
    }
}
