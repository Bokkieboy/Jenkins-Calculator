# Cloud-Based Disaster Recovery System on AWS

## Overview
This project automates disaster recovery in AWS using Infrastructure as Code (IaC). It ensures business continuity by rapidly deploying and restoring services in case of failures. The system leverages Terraform, AWS Lambda, S3, and additional AWS services to create a robust, automated disaster recovery solution.

## Features
- **Automated Disaster Recovery**: Deploys recovery infrastructure automatically upon failure detection.
- **Infrastructure as Code (IaC)**: Uses Terraform to define and manage cloud resources.
- **CI/CD Integration**: Utilizes GitHub Actions and Jenkins for seamless deployment.
- **Backup & Restore**: Regularly backs up data using Amazon S3 and restores services when needed.
- **Monitoring & Alerts**: Integrates CloudWatch and SNS for real-time monitoring and notifications.
- **Security & Compliance**: Implements IAM roles and security best practices.

## Technologies Used
- **AWS Services**: EC2, S3, RDS, Lambda, CloudWatch, IAM, SNS
- **IaC Tools**: Terraform
- **Automation & CI/CD**: GitHub Actions, Jenkins
- **Scripting**: Python (for automation scripts)

## Project Structure
```
├── terraform/        # Terraform scripts for AWS infrastructure
├── scripts/          # Python scripts for automation
├── tests/            # Unit tests for infrastructure components
│   ├── __init__.py   # Marks this as a package
│   ├── test_*.py     # Test cases using unittest
├── .github/          # CI/CD workflows
├── README.md         # Project documentation
├── Jenkinsfile       # Pipeline definition for Jenkins
└── requirements.txt  # Python dependencies
```

## Installation & Setup
### Prerequisites
- AWS account with necessary permissions
- Terraform installed (`>=1.0`)
- Python (`>=3.8`) with required dependencies (`pip install -r requirements.txt`)

### Deployment Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/cloud-dr-system.git
   cd cloud-dr-system
   ```
2. **Set Up AWS Credentials**
   ```sh
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   ```
3. **Initialize and Apply Terraform**
   ```sh
   cd terraform
   terraform init
   terraform apply -auto-approve
   ```
4. **Run Tests**
   ```sh
   python3 -m unittest discover -s tests
   ```

## Contributing
Contributions are welcome! Please fork the repo and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

