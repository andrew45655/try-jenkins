pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                sh "python -m py_compile main.py"
                stash(nameL 'compiled-results', includes: '*.py*')
            }
        }
    }

}