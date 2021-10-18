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
                script {
                    def para
                    try{
                        para = input (
                            message "Can we Proceed?",
                            ok "Yes",
                            submitter "prashantkumar",
                            parameters {
                                string(name: 'PERSON', defaultValue: 'ABC', description: 'Member')
                            }
                        )
                    } catch(all) {
                        echo "${para}, is not proceeding..."
                    }
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
