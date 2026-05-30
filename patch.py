import re

with open(r'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix mobile-visible CSS
content = content.replace('.nav-socials a:hover {\n            color: var(--accent-purple);\n            transform: scale(1.1);\n        }',
                          '.nav-socials a:hover {\n            color: var(--accent-purple);\n            transform: scale(1.1);\n        }\n\n        .mobile-visible {\n            display: none !important;\n        }')

# 2. Inside mobile media query, make mobile-visible display flex
content = content.replace('.nav-socials.mobile-visible {\n                display: flex;\n                margin-top: 15px;\n                justify-content: center;\n            }',
                          '.nav-socials.mobile-visible {\n                display: flex !important;\n                margin-top: 15px;\n                justify-content: center;\n            }')

# 3. Replace .project-about CSS with Modal CSS and button CSS
old_project_about_css = """.project-about {
            margin-bottom: 20px;
            padding: 15px;
            background: var(--bg-secondary);
            border-radius: 8px;
            border-left: 3px solid var(--accent-blue);
            font-size: 0.9rem;
            color: var(--text-secondary);
            flex-grow: 1;
        }

        .project-about h4 {
            font-size: 0.95rem;
            color: var(--text-primary);
            margin-bottom: 8px;
        }"""

new_modal_css = """/* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(10, 10, 15, 0.85);
            backdrop-filter: blur(5px);
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        :root.light-theme .modal {
            background-color: rgba(248, 249, 250, 0.85);
        }

        .modal.show {
            display: flex;
            opacity: 1;
        }

        .modal-content {
            background-color: var(--bg-card);
            border: 1px solid var(--accent-blue);
            border-radius: 12px;
            width: 90%;
            max-width: 600px;
            padding: 30px;
            position: relative;
            transform: translateY(-20px);
            transition: transform 0.3s ease;
            box-shadow: 0 15px 40px rgba(0, 212, 255, 0.15);
        }

        .modal.show .modal-content {
            transform: translateY(0);
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 20px;
            color: var(--text-secondary);
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            transition: color 0.3s;
        }

        .close-modal:hover {
            color: var(--accent-blue);
        }

        #modalTitle {
            margin-bottom: 15px;
            color: var(--accent-blue);
            font-size: 1.5rem;
        }

        #modalBody {
            color: var(--text-secondary);
            font-size: 1.05rem;
            line-height: 1.6;
        }

        .btn-project-about {
            background: transparent;
            color: var(--accent-purple);
            border: 1px solid var(--border-color);
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: var(--transition);
            margin-bottom: 20px;
            align-self: flex-start;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            flex-grow: 0;
        }

        .btn-project-about:hover {
            border-color: var(--accent-purple);
            background: rgba(124, 92, 191, 0.1);
        }"""
content = content.replace(old_project_about_css, new_modal_css)

content = content.replace('.project-desc {\n            color: var(--text-secondary);\n            font-size: 0.95rem;\n            margin-bottom: 15px;\n        }',
                          '.project-desc {\n            color: var(--text-secondary);\n            font-size: 0.95rem;\n            margin-bottom: 15px;\n            flex-grow: 1;\n        }')

# 4. Replace project cards inline about with buttons
project_about_pattern = r'<div class="project-about">\s*<h4>About Project</h4>\s*<p>(.*?)</p>\s*</div>'
matches = list(re.finditer(project_about_pattern, content))
project_descs = [m.group(1) for m in matches]

for i in range(1, 8):
    html_to_replace = f'<div class="project-about">\n                    <h4>About Project</h4>\n                    <p>{project_descs[i-1]}</p>\n                </div>'
    new_html = f'<button class="btn-project-about" onclick="openModal(\'proj{i}\')"><i class="fa-solid fa-circle-info"></i> About Project</button>'
    content = content.replace(html_to_replace, new_html)

# 5. Add Modal HTML to bottom before script
modal_html = """
    <!-- Project Modal -->
    <div id="projectModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal()">&times;</span>
            <h3 id="modalTitle">Project Details</h3>
            <div id="modalBody"></div>
        </div>
    </div>
"""
content = content.replace('<!-- Scripts -->', modal_html + '\n    <!-- Scripts -->')

# 6. Add JS for modal
modal_js = f"""
        // Modal Logic
        const projectDetails = {{
            proj1: {{ title: "Spam Email & SMS Detector", desc: "{project_descs[0]}" }},
            proj2: {{ title: "Career Path Predictor", desc: "{project_descs[1]}" }},
            proj3: {{ title: "MX Fluid — B2B E-Commerce Platform", desc: "{project_descs[2]}" }},
            proj4: {{ title: "AI Healthcare Management System", desc: "{project_descs[3]}" }},
            proj5: {{ title: "HR Analytics Dashboard", desc: "{project_descs[4]}" }},
            proj6: {{ title: "Intelligent Face Recognition Attendance", desc: "{project_descs[5]}" }},
            proj7: {{ title: "OCR Web Application", desc: "{project_descs[6]}" }}
        }};

        function openModal(id) {{
            document.getElementById('modalTitle').innerText = projectDetails[id].title;
            document.getElementById('modalBody').innerHTML = "<p>" + projectDetails[id].desc + "</p>";
            document.getElementById('projectModal').classList.add('show');
        }}

        function closeModal() {{
            document.getElementById('projectModal').classList.remove('show');
        }}

        // Close modal when clicking outside
        window.onclick = function(event) {{
            const modal = document.getElementById('projectModal');
            if (event.target == modal) {{
                closeModal();
            }}
        }}
"""
content = content.replace('// Theme Toggle Logic', modal_js + '\n        // Theme Toggle Logic')

# 7. Redesign Contact section
old_contact_cards = """<div class="contact-cards fade-in">
                <a href="mailto:bagoriahimanshu2608@gmail.com" class="contact-card">
                    <div class="contact-icon"><i class="fa-solid fa-envelope"></i></div>
                    <div class="contact-info">
                        <div class="contact-label">Email</div>
                        <div class="contact-value" style="font-size: 0.9rem;">bagoriahimanshu2608@gmail.com</div>
                    </div>
                    <div class="contact-action">Send Email <i class="fa-solid fa-arrow-right"></i></div>
                </a>

                <a href="https://wa.me/919599178756" target="_blank" rel="noopener" class="contact-card">
                    <div class="contact-icon"><i class="fa-brands fa-whatsapp"></i></div>
                    <div class="contact-info">
                        <div class="contact-label">WhatsApp</div>
                        <div class="contact-value">+91 9599178756</div>
                    </div>
                    <div class="contact-action" style="color: var(--accent-green);">Message <i class="fa-solid fa-arrow-right"></i></div>
                </a>

                <a href="https://www.linkedin.com/in/himanshu-bagoria0826" target="_blank" rel="noopener" class="contact-card">
                    <div class="contact-icon"><i class="fa-brands fa-linkedin"></i></div>
                    <div class="contact-info">
                        <div class="contact-label">LinkedIn</div>
                        <div class="contact-value">@himanshu-bagoria0826</div>
                    </div>
                    <div class="contact-action" style="color: #007bb5;">Connect <i class="fa-solid fa-arrow-right"></i></div>
                </a>

                <a href="https://github.com/Himanshu-Bagoria" target="_blank" rel="noopener" class="contact-card">
                    <div class="contact-icon" style="color: var(--text-primary);"><i class="fa-brands fa-github"></i></div>
                    <div class="contact-info">
                        <div class="contact-label">GitHub</div>
                        <div class="contact-value">@Himanshu-Bagoria</div>
                    </div>
                    <div class="contact-action" style="color: var(--text-primary);">View Profile <i class="fa-solid fa-arrow-right"></i></div>
                </a>

                <a href="/himanshuResume.pdf" download class="contact-card" style="border-color: var(--accent-purple);">
                    <div class="contact-icon"><i class="fa-solid fa-download"></i></div>
                    <div class="contact-info">
                        <div class="contact-label">Resume</div>
                        <div class="contact-value">Himanshu_Resume.pdf</div>
                    </div>
                    <div class="contact-action" style="color: var(--accent-purple);">Download <i class="fa-solid fa-arrow-right"></i></div>
                </a>
            </div>"""

new_contact_cards = """<div class="contact-info-clean fade-in">
                <div style="margin-bottom: 30px; font-size: 1.1rem; color: var(--text-secondary); line-height: 1.8;">
                    <p>I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!</p>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px;">
                    <a href="mailto:bagoriahimanshu2608@gmail.com" style="display: flex; align-items: center; gap: 15px; font-size: 1.1rem; transition: var(--transition);" onmouseover="this.style.color='var(--accent-blue)'" onmouseout="this.style.color=''">
                        <i class="fa-solid fa-envelope" style="color: var(--accent-blue); font-size: 1.5rem; width: 30px; text-align: center;"></i> bagoriahimanshu2608@gmail.com
                    </a>
                    <a href="https://wa.me/919599178756" target="_blank" rel="noopener" style="display: flex; align-items: center; gap: 15px; font-size: 1.1rem; transition: var(--transition);" onmouseover="this.style.color='var(--accent-green)'" onmouseout="this.style.color=''">
                        <i class="fa-brands fa-whatsapp" style="color: var(--accent-green); font-size: 1.5rem; width: 30px; text-align: center;"></i> +91 9599178756
                    </a>
                </div>

                <div style="display: flex; gap: 20px;">
                    <a href="https://www.linkedin.com/in/himanshu-bagoria0826" target="_blank" rel="noopener" style="width: 50px; height: 50px; border-radius: 50%; background: rgba(0, 119, 181, 0.1); color: #0077b5; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; transition: var(--transition);" onmouseover="this.style.transform='scale(1.1)'; this.style.background='#0077b5'; this.style.color='#fff';" onmouseout="this.style.transform='scale(1)'; this.style.background='rgba(0, 119, 181, 0.1)'; this.style.color='#0077b5';"><i class="fa-brands fa-linkedin-in"></i></a>
                    
                    <a href="https://github.com/Himanshu-Bagoria" target="_blank" rel="noopener" style="width: 50px; height: 50px; border-radius: 50%; background: rgba(124, 92, 191, 0.1); color: var(--text-primary); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; transition: var(--transition);" onmouseover="this.style.transform='scale(1.1)'; this.style.background='var(--text-primary)'; this.style.color='var(--bg-primary)';" onmouseout="this.style.transform='scale(1)'; this.style.background='rgba(124, 92, 191, 0.1)'; this.style.color='var(--text-primary)';"><i class="fa-brands fa-github"></i></a>
                    
                    <a href="/himanshuResume.pdf" download style="width: 50px; height: 50px; border-radius: 50%; background: rgba(124, 92, 191, 0.1); color: var(--accent-purple); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; transition: var(--transition);" onmouseover="this.style.transform='scale(1.1)'; this.style.background='var(--accent-purple)'; this.style.color='#fff';" onmouseout="this.style.transform='scale(1)'; this.style.background='rgba(124, 92, 191, 0.1)'; this.style.color='var(--accent-purple)';"><i class="fa-solid fa-file-pdf"></i></a>
                </div>
            </div>"""

content = content.replace(old_contact_cards, new_contact_cards)

with open(r'index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
