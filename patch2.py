import re

with open(r'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="contact-cards fade-in">'
end_marker = '</div>\n\n            <div class="contact-form fade-in">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
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
    
    content = content[:start_idx] + new_contact_cards + '\n\n            <div class="contact-form fade-in">' + content[end_idx + len(end_marker):]
    
    with open(r'index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced!")
else:
    print("Could not find markers")
