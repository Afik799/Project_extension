pipeline { agent any
stages {
    stage('pulling_repo') {
        steps {
            sh 'cd /Users/afik.navaro/DevOps_Class/Project_extension/Project'
            sh 'git init'
            sh 'git pull https://github.com/Afik799/Project_extension'
        }
    }
    stage('run_backend_app') {
        steps {
            sh 'nohup python3 rest_app.py &'
        }
    }
    stage('run_front_app') {
        steps {
            sh 'nohup python3 web_app.py &'
        }
    }
    stage('run_backend_test') {
        steps {
            sh 'python3 backend_testing.py'
        }
    }
    stage('run_front_test') {
        steps {
            sh 'python3 frontend_testing.py'
        }
    }
    stage('run_combined_test') {
        steps {
            sh 'python3 combined_testing.py'
        }
    }
    stage('run_clear') {
        steps {
            sh 'python3 clear_environemnt.py'
        }
    }
}
}