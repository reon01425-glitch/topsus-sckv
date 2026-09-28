# -*- coding: utf-8 -*-
"""
Script to inject the Kill Chain Matrix Modal into index.html
matching the uploaded diagram from Modul02_Kelompok05_Updated.pdf
"""

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Team Profile in modalTeam
    team_old = '''        <p><strong>Kelompok Tugas:</strong> Kelompok 05 (Kelompok Cipta dkk.)</p>
        <br />
        <p><strong>Topik Proyek:</strong> Analisis Model Ancaman (Threat Modeling) &amp; Arsitektur Pertahanan Berlapis (Defense in Depth) pada Sistem Pembayaran Elektronik (FinTech E-Wallet).</p>'''
    
    team_new = '''        <p><strong>Kelompok Tugas:</strong> Kelompok 05 (Tugas Modul 02: Ancaman &amp; Threat Landscape)</p>
        <div style="margin: 12px 0; background: rgba(255,255,255,0.04); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 10px 14px;">
          <strong style="color:#38bdf8; font-size:0.82rem;">Anggota Kelompok 05:</strong>
          <ol style="margin-top: 6px; padding-left: 20px; line-height: 1.6; font-size: 0.8rem; color: #f1f5f9;">
            <li><strong>Christiano Bryan Budiiman</strong> &mdash; NIM: 24060123130079</li>
            <li><strong>Cipta Fikri Wiratama</strong> &mdash; NIM: 24060123140172</li>
            <li><strong>Khairiya Fatih Izzudin Emarin</strong> &mdash; NIM: 24060123140166</li>
            <li><strong>Dewangga Ramadhan Halim</strong> &mdash; NIM: 24060124130118</li>
            <li><strong>Moses Morell Yosefan</strong> &mdash; NIM: 24060124130094</li>
          </ol>
        </div>
        <p><strong>Topik Proyek:</strong> Analisis Model Ancaman (Threat Modeling), Diagram Alur Serangan (Kill Chain) Per Vektor &amp; Arsitektur Pertahanan Berlapis (Defense in Depth) pada Aplikasi Dompet Digital (FinTech E-Wallet) &bull; UNDIP 2026.</p>'''

    if team_old in html:
        html = html.replace(team_old, team_new)
        print("Updated team members successfully.")
    else:
        print("Warning: team_old not found exactly.")

    # 2. Add Kill Chain button in toolbar
    btn_marker = '<button class="btn-tool" id="btnTeamModal"'
    btn_killchain = '''<button class="btn-tool" id="btnKillChainModal" title="Diagram Alur Serangan (Kill Chain) — Per Vektor (Halaman 3 Dokumen)" style="background: rgba(168, 85, 247, 0.15); border-color: #c084fc; color: #e9d5ff;">
          <span>🗺️</span> <strong>Matriks Kill Chain</strong>
        </button>
        '''
    if btn_marker in html and 'btnKillChainModal' not in html:
        html = html.replace(btn_marker, btn_killchain + btn_marker)
        print("Added Kill Chain button in toolbar.")

    # 3. Add Modal CSS for Kill Chain Panorama
    css_marker = '</style>'
    kc_css = '''
    /* KILL CHAIN MODAL & PANORAMA STYLES */
    .modal-box.modal-wide {
      max-width: 1400px;
      width: 96vw;
      max-height: 92vh;
    }
    .kc-container {
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding: 10px 4px;
    }
    .kc-row {
      border-radius: 12px;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: #111015;
      border: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      transition: all 0.25s;
    }
    .kc-row:hover {
      border-color: rgba(255, 255, 255, 0.2);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
    }
    .kc-row-v1 { background: #1c1012; border-color: rgba(239, 68, 68, 0.35); }
    .kc-row-v2 { background: #1c140c; border-color: rgba(245, 158, 11, 0.35); }
    .kc-row-v3a { background: #0c1822; border-color: rgba(6, 182, 212, 0.35); }
    .kc-row-v3b { background: #180e22; border-color: rgba(168, 85, 247, 0.35); }

    .kc-row-title {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      text-align: center;
      padding-bottom: 4px;
    }
    .kc-row-v1 .kc-row-title { color: #fca5a5; }
    .kc-row-v2 .kc-row-title { color: #fde68a; }
    .kc-row-v3a .kc-row-title { color: #7dd3fc; }
    .kc-row-v3b .kc-row-title { color: #d8b4fe; }

    .kc-flow-track {
      display: grid;
      grid-template-columns: repeat(5, 1fr) 1.25fr;
      gap: 10px;
      align-items: stretch;
    }
    @media (max-width: 1024px) {
      .kc-flow-track { grid-template-columns: 1fr; }
    }

    .kc-node {
      background: rgba(0, 0, 0, 0.45);
      border: 1.5px solid;
      border-radius: 10px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .kc-node:hover {
      transform: translateY(-3px);
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.6);
    }
    .kc-node.sim-active {
      transform: scale(1.04);
      box-shadow: 0 0 20px currentColor !important;
    }

    .kc-row-v1 .kc-node { border-color: #ef4444; color: #ef4444; }
    .kc-row-v2 .kc-node { border-color: #f59e0b; color: #f59e0b; }
    .kc-row-v3a .kc-node { border-color: #06b6d4; color: #06b6d4; }
    .kc-row-v3b .kc-node { border-color: #a855f7; color: #a855f7; }

    .kc-node-step {
      font-size: 0.72rem;
      font-weight: 800;
      color: #fff;
    }
    .kc-node-desc {
      font-size: 0.72rem;
      line-height: 1.35;
      color: var(--text-muted);
    }

    .kc-impact-card {
      border: 2px solid;
      border-radius: 10px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .kc-impact-card:hover {
      transform: scale(1.02);
    }
    .kc-impact-card.sim-active {
      transform: scale(1.05);
      box-shadow: 0 0 24px currentColor !important;
    }
    .kc-impact-label {
      font-size: 0.75rem;
      font-weight: 900;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .kc-impact-body {
      font-size: 0.73rem;
      line-height: 1.35;
      color: #f1f5f9;
    }

    .kc-row-v1 .kc-impact-card { background: rgba(239, 68, 68, 0.15); border-color: #ef4444; color: #f87171; }
    .kc-row-v2 .kc-impact-card { background: rgba(245, 158, 11, 0.15); border-color: #f59e0b; color: #fbbf24; }
    .kc-row-v3a .kc-impact-card { background: rgba(6, 182, 212, 0.15); border-color: #06b6d4; color: #38bdf8; }
    .kc-row-v3b .kc-impact-card { background: rgba(168, 85, 247, 0.15); border-color: #a855f7; color: #c084fc; }
  </style>
'''
    if 'KILL CHAIN MODAL & PANORAMA STYLES' not in html:
        html = html.replace(css_marker, kc_css)
        print("Added Kill Chain CSS.")

    # 4. Add Modal HTML for Kill Chain
    modal_insert_marker = '<!-- MODAL: DAFTAR PUSTAKA IEEE -->'
    kc_modal_html = '''<!-- MODAL: DIAGRAM ALUR SERANGAN (KILL CHAIN) PER VEKTOR -->
  <div class="modal-backdrop" id="modalKillChain">
    <div class="modal-box modal-wide">
      <div class="modal-head">
        <div>
          <h3 style="display:flex; align-items:center; gap:8px;">
            <span>DIAGRAM ALUR SERANGAN (KILL CHAIN) — PER VEKTOR</span>
          </h3>
          <p style="font-size:0.75rem; color:var(--text-muted); margin-top:2px;">
            Visualisasi tahapan serangan dari reconnaissance hingga impact pada Aplikasi Dompet Digital (Modul 02 Bab 2)
          </p>
        </div>
        <div style="display:flex; align-items:center; gap:10px;">
          <button class="btn-tool active" id="btnSimulateKillChain" style="background:#0284c7; border-color:#38bdf8; color:#fff;">
            <span>▶</span> Putar Simulasi Alur
          </button>
          <button class="modal-close-btn" data-close="modalKillChain">&times;</button>
        </div>
      </div>
      <div class="modal-body" style="padding:14px 18px;">
        <div class="kc-container">
          
          <!-- VEKTOR 1 -->
          <div class="kc-row kc-row-v1" id="kcRow1">
            <div class="kc-row-title">VEKTOR 1 — MOBILE BANKING TROJAN (Kill Chain)</div>
            <div class="kc-flow-track">
              <div class="kc-node" data-vec="1" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">1. Distribution</span>
                <span class="kc-node-desc">APK palsu disebar via store pihak ketiga, WA/Telegram group</span>
              </div>
              <div class="kc-node" data-vec="1" data-step="1" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">2. Installation</span>
                <span class="kc-node-desc">Trojan request izin Accessibility Service, persist di background</span>
              </div>
              <div class="kc-node" data-vec="1" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">3. Overlay Attack</span>
                <span class="kc-node-desc">Halaman login palsu muncul di atas app asli saat korban buka wallet</span>
              </div>
              <div class="kc-node" data-vec="1" data-step="3" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">4. Credential Capture</span>
                <span class="kc-node-desc">Keylogger rekam PIN + intercept OTP dari notifikasi SMS</span>
              </div>
              <div class="kc-node" data-vec="1" data-step="4" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">5. Exfiltration &amp; Fraud</span>
                <span class="kc-node-desc">Data dikirim ke C2 server &rarr; login akun korban &rarr; transfer ke mule</span>
              </div>
              <div class="kc-impact-card" data-vec="1" data-step="4" title="Klik untuk lihat dampak akhir">
                <div class="kc-impact-label">💥 IMPACT</div>
                <div class="kc-impact-body">Saldo terkuras<br />Akun terkunci<br />PII bocor</div>
              </div>
            </div>
          </div>

          <!-- VEKTOR 2 -->
          <div class="kc-row kc-row-v2" id="kcRow2">
            <div class="kc-row-title">VEKTOR 2 — PHISHING &amp; SOCIAL ENGINEERING (Kill Chain)</div>
            <div class="kc-flow-track">
              <div class="kc-node" data-vec="2" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">1. Reconnaissance</span>
                <span class="kc-node-desc">Kumpulkan data korban dari data leak, scraping media sosial</span>
              </div>
              <div class="kc-node" data-vec="2" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">2. Infrastructure</span>
                <span class="kc-node-desc">Buat phishing page + typosquat domain (d0mpet-pay.com)</span>
              </div>
              <div class="kc-node" data-vec="2" data-step="1" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">3. Mass Distribution</span>
                <span class="kc-node-desc">Blast SMS &amp; WhatsApp: "Akun Anda diblokir! Klik untuk verifikasi"</span>
              </div>
              <div class="kc-node" data-vec="2" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">4. Credential Harvest</span>
                <span class="kc-node-desc">Korban input HP + PIN + OTP di halaman palsu &rarr; dikirim via webhook</span>
              </div>
              <div class="kc-node" data-vec="2" data-step="3" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">5. Account Takeover</span>
                <span class="kc-node-desc">Login real app &lt; 60 detik &rarr; ganti PIN/HP &rarr; transfer keluar</span>
              </div>
              <div class="kc-impact-card" data-vec="2" data-step="3" title="Klik untuk lihat dampak akhir">
                <div class="kc-impact-label">💥 IMPACT</div>
                <div class="kc-impact-body">Saldo dikuras<br />Brand rusak<br />CS overload</div>
              </div>
            </div>
          </div>

          <!-- VEKTOR 3A -->
          <div class="kc-row kc-row-v3a" id="kcRow3a">
            <div class="kc-row-title">VEKTOR 3A — MAN-IN-THE-MIDDLE (Kill Chain)</div>
            <div class="kc-flow-track">
              <div class="kc-node" data-vec="3" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">1. Setup</span>
                <span class="kc-node-desc">Pasang rogue WiFi di tempat publik (cafe, mall, bandara)</span>
              </div>
              <div class="kc-node" data-vec="3" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">2. Victim Connects</span>
                <span class="kc-node-desc">Korban konek WiFi gratis &rarr; semua traffic lewat attacker proxy</span>
              </div>
              <div class="kc-node" data-vec="3" data-step="1" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">3. SSL Stripping</span>
                <span class="kc-node-desc">Downgrade HTTPS&rarr;HTTP jika cert validation lemah atau no cert pinning</span>
              </div>
              <div class="kc-node" data-vec="3" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">4. Session Hijack</span>
                <span class="kc-node-desc">Curi auth token / JWT dari traffic plaintext yang sudah di-strip</span>
              </div>
              <div class="kc-node" data-vec="3" data-step="3" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">5. Replay / Exploit</span>
                <span class="kc-node-desc">Replay transaksi lama atau inject request dari device attacker</span>
              </div>
              <div class="kc-impact-card" data-vec="3" data-step="3" title="Klik untuk lihat dampak akhir">
                <div class="kc-impact-label">💥 IMPACT</div>
                <div class="kc-impact-body">Transaksi ilegal<br />Session compromise<br />Data leak in-transit</div>
              </div>
            </div>
          </div>

          <!-- VEKTOR 3B -->
          <div class="kc-row kc-row-v3b" id="kcRow3b">
            <div class="kc-row-title">VEKTOR 3B — API EXPLOITATION (Kill Chain)</div>
            <div class="kc-flow-track">
              <div class="kc-node" data-vec="4" data-step="0" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">1. Reconnaissance</span>
                <span class="kc-node-desc">Download APK &rarr; decompile (jadx/apktool) &rarr; temukan API endpoint</span>
              </div>
              <div class="kc-node" data-vec="4" data-step="1" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">2. Vuln Discovery</span>
                <span class="kc-node-desc">Identifikasi BOLA/IDOR (user_id=1001 &rarr; 1002). Broken auth flow</span>
              </div>
              <div class="kc-node" data-vec="4" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">3. Exploitation</span>
                <span class="kc-node-desc">Iterasi user_id massal via scripted requests (Burp Intruder / Frida)</span>
              </div>
              <div class="kc-node" data-vec="4" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">4. Mass Data Extraction</span>
                <span class="kc-node-desc">Dump data jutaan user: PII, saldo, mutasi dalam hitungan jam</span>
              </div>
              <div class="kc-node" data-vec="4" data-step="2" title="Klik untuk lihat animasi tahap ini">
                <span class="kc-node-step">5. Monetization</span>
                <span class="kc-node-desc">Jual data di dark web atau gunakan untuk fraud / identity theft</span>
              </div>
              <div class="kc-impact-card" data-vec="4" data-step="2" title="Klik untuk lihat dampak akhir">
                <div class="kc-impact-label">💥 IMPACT</div>
                <div class="kc-impact-body">10M+ data bocor<br />PCI-DSS revoked<br />Sanksi UU PDP</div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>

  '''
    if 'id="modalKillChain"' not in html:
        html = html.replace(modal_insert_marker, kc_modal_html + modal_insert_marker)
        print("Added Kill Chain modal HTML.")

    # 5. Add JavaScript Handlers for Kill Chain Modal & Simulation
    js_marker = "btnBiblioModal: document.getElementById('btnBiblioModal')"
    js_dom_add = """,
      modalKillChain: document.getElementById('modalKillChain'),
      btnKillChainModal: document.getElementById('btnKillChainModal'),
      btnSimulateKillChain: document.getElementById('btnSimulateKillChain')"""
    if js_marker in html and 'btnKillChainModal:' not in html:
        html = html.replace(js_marker, js_marker + js_dom_add)
        print("Added DOM handles for Kill Chain modal.")

    # 6. Add simulation logic & click bindings
    js_listener_marker = "dom.btnBiblioModal.addEventListener('click', () => {"
    js_simulation_code = '''
    // Kill Chain Modal Opener
    if (dom.btnKillChainModal) {
      dom.btnKillChainModal.addEventListener('click', () => {
        openModal(dom.modalKillChain);
        sfxStep();
      });
    }

    // Kill Chain Node Click to Step Jump
    document.querySelectorAll('.kc-node, .kc-impact-card').forEach(el => {
      el.addEventListener('click', () => {
        const vec = el.getAttribute('data-vec');
        const step = parseInt(el.getAttribute('data-step') || '0', 10);
        closeAllModals();
        if (vec) {
          switchVector(vec);
          goToStep(step);
          sfxStep();
        }
      });
    });

    // Kill Chain Sequence Simulation
    let kcSimTimer = null;
    if (dom.btnSimulateKillChain) {
      dom.btnSimulateKillChain.addEventListener('click', () => {
        if (kcSimTimer) {
          clearInterval(kcSimTimer);
          kcSimTimer = null;
          dom.btnSimulateKillChain.innerHTML = '<span>▶</span> Putar Simulasi Alur';
          document.querySelectorAll('.kc-node, .kc-impact-card').forEach(n => n.classList.remove('sim-active'));
          return;
        }

        dom.btnSimulateKillChain.innerHTML = '<span>⏸</span> Jeda Simulasi';
        let stepIdx = 0;
        const totalNodes = 6; // 5 stages + 1 impact
        
        kcSimTimer = setInterval(() => {
          document.querySelectorAll('.kc-node, .kc-impact-card').forEach(n => n.classList.remove('sim-active'));
          if (stepIdx >= totalNodes) {
            clearInterval(kcSimTimer);
            kcSimTimer = null;
            dom.btnSimulateKillChain.innerHTML = '<span>▶</span> Putar Simulasi Alur';
            return;
          }

          // Highlight current column across all 4 vector rows
          ['kcRow1', 'kcRow2', 'kcRow3a', 'kcRow3b'].forEach(rowId => {
            const row = document.getElementById(rowId);
            if (!row) return;
            const nodes = row.querySelectorAll('.kc-node, .kc-impact-card');
            if (nodes[stepIdx]) {
              nodes[stepIdx].classList.add('sim-active');
            }
          });

          playTone(320 + stepIdx * 65, 'sine', 0.08, 0.07);
          stepIdx++;
        }, 900);
      });
    }
'''
    if js_listener_marker in html and 'btnKillChainModal.addEventListener' not in html:
        html = html.replace(js_listener_marker, js_simulation_code + "\n    " + js_listener_marker)
        print("Added Kill Chain simulation logic.")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html fully updated!")

if __name__ == '__main__':
    update_index()
