pipeline{
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    tools{
        maven 'M3'
    }
    stages {
        stage('Desarrollo') {
            steps {
                echo "Actualizando datos repositorio"
                }
        }
        stage('QA'){
            steps{
                bat "docker build -t calcutest ."
                bat "docker run -d -p 20:80 --name calcutest calcutest"
                echo "Probando..."
                //bat 'pip3 install selenium'
                //bat 'pip3 install webdriver_manager'
                bat 'python test.py'
                bat "docker stop calcutest"
                bat "docker rm calcutest"
                bat "docker rmi calcutest"
            }
        }
        stage('Despliegue'){
            steps{
                echo "Generando imagen"
                bat "docker build -t calculadora ."
                echo "Desplegando..."
                bat "docker run -d -p 80:80 --name calculadora calculadora"
            }
        }
    }
}