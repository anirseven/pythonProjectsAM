// Test Jenkinsfile to verify that the program runs as intended. This is intended for Windows

pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                cleanWs()

                withPythonEnv('python') {
                    bat "python --version"
                    bat "pip -V"
                }

            }
        }
		stage('hello') {
			steps {
				cd pythonProject
				bat 'python -m pytest'
      }
    }
    }
}