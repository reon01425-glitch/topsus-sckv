# -*- coding: utf-8 -*-
"""
Builder for Vektor 3A: Man-in-the-Middle (MitM)
From Modul02_Kelompok05_Updated.pdf
"""

def get_v3a():
    return {
        "title": "Vektor 3A: Man-in-the-Middle (MitM)",
        "subtitle": "Rogue WiFi, SSL Stripping & Pembajakan Sesi Transaksi In-Transit",
        "accentColor": "#06b6d4",
        "accentBg": "rgba(6, 182, 212, 0.12)",
        "steps": [
            {
                "title": "Setup Rogue Access Point (Evil Twin)",
                "statusText": "Penyebaran Access Point Palsu",
                "statusCls": "warn",
                "desc": "Penyerang membawa perangkat router portabel (WiFi Pineapple / Rogue AP) ke lokasi publik ramai seperti bandara, kafe, atau mall. Penyerang memancarkan nama jaringan (SSID) terbuka tanpa password, misalnya: 'FREE_AIRPORT_HIGH_SPEED_WIFI'.",
                "defenseDesc": "Mitigasi Pilar Pengguna & Kebijakan: Penggunaan VPN korporat terenkripsi penuh saat berada di jaringan publik, serta peringatan in-app untuk menghindari transaksi finansial di WiFi publik tanpa enkripsi.",
                "analogy": "Seperti memasang corong penyadap di pipa air umum di pinggir jalan sehingga semua air yang mengalir bisa diminum dan diperiksa terlebih dahulu.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Rogue Access Point", "Titik akses nirkabel tidak sah yang dikendalikan oleh penyerang"],
                    ["Evil Twin SSID", "Meniru nama WiFi resmi bandara atau hotel untuk memancing korban"],
                    ["Proximity Threat", "Serangan yang mensyaratkan kedekatan fisik penyerang dengan lokasi korban"]
                ],
                "quiz": {
                    "q": "Apa tujuan utama penyerang memancarkan sinyal Rogue WiFi tanpa kata sandi (Open WiFi) di area publik?",
                    "options": [
                        "Memancing korban sebanyak mungkin untuk tersambung sehingga seluruh lalu lintas data mereka mengalir melalui perangkat penyerang.",
                        "Memberikan akses internet gratis bagi masyarakat yang membutuhkan.",
                        "Memperbaiki sinyal operator seluler lokal."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Jaringan terbuka tanpa password memancing koneksi otomatis dari smartphone korban yang sedang mencari WiFi gratis."
                },
                "svg": '''
                  <!-- Attacker Rogue AP Node -->
                  <rect x="70" y="60" width="300" height="280" rx="14" fill="url(#serverGrad)" stroke="#06b6d4" stroke-width="2" filter="url(#glowV3a)"/>
                  <text x="220" y="90" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">ROGUE AP (WIFI PINEAPPLE)</text>
                  <rect x="85" y="110" width="270" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <circle cx="220" cy="150" r="28" fill="#082f49" stroke="#06b6d4" stroke-width="2"/>
                  <text x="220" y="157" text-anchor="middle" fill="#38bdf8" font-size="20">&#128246;</text>
                  
                  <!-- WiFi Waves -->
                  <path d="M 175 140 A 45 45 0 0 1 265 140" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
                  <path d="M 160 130 A 65 65 0 0 1 280 130" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.4"/>

                  <text x="220" y="195" text-anchor="middle" fill="#fde68a" font-size="10" font-weight="800">SSID: \"FREE_AIRPORT_WIFI\"</text>
                  <text x="220" y="212" text-anchor="middle" fill="#94a3b8" font-size="8">Open Security (Tanpa Password)</text>
                  <rect x="95" y="230" width="250" height="70" rx="6" fill="#1e1b4b"/>
                  <text x="105" y="250" fill="#38bdf8" font-size="8" font-family="monospace">&gt; bettercap -iface wlan0</text>
                  <text x="105" y="268" fill="#4ade80" font-size="8" font-family="monospace">[+] DHCP Server: 192.168.1.1</text>
                  <text x="105" y="285" fill="#facc15" font-size="8" font-family="monospace">[+] DNS Spoofing: Active</text>

                  <!-- Radio Wave Stream -->
                  <path d="M 385 190 L 485 190" stroke="#06b6d4" stroke-width="2.5" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#06b6d4"/>

                  <!-- Public Location Box -->
                  <rect x="505" y="60" width="245" height="280" rx="14" fill="url(#serverGrad)" stroke="#06b6d4" stroke-width="1.8"/>
                  <text x="627" y="90" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">LOKASI PUBLIK (BANDARA / CAFE)</text>
                  <rect x="520" y="110" width="215" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="627" cy="160" r="32" fill="#082f49"/>
                  <text x="627" y="168" text-anchor="middle" fill="#38bdf8" font-size="22">&#127970;</text>
                  <text x="627" y="215" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">Area Padat Calon Korban</text>
                  <text x="627" y="235" text-anchor="middle" fill="#94a3b8" font-size="8.5">Banyak pengguna mencari sinyal gratis</text>
                  <rect x="535" y="255" width="185" height="35" rx="4" fill="#0c4a6e"/>
                  <text x="627" y="277" text-anchor="middle" fill="#7dd3fc" font-size="8.5" font-weight="700">Langkah 2: Menunggu Korban Konek</text>
                ''',
                "defenseSvg": '''
                  <!-- VPN & Network Security Warning -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; DETEKSI JARINGAN PUBLIK TIDAK AMAN</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Perlindungan Klien FinTech:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Sistem operasi mendeteksi jaringan tanpa enkripsi (Captive Portal tidak tepercaya)</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Terowongan VPN terenkripsi otomatis aktif sebelum data finansial dikirimkan</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Larangan penggunaan jaringan terbuka untuk transaksi finansial kritikal</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">TEROWONGAN VPN TERENKRIPSI AMAN</text>
                '''
            },
            {
                "title": "Victim Connects (Korban Tersambung)",
                "statusText": "Jalur Data Dibelokkan",
                "statusCls": "warn",
                "desc": "Korban memilih WiFi gratis tersebut pada smartphone mereka. Begitu tersambung, default gateway perangkat korban dialihkan ke mesin proxy penyerang (192.168.1.1). Semua lalu lintas paket data keluar dan masuk dipaksa melewati laptop penyerang.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Penggunaan enkripsi jaringan end-to-end; aplikasi menolak komunikasi pada port tidak aman.",
                "analogy": "Seperti mengalihkan rel kereta api sehingga semua gerbong penumpang wajib melintasi stasiun pribadi milik penyerang sebelum menuju stasiun tujuan.",
                "triad": {
                    "c": {"text": "Terancam", "cls": "warn"},
                    "i": {"text": "Terancam", "cls": "warn"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Default Gateway", "Pintu gerbang jaringan lokal tempat semua paket diteruskan"],
                    ["Transparent Proxy", "Server perantara yang membaca dan meneruskan paket tanpa disadari klien"],
                    ["Man-in-the-Middle (MitM)", "Posisi penyerang yang berada tepat di tengah jalur komunikasi korban dan server"]
                ],
                "quiz": {
                    "q": "Apa yang terjadi pada paket data pengguna ketika terhubung ke Rogue WiFi?",
                    "options": [
                        "Seluruh paket data melewati mesin proxy penyerang terlebih dahulu sebelum diteruskan ke internet.",
                        "Paket data secara otomatis terhapus dari ponsel.",
                        "Kecepatan internet korban meningkat 100 kali lipat."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Berada di gateway memungkinkan penyerang menginspeksi, memodifikasi, atau memutus aliran paket data korban."
                },
                "svg": '''
                  <!-- Victim Smartphone Connected -->
                  <rect x="70" y="50" width="210" height="300" rx="18" fill="url(#phoneGrad)" stroke="#06b6d4" stroke-width="2"/>
                  <rect x="82" y="68" width="186" height="264" rx="10" fill="#0f172a"/>
                  <rect x="82" y="68" width="186" height="30" fill="#082f49"/>
                  <text x="175" y="88" text-anchor="middle" fill="#7dd3fc" font-size="9" font-weight="700">&#128246; Konek ke Free WiFi</text>
                  
                  <rect x="92" y="115" width="166" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="175" y="138" text-anchor="middle" fill="#86efac" font-size="10" font-weight="700">TERHUBUNG KE WIFI</text>
                  <text x="102" y="162" fill="#cbd5e1" font-size="8">IP Korban: 192.168.1.105</text>
                  <text x="102" y="180" fill="#fde68a" font-size="8">Gateway: 192.168.1.1 (Attacker)</text>
                  <text x="102" y="198" fill="#a7f3d0" font-size="8">Status: Buka App Dompet Digital</text>

                  <rect x="92" y="250" width="166" height="40" rx="6" fill="#1e1b4b"/>
                  <text x="175" y="272" text-anchor="middle" fill="#c7d2fe" font-size="8.5" font-weight="700">SEMUA TRAFIK DILALUKAN</text>

                  <!-- Pipe Stream to Attacker Machine -->
                  <path d="M 295 190 L 495 190" stroke="#06b6d4" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="495,185 507,190 495,195" fill="#06b6d4"/>
                  <text x="395" y="178" text-anchor="middle" fill="#7dd3fc" font-size="9" font-weight="800">Paket Melewati Proxy</text>

                  <!-- Attacker Proxy Sniffer -->
                  <rect x="510" y="60" width="245" height="280" rx="14" fill="url(#hackerGrad)" stroke="#06b6d4" stroke-width="2" filter="url(#glowV3a)"/>
                  <text x="632" y="90" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">ATTACKER MITM PROXY</text>
                  <rect x="525" y="110" width="215" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="535" y="135" fill="#4ade80" font-size="8" font-family="monospace">[+] NEW CLIENT CONNECTED!</text>
                  <text x="535" y="152" fill="#38bdf8" font-size="8" font-family="monospace">MAC: 4A:2B:99:EE:12:88</text>
                  <text x="535" y="170" fill="#facc15" font-size="8" font-family="monospace">Target: api.dompetpay.com</text>
                  <text x="535" y="188" fill="#f87171" font-size="8" font-family="monospace">Port: 443 (HTTPS Detected)</text>
                  <rect x="535" y="210" width="195" height="85" rx="6" fill="#1e1b4b"/>
                  <text x="632" y="235" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="800">Langkah Berikutnya:</text>
                  <text x="632" y="255" text-anchor="middle" fill="#cbd5e1" font-size="8">Eksploitasi SSL Stripping</text>
                  <text x="632" y="272" text-anchor="middle" fill="#fca5a5" font-size="8">Turunkan HTTPS ke HTTP biasa</text>
                ''',
                "defenseSvg": '''
                  <!-- Network Security Config Blocks Plaintext -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; LARANGAN CLEARTEXT &amp; NETWORK SECURITY CONFIG</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Proteksi Sistem Operasi Android / iOS:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; android:usesCleartextTraffic = FALSE (Menolak semua koneksi HTTP polos tanpa TLS)</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; OS menolak mempercayai sertifikat Root CA pengguna (User Added CA Certificate)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Trafik aplikasi dompet digital terisolasi dan menolak dipantau oleh proxy lokal</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">JARINGAN TERENKRIPSI TETAP AMAN</text>
                '''
            },
            {
                "title": "SSL Stripping & Downgrade Attack",
                "statusText": "Pelepasan Enkripsi HTTPS",
                "statusCls": "bad",
                "desc": "Jika aplikasi dompet digital memiliki validasi sertifikat yang lemah atau tidak mengaktifkan Certificate Pinning, proxy penyerang mencegat negosiasi TLS dan menurunkan (downgrade) protokol dari HTTPS (port 443 terenkripsi) menjadi HTTP biasa (port 80 plaintext).",
                "defenseDesc": "Mitigasi Pilar Teknologi: Penerapan Strict SSL / Certificate Pinning (TrustKit / Network Security Config) dan HSTS Preload. Jika sertifikat yang diterima tidak cocok dengan public key hash yang tertanam di kode aplikasi, koneksi langsung diputus.",
                "analogy": "Seperti membuka gembok brankas surat berharga di perjalanan dan menggantinya dengan amplop kertas biasa yang transparan.",
                "triad": {
                    "c": {"text": "Bocor Parah", "cls": "bad"},
                    "i": {"text": "Terkorup", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["SSL Stripping", "Teknik memaksa browser/aplikasi berkomunikasi menggunakan HTTP tanpa enkripsi"],
                    ["Certificate Pinning", "Menanamkan hash fingerprint sertifikat resmi di dalam binary aplikasi"],
                    ["HSTS (Strict-Transport-Security)", "Header keamanan yang mewajibkan komunikasi hanya lewat HTTPS"]
                ],
                "quiz": {
                    "q": "Bagaimana Certificate Pinning berhasil menggagalkan serangan SSL Stripping / Rogue CA?",
                    "options": [
                        "Aplikasi membandingkan kunci publik sertifikat yang diterima dari server dengan hash resmi yang ditanam di dalam kode; jika berbeda, koneksi seketika dibatalkan.",
                        "Certificate Pinning menghapus kartu SIM ponsel.",
                        "Certificate Pinning mematikan antena WiFi ponsel."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Pinning menjamin aplikasi hanya percaya pada satu kunci publik spesifik milik fintech, menolak sertifikat buatan hacker."
                },
                "svg": '''
                  <!-- SSL Stripping Mechanism -->
                  <rect x="70" y="60" width="280" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                  <text x="210" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">ENKRIPSI HTTPS DILUCUTI</text>
                  <rect x="85" y="110" width="250" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="95" y="125" width="230" height="50" rx="6" fill="#450a0a" stroke="#ef4444" class="shake-node"/>
                  <text x="210" y="145" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">&#128275; HTTPS DI-DOWNGRADE KE HTTP</text>
                  <text x="210" y="162" text-anchor="middle" fill="#fca5a5" font-size="8">Port 443 TLS &rarr; Port 80 Plaintext</text>

                  <rect x="95" y="185" width="230" height="115" rx="6" fill="#1e1b4b"/>
                  <text x="105" y="205" fill="#f87171" font-size="8" font-family="monospace">&gt; sslstrip.py running</text>
                  <text x="105" y="222" fill="#38bdf8" font-size="8" font-family="monospace">[+] Rewriting Location headers</text>
                  <text x="105" y="240" fill="#facc15" font-size="8" font-family="monospace">[+] No Certificate Pinning Found!</text>
                  <text x="105" y="260" fill="#4ade80" font-size="8" font-family="monospace">[+] Intercepting plaintext traffic...</text>
                  <text x="210" y="285" text-anchor="middle" fill="#f87171" font-size="8.5" font-weight="800">KONEKSI TERBUKA TELANJANG</text>

                  <!-- Broken Lock Stream Arrow -->
                  <path d="M 365 190 L 485 190" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#ef4444"/>
                  <text x="425" y="178" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">Plaintext Data</text>

                  <!-- Intercept Logger -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV3a)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">WIRESHARK PACKET CAPTURE</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="525" y="135" fill="#38bdf8" font-size="8" font-family="monospace">GET /api/v1/user/profile HTTP/1.1</text>
                  <text x="525" y="152" fill="#cbd5e1" font-size="8" font-family="monospace">Host: api.dompetpay.com</text>
                  <text x="525" y="172" fill="#facc15" font-size="8" font-family="monospace">Authorization: Bearer eyJhbGci...</text>
                  <rect x="525" y="195" width="200" height="105" rx="6" fill="#7f1d1d"/>
                  <text x="625" y="220" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">TOKEN OTENTIKASI BOCOR!</text>
                  <text x="625" y="240" text-anchor="middle" fill="#fecaca" font-size="8">JWT Bearer Token terbaca jelas</text>
                  <text x="625" y="260" text-anchor="middle" fill="#fca5a5" font-size="8">tanpa perlu enkripsi</text>
                ''',
                "defenseSvg": '''
                  <!-- Certificate Pinning Protection Active -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128274; STRICT SSL &amp; CERTIFICATE PINNING ACTIVE</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Verifikasi Kunci Publik Sertifikat Bank:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; SHA-256 Pin Hash: pin-sha256=\"WoiWRGRiT2anIpEx4UstDUozndYj...\"</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Sertifikat dari proxy Rogue AP ditolak seketika (SSLHandshakeException)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Aplikasi memutus koneksi dan menampilkan 'Kesalahan Koneksi Aman' ke layar pengguna</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">SSL STRIPPING DIGAGALKAN TOTAL</text>
                '''
            },
            {
                "title": "Session Hijacking (Pembajakan Sesi)",
                "statusText": "Pencurian Token JWT",
                "statusCls": "bad",
                "desc": "Dari paket plaintext yang telah di-strip, penyerang menyalin token otentikasi aktif (`Authorization: Bearer <JWT>`). Token ini mewakili sesi resmi korban di server dompet digital dan dapat digunakan tanpa memerlukan PIN atau password.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Token JWT berumur sangat pendek (Short-lived TTL < 5 menit), Token Binding ke sertifikat perangkat klien (DPoP / mTLS), dan deteksi IP/Fingerprint mismatch pada API Gateway.",
                "analogy": "Seperti mencuri tiket gelang VIP konser saat Anda berjalan di lorong, lalu memakai gelang itu untuk masuk ke ruang VIP seolah-olah penjahat tersebut adalah Anda.",
                "triad": {
                    "c": {"text": "Bocor Total", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Session Hijacking", "Pengambilalihan sesi login aktif pengguna oleh pihak ketiga"],
                    ["JWT (JSON Web Token)", "Format token ringkas dan mandiri untuk transmisi klaim keamanan"],
                    ["Token Replay", "Mengirimkan ulang token yang disadap untuk memperoleh hak akses korban"]
                ],
                "quiz": {
                    "q": "Mengapa pencurian token JWT (Session Hijacking) sangat berbahaya pada aplikasi e-wallet?",
                    "options": [
                        "Karena API backend menganggap siapapun yang memegang token valid sebagai pemilik akun sah tanpa meminta autentikasi ulang.",
                        "Karena token JWT dapat menggandakan uang di rekening.",
                        "Karena token JWT merusak layar kaca smartphone."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Konsep arsitektur REST Stateless memverifikasi request murni berdasarkan token; jika token dicuri, penyerang memperoleh hak akses penuh."
                },
                "svg": '''
                  <!-- Session Token Extraction -->
                  <rect x="80" y="60" width="300" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                  <text x="230" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PAKET HTTP TERINSPEKSI</text>
                  <rect x="95" y="110" width="270" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="105" y="125" width="250" height="60" rx="4" fill="#312e81" stroke="#6366f1"/>
                  <text x="115" y="145" fill="#c7d2fe" font-size="8.5" font-weight="700">Decoded JWT Payload (JSON):</text>
                  <text x="115" y="162" fill="#86efac" font-size="7.5" font-family="monospace">{\"sub\": \"user_9981\", \"role\": \"customer\",</text>
                  <text x="115" y="174" fill="#86efac" font-size="7.5" font-family="monospace"> \"wallet_id\": \"W-8812\", \"bal\": 12000000}</text>

                  <rect x="105" y="195" width="250" height="105" rx="6" fill="#450a0a" stroke="#ef4444"/>
                  <text x="230" y="218" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">&#10007; AUTHENTICATION BYPASS</text>
                  <text x="230" y="235" text-anchor="middle" fill="#fca5a5" font-size="8">Token masih berlaku 24 jam ke depan</text>
                  <text x="230" y="252" text-anchor="middle" fill="#fca5a5" font-size="8">Tidak membutuhkan input PIN ulang</text>
                  <text x="230" y="275" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">SESI KORBAN TERBAJAK TOTAL</text>

                  <!-- Transfer to Attacker Injector -->
                  <path d="M 395 190 L 485 190" stroke="#06b6d4" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#06b6d4"/>

                  <!-- Attacker Device Console -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#06b6d4" stroke-width="2" filter="url(#glowV3a)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">POSTMAN / CURL ATTACKER</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="525" y="135" fill="#f87171" font-size="8" font-family="monospace">&gt; curl -X POST api.dompetpay.com</text>
                  <text x="525" y="152" fill="#38bdf8" font-size="8" font-family="monospace">-H \"Authorization: Bearer ...\"</text>
                  <text x="525" y="170" fill="#facc15" font-size="8" font-family="monospace">-d '{\"action\": \"transfer\"}'</text>
                  <rect x="525" y="195" width="200" height="105" rx="6" fill="#1e1b4b"/>
                  <text x="625" y="220" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="800">Langkah Berikutnya:</text>
                  <text x="625" y="240" text-anchor="middle" fill="#cbd5e1" font-size="8">Replay request transaksi</text>
                  <text x="625" y="260" text-anchor="middle" fill="#cbd5e1" font-size="8">atau inject pembayaran ilegal</text>
                  <text x="625" y="280" text-anchor="middle" fill="#fca5a5" font-size="8">dari perangkat penyerang</text>
                ''',
                "defenseSvg": '''
                  <!-- DPoP / mTLS Token Binding Defense -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; TOKEN BINDING &amp; DPOP (DEMONSTRATING PROOF-OF-POSSESSION)</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Token Terikat Kunci Perangkat Korban:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Token JWT diikat secara kriptografis ke kunci privat perangkat ponsel korban</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Penyerang yang mencuri token tidak dapat menggunakannya di laptop mereka (DPoP Mismatch)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; API Gateway menolak request dengan status: HTTP 401 Unauthorized (Invalid Signature)</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">TOKEN CURISAN TIDAK DAPAT DIPAKAI</text>
                '''
            },
            {
                "title": "Replay / Exploit (Eksekusi Transaksi Ilegal)",
                "statusText": "Injeksi Transaksi Ilegal",
                "statusCls": "bad",
                "desc": "Penyerang menyuntikkan (inject) permintaan transaksi transfer dana atau mengulang request pembayaran lama (Replay Attack) langsung dari laptop penyerang. Backend dompet digital memproses pembayaran tersebut karena token sesi dianggap sah.",
                "defenseDesc": "Mitigasi Pilar Teknologi & Operasional: Implementasi Anti-Replay Nonce, Timestamp Request Signing dengan toleransi < 30 detik, serta verifikasi Mutual TLS (mTLS) di level API Gateway.",
                "analogy": "Seperti mengkopi tanda tangan sah seseorang di atas lembar cek kosong dan mencairkannya di teller yang tidak mencurigainya.",
                "triad": {
                    "c": {"text": "Bocor", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Terganggu", "cls": "warn"}
                },
                "terms": [
                    ["Replay Attack", "Menembakkan ulang paket transaksi yang valid untuk menduplikasi efeknya"],
                    ["Cryptographic Nonce", "Angka acak unik satu kali pakai untuk mencegah request diduplikasi"],
                    ["Request Timestamping", "Batas kadaluwarsa request dalam hitungan detik"]
                ],
                "quiz": {
                    "q": "Bagaimana mekanisme Nonce dan Timestamp mencegah serangan Replay Attack?",
                    "options": [
                        "Server mencatat setiap nomor acak (nonce) yang sudah pernah digunakan dan menolak request dengan nonce sama atau timestamp yang sudah kedaluwarsa.",
                        "Nonce membuat server mematikan koneksi internet.",
                        "Timestamp membatasi ukuran file gambar transfer."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Nonce sekali pakai (Number Used Once) memastikan request lama yang disadap tidak pernah bisa dieksekusi ulang."
                },
                "svg": '''
                  <!-- Injection Attack Sequence -->
                  <rect x="70" y="60" width="300" height="280" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV3a)"/>
                  <text x="220" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">INJEKSI REQUEST DARI LAPTOP ATTACKER</text>
                  <rect x="85" y="110" width="270" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="132" fill="#38bdf8" font-size="8.5" font-family="monospace">POST /api/v1/payment/transfer</text>
                  <text x="95" y="150" fill="#f87171" font-size="8" font-family="monospace">Payload Injected:</text>
                  <text x="95" y="168" fill="#facc15" font-size="7.5" font-family="monospace">{\"source_wallet\": \"W-8812\",</text>
                  <text x="95" y="184" fill="#facc15" font-size="7.5" font-family="monospace"> \"target_wallet\": \"ATTACKER-MULE-01\",</text>
                  <text x="95" y="200" fill="#facc15" font-size="7.5" font-family="monospace"> \"amount\": 10000000}</text>
                  <rect x="95" y="220" width="250" height="80" rx="4" fill="#7f1d1d"/>
                  <text x="220" y="245" text-anchor="middle" fill="#fecaca" font-size="8.5" font-weight="800">&#9888; REPLAY REQUEST DILUNCURKAN</text>
                  <text x="220" y="265" text-anchor="middle" fill="#fff" font-size="8">Menggunakan token curian korban</text>
                  <text x="220" y="285" text-anchor="middle" fill="#a7f3d0" font-size="8">Response: HTTP 200 OK (Processed)</text>

                  <!-- Stream to Bank Core -->
                  <path d="M 385 190 L 485 190" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#ef4444"/>

                  <!-- Bank Server Core Ledger -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#serverGrad)" stroke="#38bdf8" stroke-width="1.8"/>
                  <text x="625" y="90" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="800">CORE BANKING LEDGER</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="525" y="125" width="200" height="40" rx="4" fill="#450a0a" stroke="#ef4444"/>
                  <text x="625" y="145" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="700">TRANSAKSI ILEGAL DIPROSES:</text>
                  <text x="625" y="158" text-anchor="middle" fill="#f87171" font-size="11" font-weight="800">- Rp 10.000.000</text>
                  
                  <rect x="525" y="175" width="200" height="45" rx="4" fill="#064e3b" stroke="#22c55e"/>
                  <text x="625" y="195" text-anchor="middle" fill="#a7f3d0" font-size="8" font-weight="700">DANA MASUK KE ATTACKER:</text>
                  <text x="625" y="208" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="800">+ Rp 10.000.000</text>

                  <rect x="525" y="230" width="200" height="75" rx="4" fill="#1e1b4b"/>
                  <text x="625" y="255" text-anchor="middle" fill="#c7d2fe" font-size="8.5" font-weight="700">KORBAN TIDAK SADAR:</text>
                  <text x="625" y="272" text-anchor="middle" fill="#cbd5e1" font-size="7.5">Ponsel korban masih tersambung WiFi,</text>
                  <text x="625" y="288" text-anchor="middle" fill="#fca5a5" font-size="7.5">uang di rekening telah terpotong.</text>
                ''',
                "defenseSvg": '''
                  <!-- Anti Replay Nonce & HMAC Signature Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; VERIFIKASI ANTI-REPLAY NONCE &amp; HMAC REQUEST SIGNATURE</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Validasi Integritas Transaksi di Gateway:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; X-Signature Header: Hash HMAC payload ditandatangani kunci sesi privat</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Nonce Cache memeriksa: 'nonce=88192a' telah digunakan sebelumnya</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Gateway menolak injeksi penyerang: HTTP 400 Bad Request (Replay Detected)</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">INJEKSI TRANSAKSI DIGAGALKAN</text>
                '''
            },
            {
                "title": "Dampak Akhir Serangan (Impact Vektor 3A)",
                "statusText": "In-Transit Breach",
                "statusCls": "bad",
                "desc": "Terjadinya transaksi ilegal tanpa otorisasi korban, kompromi sesi pengguna, kebocoran data sensitif saat transit di jaringan publik, serta pelanggaran berat standar PCI-DSS Requirement 4.",
                "defenseDesc": "Evaluasi Resiliensi: Penerapan Certificate Pinning secara mutlak mencegah serangan MitM dan SSL Stripping pada layer transmisi jaringan.",
                "analogy": "Seperti seluruh kuitansi, nomor rekening, dan uang nasabah disalin saat kurir melintasi jembatan penyeberangan umum.",
                "triad": {
                    "c": {"text": "Bocor In-Transit", "cls": "bad"},
                    "i": {"text": "Terkorup", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Transaksi Ilegal", "Pemindahan dana tanpa persetujuan atau interaksi korban"],
                    ["Session Compromise", "Sesi autentikasi dibajak untuk mengeksekusi operasi kritis"],
                    ["Data Leak In-Transit", "Kebocoran informasi finansial selama proses transmisi jaringan"]
                ],
                "quiz": {
                    "q": "Standar keamanan internasional manakah yang mewajibkan enkripsi kuat terhadap data finansial saat transit (in-transit)?",
                    "options": [
                        "PCI-DSS (Payment Card Industry Data Security Standard) Requirement 4.",
                        "Aturan lalu lintas jalan raya kota.",
                        "Panduan pemeliharaan kabel fiber optik bawah tanah."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! PCI-DSS Req 4 mewajibkan proteksi data pemegang kartu dengan kriptografi kuat saat ditransmisikan melalui jaringan publik terbuka."
                },
                "svg": '''
                  <!-- Impact Vector 3A Visual -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="#081e28" stroke="#06b6d4" stroke-width="2.5" filter="url(#glowV3a)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="800">DAMPAK SERANGAN VEKTOR 3A — MAN-IN-THE-MIDDLE</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#042f2e" stroke="#06b6d4"/>
                  <text x="210" y="145" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">TRANSAKSI ILEGAL</text>
                  <text x="210" y="180" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="800">DEBIT ANOMALI</text>
                  <text x="210" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Replay Attack Sukses</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#042f2e" stroke="#06b6d4"/>
                  <text x="410" y="145" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">SESSION HIJACK</text>
                  <text x="410" y="175" text-anchor="middle" fill="#f87171" font-size="24">&#128275;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#fca5a5" font-size="8.5">Token JWT Bocor</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#042f2e" stroke="#06b6d4"/>
                  <text x="610" y="145" text-anchor="middle" fill="#7dd3fc" font-size="11" font-weight="800">DATA LEAK TRANSIT</text>
                  <text x="610" y="180" text-anchor="middle" fill="#f87171" font-size="12" font-weight="800">PCI-DSS NON-COMPLIANT</text>
                  <text x="610" y="210" text-anchor="middle" fill="#fca5a5" font-size="8.5">Pelanggaran Req 4</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#0c4a6e" stroke="#06b6d4"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">KESIMPULAN: KONEKSI TANPA CERTIFICATE PINNING RENTAN DISADAP</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Fintech wajib mengunci fingerprint sertifikat pada binary aplikasi untuk meniadakan risiko MitM.</text>
                ''',
                "defenseSvg": '''
                  <!-- Resilient Defense Matrix V3A -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="14" font-weight="800">&#128737; RESILIENSI TRANSMISI DENGAN CERTIFICATE PINNING</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="210" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">ZERO REPLAY</text>
                  <text x="210" y="180" text-anchor="middle" fill="#34d399" font-size="16" font-weight="800">NONCE VALID</text>
                  <text x="210" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Request Lama Ditolak</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="410" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">SESI TERKUNCI</text>
                  <text x="410" y="175" text-anchor="middle" fill="#34d399" font-size="24">&#128272;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">DPoP Kunci Perangkat</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="610" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">PCI-DSS COMPLIANT</text>
                  <text x="610" y="180" text-anchor="middle" fill="#34d399" font-size="13" font-weight="800">TLS 1.3 ENKRIPSI</text>
                  <text x="610" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Kepatuhan Regulasi 100%</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">INTEGRITAS KANAL KOMUNIKASI TERLINDUNGI PENUH</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Serangan downgrade dan penyadapan proxy berhasil digagalkan sejak tahap awal.</text>
                '''
            },
            {
                "title": "Rangkuman Kontrol Mitigasi Vektor 3A",
                "statusText": "Pertahanan Lapisan Jaringan",
                "statusCls": "ok",
                "desc": "Implementasi 4 pilar kontrol mitigasi Vektor 3A: Strict SSL / Certificate Pinning, Larangan Cleartext Traffic, HSTS Preload, DPoP Token Binding, Anti-Replay Nonce, dan Mutual TLS (mTLS).",
                "defenseDesc": "Mekanisme pengamanan jaringan memastikan integritas jalur transmisi data nasabah tetap terlindungi meskipun koneksi melewati infrastruktur yang tidak terpercaya.",
                "analogy": "Seperti mengirimkan surat berharga di dalam tabung baja dengan kunci kombinasi ganda yang hanya bisa dibuka di kantor pusat bank.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Pilar Teknologi", "Certificate Pinning, TLS 1.3, DPoP Token Binding"],
                    ["Pilar Operasional", "Monitoring rogue AP, Edukasi penggunaan VPN"],
                    ["Pilar Tata Kelola", "Kepatuhan audit PCI-DSS Req 4 & ISO 27001"]
                ],
                "quiz": {
                    "q": "Di tahap manakah serangan Vektor 3A (Man-in-the-Middle) paling efektif dipatahkan sesuai dokumen Modul 02?",
                    "options": [
                        "Pada tahap SSL Stripping dengan menerapkan Certificate Pinning.",
                        "Setelah uang berhasil ditransfer ke rekening hacker.",
                        "Saat ponsel kehabisan daya baterai."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Dokumen Modul 02 menekankan bahwa V3A bisa diblokir di tahap SSL Stripping dengan certificate pinning."
                },
                "svg": '''
                  <!-- Matrix V3A Controls Visual -->
                  <rect x="80" y="60" width="660" height="280" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">MATRIKS KONTROL PERTAHANAN BERLAPIS — VEKTOR 3A (JARINGAN &amp; MITM)</text>
                  
                  <rect x="100" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="170" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TEKNOLOGI</text>
                  <text x="110" y="165" fill="#cbd5e1" font-size="8">&bull; Certificate Pinning</text>
                  <text x="110" y="185" fill="#cbd5e1" font-size="8">&bull; HSTS Preload</text>
                  <text x="110" y="205" fill="#cbd5e1" font-size="8">&bull; DPoP Token Binding</text>
                  <text x="110" y="225" fill="#cbd5e1" font-size="8">&bull; Blokir Cleartext HTTP</text>
                  <text x="110" y="245" fill="#cbd5e1" font-size="8">&bull; Anti-Replay Nonce</text>
                  <text x="110" y="265" fill="#cbd5e1" font-size="8">&bull; TLS 1.3 Strict</text>

                  <rect x="260" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="330" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">OPERASIONAL</text>
                  <text x="270" y="165" fill="#cbd5e1" font-size="8">&bull; Kebijakan VPN Wajib</text>
                  <text x="270" y="185" fill="#cbd5e1" font-size="8">&bull; Deteksi Jaringan Terbuka</text>
                  <text x="270" y="205" fill="#cbd5e1" font-size="8">&bull; Short-Lived JWT TTL</text>
                  <text x="270" y="225" fill="#cbd5e1" font-size="8">&bull; Audit Sertifikat Rutin</text>
                  <text x="270" y="245" fill="#cbd5e1" font-size="8">&bull; Alert TLS Mismatch</text>
                  <text x="270" y="265" fill="#cbd5e1" font-size="8">&bull; Pemantauan WiFi Publik</text>

                  <rect x="420" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="490" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TATA KELOLA</text>
                  <text x="430" y="165" fill="#cbd5e1" font-size="8">&bull; Kepatuhan PCI-DSS 4</text>
                  <text x="430" y="185" fill="#cbd5e1" font-size="8">&bull; SOP Rotasi Kunci CA</text>
                  <text x="430" y="205" fill="#cbd5e1" font-size="8">&bull; Standar Enkripsi BI</text>
                  <text x="430" y="225" fill="#cbd5e1" font-size="8">&bull; Pen-testing Jaringan</text>
                  <text x="430" y="245" fill="#cbd5e1" font-size="8">&bull; Audit Keamanan Tahunan</text>
                  <text x="430" y="265" fill="#cbd5e1" font-size="8">&bull; Manajemen Risiko Siber</text>

                  <rect x="580" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="650" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PENCADANGAN</text>
                  <text x="590" y="165" fill="#cbd5e1" font-size="8">&bull; Backup Kunci Kripto</text>
                  <text x="590" y="185" fill="#cbd5e1" font-size="8">&bull; HSM Redundant Cluster</text>
                  <text x="590" y="205" fill="#cbd5e1" font-size="8">&bull; Log Transaksi WORM</text>
                  <text x="590" y="225" fill="#cbd5e1" font-size="8">&bull; Replikasi Sesi Gateway</text>
                  <text x="590" y="245" fill="#cbd5e1" font-size="8">&bull; Failover Gateway Multi-AZ</text>
                  <text x="590" y="265" fill="#cbd5e1" font-size="8">&bull; Audit Forensik Paket</text>
                ''',
                "defenseSvg": None
            }
        ]
    }

print("get_v3a defined.")
