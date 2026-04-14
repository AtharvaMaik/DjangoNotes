import base64
import os

def get_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Finalized HTML Template with Online Compiler Integration
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Project Report - Minimalist Notes Application</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <!-- PDF Library -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    
    <style>
        @font-face {{
            font-family: 'Aptos';
            src: local('Aptos'), local('Segoe UI'), local('Inter'), local('system-ui');
        }}

        :root {{
            --primary-blue: #2563eb;
            --secondary-blue: #3b82f6;
            --text-main: #1e293b;
        }}

        body {{
            background-color: #f1f5f9;
            font-family: 'Aptos', 'Segoe UI', 'Inter', sans-serif;
            font-size: 11pt;
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }}

        #reportContent {{
            background: white;
            width: 210mm;
            margin: 0 auto;
            padding: 30mm 20mm;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }}

        section {{ margin-bottom: 40px; }}
        h2 {{ font-size: 1.8rem; color: #0f172a; border-bottom: 2px solid var(--primary-blue); padding-bottom: 10px; margin-top: 50px; margin-bottom: 25px; }}
        h2:first-of-type {{ margin-top: 0; }}
        h3 {{ font-size: 1.3rem; margin-top: 30px; font-weight: 600; }}
        p {{ margin-bottom: 1.2rem; text-align: justify; }}

        .figure {{ margin: 30px 0; text-align: center; page-break-inside: avoid; }}
        .screenshot {{ width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .caption {{ font-size: 0.9rem; color: var(--text-muted); margin-top: 10px; font-style: italic; }}

        .tech-card {{ background-color: #f8fafc; border-left: 4px solid var(--primary-blue); padding: 20px; margin: 25px 0; page-break-inside: avoid; }}
        pre {{ background: #1e293b; color: #f8fafc; padding: 15px; border-radius: 8px; font-size: 0.85rem; margin-top: 15px; page-break-inside: avoid; word-wrap: break-word; white-space: pre-wrap; }}

        #controls {{
            position: fixed;
            top: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }}

        .btn-dl {{
            background-color: var(--primary-blue);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 600;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.1);
            transition: all 0.3s;
            text-decoration: none;
            text-align: center;
        }}

        .btn-latex {{
            background-color: #059669; /* Green for LaTeX */
            box-shadow: 0 4px 6px rgba(5, 150, 105, 0.1);
        }}

        .btn-dl:hover {{
            transform: translateY(-2px);
            opacity: 0.9;
            color: white;
        }}

        @media print {{
            #controls {{ display: none !important; }}
            #reportContent {{ width: 100%; margin: 0; padding: 0; box-shadow: none; }}
            h2 {{ page-break-before: always; }}
        }}
    </style>
</head>
<body>

    <div id="controls" class="no-print">
        <a href="https://latexonline.cc/compile?git=https://github.com/AtharvaMaik/DjangoNotes&target=report.tex&branch=jazzyfucnts" 
           target="_blank" class="btn-dl btn-latex">
            Download High-Quality PDF (via LaTeX Online)
        </a>
        <button onclick="generatePDF()" class="btn-dl">
            Download Fast Preview PDF (Internal)
        </button>
    </div>

    <div id="reportContent">
        <div style="text-align: center; height: 1000px; display: flex; flex-direction: column; justify-content: center; padding-bottom: 200px;">
            <h1 style="font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 10px;">Minimalist Notes App</h1>
            <p style="text-transform: uppercase; letter-spacing: 2px; color: #64748b; margin-bottom: 60px;">Final Project Report | Web Programming Lab</p>
            
            <img src="data:image/png;base64,{main_app_b64}" alt="Hero Image" style="width: 80%; max-width: 500px; margin: 0 auto 60px auto; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            
            <div style="border-top: 1px solid #e2e8f0; padding-top: 40px; font-size: 1.2rem;">
                <p>SUBMITTED BY:</p>
                <p style="font-weight: 600; color: var(--primary-blue); margin: 5px 0;">Atharva Maikhuri (235816206)</p>
                <p style="font-weight: 600; color: var(--primary-blue); margin: 5px 0;">Harshita Gaurav (235816036)</p>
            </div>
            
            <div style="margin-top: 100px; color: #64748b;">
                <p>APRIL 14, 2026</p>
                <p style="font-size: 0.9rem;">DEPARTMENT OF COMPUTER APPLICATIONS</p>
            </div>
        </div>

        <section id="section1">
            <h2>1. Project Objective and Scope</h2>
            <p>The core objective of this project is to develop a lightweight web application focusing on the integration of a Python-based backend (Django) with a dynamic JavaScript frontend (jQuery & AJAX).</p>
        </section>

        <section id="section2">
            <h2>2. Design Philosophy: The Power of Minimalism</h2>
            <p>In modern web development, "Minimalism" is used to reduce cognitive load while ensuring high-quality interactions and a professional feel.</p>
        </section>

        <section id="section4">
            <h2>3. Scalability and Efficiency</h2>
            <p>The system is designed to handle growth effortlessly via the Django ORM, ensuring longevity and ease of maintenance.</p>
            <div class="figure">
                <img src="data:image/png;base64,{main_app_b64}" class="screenshot" alt="Main Dashboard">
                <p class="caption">Figure 1.0: Live metrics updated via background AJAX tasks.</p>
            </div>
        </section>

        <section id="section6">
            <h2>4. Security and Input Integrity</h2>
            <p>Security is a primary pillar, with CSRF protection and real-time input validation enforced throughout the application lifecycle.</p>
            <div class="figure">
                <img src="data:image/png;base64,{validation_b64}" class="screenshot" alt="Validation Error">
                <p class="caption">Figure 2.0: Validation logic preventing invalid database entries.</p>
            </div>
        </section>

        <section id="section8">
            <h2>5. Dynamic Modals & Maintenance</h2>
            <p>Centered editing experience via Bootstrap Modals ensures zero-distraction updates to existing data.</p>
            <div class="figure">
                <img src="data:image/png;base64,{edit_modal_b64}" class="screenshot" alt="Edit Modal">
                <p class="caption">Figure 3.0: High-focus editing environment powered by Bootstrap 5.</p>
            </div>
        </section>

        <section id="conclusion">
            <h2>Conclusion</h2>
            <p>The Minimalist Notes Application successfully fulfills all requirements. By bridging Python strengths with JavaScript agility, we have produced a functional, high-end web application from scratch.</p>
        </section>
    </div>

    <script>
        function generatePDF() {{
            const element = document.getElementById('reportContent');
            const opt = {{
                margin: [10, 0, 10, 0],
                filename: 'Notes_App_Preview.pdf',
                image: {{ type: 'jpeg', quality: 0.98 }},
                html2canvas: {{ scale: 2, useCORS: true }},
                jsPDF: {{ unit: 'mm', format: 'a4', orientation: 'portrait' }},
                pagebreak: {{ mode: ['css', 'legacy'] }}
            }};

            // Force breaks before H2s
            element.querySelectorAll('h2').forEach((h, i) => {{
                if (i > 0) h.style.pageBreakBefore = 'always';
            }});

            html2pdf().set(opt).from(element).save();
        }}
    </script>
</body>
</html>
"""

# Embed images
main_app = get_base64("c:/AISH20/WP PROJECT/main_app.png")
edit_modal = get_base64("c:/AISH20/WP PROJECT/edit_modal.png")
validation = get_base64("c:/AISH20/WP PROJECT/validation_error.png")

final_html = html_template.format(
    main_app_b64=main_app,
    edit_modal_b64=edit_modal,
    validation_b64=validation
)

with open("c:/AISH20/WP PROJECT/report.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Report updated with Online Compiler integration!")
