pipeline {
    agent any

    stages {
        stage('Env GIT variables') {
            agent any
            steps {
                echo '${env.BRANCH_NAME}'
                echo '${env.CHANGE_ID}'
            }
        }
        stage('Env Jenkins variables') {
            agent any
            steps {
                echo '${env.BUILD_ID}'
                echo '${env.BUILD_NUMBER}'
                echo 'BUILD_TAG ${env.BUILD_TAG}'
                echo '${env.BUILD_URL}'
                echo 'EXECUTOR_NUMBER ${env.EXECUTOR_NUMBER}'
                echo '${env.JAVA_HOME}'
                echo '${env.JENKINS_URL}'
                echo '${env.JOB_NAME}'
                echo '${env.NODE_NAME}'
                echo '${env.WORKSPACE}'
            }
        }
        stage('Setting variables') {
            agent any
            environment {
                CC = 'DD'
            }
            steps {
                echo 'printenv'
            }
        }
    }
}