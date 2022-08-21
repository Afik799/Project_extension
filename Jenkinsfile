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
            sh 'python3 rest_app.py'
        }
    }
    stage('run_backend_test') {
        steps {
            sh 'python3 backend_testing.py'
        }
    }
    stage('run_clear') {
        steps {
            sh 'python3 clear_environemnt.py'
        }
    }
    stage('build_docker') {
        steps {
            sh 'docker build -t rest_app .'
        }
    }
    stage('push_docker_image') {
        steps {
            sh 'docker tag rest_app afik799/project_extension:rest_app'
            sh 'docker push afik799/project_extension:rest_app'
        }
    }
    stage('compose_version') {
        steps {
            sh 'echo IMAGE_TAG=$BUILD_NUMBER > .env'
        }
    }
    stage('docker_compose') {
        steps {
            sh 'docker-compose up -d'
        }
    }
    stage('test_dockerized_api') {
        steps {
            sh 'python3 backend_testing.py'
        }
    }
    stage ('docker_down') {
        steps {
            sh 'docker-compose down'
            sh 'docker rmi rest_app'
        }
    }
}
}
