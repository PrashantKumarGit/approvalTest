pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Approval') {
            steps {
                echo 'Approving...'
                timeout(time: 1, unit: 'DAYS') {
                    input message: "Checklist", submitter: 'prashantkumar'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
