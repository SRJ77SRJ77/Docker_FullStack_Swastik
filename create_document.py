from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from pathlib import Path

project = Path.home() / "Desktop/Docker_FullStack_Swastik"
screenshots = project / "screenshots"

doc = Document()

# Page formatting
section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)

# Default font
style = doc.styles["Normal"]
style.font.name = "Arial"
style.font.size = Pt(10)

# Title
title = doc.add_heading("DOCKER FULL STACK APPLICATION", 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph("DEVOPS ASSIGNMENT")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

p = doc.add_paragraph("Submitted by: Swastik")
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph("")

doc.add_heading("1. Objective", level=1)
doc.add_paragraph(
    "The objective of this assignment is to containerize a full-stack "
    "application consisting of a Node.js/Express frontend and a Flask "
    "backend using Docker and Docker Compose."
)

doc.add_heading("2. Technologies Used", level=1)
for item in [
    "Node.js and Express.js",
    "Python and Flask",
    "Docker and Docker Compose",
    "Git and GitHub",
    "Docker Hub"
]:
    doc.add_paragraph(item, style="List Bullet")

doc.add_heading("3. Project Structure", level=1)
doc.add_paragraph(
    "The application is organized into separate frontend and backend "
    "directories. Each service contains its own Dockerfile. The "
    "docker-compose.yml file defines and connects both services."
)

doc.add_heading("4. Frontend Implementation", level=1)
doc.add_paragraph(
    "The frontend is developed using Node.js and Express. It serves "
    "a web form on port 3000 and forwards form submissions to the "
    "Flask backend."
)

doc.add_heading("5. Backend Implementation", level=1)
doc.add_paragraph(
    "The backend is developed using Flask. It receives submitted "
    "form data through the /api/submit endpoint on port 5000 and "
    "processes the request."
)

doc.add_heading("6. Docker Configuration", level=1)
doc.add_paragraph(
    "Separate Dockerfiles were created for the frontend and backend. "
    "Docker Compose builds and starts both containers in a shared "
    "network, allowing the frontend to communicate with the backend."
)

doc.add_heading("7. Project Structure Screenshot", level=1)
doc.add_paragraph(
    "The following screenshot shows the frontend, backend, Docker "
    "configuration, README and screenshots directories."
)

def add_screenshot(filename, caption):
    path = screenshots / filename
    if path.exists():
        doc.add_picture(str(path), width=Inches(6.0))
        p = doc.add_paragraph(caption)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        doc.add_paragraph("Screenshot missing: " + filename)

add_screenshot(
    "01-project-structure.png",
    "Figure 1: Full project directory structure"
)

doc.add_heading("8. Docker Build", level=1)
doc.add_paragraph(
    "Docker Compose successfully built the frontend and backend images "
    "and started both containers."
)
add_screenshot("02-docker-build.png", "Figure 2: Docker Compose build")

doc.add_heading("9. Running Containers", level=1)
doc.add_paragraph(
    "The docker ps command confirmed that the Node.js frontend and "
    "Flask backend containers were running."
)
add_screenshot("03-running-containers.png", "Figure 3: Running containers")

doc.add_heading("10. Docker Images", level=1)
doc.add_paragraph(
    "The Docker images were built locally and uploaded to Docker Hub."
)
add_screenshot("04-docker-images.png", "Figure 4: Docker images")

doc.add_heading("11. Backend Integration Test", level=1)
doc.add_paragraph(
    "The frontend successfully sent a POST request to the Flask "
    "endpoint /api/submit. The backend returned HTTP status 200, "
    "confirming successful request processing."
)
add_screenshot("05-backend-success.png", "Figure 5: Successful backend POST request")

doc.add_heading("12. Frontend Form Result", level=1)
doc.add_paragraph(
    "The frontend form was tested in the browser by submitting sample "
    "information and checking the displayed result."
)
add_screenshot("06-frontend-form-result.png", "Figure 6: Frontend form test")

doc.add_heading("13. Docker Hub Images", level=1)
doc.add_paragraph(
    "Frontend image: https://hub.docker.com/r/riskseishq/docker-frontend"
)
doc.add_paragraph(
    "Backend image: https://hub.docker.com/r/riskseishq/flask-backend"
)

doc.add_heading("14. GitHub Repository", level=1)
doc.add_paragraph(
    "Project source code: "
    "https://github.com/SRJ77SRJ77/Docker_FullStack_Swastik"
)

doc.add_heading("15. Conclusion", level=1)
doc.add_paragraph(
    "The full-stack application was successfully containerized using "
    "Docker and Docker Compose. Both containers ran successfully, "
    "frontend-to-backend communication was verified, Docker images "
    "were uploaded to Docker Hub, and source code was pushed to GitHub."
)

output = project / "Docker_FullStack_Documentation.docx"
doc.save(output)

print("Documentation created successfully:", output)
