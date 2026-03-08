# AWS Serverless Contact Form

![Architecture Diagram](architecture.png)

A serverless contact form backend built using **Amazon API Gateway, AWS Lambda, and DynamoDB**.

This backend powers the **contact form on my portfolio website**, allowing users to submit messages which are processed by Lambda and stored in DynamoDB.

🌐 **Live Portfolio**  
https://dc61g20ci9ox4.cloudfront.net/

---

# Architecture Overview

This project follows a **serverless architecture** where the contact form sends requests to an API that triggers Lambda to store submissions in DynamoDB.

Workflow:

User → Portfolio Website → API Gateway → Lambda → DynamoDB → CloudWatch Logs

---

# AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- Amazon S3 (Portfolio hosting)
- Amazon CloudFront (Content delivery)

---

# Workflow

1. A user submits the contact form on the portfolio website.
2. The form sends a **POST request** to API Gateway.
3. API Gateway triggers **AWS Lambda**.
4. Lambda validates and processes the request.
5. Lambda stores the message in **DynamoDB**.
6. Execution logs are stored in **CloudWatch Logs** for monitoring and troubleshooting.

---

# API Gateway Configuration

API Gateway exposes an endpoint to receive form submissions.

### API Gateway Routes

![API Gateway Routes](API-Gateway-Routes.png)

### API Gateway Integration

![API Gateway Integration](API-Gateway-Integration.png)

---

# Lambda Function

The Lambda function processes the incoming request and stores form submissions in DynamoDB.

![Lambda Function](Lambda.png)

Responsibilities of the Lambda function:

- Parse request body
- Validate input data
- Generate unique submission ID
- Store submission in DynamoDB
- Return success response

---

# DynamoDB Table

Contact form submissions are stored in a DynamoDB table.

![DynamoDB Table](DynamoDB.png)

Each stored record contains:

- ID
- Name
- Email
- Message
- Timestamp

### Stored Items Example

![DynamoDB Items](dynamodb-items.png)

---

# CloudWatch Logs

CloudWatch logs help monitor Lambda execution and troubleshoot issues.

![CloudWatch Logs](cloudwatch-logs.png)

Logs confirm successful processing of form submissions.

---

# Security Implementation

This project follows AWS security best practices:

- IAM role with **least privilege**
- Lambda allowed only **dynamodb:PutItem**
- Input validation in Lambda
- Hidden honeypot field in the contact form to prevent spam

---

# Sample Request Payload

Example payload sent from the contact form to API Gateway:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, this is a test message."
}
```

---

# How to Test

1. Open the portfolio website:  
   https://dc61g20ci9ox4.cloudfront.net/

2. Navigate to the **Contact** section.

3. Submit a test message using the form.

4. Verify that the message appears in the **DynamoDB table**.

5. Check **CloudWatch Logs** to confirm Lambda execution.

---

# Challenges & Troubleshooting

### API Deployment Issue

Error:

```
Unable to deploy API because no valid routes exist
```

Fix:

Configured the correct **POST route and Lambda integration**.

---

### DynamoDB Permission Error

Error:

```
AccessDeniedException: dynamodb:PutItem
```

Fix:

Updated the **Lambda IAM role policy** to allow DynamoDB PutItem.

---

### API Testing Error

Error:

```
Invoke-RestMethod : {"message":"Not Found"}
```

Fix:

Used the correct **API Gateway endpoint and route path**.

---

# Project Structure

```
aws-serverless-contact-form/
│
├── README.md
├── lambda_function.py
├── architecture.png
├── API-Gateway-Routes.png
├── API-Gateway-Integration.png
├── Lambda.png
├── DynamoDB.png
├── dynamodb-items.png
└── cloudwatch-logs.png
```

---

# Future Improvements

Possible future enhancements:

- Email notifications using **Amazon SES**
- Input validation improvements
- Rate limiting
- CAPTCHA protection
- CloudWatch monitoring alarms

---

# Key Learnings

- Building serverless APIs with API Gateway
- Integrating Lambda with DynamoDB
- Implementing IAM least privilege policies
- Debugging applications with CloudWatch logs
- Designing end-to-end serverless architectures

---

# Author

**Jayveersinh Vihol**

AWS Cloud Practitioner | Aspiring Cloud Engineer

🌐 Portfolio  
https://dc61g20ci9ox4.cloudfront.net/

💻 GitHub  
https://github.com/Vjayveersinh
