pipeline {
    agent any
    parameter
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
            environment {
                jiraStoryList = "foo"
            }
            steps {
                script {
                    jiraStoryList = sh(script: "python jiraStory.py", returnStdout: true).toString().trim()
                    echo 'Story ID: ${jiraStoryList}'
                }
            }
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
