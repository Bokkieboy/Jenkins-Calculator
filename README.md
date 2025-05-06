# Jenkins Calculator  
Jenkins Calculator is a simple web-based calculator application developed to demonstrate Continuous Integration and Continuous Deployment (CI/CD) using Jenkins, Docker, and GitHub.  
## Features  
- Basic arithmetic operations (add, subtract, multiply, divide)  
- Dockerized application for easy deployment  
- Jenkins pipeline automation  
- GitHub integration with webhook-triggered builds  
- Post-build log generation for monitoring  
## Technologies Used  
- HTML/CSS/JavaScript (or React if extended)  
- Docker  
- Jenkins  
- Git & GitHub  
## Getting Started  
### Prerequisites  
- Docker installed on your system  
- Jenkins installed (locally or using Docker)  
- GitHub account  
### Clone the Repository  
`git clone https://github.com/Bokkieboy/Jenkins-Calculator.git && cd Jenkins-Calculator`  
### Running Locally with Docker  
`docker build -t simple-calculator . && docker run -p 3000:3000 simple-calculator`  
## Jenkins Setup  
1. Install Jenkins using Docker: `docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts`  
2. Complete the Jenkins setup wizard and install recommended plugins.  
3. Install additional plugins: Git, Docker Pipeline, GitHub Integration.  
4. Create a new Pipeline job.  
5. Configure the job: set Pipeline script from SCM, select Git, and use repository URL `https://github.com/Bokkieboy/Jenkins-Calculator.git`.  
6. Ensure webhook is configured on GitHub under Repo Settings > Webhooks, with Payload URL `http://<your-jenkins-host>/github-webhook/` and content type `application/json`.  
7. Add a `Jenkinsfile` to your repo that defines build, test, and deploy stages using Docker.  
8. Ensure Docker is accessible to the Jenkins container (mount the Docker socket).  
9. Trigger a build by pushing code to `main` branch.  
10. View build logs and results in Jenkins interface.  
## License  
This project is for educational purposes and is not intended for production use.
