pipeline{
    agent any
    options{
        skipStagesAfterUnstable()
    }
    stages{
        stage("Build"){
            steps{
                sh "python -m py_compile main.py"
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage("Test"){
            steps{
                sh "py.test --junit-xml test_result/results.xml test_calc.py" //
            }
            post{
                always{
                    junit 'test_result/results.xml'
                }
            }
        }
        stage("Delivery"){
            steps{
                sh "pyinstaller --onefile cal.py"
            }
            post{
                always{
                    archiveArtifacts 'dist/cal'
                }
            }
        }
    }

}