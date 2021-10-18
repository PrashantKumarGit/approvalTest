pipeline {
    agent any
    parameters {
        string(name: 'StoryLine', defaultValue: '', description: 'How should I greet the world?')
    }
    environment {
                jiraStoryList = "foo"
     }
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
        stage('Get Jira Story') {
            steps {
                script {
                    jiraStoryList = sh(script: "python jiraStory.py ${params.StoryLine}", returnStdout: true).toString().trim()
                    echo 'Story ID: ${jiraStoryList}'
                }
            }
        }
        stage('Approval') {
            steps {
                echo 'Approving...'
                timeout(time: 1, unit: 'DAYS') {
                    input message: "${jiraStoryList}", submitter: 'prashantkumar', parameters {string(name:'PERSON', defaultValue: 'Bhaskar', description: 'username can be entered')}
                    echo "${PERSON}, is proceeding..."
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
