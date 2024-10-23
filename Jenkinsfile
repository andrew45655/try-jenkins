pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                sh "python -m py_compile main.py"
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage("Test"){
            steps{
                sh "py.test  --junit-xml test-reports/results.xml test_calc.py"
            }
            post{
                always{
                    junit 'test-reports/result.xml'
                }
            }
        }
    }

}