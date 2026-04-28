import os

footer_html = """  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-top">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a href="index.html" class="nav-logo">AV<span class="dot">.</span></a>
            <p class="footer-desc">Membangun pengalaman web yang modern, interaktif, dan berkesan. Siap berkolaborasi untuk proyek impianmu.</p>
          </div>
          <div class="footer-links-group">
            <h4 class="footer-title">Jelajahi</h4>
            <ul class="footer-links">
              <li><a href="index.html">Home</a></li>
              <li><a href="about.html">About Me</a></li>
              <li><a href="portofolio.html">Portfolio</a></li>
              <li><a href="special.html">Special Section</a></li>
            </ul>
          </div>
          <div class="footer-links-group">
            <h4 class="footer-title">Hubungi Saya</h4>
            <ul class="footer-links">
              <li><a href="contact.html">Contact Form</a></li>
              <li><a href="mailto:agiefgante@gmail.com">agiefgante@gmail.com</a></li>
              <li><a href="tel:08988650502">0898 8650 502</a></li>
            </ul>
          </div>
          <div class="footer-social">
            <h4 class="footer-title">Socials</h4>
            <div class="social-icons">
              <a href="https://instagram.com/gf.vemz" target="_blank" aria-label="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
              <a href="https://github.com/AgiefVemas" target="_blank" aria-label="GitHub"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg></a>
              <a href="https://open.spotify.com/user/31fblw3y67f33d7x2t5ov73mzhp4?si=bb8d3df626c74de9" target="_blank" aria-label="Spotify"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.84.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.02.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.6.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/></svg></a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <div class="footer-bottom-inner">
          <p>&copy; 2025 Agief Vemas Afrivanzah. All rights reserved.</p>
          <button class="back-to-top" aria-label="Back to top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
          </button>
        </div>
      </div>
    </div>
  </footer>"""

footer_css = """

/* ===========================
   FOOTER ENHANCEMENTS
=========================== */
.footer {
    background-color: var(--surface);
    border-top: 1px solid var(--border);
    padding-top: 80px;
    position: relative;
    overflow: hidden;
    margin-top: 60px;
}

.footer::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.05) 0%, transparent 60%);
    pointer-events: none;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 40px;
    margin-bottom: 60px;
    position: relative;
    z-index: 1;
}

@media (max-width: 992px) {
    .footer-grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 576px) {
    .footer-grid {
        grid-template-columns: 1fr;
        gap: 30px;
    }
}

.footer-brand .nav-logo {
    display: inline-block;
    margin-bottom: 20px;
    font-size: 2rem;
}

.footer-desc {
    color: var(--muted);
    font-size: 0.95rem;
    line-height: 1.6;
    max-width: 350px;
}

.footer-title {
    font-size: 1.1rem;
    margin-bottom: 24px;
    color: var(--text-bright);
    font-weight: 700;
}

.footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-links li {
    margin-bottom: 12px;
}

.footer-links a {
    color: var(--muted);
    font-size: 0.95rem;
    transition: all var(--transition);
    display: inline-block;
    position: relative;
}

.footer-links a:hover {
    color: var(--accent);
    transform: translateX(5px);
}

.social-icons {
    display: flex;
    gap: 16px;
}

.social-icons a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    background: var(--surface2);
    color: var(--text);
    border-radius: 50%;
    transition: all var(--transition);
}

.social-icons a:hover {
    background: var(--gradient-primary);
    color: white;
    transform: translateY(-5px);
    box-shadow: var(--shadow-glow);
}

.footer-bottom {
    border-top: 1px solid var(--border);
    padding: 24px 0;
    background: rgba(255, 255, 255, 0.5);
    position: relative;
    z-index: 1;
}

.footer-bottom-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}

.footer-bottom p {
    color: var(--muted);
    font-size: 0.9rem;
    margin: 0;
}

.back-to-top {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: var(--surface2);
    color: var(--accent);
    border-radius: 12px;
    transition: all var(--transition);
    border: none;
    cursor: pointer;
}

.back-to-top:hover {
    background: var(--accent);
    color: white;
    transform: translateY(-3px);
}
"""

html_files = ['index.html', 'about.html', 'contact.html', 'portofolio.html', 'special.html']

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start_idx = content.find('<!-- FOOTER -->')
        if start_idx != -1:
            end_idx = content.find('</footer>', start_idx)
            if end_idx != -1:
                end_idx += len('</footer>')
                new_content = content[:start_idx] + footer_html + content[end_idx:]
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated footer in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

try:
    with open('css/style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    if "FOOTER ENHANCEMENTS" not in css_content:
        with open('css/style.css', 'a', encoding='utf-8') as f:
            f.write(footer_css)
        print("Appended footer CSS to style.css")
except Exception as e:
    print(f"Error updating style.css: {e}")
