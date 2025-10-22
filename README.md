**Secure Cloud Architecture on AWS**

A multi-tier cloud application demonstrating secure infrastructure design, Docker-based deployment, and production-grade network isolation using AWS VPCs, Nginx, and FastAPI.

**🧠 Overview**

This project showcases how to design and deploy a secure, scalable cloud application following AWS best practices.
It uses a public subnet for the reverse proxy (Nginx) and a private subnet for the backend application (FastAPI) — ensuring that sensitive workloads are not directly exposed to the internet.

**🏗️ Architecture**

                +-----------------------------+
                |        Internet              |
                +---------------+--------------+
                                |
                                v
                    +----------------------+
                    |   Public Subnet      |
                    |  (Nginx Reverse Proxy)|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Private Subnet     |
                    |  (FastAPI + Docker)  |
                    +----------------------+
                               |
                               v
                    +----------------------+
                    |   PostgreSQL (RDS)   |
                    |   Private Network    |
                    +----------------------+

**🚀 Features**

🔐 Custom AWS VPC with public and private subnets

🌐 Nginx reverse proxy routing HTTPS traffic to the backend

🐳 Containerized backend using Docker

⚙️ Security groups restricting access between tiers

📜 SSL certificates issued via Let’s Encrypt (Certbot)

🧱 Deployed on AWS EC2 (Ubuntu) following cloud security best practices


**🧰 Tech Stack**

Cloud: AWS (EC2, VPC, Security Groups)
Backend: FastAPI
Proxy: Nginx
Containerization: Docker
SSL: Certbot (Let’s Encrypt)
OS: Ubuntu 24.04

**🧾 Deployment Overview**

1. Create a custom VPC with public and private subnets.

2. Deploy Nginx as a reverse proxy in the public subnet.

3. Deploy the FastAPI backend in the private subnet.

4. Configure security groups for strict access control.

5. Obtain and install SSL certificate using Certbot.

6. Verify HTTPS access at: https://ishan-visionary.tech


**🧠 Key Learning Outcomes**

Hands-on experience with secure cloud architecture principles.

Understanding of reverse proxying, subnets, and SSL configuration.

Real-world application of network isolation and access control.


**🌐 Live Demo**
👉 https://ishan-visionary.tech

**💻 Repository 📂**
[GitHub Repository](https://github.com/IshanLenin/Image-analyzer)




