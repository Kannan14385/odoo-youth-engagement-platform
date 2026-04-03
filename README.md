# 🌍 ERP-Based Youth Engagement & Fund Management Platform

![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67?style=for-the-badge&logo=odoo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## 📖 Project Overview
The ERP-Based Youth Engagement and Fund Management Platform is a centralized, large-scale ecosystem designed to bridge the gap between Youth, NGOs, and Donors. By tracking funds across activities and improving collaboration among all stakeholders, the system ensures optimal resource utilization, enhances financial transparency, and supports data-driven decision-making to strengthen the impact of youth development programs.

By solving the problem of scattered information, the platform provides a secure gateway for Students to build verified "social portfolios," empowers NGOs to broadcast resource requirements, and allows Donors/CSR organizations to pinpoint credible projects for funding.

---

## 👨‍💻 My Contribution: The Admin Module
As part of this overarching ecosystem, my primary focus was architecting and developing the **Admin Module**—the central backend control panel operating within the Odoo framework. 

Because data integrity and trust are the foundation of philanthropic funding, the Admin Module acts as the ultimate gatekeeper. It ensures that no user, project, grant, or event goes live on the public-facing community hub without strict administrative verification and approval. 

### ⚙️ Core Admin Features

#### 1. Advanced Stakeholder & Access Management
* **Role-Based Access Control (RBAC):** Engineered strict permission matrices for diverse user types, including Students, NGOs, Donors, CSR Companies, and Institutional Coordinators.
* **Profile Governance:** Automated workflows for administrators to review, verify, approve, suspend, or activate stakeholder accounts based on compliance checks.
* **Security & Credentials:** Managed secure login parameters, password policies, and system-wide admin communication settings.

#### 2. Comprehensive Content Approval Pipeline
* **Centralized Vetting:** Developed the backend authority matrix allowing admins to create, update, review, and approve critical platform content.
* **Content Types Managed:** Social Projects, Volunteer Internships, Community Events, Skill Development Workshops, Articles, Testimonies, and Blogs.
* **Dynamic Publishing:** Built the logic that automatically pushes approved backend data to the live, public-facing community website.

#### 3. Financial Mapping & Grant Management
* **Fund Tracking:** Facilitated complex backend fund mapping to track major donor and CSR contributions against specific on-ground project requirements.
* **Regulatory Compliance Data Entry:** Designed detailed data entry schemas for funding grants, capturing critical metrics such as thematic focus, grant size, eligibility, and legal compliance requirements (e.g., FCRA, 12A, 80G).

#### 4. Structured Data Collection Models
* **Project Posting Forms:** Captured granular project details including specific Sustainable Development Goal (SDG) alignments, volunteer capacity, locations, and multimedia.
* **Educational Tracking:** Modeled database schemas to track skill development programs, including organizing bodies, subject areas, and programmatic durations.
* **Recognition Systems:** Built forms to seamlessly track community awards and volunteer recognitions.

#### 5. Real-Time Dashboards & Analytics
* **Registration & Approval Dashboard:** Created interactive admin views displaying total user metrics, geographic locations, and a queue of pending content awaiting administrative review.
* **Power BI Integration:** Designed overarching analytical dashboards to help Donors and NGOs visualize funding trends, identify requirement gaps, and measure project impact.

---

## 🛠️ Technical Stack (Admin Module)
* **Backend Framework:** Odoo 18 (Python, ORM)
* **Database:** PostgreSQL
* **Frontend UI (Backend Views):** XML, QWeb
* **Analytics/Visualization:** Power BI
* **Architecture:** Modular ERP architecture with custom inherited models (`res.partner`, `res.users`) and newly authored tables (`youth.project`, `social.grant`, etc.)

---

## 📸 System Previews
> **Note:** *Admin Backend dashboard :
<img width="1016" height="538" alt="image" src="https://github.com/user-attachments/assets/e7edbd94-981b-441b-9afc-3e309013e6d4" />

<img width="1015" height="421" alt="image" src="https://github.com/user-attachments/assets/310879fe-0c8b-46a5-908d-81a99e12a933" />

Admin Frontend dashboard :

<img width="1016" height="546" alt="image" src="https://github.com/user-attachments/assets/af5e8c03-7696-4644-8619-92314308b9e4" />

Home page :

<img width="1016" height="538" alt="image" src="https://github.com/user-attachments/assets/b54fe4a2-d294-45f4-a7ef-32677ea87fb5" />

<img width="1016" height="354" alt="image" src="https://github.com/user-attachments/assets/448fe566-fcd3-4d2a-a8a8-27c24a3cd5df" />

<img width="1016" height="405" alt="image" src="https://github.com/user-attachments/assets/2e68ef4a-effa-4e7d-9b99-1b3324433f11" />
*

** ---

## 🚀 How to Run Locally
*Note: This repository contains the custom modules specifically developed for the Admin functionality. It requires a pre-existing Odoo 18 environment.*

1. Clone this repository into your Odoo `addons` directory:
   ```bash
   git clone [https://github.com/Kannan14385/YOUR_REPO_NAME.git](https://github.com/Kannan14385/YOUR_REPO_NAME.git)
