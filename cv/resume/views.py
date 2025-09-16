# resume/views.py
from django.shortcuts import render

def cv(request):
    cv = {
        "name": "Aniket Singh",
        "title": "MS CS @ NYU",
        "location": "New York, NY 10025",
        "email": "aniketsingh@nyu.edu",
        "phone": "+1-646-425-1818",
        "linkedin": "aniketsingh222",

        "experience": [
            {
                "role": "Software Developer Intern",
                "company": "Infosys",
                "location": "Chennai, India",
                "start": "Apr 2023",
                "end": "May 2023",
                "bullets": [
                    "Launched an iOS hospital management system (Swift, SwiftUI, watchOS) in 20 days, enabling seamless patient data access.",
                    "Integrated and optimized Firebase-based workflows, reducing sync latency and ensuring real-time record updates.",
                    "Led a team of 10 developers in Agile sprints, improving delivery speed and scalability of new modules.",
                    "Proposed and deployed automated medicine tracking and patient data systems, cutting paperwork by 90% and accelerating operations.",
                ],
            }
        ],

        "projects": [
            {
                "name": "Sarcasm Detection via Contrastive Few-Shot Learning",
                "stack": "PyTorch, HuggingFace",
                "date": "Jan 2024 – May 2024",
                "bullets": [
                    "Engineered transformer-based models comparing Zero-Shot BART-MNLI vs Few-Shot SetFit MiniLM.",
                    "Built NLP pipelines for preprocessing, embeddings, and contrastive fine-tuning.",
                    "Quantified gains: 65% (Zero-Shot BART) → 82% (Few-Shot SetFit MiniLM) in low-resource NLP.",
                ],
            },
            {
                "name": "NSDC Transportation Analytics",
                "stack": "Pandas, Seaborn, Folium",
                "date": "Sep 2023 – Dec 2023",
                "bullets": [
                    "Analyzed geospatial/temporal NYC traffic data to identify high-risk accident zones.",
                    "Uncovered a 76.6% surge in Friday incidents, shaping policy reforms and infrastructure upgrades.",
                    "Built visualization dashboards to support data-driven city planning decisions.",
                ],
            },
            {
                "name": "Dog Breed Detection with YOLOv7 + WOA-CNN",
                "stack": "PyTorch, OpenCV",
                "date": "Jan 2023 – Apr 2023",
                "bullets": [
                    "Integrated YOLOv7 with WOA-enhanced CNN, boosting accuracy to 93.1% and surpassing baseline CNNs.",
                    "Published peer-reviewed research in IEEE ICCSP 2024.",
                ],
            },
            {
                "name": "HappyPaws: Appointment Booking & Community App",
                "stack": "SwiftUI, Firebase, Figma",
                "date": "Aug 2022 – Dec 2022",
                "bullets": [
                    "Launched a SwiftUI + Firebase booking platform, reducing scheduling time by 70% for dog parents.",
                    "Designed accessible UI/UX in Figma; community feature boosted engagement and secured Apple Accelerator (Bangalore) approval.",
                ],
            },
        ],

        "education": [
            {
                "degree": "Master of Science in Computer Science",
                "school": "New York University",
                "location": "New York, NY",
                "start": "Sep 2024",
                "end": "May 2026",
                "coursework": [
                    "Design & Analysis of Algorithms",
                    "Operating Systems",
                    "Principles of Database",
                    "Machine Learning",
                    "Big Data",
                    "Post-Quantum Cryptography",
                ],
            },
            {
                "degree": "Bachelor of Technology in Computer Science",
                "school": "SRM Institute of Science and Technology",
                "location": "Chennai, India",
                "start": "Sep 2020",
                "end": "May 2024",
                "coursework": [
                    "Data Mining",
                    "Biometrics",
                    "Application Development (ServiceNow)",
                    "Artificial Intelligence",
                ],
            },
        ],
        
        "skills": {
            "languages": ["C++", "Python", "SQL", "Swift", "HTML", "CSS", "JavaScript"],
            "frameworks": ["PyTorch", "HuggingFace", "TensorFlow", "Flask", "React", "Node.js"],
            "cloud_tools": ["AWS (ECS, S3)", "Azure", "Docker", "Kubernetes", "DynamoDB", "CI/CD", "GitHub"],
            "certifications": [
                "AWS Academy Data Analytics; Machine Learning; Cloud Foundations",
                "MathWorks ML Onramp; Oracle Database Foundations",
            ],
            "achievements": [
                "Top-5 team reviewed by Apple Accelerator (HappyPaws); newspaper coverage recognizing innovation."
            ],
        },
    }

    return render(request, "resume.html", {"cv": cv})
