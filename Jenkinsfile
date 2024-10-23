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
                sh "py.test test_calc.py" //--junit-xml test_result/results.xml
            }
            //post{
            //    always{
            //        junit 'test_result/results.xml'
            //    }
            }
        }
    }

}