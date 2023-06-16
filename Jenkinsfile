pipeline{
    agent any
    triggers {
        pollSCM 'H/5 * * * *'
    }
    tools{
        maven 'M3'
    }
    stages {
        stage('Desarrollo') {
            steps {
                git branch: 'main', credentialsId: 'jenkins-token', url: 'https://github.com/jhontaff/DevOps-Aut.git'
                echo "Actualizando datos repositorio"
                }
        }
        stage('QA'){
            steps{
                bat 'python --version'
                //bat 'pip install selenium'
                //bat 'pip install webdriver_manager'
                bat "docker build -t calcutest ."
                bat "docker run -d -p 80:80 --name calcutest calcutest"
                echo "Probando..."
                bat 'python test.py'
                script { def exitCode = powershell(returnStatus: true, script: 'echo $LASTEXITCODE')
                    if (exitCode == 0) {
                        echo 'El archivo se ejecutó correctamente.'
                    } else {
                        error 'El archivo no se ejecutó correctamente.'
                    }
                }
                bat "docker stop calcutest"
                bat "docker rm calcutest"
                bat "docker rmi calcutest"
            }
        }
        stage('Despliegue'){
            steps{
                bat "docker stop calculadora"
                bat "docker rm calculadora"
                bat "docker rmi calculadora"
                echo "Generando imagen"
                bat "docker build -t calculadora ."
                echo "Desplegando..."
                bat "docker run -d -p 80:80 --name calculadora calculadora"
            }
        }
    }
}