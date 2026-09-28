# -*- coding: utf-8 -*-
"""
Builder for complete dataset: Vektor 1, 2, 3A, 3B, Panorama, and Defense Pillars.
Writes scenario_data.py and builds index.html
"""
import json

def get_v2():
    return {
        "title": "Vektor 2: Phishing & Social Engineering",
        "subtitle": "Pengintaian Data, Domain Typosquatting & Pengambilalihan Akun (ATO)",
        "accentColor": "#f59e0b",
        "accentBg": "rgba(245, 158, 11, 0.12)",
        "steps": [
            {
                "title": "Reconnaissance (Pengumpulan Data Korban)",
                "statusText": "Pengintaian Target",
                "statusCls": "warn",
                "desc": "Penyerang mengumpulkan nomor ponsel, nama lengkap, dan data pribadi calon korban melalui kompilasi data bocor (data breach e-commerce) serta memantau nasabah yang mengajukan keluhan publik di media sosial fintech.",
                "defenseDesc": "Mitigasi Pilar Operasional: Pemantauan kebocoran data siber (Cyber Threat Intelligence) dan edukasi nasabah untuk tidak pernah mempublikasikan nomor ponsel/tiket aduan di kolom komentar media sosial terbuka.",
                "analogy": "Seperti penjahat yang mengamati buku tamu atau menguping percakapan orang yang mengeluh tentang kartu banknya untuk mengetahui nama dan nomor telepon mereka.",
                "triad": {
                    "c": {"text": "Bocor", "cls": "bad"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Reconnaissance", "Fase awal pengumpulan intelijen mengenai profil target"],
                    ["Data Leak Database", "Kumpulan dump kredensial yang bocor di forum gelap / dark web"],
                    ["Social Scraping", "Penyedotan informasi publik dari nasabah di Twitter/Instagram resmi"]
                ],
                "quiz": {
                    "q": "Mengapa pengintaian melalui media sosial sangat efektif bagi penipu finansial?",
                    "options": [
                        "Karena korban yang sedang panik atau komplain di media sosial sangat mudah diperdaya oleh akun palsu yang berpura-pura menjadi Customer Service resmi.",
                        "Karena media sosial secara otomatis membagikan password pengguna.",
                        "Karena akun media sosial bank tidak dapat diverifikasi."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Penipu memanfaatkan kepanikan nasabah (urgensi psikologis) untuk mengarahkan mereka ke tautan verifikasi palsu."
                },
                "svg": '''
                  <!-- Attacker OSINT Terminal -->
                  <rect x="70" y="60" width="300" height="280" rx="14" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2" filter="url(#glowV2)"/>
                  <text x="220" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">PENGINTAIAN OSINT &amp; DATA LEAK</text>
                  <rect x="85" y="110" width="270" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="132" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; grep -i \"fintech_user\" breach_db.csv</text>
                  <text x="95" y="152" fill="#4ade80" font-size="8" font-family="monospace">[+] Found: 42,109 active phone numbers</text>
                  <text x="95" y="172" fill="#facc15" font-size="8" font-family="monospace">[+] Scraping X/Twitter: @CS_Fintech keluhan</text>
                  <text x="95" y="195" fill="#fca5a5" font-size="8" font-family="monospace">Target: Bpk. Hendra (0812-9988-xxxx)</text>
                  <text x="95" y="215" fill="#cbd5e1" font-size="8" font-family="monospace">Status: Saldo tertahan saat top up</text>
                  <rect x="95" y="235" width="250" height="40" rx="4" fill="#78350f"/>
                  <text x="220" y="258" text-anchor="middle" fill="#fef08a" font-size="8.5" font-weight="700">PROFIL KORBAN TERIDENTIFIKASI</text>

                  <!-- Flow Arrow -->
                  <path d="M 390 190 L 470 190" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="470,185 482,190 470,195" fill="#f59e0b"/>

                  <!-- Data Lake Target Box -->
                  <rect x="490" y="60" width="260" height="280" rx="14" fill="url(#serverGrad)" stroke="#f59e0b" stroke-width="1.8"/>
                  <text x="620" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">DATABASE TARGET SPEAR-PHISHING</text>
                  <rect x="505" y="110" width="230" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="620" cy="160" r="32" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2"/>
                  <text x="620" y="168" text-anchor="middle" fill="#fde68a" font-size="20">&#128100;</text>
                  <text x="620" y="215" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">Target Siap Dihubungi</text>
                  <text x="620" y="235" text-anchor="middle" fill="#94a3b8" font-size="8.5">Nomor HP + Profil Finansial</text>
                  <rect x="520" y="255" width="200" height="30" rx="4" fill="#451a03"/>
                  <text x="620" y="274" text-anchor="middle" fill="#fcd34d" font-size="8.5" font-weight="700">Langkah 2: Siapkan Server Phishing</text>
                ''',
                "defenseSvg": '''
                  <!-- Defense: Brand Monitoring & Threat Intel -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; PROAKTIF THREAT INTELLIGENCE &amp; SOCIAL MONITORING</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Tindakan Pencegahan Sisi Bank:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Akun Customer Service resmi bercentang biru menghapus otomatis nomor HP yang diposting publik</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Intelijen kebocoran data mendeteksi kredensial yang beredar dan memicu reset password paksa</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Kampanye berkala mengingatkan nasabah untuk waspada terhadap akun CS gadungan</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">PROFIL NASABAH TERLINDUNGI</text>
                '''
            },
            {
                "title": "Infrastruktur Phishing & Typosquatting",
                "statusText": "Penyiapan Situs Palsu",
                "statusCls": "warn",
                "desc": "Penyerang menyewa server dan mendaftarkan domain typosquatting yang mirip dengan merek asli (contoh: 'd0mpet-pay.com' menggantikan 'dompetpay.com'). Di belakangnya dipasang reverse proxy (seperti Evilginx2) untuk memintas 2FA OTP secara real-time.",
                "defenseDesc": "Mitigasi Pilar Teknologi & Operasional: Domain Monitoring & DNS Takedown otomatis; implementasi FIDO2/Passkeys yang bersifat origin-bound sehingga browser menolak autentikasi pada domain palsu.",
                "analogy": "Seperti menyewa ruko palsu di seberang kantor bank resmi dengan cat, logo, dan plang nama yang sengaja dibuat sangat mirip untuk mengelabui nasabah.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Terganggu", "cls": "warn"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Typosquatting", "Mendaftarkan domain dengan ejaan sengaja dibuat mirip (d0mpet vs dompet)"],
                    ["Reverse Proxy AiTM", "Server penyerang meneruskan request ke bank asli dan mencuri session cookie"],
                    ["Origin-Bound", "Karakteristik kriptografi yang hanya mengikat pada URL domain resmi"]
                ],
                "quiz": {
                    "q": "Mengapa domain typosquatting seperti 'd0mpet-pay.com' masih dapat mengecoh pengguna awam?",
                    "options": [
                        "Karena pengguna sering tergesa-gesa dan secara visual huruf angka '0' dan 'o' terlihat sangat identik pada layar ponsel kecil.",
                        "Karena domain typosquatting resmi disahkan oleh Bank Indonesia.",
                        "Karena domain tersebut otomatis memblokir browser korban."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Bias visual dan kelalaian pengguna di layar ponsel menjadi celah utama yang dimanfaatkan oleh serangan typosquatting."
                },
                "svg": '''
                  <!-- Infrastructure Diagram -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#serverGrad)" stroke="#f59e0b" stroke-width="2"/>
                  <text x="225" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">DOMAIN TYPOSQUATTING AKTIF</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="95" y="125" width="260" height="40" rx="4" fill="#451a03" stroke="#f59e0b"/>
                  <text x="105" y="145" fill="#fde68a" font-size="9" font-family="monospace">URL: https://d0mpet-pay.com/login</text>
                  <text x="105" y="158" fill="#fbbf24" font-size="7.5">&#9888; Karakter '0' menggantikan 'o' resmi</text>
                  
                  <rect x="95" y="175" width="260" height="60" rx="4" fill="#1e1b4b"/>
                  <text x="105" y="195" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; evilginx2 reverse-proxy</text>
                  <text x="105" y="210" fill="#a7f3d0" font-size="8" font-family="monospace">[+] SSL Certificate: Let's Encrypt Active</text>
                  <text x="105" y="225" fill="#fca5a5" font-size="8" font-family="monospace">[+] Lure URL generated: /verify-account</text>

                  <rect x="95" y="245" width="260" height="60" rx="4" fill="#022c22"/>
                  <text x="225" y="268" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700">AiTM Proxy Siaga</text>
                  <text x="225" y="285" text-anchor="middle" fill="#cbd5e1" font-size="8">Meneruskan token sesi korban secara real-time</text>

                  <!-- Flow to Webhook -->
                  <path d="M 400 190 L 480 190" stroke="#f59e0b" stroke-width="2.5" class="dash-flow"/>
                  <polygon points="480,185 492,190 480,195" fill="#f59e0b"/>

                  <!-- Attacker Webhook Node -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2" filter="url(#glowV2)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">WEBHOOK EXFILTRASI</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="525" y="140" fill="#a855f7" font-size="9" font-family="monospace">Listener: Telegram Bot</text>
                  <text x="525" y="165" fill="#38bdf8" font-size="8.5" font-family="monospace">Token: 618293:AAH...</text>
                  <text x="525" y="190" fill="#4ade80" font-size="8.5" font-family="monospace">Status: Ready to harvest</text>
                  <rect x="525" y="210" width="200" height="90" rx="6" fill="#1e1b4b"/>
                  <text x="625" y="235" text-anchor="middle" fill="#c7d2fe" font-size="9" font-weight="700">Tujuan:</text>
                  <text x="625" y="255" text-anchor="middle" fill="#cbd5e1" font-size="8">Menangkap kredensial + OTP</text>
                  <text x="625" y="275" text-anchor="middle" fill="#cbd5e1" font-size="8">yang dimasukkan korban</text>
                ''',
                "defenseSvg": '''
                  <!-- Proactive DNS Takedown -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; PROACTIVE DNS TAKEDOWN &amp; DOMAIN SUSPENSION</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Respon Proaktif Tim Keamanan Bank:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Brand Protection Engine mendeteksi registrasi domain 'd0mpet-pay.com' dalam hitungan menit</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Permintaan Abuse Report &amp; DNS Takedown dikirim otomatis ke registrar penyedia domain</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Browser modern (Chrome/Safari) menandai situs sebagai 'Deceptive Site / Phishing Red Page'</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">DOMAIN PALSU BERHASIL DIBLOKIR</text>
                '''
            },
            {
                "title": "Distribusi Pesan Massal (Scare Tactics)",
                "statusText": "Penyebaran Pesan Blast",
                "statusCls": "warn",
                "desc": "Penyerang melancarkan SMS dan pesan WhatsApp massal bernada ancaman darurat: 'Akun Anda diblokir karena aktivitas mencurigakan! Klik https://d0mpet-pay.com dalam 15 menit untuk verifikasi pembukaan blokir'.",
                "defenseDesc": "Mitigasi Pilar Operasional: Registrasi SMS Sender ID resmi (Brand ID), integrasi DMARC / SPF untuk email, dan kampanye edukasi 'Bank Tidak Pernah Meminta Verifikasi via Link SMS'.",
                "analogy": "Seperti menerima surat kabar atau selebaran bertuliskan 'Segera telepon nomor ini dalam 10 menit atau rumah Anda akan disita'.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Terganggu", "cls": "warn"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Scare Tactics", "Eksploitasi emosi kepanikan dan rasa takut kehilangan dana nasabah"],
                    ["Urgency Hook", "Pembatasan waktu ketat agar korban tidak sempat berpikir logis"],
                    ["SMS Spoofing", "Pengiriman SMS seolah-olah berasal dari nama institusi resmi"]
                ],
                "quiz": {
                    "q": "Faktor psikologis utama apa yang dieksploitasi oleh penyerang dalam pesan phishing massal?",
                    "options": [
                        "Sense of Urgency (urgensi waktu) dan ketakutan saldo akun akan hilang atau dibekukan.",
                        "Rasa kantuk pengguna di malam hari.",
                        "Keinginan pengguna untuk memperbarui sistem operasi."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Kepanikan membuat korban mengabaikan keanehan pada alamat website (URL) dan langsung memasukkan kredensialnya."
                },
                "svg": '''
                  <!-- Blast Machine -->
                  <rect x="70" y="60" width="260" height="280" rx="14" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2" filter="url(#glowV2)"/>
                  <text x="200" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">SMS / WA MODEM POOL</text>
                  <rect x="85" y="110" width="230" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="135" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; blast_gateway.sh</text>
                  <text x="95" y="155" fill="#f59e0b" font-size="8" font-family="monospace">Target: 50,000 nomor</text>
                  <text x="95" y="175" fill="#f87171" font-size="8" font-family="monospace">Pesan: AKUN DIBLOKIR!</text>
                  <rect x="95" y="195" width="210" height="110" rx="6" fill="#1e1b4b"/>
                  <text x="200" y="218" text-anchor="middle" fill="#fef08a" font-size="9" font-weight="800">&#9888; TEMPLATE SCARE TACTIC</text>
                  <text x="105" y="238" fill="#cbd5e1" font-size="7.5">\"Peringatan: Ada login tak dikenal.</text>
                  <text x="105" y="252" fill="#cbd5e1" font-size="7.5">Klik link d0mpet-pay.com dlm 15m</text>
                  <text x="105" y="266" fill="#cbd5e1" font-size="7.5">agar saldo Anda tidak hangus!\"</text>
                  <text x="200" y="292" text-anchor="middle" fill="#a7f3d0" font-size="8">Status: 98% Terkirim</text>

                  <!-- Packet Blast Arrows -->
                  <path d="M 345 180 L 485 180" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,175 497,180 485,185" fill="#f59e0b"/>

                  <!-- Victim Phone Receiving SMS -->
                  <rect x="510" y="45" width="220" height="310" rx="20" fill="url(#phoneGrad)" stroke="#f59e0b" stroke-width="2"/>
                  <rect x="522" y="65" width="196" height="270" rx="10" fill="url(#screenGrad)"/>
                  <rect x="585" y="52" width="70" height="6" rx="3" fill="#334155"/>
                  
                  <rect x="532" y="90" width="176" height="120" rx="8" fill="#451a03" stroke="#f59e0b" class="shake-node"/>
                  <text x="542" y="112" fill="#fde68a" font-size="9.5" font-weight="800">&#9888; SMS DARI: BANK-INFO</text>
                  <text x="542" y="132" fill="#fecaca" font-size="8.5">\"Akun Anda terancam diblokir!</text>
                  <text x="542" y="148" fill="#fecaca" font-size="8.5">Klik link ini sekarang:</text>
                  <rect x="542" y="156" width="156" height="24" rx="4" fill="#78350f"/>
                  <text x="620" y="172" text-anchor="middle" fill="#38bdf8" font-size="8.5" font-weight="700">https://d0mpet-pay.com</text>
                  <text x="542" y="196" fill="#fca5a5" font-size="7.5">Waktu tersisa: 14 menit 58 detik</text>
                  
                  <rect x="532" y="225" width="176" height="40" rx="6" fill="#1e1b4b"/>
                  <text x="620" y="244" text-anchor="middle" fill="#c7d2fe" font-size="8.5" font-weight="700">KORBAN PANIK &amp; MENGKLIK</text>
                  <text x="620" y="256" text-anchor="middle" fill="#94a3b8" font-size="7.5">Membuka browser ke situs penipu</text>
                ''',
                "defenseSvg": '''
                  <!-- Defense: Brand SMS Filtering & Anti Phishing -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; VERIFIKASI SENDER ID &amp; EDUKASI ANTI-PHISHING</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Mekanisme Proteksi Operator &amp; Bank:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Filter Spam Operator Telekomunikasi memblokir blast SMS dengan tautan domain mencurigakan</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Sender ID Resmi perbankan terlindungi enkripsi dan whitelist registrasi nasional</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Aplikasi E-Wallet menampilkan notifikasi in-app: 'Jangan pernah klik link dari SMS asing'</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">KORBAN TEREDUKASI &amp; MENGABAIKAN LINK</text>
                '''
            },
            {
                "title": "Credential Harvest (Pemanenan Kredensial)",
                "statusText": "Penyadapan Kredensial",
                "statusCls": "bad",
                "desc": "Korban yang panik membuka situs palsu di browser, memasukkan nomor ponsel, PIN 6 digit, dan kode OTP. Reverse proxy penyerang menangkap seluruh input ini secara real-time dan meneruskannya via webhook ke penyerang.",
                "defenseDesc": "Mitigasi Pilar Teknologi: FIDO2 / WebAuthn Passkeys. Kunci privat kriptografi terikat secara fisik ke domain asli (Origin-Bound). Browser menolak melepaskan kunci pada domain 'd0mpet-pay.com' sehingga serangan gagal total.",
                "analogy": "Seperti memberikan anak kunci rumah dan kartu identitas Anda kepada penipu yang menyamar di meja resepsionis palsu.",
                "triad": {
                    "c": {"text": "Bocor Total", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Credential Harvesting", "Proses pengumpulan massal kredensial login melalui form palsu"],
                    ["Webhook Exfiltration", "Pengiriman data curian langsung ke bot Telegram/Discord penyerang"],
                    ["FIDO2 Passkeys", "Standar autentikasi tahan phishing yang menggantikan password & OTP"]
                ],
                "quiz": {
                    "q": "Mengapa teknologi FIDO2 / Passkeys kebal terhadap serangan Phishing Reverse Proxy (AiTM)?",
                    "options": [
                        "Karena kunci kriptografis bersifat Origin-Bound (terikat domain resmi) dan hanya dapat ditandatangani jika URL di browser cocok 100% dengan server bank.",
                        "Karena FIDO2 mengharuskan pengguna datang ke kantor cabang.",
                        "Karena FIDO2 tidak menggunakan koneksi internet."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Sifat Origin-Bound memastikan kunci tidak akan pernah dikirimkan ke domain palsu atau typosquatting."
                },
                "svg": '''
                  <!-- Fake Portal on Phone -->
                  <rect x="80" y="50" width="220" height="300" rx="18" fill="url(#phoneGrad)" stroke="#f59e0b" stroke-width="2"/>
                  <rect x="92" y="68" width="196" height="264" rx="10" fill="#0f172a"/>
                  <rect x="92" y="68" width="196" height="36" fill="#451a03"/>
                  <text x="190" y="90" text-anchor="middle" fill="#fde68a" font-size="9" font-family="monospace">&#128274; d0mpet-pay.com</text>
                  
                  <rect x="102" y="115" width="176" height="150" rx="6" fill="#1e1b4b" stroke="#f59e0b"/>
                  <text x="190" y="135" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">VERIFIKASI AKUN</text>
                  
                  <text x="112" y="155" fill="#cbd5e1" font-size="8">No Handphone:</text>
                  <rect x="112" y="160" width="156" height="20" rx="3" fill="#020617"/>
                  <text x="118" y="174" fill="#38bdf8" font-size="8.5" font-family="monospace">081299881234</text>
                  
                  <text x="112" y="195" fill="#cbd5e1" font-size="8">PIN 6-Digit &amp; OTP:</text>
                  <rect x="112" y="200" width="156" height="20" rx="3" fill="#020617"/>
                  <text x="118" y="214" fill="#f87171" font-size="8.5" font-family="monospace">****** | 741920</text>

                  <rect x="112" y="230" width="156" height="22" rx="4" fill="#f59e0b"/>
                  <text x="190" y="245" text-anchor="middle" fill="#000" font-size="9" font-weight="800">KIRIM VERIFIKASI</text>

                  <!-- Exfil Webhook Arrow -->
                  <path d="M 315 200 L 490 200" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="490,195 502,200 490,205" fill="#ef4444"/>
                  <text x="400" y="190" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">Webhook POST</text>

                  <!-- Attacker Telegram Bot -->
                  <rect x="515" y="60" width="240" height="280" rx="14" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2" filter="url(#glowV2)"/>
                  <text x="635" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">BOT NOTIFIKASI TELEGRAM</text>
                  <rect x="530" y="110" width="210" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="540" y="135" fill="#4ade80" font-size="8.5" font-family="monospace">&#128293; NEW VICTIM SUBMISSION!</text>
                  <text x="540" y="155" fill="#38bdf8" font-size="8" font-family="monospace">Phone: +6281299881234</text>
                  <text x="540" y="175" fill="#f87171" font-size="8" font-family="monospace">PIN: 819204</text>
                  <text x="540" y="195" fill="#facc15" font-size="8" font-family="monospace">OTP: 741920</text>
                  <text x="540" y="215" fill="#cbd5e1" font-size="8" font-family="monospace">Timer OTP: 58 Detik Tersisa!</text>
                  <rect x="540" y="235" width="190" height="40" rx="4" fill="#7f1d1d"/>
                  <text x="635" y="258" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">LOGIN KE APP SEKARANG</text>
                ''',
                "defenseSvg": '''
                  <!-- FIDO2 / Passkey Origin Bound Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; PROTEKSI ASLI FIDO2 / WEBAUTHN PASSKEYS</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Verifikasi Kriptografi Origin-Bound Menolak Otomatis:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Domain terdeteksi: 'd0mpet-pay.com' &ne; Domain Resmi 'dompetpay.com'</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Perangkat pengguna MENOLAK merilis kunci privat kepada website tiruan</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Penyerang tidak memperoleh token, password, ataupun kode yang dapat digunakan</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">PHISHING REVERSE PROXY GAGAL TOTAL</text>
                '''
            },
            {
                "title": "Account Takeover (Pengambilalihan Akun)",
                "statusText": "Pembajakan Akun < 60s",
                "statusCls": "bad",
                "desc": "Menggunakan OTP yang masih valid (< 60 detik), penyerang login ke aplikasi resmi dari perangkat mereka. Penyerang segera mengganti PIN, mengganti nomor HP pemulihan, memutus sesi ponsel korban, dan mentransfer seluruh saldo ke luar.",
                "defenseDesc": "Mitigasi Pilar Operasional & Tata Kelola: Impossible Travel Detection oleh SOC (anomali login IP berbeda lokasi dalam waktu singkat); aturan Dual-Control (Maker-Checker) sebelum perubahan data nomor telepon dan pencairan limit besar disahkan.",
                "analogy": "Seperti seseorang yang merebut kartu identitas Anda di loket bank, langsung mengganti tanda tangan di buku tabungan, dan menguras seluruh isi rekening Anda.",
                "triad": {
                    "c": {"text": "Terkorup", "cls": "bad"},
                    "i": {"text": "Hancur", "cls": "bad"},
                    "a": {"text": "Terkunci", "cls": "bad"}
                },
                "terms": [
                    ["Account Takeover (ATO)", "Kondisi di mana akun pengguna sepenuhnya dikendalikan pihak tidak sah"],
                    ["Session Invalidation", "Sesi korban diputus paksa sehingga korban tidak bisa login lagi"],
                    ["Impossible Travel", "Indikator anomali ketika akun login dari 2 kota berjauhan dalam hitungan menit"]
                ],
                "quiz": {
                    "q": "Apa mekanisme deteksi SOC yang efektif mendeteksi serangan Account Takeover setelah kredensial dicuri?",
                    "options": [
                        "Impossible Travel Detection (mendeteksi perpindahan geolokasi IP drastis dalam jeda waktu singkat).",
                        "Mematikan seluruh server database bank setiap sore hari.",
                        "Menghapus riwayat transaksi nasabah lama."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Jika nasabah baru login di Jakarta, lalu 2 menit kemudian ada login dari server IP penyerang di luar negeri, sistem menandainya sebagai Impossible Travel."
                },
                "svg": '''
                  <!-- Attacker Device Hijacking -->
                  <rect x="70" y="60" width="280" height="280" rx="14" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2" filter="url(#glowV2)"/>
                  <text x="210" y="90" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">PERANGKAT PENYERANG (LOGIN &lt; 60s)</text>
                  <rect x="85" y="110" width="250" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="135" fill="#4ade80" font-size="8.5" font-family="monospace">[+] Login Authenticated (Token Valid)</text>
                  <text x="95" y="155" fill="#f87171" font-size="8" font-family="monospace">&gt; Action 1: Ganti No HP Pemulihan</text>
                  <text x="95" y="175" fill="#f87171" font-size="8" font-family="monospace">&gt; Action 2: Ganti PIN Transaksi Baru</text>
                  <text x="95" y="195" fill="#f87171" font-size="8" font-family="monospace">&gt; Action 3: Transfer Saldo Rp 18.500.000</text>
                  <rect x="95" y="215" width="230" height="85" rx="6" fill="#7f1d1d"/>
                  <text x="210" y="238" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">&#10007; AKUN RESMI DIKUASAI</text>
                  <text x="210" y="255" text-anchor="middle" fill="#fca5a5" font-size="8">Sesi HP korban ditutup paksa</text>
                  <text x="210" y="272" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">DANA DIKURAS KELUAR</text>

                  <!-- Flow to Victim Phone Kickout -->
                  <path d="M 365 190 L 465 190" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="465,185 477,190 465,195" fill="#ef4444"/>

                  <!-- Victim Phone Locked Out -->
                  <rect x="490" y="45" width="220" height="310" rx="20" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2"/>
                  <rect x="502" y="65" width="196" height="270" rx="10" fill="#0f172a"/>
                  <rect x="565" y="52" width="70" height="6" rx="3" fill="#334155"/>
                  
                  <rect x="512" y="95" width="176" height="150" rx="8" fill="#450a0a" stroke="#ef4444" class="shake-node"/>
                  <circle cx="600" cy="135" r="22" fill="#7f1d1d"/>
                  <text x="600" y="143" text-anchor="middle" fill="#fca5a5" font-size="18">&#128274;</text>
                  <text x="600" y="175" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">SESI ANDA TELAH BERAKHIR</text>
                  <text x="600" y="195" text-anchor="middle" fill="#fca5a5" font-size="8">Akun Anda sedang dibuka di perangkat lain.</text>
                  <text x="600" y="210" text-anchor="middle" fill="#fca5a5" font-size="8">PIN Anda telah diubah oleh pengguna.</text>
                  
                  <rect x="512" y="260" width="176" height="45" rx="6" fill="#1e1b4b"/>
                  <text x="600" y="280" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="700">KORBAN KEHILANGAN KENDALI</text>
                  <text x="600" y="294" text-anchor="middle" fill="#94a3b8" font-size="7.5">Tidak bisa masuk kembali</text>
                ''',
                "defenseSvg": '''
                  <!-- SOC Impossible Travel Alert & Dual Control -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; SOC IMPOSSIBLE TRAVEL DETECTION &amp; DUAL-CONTROL</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Anomali Terdeteksi Otomatis:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Anomali IP: Device korban (Jakarta) vs Login Penyerang (Frankfurt, jeda 40 detik)</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Kebijakan Maker-Checker membekukan permintaan ganti nomor HP secara instan</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Tim SOC memicu sesi verifikasi video biometrik sebelum perubahan diizinkan</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">PENGAMBILALIHAN AKUN DIGAGALKAN</text>
                '''
            },
            {
                "title": "Dampak Akhir Serangan (Impact Vektor 2)",
                "statusText": "Kerugian Reputasi & Saldo",
                "statusCls": "bad",
                "desc": "Saldo nasabah dikuras keluar, reputasi brand fintech hancur di media sosial, dan pusat bantuan (Customer Service) kewalahan akibat lonjakan komplain nasabah yang serentak menjadi korban.",
                "defenseDesc": "Evaluasi Resiliensi: Migrasi ke FIDO2 Passkeys dan prosedur DNS Takedown terbukti memotong rantai kill chain pada tahap awal sebelum terjadi pemanenan kredensial.",
                "analogy": "Seperti kantor bank yang didemo ratusan nasabah di depan pintu karena rekening mereka terkuras akibat sindikat penipu.",
                "triad": {
                    "c": {"text": "Bocor Parah", "cls": "bad"},
                    "i": {"text": "Hancur", "cls": "bad"},
                    "a": {"text": "Overload CS", "cls": "bad"}
                },
                "terms": [
                    ["Saldo Dikuras", "Kerugian finansial langsung bagi nasabah"],
                    ["Brand Rusak", "Penurunan drastis tingkat kepercayaan publik terhadap aplikasi"],
                    ["CS Overload", "Pusat bantuan pelanggan kolaps menangani ribuan laporan serentak"]
                ],
                "quiz": {
                    "q": "Menurut dokumen Modul 02, mengapa Vektor 2 memiliki probabilitas keterjadian (Likelihood) yang sangat tinggi?",
                    "options": [
                        "Karena 74% insiden kebocoran data global melibatkan manipulasi faktor manusia (human element) dan rekayasa sosial.",
                        "Karena pembuatan website phishing membutuhkan biaya miliaran rupiah.",
                        "Karena penyerang harus mendatangi rumah korban secara langsung."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Laporan Verizon DBIR menunjukkan manipulasi psikologis manusia adalah vektor serangan yang paling sering berhasil."
                },
                "svg": '''
                  <!-- Impact Vector 2 Visual -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="#2d1305" stroke="#f59e0b" stroke-width="2.5" filter="url(#glowV2)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="800">DAMPAK SERANGAN VEKTOR 2 — PHISHING &amp; SOCIAL ENGINEERING</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#451a03" stroke="#f59e0b"/>
                  <text x="210" y="145" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">SALDO DIKURAS</text>
                  <text x="210" y="180" text-anchor="middle" fill="#fbbf24" font-size="18" font-weight="800">Rp 0</text>
                  <text x="210" y="210" text-anchor="middle" fill="#fef08a" font-size="8.5">Transfer Keluar < 60 Detik</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#451a03" stroke="#f59e0b"/>
                  <text x="410" y="145" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">REPUTASI BRAND RUSAK</text>
                  <text x="410" y="175" text-anchor="middle" fill="#f87171" font-size="24">&#9760;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#fecaca" font-size="8.5">Viralitas Negatif Medsos</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#451a03" stroke="#f59e0b"/>
                  <text x="610" y="145" text-anchor="middle" fill="#fde68a" font-size="11" font-weight="800">CS OVERLOAD</text>
                  <text x="610" y="180" text-anchor="middle" fill="#fbbf24" font-size="16" font-weight="800">&gt; 5,000 Tiket</text>
                  <text x="610" y="210" text-anchor="middle" fill="#fef08a" font-size="8.5">Antrean Komplain Lumpuh</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#1c0b02" stroke="#f59e0b"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fde68a" font-size="10" font-weight="800">KESIMPULAN: KELEMAHAN OTP SMS MEMBAWA DAMPAK SISTEMIK</text>
                  <text x="410" y="300" text-anchor="middle" fill="#cbd5e1" font-size="9">Migrasi menuju autentikasi FIDO2 Passkeys dan perlindungan Brand wajib diterapkan secara menyeluruh.</text>
                ''',
                "defenseSvg": '''
                  <!-- Resilient Defense Matrix V2 -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="14" font-weight="800">&#128737; RESILIENSI IDENTITAS DENGAN FIDO2 PASSKEYS</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="210" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">DANA AMAN</text>
                  <text x="210" y="180" text-anchor="middle" fill="#34d399" font-size="16" font-weight="800">100% UTUH</text>
                  <text x="210" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Tidak Dapat Ditransfer</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="410" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">BRAND REPUTATION</text>
                  <text x="410" y="175" text-anchor="middle" fill="#34d399" font-size="24">&#10004;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Kepercayaan Publik Terjaga</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="610" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">OPERASI NORMAL</text>
                  <text x="610" y="180" text-anchor="middle" fill="#34d399" font-size="14" font-weight="800">CS STABIL</text>
                  <text x="610" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Zero Spammed Complaints</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">KONTROL JALUR IDENTITAS BERHASIL MEMECAHKAN SIKLUS ATO</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Teknologi origin-bound dan verifikasi ganda melindungi nasabah secara proaktif.</text>
                '''
            },
            {
                "title": "Rangkuman Kontrol Mitigasi Vektor 2",
                "statusText": "Pertahanan Terpadu",
                "statusCls": "ok",
                "desc": "Implementasi 4 pilar kontrol mitigasi Vektor 2: FIDO2 Passkeys (origin-bound), Mutual TLS (mTLS), Impossible Travel Detection, Proactive DNS Takedown, Kampanye Awareness, Maker-Checker Dual-Control, dan Audit Trail Log.",
                "defenseDesc": "Pendekatan komprehensif mengamankan seluruh siklus otentikasi identitas dari fase sebelum serangan (monitoring) hingga pasca insiden (forensik).",
                "analogy": "Seperti bank yang mengganti tanda tangan manual dengan kunci paspor biometrik unik yang mustahil dipalsukan.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Pilar Teknologi", "FIDO2 / WebAuthn, Mutual TLS (mTLS)"],
                    ["Pilar Operasional", "Impossible Travel Detection, DNS Takedown"],
                    ["Pilar Tata Kelola", "Maker-Checker dual-control, Security Training"]
                ],
                "quiz": {
                    "q": "Apa keunggulan terbesar FIDO2 dibandingkan skema OTP konvensional dalam laporan Modul 02?",
                    "options": [
                        "Kunci kriptografis hanya berfungsi pada domain terdaftar resmi; jika korban membuka situs typosquatting, verifikasi otomatis ditolak.",
                        "FIDO2 dapat mengirimkan uang secara otomatis.",
                        "FIDO2 tidak memerlukan perangkat smartphone."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Origin-bound binding adalah keunggulan fundamental FIDO2 yang meniadakan risiko phishing credential harvesting."
                },
                "svg": '''
                  <!-- Matrix V2 Controls Visual -->
                  <rect x="80" y="60" width="660" height="280" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">MATRIKS KONTROL PERTAHANAN BERLAPIS — VEKTOR 2 (JALUR IDENTITAS)</text>
                  
                  <rect x="100" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="170" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TEKNOLOGI</text>
                  <text x="110" y="165" fill="#cbd5e1" font-size="8">&bull; FIDO2 / WebAuthn</text>
                  <text x="110" y="185" fill="#cbd5e1" font-size="8">&bull; Origin-Bound Keys</text>
                  <text x="110" y="205" fill="#cbd5e1" font-size="8">&bull; Mutual TLS (mTLS)</text>
                  <text x="110" y="225" fill="#cbd5e1" font-size="8">&bull; Anti-Spoofing Cert</text>
                  <text x="110" y="245" fill="#cbd5e1" font-size="8">&bull; DMARC / SPF / DKIM</text>
                  <text x="110" y="265" fill="#cbd5e1" font-size="8">&bull; Biometric Passkey</text>

                  <rect x="260" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="330" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">OPERASIONAL</text>
                  <text x="270" y="165" fill="#cbd5e1" font-size="8">&bull; Impossible Travel</text>
                  <text x="270" y="185" fill="#cbd5e1" font-size="8">&bull; Proactive Takedown</text>
                  <text x="270" y="205" fill="#cbd5e1" font-size="8">&bull; Brand Monitoring</text>
                  <text x="270" y="225" fill="#cbd5e1" font-size="8">&bull; Awareness Merchant</text>
                  <text x="270" y="245" fill="#cbd5e1" font-size="8">&bull; Simulasi Phishing</text>
                  <text x="270" y="265" fill="#cbd5e1" font-size="8">&bull; SOC 24/7 Monitoring</text>

                  <rect x="420" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="490" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TATA KELOLA</text>
                  <text x="430" y="165" fill="#cbd5e1" font-size="8">&bull; Maker-Checker</text>
                  <text x="430" y="185" fill="#cbd5e1" font-size="8">&bull; Kebijakan FIDO2</text>
                  <text x="430" y="205" fill="#cbd5e1" font-size="8">&bull; Dual-Control Rekening</text>
                  <text x="430" y="225" fill="#cbd5e1" font-size="8">&bull; SOP Takedown Domain</text>
                  <text x="430" y="245" fill="#cbd5e1" font-size="8">&bull; Audit Trail Sesi</text>
                  <text x="430" y="265" fill="#cbd5e1" font-size="8">&bull; Kepatuhan UU PDP</text>

                  <rect x="580" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="650" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PENCADANGAN</text>
                  <text x="590" y="165" fill="#cbd5e1" font-size="8">&bull; Log Sesi Terpisah</text>
                  <text x="590" y="185" fill="#cbd5e1" font-size="8">&bull; Immutable WORM Trail</text>
                  <text x="590" y="205" fill="#cbd5e1" font-size="8">&bull; Rollback Data Rekening</text>
                  <text x="590" y="225" fill="#cbd5e1" font-size="8">&bull; Retensi Audit &gt; 1 Thn</text>
                  <text x="590" y="245" fill="#cbd5e1" font-size="8">&bull; Snapshot Integritas</text>
                  <text x="590" y="265" fill="#cbd5e1" font-size="8">&bull; Disaster Failover</text>
                ''',
                "defenseSvg": None
            }
        ]
    }

print("get_v2 defined.")
