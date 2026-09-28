# -*- coding: utf-8 -*-
"""
Data definitions for all 6 FinTech Threat Vectors:
  Vector 1: Mobile Banking Trojan & Overlay Attack (Sisi Client)
  Vector 2: Phishing & Adversary-in-the-Middle (AitM) Reverse Proxy (Jalur Identitas)
  Vector 3: Man-in-the-Middle & Rogue WiFi (Jalur Jaringan)
  Vector 4: API Exploitation — Broken Object Level Authorization (BOLA / IDOR)
  Vector 5: Layer 7 API Flooding / DDoS (Infrastruktur Backend)
  Vector 6: Resiliensi Data — Skema Backup 3-2-1 & Immutable WORM
"""

SCENARIOS = {
    1: {
        "tag": "VEKTOR 1 &bull; MOBILE BANKING TROJAN &amp; OVERLAY",
        "title": "Vektor 1: Mobile Banking Trojan &amp; Overlay Attack (Sisi Client)",
        "badge": "V1 &bull; Client Malware",
        "desc_overview": "Serangan malware perbankan Android yang mengeksploitasi sideloading APK palsu, membajak izin Accessibility Service, dan menampilkan jendela overlay palsu di atas aplikasi dompet digital asli untuk mencuri PIN, menyadap SMS OTP, dan mengeksekusi transfer otomatis (ATS).",
        "steps": [
            {
                "title": "Pengiriman & Sideloading APK Palsu (Social Delivery)",
                "status": {"text": "Phishing Infiltrasi", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Penyerang mengirimkan berkas APK berbahaya (misal: 'Undangan_Digital.apk' atau 'Resi_Paket_JNE.apk') melalui pesan WhatsApp / Telegram. Korban terpedaya untuk memasang berkas tersebut di luar toko resmi Google Play Store (sideloading) sehingga luput dari kurasi awal.",
                "terms": [
                    ["Vektor Distribusi", "Social Engineering via Pesan Instan (WhatsApp / SMS)"],
                    ["Tipe Malware", "Android Banking Trojan (Keluarga Anatsa / TeaBot / Godfather)"],
                    ["Tujuan Awal", "Mendapatkan foothold di perangkat korban tanpa membutuhkan hak root"]
                ],
                "defenseInfo": "Edukasi nasabah anti-sideloading dan pembatasan instalasi aplikasi dari sumber tidak resmi (unknown sources) pada level OS/kebijakan korporasi.",
                "svg": """
                    <!-- Adversary Box -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="1.5" filter="url(#glowRed)"/>
                    <text x="130" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYERANG (C2 SERVER)</text>
                    <rect x="55" y="105" width="150" height="85" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="125" fill="#38bdf8" font-size="9" font-family="monospace">&gt; python3 blast_phish.py</text>
                    <text x="65" y="142" fill="#f87171" font-size="9" font-family="monospace">[+] payload: Undangan.apk</text>
                    <text x="65" y="159" fill="#4ade80" font-size="9" font-family="monospace">[+] victim: +62812xxxxxx</text>
                    <text x="65" y="176" fill="#fcd34d" font-size="9" font-family="monospace">[*] Sending social bait...</text>
                    <rect x="55" y="200" width="150" height="35" rx="6" fill="#18181b" stroke="#ef4444"/>
                    <text x="130" y="222" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="700">APK Malware Ready</text>

                    <!-- Delivery Arrow -->
                    <path d="M 230 180 L 360 180" stroke="#f59e0b" stroke-width="2.5" class="flow-packet"/>
                    <polygon points="360,174 374,180 360,186" fill="#f59e0b"/>
                    <text x="295" y="168" text-anchor="middle" fill="#fcd34d" font-size="10" font-weight="700">Kirim APK Palsu</text>

                    <!-- Victim Smartphone -->
                    <rect x="390" y="35" width="220" height="310" rx="22" fill="url(#phoneGrad)" stroke="#38bdf8" stroke-width="2"/>
                    <rect x="404" y="58" width="192" height="265" rx="12" fill="url(#screenGrad)"/>
                    <rect x="475" y="42" width="50" height="6" rx="3" fill="#334155"/>
                    
                    <!-- WhatsApp Chat Mockup -->
                    <rect x="414" y="70" width="172" height="30" rx="6" fill="#075e54"/>
                    <text x="440" y="89" fill="#fff" font-size="10" font-weight="700">WhatsApp &bull; Kurir Paket</text>
                    <rect x="418" y="110" width="164" height="85" rx="8" fill="#065f46" stroke="#059669"/>
                    <text x="428" y="130" fill="#a7f3d0" font-size="9" font-weight="700">Paket Anda Tertunda!</text>
                    <text x="428" y="145" fill="#ecfdf5" font-size="8.5">Unduh resi pelacakan resmi:</text>
                    <rect x="428" y="153" width="144" height="26" rx="4" fill="#047857"/>
                    <text x="438" y="170" fill="#fef08a" font-size="9" font-weight="700">&#128230; Resi_JNT_Paket.apk (5.8MB)</text>

                    <!-- Sideload Warning Dialog -->
                    <rect x="418" y="210" width="164" height="75" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="500" y="230" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">Pasang Aplikasi Tidak Dikenal?</text>
                    <text x="500" y="246" text-anchor="middle" fill="#cbd5e1" font-size="8">Sumber WhatsApp tidak diizinkan</text>
                    <rect x="430" y="255" width="65" height="20" rx="4" fill="#7f1d1d"/>
                    <text x="462" y="269" text-anchor="middle" fill="#fff" font-size="8">Batal</text>
                    <rect x="505" y="255" width="65" height="20" rx="4" fill="#ef4444"/>
                    <text x="537" y="269" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">Izinkan</text>

                    <!-- Target Ledger / Bank Box -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="730" y="90" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="800">CORE BANKING API</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <circle cx="685" cy="135" r="5" fill="#22c55e"/>
                    <text x="698" y="139" fill="#94a3b8" font-size="9">API Gateway: Normal</text>
                    <circle cx="685" cy="165" r="5" fill="#22c55e"/>
                    <text x="698" y="169" fill="#94a3b8" font-size="9">Core Ledger: Normal</text>
                    <text x="730" y="230" text-anchor="middle" fill="#64748b" font-size="9">Belum Ada Transaksi</text>
                """,
                "checkpoint": {
                    "q": "Mengapa malware Android perbankan didistribusikan melalui pesan WhatsApp/sideloading APK di luar Play Store?",
                    "options": [
                        "Untuk menghindari mekanisme kurasi dan pemindaian Google Play Protect yang otomatis mendeteksi signature malware.",
                        "Karena sistem operasi Android secara otomatis memberikan hak root ke semua berkas yang dikirim via WhatsApp.",
                        "Karena aplikasi perbankan hanya mengizinkan transaksi jika dipasang dari browser."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Distribusi sideloading APK dilakukan sengaja untuk menghindari gerbang kurasi Google Play Store dan Play Protect."
                }
            },
            {
                "title": "Penyalahgunaan Izin Accessibility Service (The Silent Enabler)",
                "status": {"text": "Eskalasi Izin", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Setelah terpasang, trojan memunculkan layar penipuan yang memaksa korban mengaktifkan 'Layanan Aksesibilitas' (Accessibility Service) dengan dalih pembaruan sistem. Begitu izin BIND_ACCESSIBILITY_SERVICE diberikan, malware memperoleh kendali penuh untuk membaca seluruh teks di layar (UI tree inspection), mendeteksi aplikasi apa yang sedang aktif, dan menyimulasikan ketukan tombol.",
                "terms": [
                    ["Izin Kritis", "android.permission.BIND_ACCESSIBILITY_SERVICE"],
                    ["Kapabilitas Malware", "Membaca teks antarmuka (UI Tree), keylogging, auto-click tombol sistem"],
                    ["Trik Rekayasa", "Menyamarkan nama layanan menjadi 'Pembaruan Keamanan Sistem Android'"]
                ],
                "defenseInfo": "Pendeteksian proaktif aplikasi mencurigakan yang memiliki izin Accessibility aktif serta pencabutan otomatis melalui kebijakan MDM / deteksi RASP.",
                "svg": """
                    <!-- Attacker monitoring -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="130" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYERANG (C2)</text>
                    <rect x="55" y="110" width="150" height="90" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="130" fill="#f87171" font-size="9" font-family="monospace">[*] Waiting for A11y...</text>
                    <text x="65" y="148" fill="#eab308" font-size="9" font-family="monospace">[!] Hooking UI Events</text>
                    <text x="65" y="166" fill="#4ade80" font-size="9" font-family="monospace">[+] ACCESSIBILITY: GRANTED</text>
                    <text x="65" y="184" fill="#38bdf8" font-size="9" font-family="monospace">&gt; Full UI Control Active</text>

                    <!-- Connection -->
                    <path d="M 230 180 L 360 180" stroke="#ef4444" stroke-width="2.5" class="flow-packet"/>
                    <polygon points="230,174 216,180 230,186" fill="#ef4444"/>
                    <text x="295" y="168" text-anchor="middle" fill="#f87171" font-size="9" font-weight="700">A11y Control Hooked</text>

                    <!-- Smartphone - Accessibility Setting Screen -->
                    <rect x="390" y="35" width="220" height="310" rx="22" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <rect x="404" y="58" width="192" height="265" rx="12" fill="url(#screenGrad)"/>
                    <rect x="475" y="42" width="50" height="6" rx="3" fill="#334155"/>

                    <!-- Settings Header -->
                    <rect x="414" y="70" width="172" height="30" rx="6" fill="#1e293b"/>
                    <text x="424" y="89" fill="#f1f5f9" font-size="10" font-weight="700">&larr; Aksesibilitas Sistem</text>

                    <!-- Accessibility Service Item -->
                    <rect x="418" y="110" width="164" height="60" rx="8" fill="#1e1b4b" stroke="#818cf8"/>
                    <text x="428" y="128" fill="#c7d2fe" font-size="9" font-weight="700">Pembaruan Sistem (Malware)</text>
                    <text x="428" y="142" fill="#94a3b8" font-size="8">Layanan aktif memantau layar</text>
                    <rect x="535" y="120" width="36" height="18" rx="9" fill="#22c55e"/>
                    <circle cx="560" cy="129" r="7" fill="#fff"/>

                    <!-- Danger Prompt -->
                    <rect x="418" y="185" width="164" height="100" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="500" y="205" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">&#9888; Izinkan Kontrol Penuh?</text>
                    <text x="428" y="222" fill="#fecaca" font-size="7.8">&bull; Baca semua konten &amp; input PIN</text>
                    <text x="428" y="235" fill="#fecaca" font-size="7.8">&bull; Pantau interaksi layar nasabah</text>
                    <text x="428" y="248" fill="#fecaca" font-size="7.8">&bull; Buat jendela di atas aplikasi</text>
                    <rect x="505" y="258" width="65" height="20" rx="4" fill="#ef4444"/>
                    <text x="537" y="272" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">Izinkan</text>

                    <!-- Bank Server -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="730" y="90" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="800">CORE BANKING API</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="730" y="180" text-anchor="middle" fill="#64748b" font-size="9">Server Belum Curiga</text>
                    <text x="730" y="200" text-anchor="middle" fill="#ef4444" font-size="8.5">(Ancaman Tersembunyi di Klien)</text>
                """,
                "checkpoint": {
                    "q": "Mengapa izin Accessibility Service sangat berbahaya jika disalahgunakan oleh malware perbankan?",
                    "options": [
                        "Karena malware dapat membaca seluruh struktur antarmuka (UI tree), menyadap ketukan layar, dan menekan tombol secara otomatis tanpa campur tangan pengguna.",
                        "Karena Accessibility Service secara permanen menghapus data di memory card pengguna.",
                        "Karena izin tersebut memutus jaringan internet pada perangkat seluler korban."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Accessibility Service diciptakan untuk membantu difabel, namun jika disalahgunakan malware, dapat membaca seluruh elemen UI dan menyimulasikan sentuhan layar."
                }
            },
            {
                "title": "Injeksi Jendela Overlay Palsu (Cloak & Dagger Attack)",
                "status": {"text": "Eksploitasi Overlay", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Ketika korban membuka aplikasi dompet digital asli (misal: Bank/E-Wallet resmi), Accessibility Service mendeteksi event peluncuran package com.fintech.ewallet. Dalam hitungan milidetik, trojan memunculkan jendela overlay palsu (SYSTEM_ALERT_WINDOW) yang 100% identik tepat di atas aplikasi asli. Korban merasa masih berada di aplikasi resmi.",
                "terms": [
                    ["Izin Android", "android.permission.SYSTEM_ALERT_WINDOW"],
                    ["Teknik Serangan", "UI Redressing / Overlay Attack / Tapjacking"],
                    ["Referensi Riset", "Cloak & Dagger (Fratantonio et al., USENIX / Black Hat)"]
                ],
                "defenseInfo": "Penerapan filter anti-tapjacking pada kode Android (setFilterTouchesWhenObscured) dan deteksi runtime window overlay.",
                "svg": """
                    <!-- Attacker Trigger -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="130" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">TROJAN DAEMON</text>
                    <rect x="55" y="110" width="150" height="90" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="128" fill="#eab308" font-size="8.5" font-family="monospace">[EVENT] pkg: com.fintech.ewallet</text>
                    <text x="65" y="146" fill="#f87171" font-size="8.5" font-family="monospace">[ACTION] Draw Overlay Window</text>
                    <text x="65" y="164" fill="#38bdf8" font-size="8.5" font-family="monospace">[STATUS] Obscuring real app</text>
                    <text x="65" y="182" fill="#4ade80" font-size="8.5" font-family="monospace">&gt; Awaiting PIN input</text>

                    <!-- Split Phone Visualization -->
                    <rect x="360" y="35" width="280" height="310" rx="22" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <rect x="375" y="58" width="250" height="265" rx="12" fill="#030712"/>
                    <rect x="475" y="42" width="50" height="6" rx="3" fill="#334155"/>

                    <!-- Layer 1: Real App (Underneath) -->
                    <rect x="385" y="70" width="230" height="110" rx="8" fill="#0c4a6e" stroke="#0284c7" stroke-dasharray="4 2"/>
                    <text x="500" y="90" text-anchor="middle" fill="#7dd3fc" font-size="9" font-weight="700">APLIKASI DOMPET DIGITAL ASLI (Tertutup di Bawah)</text>
                    <text x="500" y="106" text-anchor="middle" fill="#bae6fd" font-size="8">Package: com.fintech.ewallet</text>
                    <rect x="440" y="115" width="120" height="20" rx="4" fill="#0369a1"/>
                    <text x="500" y="129" text-anchor="middle" fill="#fff" font-size="8">Antarmuka Asli</text>

                    <!-- Arrow Overlay Drop -->
                    <path d="M 500 185 L 500 205" stroke="#ef4444" stroke-width="3" marker-end="url(#arrowRed)"/>
                    <text x="500" y="198" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="800">OVERLAY INJECTED</text>

                    <!-- Layer 2: Fake Overlay Window (On Top) -->
                    <rect x="385" y="210" width="230" height="105" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="2"/>
                    <text x="500" y="228" text-anchor="middle" fill="#fecaca" font-size="9.5" font-weight="800">&#9888; JENDELA OVERLAY PALSU (Di Depan)</text>
                    <text x="500" y="244" text-anchor="middle" fill="#fed7aa" font-size="8">Masukkan 6 Digit PIN Transaksi E-Wallet Anda:</text>
                    <!-- Fake PIN Inputs -->
                    <circle cx="445" cy="265" r="7" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="465" cy="265" r="7" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="485" cy="265" r="7" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="505" cy="265" r="7" fill="#18181b" stroke="#71717a"/>
                    <circle cx="525" cy="265" r="7" fill="#18181b" stroke="#71717a"/>
                    <circle cx="545" cy="265" r="7" fill="#18181b" stroke="#71717a"/>
                    <text x="500" y="295" text-anchor="middle" fill="#fca5a5" font-size="7.5" font-weight="700">Input Disadap Langsung oleh Trojan</text>

                    <!-- Server -->
                    <rect x="670" y="60" width="140" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="740" y="90" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="800">BANK BACKEND</text>
                    <rect x="680" y="110" width="120" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="740" y="190" text-anchor="middle" fill="#64748b" font-size="8.5">Menunggu Permintaan</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana cara kerja serangan Overlay Attack (Cloak & Dagger)?",
                    "options": [
                        "Malware menggambar jendela palsu berizin SYSTEM_ALERT_WINDOW di atas aplikasi perbankan asli sehingga pengguna mengetikkan PIN pada jendela penyerang.",
                        "Malware membongkar casing fisik ponsel dan memasang mikrochip di baterai.",
                        "Malware mengubah warna wallpaper ponsel menjadi merah."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Serangan Overlay menampilkan UI palsu persis di atas aplikasi resmi untuk mencegat input kredensial pengguna."
                }
            },
            {
                "title": "Pencurian Kredensial PIN & Intersepsi SMS OTP",
                "status": {"text": "Credential Theft", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Korban yang tidak menyadari adanya jendela palsu memasukkan 6 digit PIN. Keylogger trojan mencatat setiap digit. Pada saat yang sama, SMS OTP verifikasi yang dikirim perbankan otomatis dicegat oleh receiver Accessibility Service trojan sebelum ditampilkan ke notifikasi pengguna, kemudian langsung dieksfiltrasi ke C2 server.",
                "terms": [
                    ["Data Curian", "6 Digit PIN Transaksi + Kode OTP SMS"],
                    ["Intersepsi SMS", "Accessibility Notification Listener / Broadcast Receiver Mining"],
                    ["Eksfiltrasi", "Mengirim kredensial terenkripsi ke Command & Control Server penyerang"]
                ],
                "defenseInfo": "Penyimpanan kredensial biometrik lokal di Hardware-backed Keystore (Secure Enclave / TEE) sebagai pengganti OTP SMS.",
                "svg": """
                    <!-- Attacker Terminal Exfiltration -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="140" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">C2 EXFILTRATION SERVER</text>
                    <rect x="55" y="110" width="170" height="100" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="130" fill="#4ade80" font-size="9" font-family="monospace">[+] INCOMING EXFIL DATA:</text>
                    <text x="65" y="148" fill="#fde047" font-size="9" font-family="monospace">Target: Budi Santoso</text>
                    <text x="65" y="166" fill="#f87171" font-size="9.5" font-weight="700" font-family="monospace">STOLEN_PIN = 819230</text>
                    <text x="65" y="184" fill="#f87171" font-size="9.5" font-weight="700" font-family="monospace">STOLEN_OTP = 492011</text>
                    <text x="65" y="200" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; Ready to trigger ATS</text>

                    <!-- Exfil Packet Arrow -->
                    <path d="M 400 180 L 250 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <polygon points="250,174 236,180 250,186" fill="#ef4444"/>
                    <text x="325" y="170" text-anchor="middle" fill="#fca5a5" font-size="9.5" font-weight="800">PIN &amp; OTP Dicuri &rarr;</text>

                    <!-- Smartphone -->
                    <rect x="410" y="35" width="210" height="310" rx="22" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2"/>
                    <rect x="424" y="58" width="182" height="265" rx="12" fill="url(#screenGrad)"/>
                    <rect x="490" y="42" width="50" height="6" rx="3" fill="#334155"/>

                    <!-- Stolen Notification Intercept -->
                    <rect x="432" y="75" width="166" height="60" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
                    <text x="442" y="93" fill="#a5b4fc" font-size="8.5" font-weight="700">&#128274; SMS OTP Masuk (Dicegat)</text>
                    <text x="442" y="108" fill="#f1f5f9" font-size="8">Bank: Jangan beri tahu siapa pun!</text>
                    <text x="442" y="122" fill="#fde047" font-size="9" font-weight="800">Kode OTP Anda: 492011</text>

                    <rect x="432" y="150" width="166" height="95" rx="6" fill="#450a0a" stroke="#ef4444"/>
                    <text x="515" y="172" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">Input PIN Tercatat</text>
                    <text x="515" y="195" text-anchor="middle" fill="#fff" font-size="16" letter-spacing="4">&bull;&bull;&bull;&bull;&bull;&bull;</text>
                    <rect x="442" y="210" width="146" height="22" rx="4" fill="#991b1b"/>
                    <text x="515" y="225" text-anchor="middle" fill="#fecaca" font-size="8" font-weight="700">Terekam oleh Keylogger</text>

                    <!-- Server -->
                    <rect x="660" y="60" width="150" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="735" y="90" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="800">SMS GATEWAY</text>
                    <rect x="675" y="110" width="120" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <path d="M 670 120 L 610 120" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
                    <text x="735" y="150" text-anchor="middle" fill="#94a3b8" font-size="8.5">OTP Terkirim Resmi</text>
                    <text x="735" y="170" text-anchor="middle" fill="#ef4444" font-size="8">(Tetapi Dicegat Trojan)</text>
                """,
                "checkpoint": {
                    "q": "Mengapa verifikasi SMS OTP konvensional tidak berdaya melawan malware perbankan di sisi klien?",
                    "options": [
                        "Karena malware memiliki izin Accessibility yang mampu membaca teks SMS masuk secara instan dan menyembunyikan notifikasi dari korban.",
                        "Karena SMS OTP dikirim tanpa enkripsi oleh satelit NASA.",
                        "Karena SMS OTP hanya berlaku selama 1 detik."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Malware dengan izin Accessibility dapat membaca SMS yang masuk secara instan di perangkat korban sebelum disadari oleh pemiliknya."
                }
            },
            {
                "title": "Automated Transfer System (ATS) & Pengurasan Dana",
                "status": {"text": "Dampak Finansial", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Trojan mengaktifkan modul Automated Transfer System (ATS). Di latar belakang, trojan secara otomatis membuka aplikasi e-wallet asli, mengisi nomor rekening penampung (mule account), memasukkan PIN curian, dan menekan tombol konfirmasi transfer—seluruhnya dilakukan dalam hitungan detik saat layar dipadamkan (black screen) agar korban tidak curiga.",
                "terms": [
                    ["Modul Penipuan", "Automated Transfer System (ATS) Engine"],
                    ["Rekening Tujuan", "Rekening Penampung (Money Mule Account)"],
                    ["Dampak Kerugian", "Kerugian Finansial Massal Langsung & Pelanggaran Regulasi BI/OJK"]
                ],
                "defenseInfo": "SOP deteksi pola Automated Transfer System (ATS) dan hold otomatis transaksi anomali sebelum settlement final dilakukan.",
                "svg": """
                    <!-- Attacker Mule Account -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="130" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">REKENING PENAMPUNG (MULE)</text>
                    <rect x="55" y="110" width="150" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="135" fill="#4ade80" font-size="9" font-family="monospace">[+] ATS SUCCESS</text>
                    <text x="65" y="155" fill="#fde047" font-size="9" font-weight="700" font-family="monospace">+ Rp 15.000.000</text>
                    <text x="65" y="175" fill="#94a3b8" font-size="8" font-family="monospace">From: Budi Santoso</text>
                    <text x="65" y="195" fill="#94a3b8" font-size="8" font-family="monospace">TxID: ATS-9940128</text>
                    <rect x="65" y="215" width="130" height="25" rx="4" fill="#991b1b"/>
                    <text x="130" y="232" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">DANA TERCUCI</text>

                    <!-- Smartphone Executing ATS -->
                    <rect x="360" y="35" width="220" height="310" rx="22" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2"/>
                    <rect x="374" y="58" width="192" height="265" rx="12" fill="#090514"/>
                    <rect x="445" y="42" width="50" height="6" rx="3" fill="#334155"/>

                    <rect x="384" y="70" width="172" height="30" rx="6" fill="#450a0a"/>
                    <text x="470" y="89" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">ATS RUNNING IN BG</text>

                    <rect x="384" y="110" width="172" height="135" rx="6" fill="#18181b" stroke="#ef4444"/>
                    <text x="394" y="130" fill="#f87171" font-size="8" font-weight="700">Auto-Click Transfer...</text>
                    <text x="394" y="148" fill="#cbd5e1" font-size="8">Tujuan: 549102910</text>
                    <text x="394" y="165" fill="#cbd5e1" font-size="8">Nominal: Rp 15.000.000</text>
                    <text x="394" y="182" fill="#4ade80" font-size="8">PIN: 819230 [Auto-Filled]</text>
                    <rect x="394" y="195" width="152" height="24" rx="4" fill="#ef4444"/>
                    <text x="470" y="211" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Transfer Berhasil</text>

                    <text x="470" y="270" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="700">&#128546; Saldo Korban: Rp 5.000</text>

                    <!-- Bank Core Server -->
                    <rect x="620" y="60" width="190" height="250" rx="12" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                    <text x="715" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">CORE BANKING LEDGER</text>
                    <rect x="635" y="110" width="160" height="180" rx="6" fill="#090e1a" stroke="#334155"/>
                    <text x="645" y="135" fill="#f87171" font-size="9" font-family="monospace">&gt; DEBIT ACC: 10023412</text>
                    <text x="645" y="155" fill="#f87171" font-size="9" font-family="monospace">&gt; AMOUNT: Rp 15.000.000</text>
                    <text x="645" y="175" fill="#4ade80" font-size="9" font-family="monospace">&gt; CREDIT MULE: 549102910</text>
                    <text x="645" y="195" fill="#eab308" font-size="9" font-family="monospace">&gt; STATUS: SETTLED</text>
                    <rect x="645" y="220" width="140" height="30" rx="4" fill="#450a0a" stroke="#ef4444"/>
                    <text x="715" y="240" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">BREACH SELESAI</text>
                """,
                "checkpoint": {
                    "q": "Apa yang dimaksud dengan Automated Transfer System (ATS) pada malware perbankan?",
                    "options": [
                        "Modul otomatis yang mengeksekusi instruksi transfer dana ilegal di latar belakang tanpa campur tangan dan tanpa disadari pemilik rekening.",
                        "Fitur transfer gratis antar bank dari Bank Indonesia.",
                        "Pembersih cache otomatis untuk mempercepat performa smartphone."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! ATS adalah kemampuan trojan modern untuk menyelesaikan seluruh proses transfer uang secara otonom menggunakan kredensial curian."
                }
            },
            {
                "title": "Mitigasi Pertahanan: RASP & Anti-Tapjacking Filter",
                "status": {"text": "Mitigasi Aktif", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Pertahanan Defense-in-Depth diterapkan langsung di sisi client: Runtime Application Self-Protection (RASP) ditanamkan dalam kode aplikasi dompet digital. RASP mendeteksi keberadaan overlay aktif (FLAG_WINDOW_IS_OBSCURED), menolak touch event via filter anti-tapjacking, dan langsung memutus sesi transaksi seketika (Session Kill) serta mencatat log audit ke penyimpanan WORM immutable.",
                "terms": [
                    ["Pilar Teknologi", "Runtime Application Self-Protection (RASP) & Anti-Tapjacking Filter"],
                    ["Pilar Operasional", "Pencabutan otomatis izin Accessibility mencurigakan & edukasi nasabah"],
                    ["Pilar Tata Kelola", "Verifikasi code signing sebelum rilis & integrasi threat intelligence malware"]
                ],
                "defenseInfo": "Penerapan pertahanan holistik 3 pilar memotong alur kill chain malware pada tahap awal instalasi dan eksekusi.",
                "svg": """
                    <!-- Blocked Trojan -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#475569" stroke-width="1.5"/>
                    <text x="130" y="90" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="800">MALWARE DILUMPUHKAN</text>
                    <rect x="55" y="110" width="150" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="135" fill="#ef4444" font-size="9" font-family="monospace">[!] Overlay Rejected</text>
                    <text x="65" y="155" fill="#ef4444" font-size="9" font-family="monospace">[!] Touch Blocked</text>
                    <text x="65" y="175" fill="#ef4444" font-size="9" font-family="monospace">[!] Session Terminated</text>
                    <text x="65" y="200" fill="#64748b" font-size="8.5" font-family="monospace">Payload Inactive</text>

                    <!-- Protected Smartphone with RASP Shield -->
                    <rect x="330" y="35" width="280" height="310" rx="22" fill="url(#phoneGrad)" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="344" y="58" width="252" height="265" rx="12" fill="url(#screenGrad)"/>
                    <rect x="445" y="42" width="50" height="6" rx="3" fill="#334155"/>

                    <!-- Green Shield Banner -->
                    <rect x="355" y="70" width="230" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="470" y="88" text-anchor="middle" fill="#6ee7b7" font-size="10" font-weight="800">&#128737; RASP SECURITY ACTIVE</text>
                    <text x="470" y="102" text-anchor="middle" fill="#d1fae5" font-size="8">Runtime Application Self-Protection</text>

                    <!-- Protected Card -->
                    <rect x="355" y="125" width="230" height="180" rx="8" fill="#0f172a" stroke="#22c55e"/>
                    <circle cx="470" cy="165" r="26" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="470" y="172" text-anchor="middle" fill="#86efac" font-size="20">&#10004;</text>
                    <text x="470" y="210" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">OVERLAY TERDETEKSI &amp; DIBLOKIR</text>
                    <text x="470" y="228" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Filter Anti-Tapjacking menolak input sentuhan.</text>
                    <text x="470" y="242" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Sesi perbankan langsung dihentikan otomatis.</text>
                    <rect x="385" y="260" width="170" height="24" rx="4" fill="#15803d"/>
                    <text x="470" y="276" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Saldo Nasabah 100% Aman</text>

                    <!-- Bank Core / WORM Storage -->
                    <rect x="640" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="725" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">IMMUTABLE WORM LOG</text>
                    <rect x="655" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="665" y="135" fill="#22c55e" font-size="8.5" font-family="monospace">[AUDIT FORENSIK]</text>
                    <text x="665" y="155" fill="#94a3b8" font-size="8" font-family="monospace">Event: Overlay Detected</text>
                    <text x="665" y="175" fill="#94a3b8" font-size="8" font-family="monospace">Action: Kill Session</text>
                    <text x="665" y="195" fill="#94a3b8" font-size="8" font-family="monospace">Log: WORM Stored</text>
                    <rect x="665" y="220" width="120" height="30" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="725" y="239" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Zero Financial Loss</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana RASP (Runtime Application Self-Protection) memitigasi serangan Overlay?",
                    "options": [
                        "Dengan mendeteksi keberadaan jendela overlay di atas antarmuka aplikasi, mengabaikan ketukan palsu via anti-tapjacking, dan langsung mematikan sesi aplikasi sebelum PIN tercuri.",
                        "Dengan menghapus nomor telepon nasabah dari jaringan seluler.",
                        "Dengan mengubah mata uang rupiah menjadi dollar secara otomatis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! RASP memantau runtime aplikasi secara mandiri untuk mendeteksi anomali seperti overlay, debugger, atau injeksi kode dan menghentikan sesi seketika."
                }
            }
        ]
    },

    2: {
        "tag": "VEKTOR 2 &bull; PHISHING &amp; AITM REVERSE PROXY",
        "title": "Vektor 2: Phishing &amp; Adversary-in-the-Middle (AitM) Reverse Proxy (Jalur Identitas)",
        "badge": "V2 &bull; AitM Reverse Proxy",
        "desc_overview": "Serangan phishing generasi baru menggunakan toolkit reverse proxy (Evilginx) dan domain typosquatting untuk mem-proxy sesi login secara real-time, mencegat SMS OTP secara live, dan mencuri authenticated session cookie untuk membajak akun (ATO) kurang dari 60 detik.",
        "steps": [
            {
                "title": "Domain Typosquatting & Setup Reverse Proxy Evilginx",
                "status": {"text": "Persiapan AitM", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Penyerang mendaftarkan domain typosquatting yang mirip domain resmi (misal: m-ewallet-login.id) lengkap dengan sertifikat SSL gratis (Let's Encrypt). Di server tersebut dipasang toolkit reverse proxy seperti Evilginx2 yang dikonfigurasi untuk mem-proxy seluruh permintaan ke server bank asli m-ewallet.id.",
                "terms": [
                    ["Toolkit Serangan", "Evilginx2 / Modlishka / Muraena"],
                    ["Domain Palsu", "Typosquatting (cth: m-ewallet-login.id vs m-ewallet.id)"],
                    ["Sertifikat SSL", "HTTPS Valid (gembok hijau palsu membuat korban lengah)"]
                ],
                "defenseInfo": "Pemberantasan proaktif melalui monitoring domain typosquatting dan prosedur DNS takedown.",
                "svg": """
                    <!-- Attacker Evilginx Server -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#a855f7" stroke-width="2" filter="url(#glowCyan)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#d8b4fe" font-size="11" font-weight="800">REVERSE PROXY (EVILGINX2)</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#a855f7"/>
                    <text x="65" y="132" fill="#38bdf8" font-size="9" font-family="monospace">&gt; evilginx2</text>
                    <text x="65" y="150" fill="#a855f7" font-size="9" font-family="monospace">: phishlets hostname ewallet</text>
                    <text x="65" y="168" fill="#fde047" font-size="8.5" font-family="monospace">&gt; m-ewallet-login.id (FAKE)</text>
                    <text x="65" y="186" fill="#4ade80" font-size="8.5" font-family="monospace">&gt; Target: m-ewallet.id (REAL)</text>
                    <text x="65" y="204" fill="#38bdf8" font-size="8.5" font-family="monospace">[+] SSL Cert: Valid Let's Encrypt</text>
                    <rect x="65" y="225" width="170" height="30" rx="4" fill="#2e1065" stroke="#a855f7"/>
                    <text x="150" y="244" text-anchor="middle" fill="#d8b4fe" font-size="9" font-weight="800">Proxy Siap Mencegat</text>

                    <!-- Network Link to Victim -->
                    <path d="M 270 180 L 370 180" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
                    <text x="320" y="170" text-anchor="middle" fill="#fcd34d" font-size="9">Link Phishing</text>

                    <!-- Victim Browser Mockup -->
                    <rect x="380" y="55" width="220" height="260" rx="10" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                    <rect x="380" y="55" width="220" height="35" rx="10" fill="#1e293b"/>
                    <!-- URL Bar with Lock -->
                    <rect x="395" y="63" width="190" height="20" rx="4" fill="#020617" stroke="#334155"/>
                    <text x="405" y="77" fill="#22c55e" font-size="9">&#128274;</text>
                    <text x="420" y="77" fill="#fca5a5" font-size="8.5" font-weight="700">m-ewallet-login.id/auth</text>

                    <rect x="395" y="105" width="190" height="190" rx="6" fill="#090e1a"/>
                    <text x="490" y="130" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="800">DOMPET DIGITAL RESMI</text>
                    <text x="490" y="148" text-anchor="middle" fill="#94a3b8" font-size="8">(Padahal Tampilan dari Proxy)</text>
                    <rect x="410" y="165" width="160" height="22" rx="4" fill="#1e293b"/>
                    <text x="420" y="180" fill="#64748b" font-size="8">Username / No HP</text>
                    <rect x="410" y="195" width="160" height="22" rx="4" fill="#1e293b"/>
                    <text x="420" y="210" fill="#64748b" font-size="8">Password Akun</text>

                    <!-- Real Bank Server -->
                    <rect x="630" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="715" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">SERVER RESMI BANK</text>
                    <rect x="645" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="715" y="140" text-anchor="middle" fill="#38bdf8" font-size="8.5">m-ewallet.id</text>
                    <text x="715" y="170" text-anchor="middle" fill="#64748b" font-size="8">Menunggu Akses Asli</text>
                """,
                "checkpoint": {
                    "q": "Mengapa gembok hijau HTTPS (SSL) pada situs phishing tidak menjamin situs tersebut aman?",
                    "options": [
                        "Karena sertifikat SSL gratis (seperti Let's Encrypt) dapat dibuat oleh siapa saja untuk domain palsu, hanya mengenkripsi koneksi tetapi tidak membuktikan keaslian entitas pemilik.",
                        "Karena gembok SSL hanya berlaku untuk komputer Windows.",
                        "Karena browser selalu salah menampilkan tanda gembok."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Sertifikat SSL hanya mengamankan jalur transmisi, bukan membuktikan reputasi atau kejujuran dari pemilik domain tersebut."
                }
            },
            {
                "title": "Korban Mengakses Reverse Proxy yang Mirip Asli",
                "status": {"text": "AitM Aktif", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Korban menerima pesan spear-phishing dan mengklik link. Browser korban terhubung ke Evilginx. Di saat yang sama, Evilginx membuka koneksi real-time ke server bank resmi, mengambil halaman login resmi, dan menampilkannya kembali ke korban. Antarmuka yang dilihat korban 100% sama dengan aslinya.",
                "terms": [
                    ["Metode Intersepsi", "Adversary-in-the-Middle (AitM) Reverse Proxy"],
                    ["Tampilan Korban", "Identik dengan situs resmi karena di-relay langsung dari server bank"],
                    ["Status Koneksi", "Korban &harr; Evilginx (Fake) &harr; Server Bank (Real)"]
                ],
                "defenseInfo": "Security awareness training bagi staf dan nasabah untuk memeriksa alamat URL dengan teliti.",
                "svg": """
                    <!-- Flow 3 Blocks -->
                    <!-- 1. Victim Browser -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="140" y="90" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="800">KORBAN (BROWSER)</text>
                    <rect x="55" y="110" width="170" height="180" rx="6" fill="#020617"/>
                    <text x="140" y="135" text-anchor="middle" fill="#cbd5e1" font-size="9">Akses: m-ewallet-login.id</text>
                    <text x="140" y="160" text-anchor="middle" fill="#fde047" font-size="8.5">Mengisi Username &amp; Sandi</text>
                    <rect x="70" y="180" width="140" height="24" rx="4" fill="#0284c7"/>
                    <text x="140" y="196" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">Kirim Data Login &rarr;</text>

                    <!-- Forward Packet 1 -->
                    <path d="M 245 180 L 330 180" stroke="#f59e0b" stroke-width="3" class="flow-packet"/>
                    <polygon points="330,174 344,180 330,186" fill="#f59e0b"/>

                    <!-- 2. Evilginx Reverse Proxy in the Middle -->
                    <rect x="345" y="60" width="210" height="250" rx="12" fill="url(#hackerGrad)" stroke="#a855f7" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="450" y="88" text-anchor="middle" fill="#d8b4fe" font-size="10.5" font-weight="800">EVILGINX (IN-THE-MIDDLE)</text>
                    <rect x="360" y="105" width="180" height="185" rx="6" fill="#030712" stroke="#a855f7"/>
                    <text x="370" y="125" fill="#f87171" font-size="8" font-family="monospace">[AITM PROXY INTERCEPT]</text>
                    <text x="370" y="142" fill="#38bdf8" font-size="8" font-family="monospace">&gt; Capturing input params</text>
                    <text x="370" y="160" fill="#fde047" font-size="8" font-family="monospace">&gt; Forwarding to m-ewallet.id</text>
                    <rect x="370" y="180" width="160" height="40" rx="4" fill="#2e1065"/>
                    <text x="450" y="197" text-anchor="middle" fill="#d8b4fe" font-size="8.5" font-weight="700">Relay Real-Time</text>
                    <text x="450" y="212" text-anchor="middle" fill="#94a3b8" font-size="7.5">Kedua belah pihak tidak sadar</text>

                    <!-- Forward Packet 2 -->
                    <path d="M 560 180 L 635 180" stroke="#38bdf8" stroke-width="3" class="flow-packet"/>
                    <polygon points="635,174 649,180 635,186" fill="#38bdf8"/>

                    <!-- 3. Real Bank Server -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="1.5"/>
                    <text x="730" y="90" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">SERVER RESMI BANK</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="730" y="135" text-anchor="middle" fill="#86efac" font-size="8.5">m-ewallet.id</text>
                    <text x="730" y="160" text-anchor="middle" fill="#38bdf8" font-size="8">Menerima Login</text>
                    <rect x="675" y="185" width="110" height="25" rx="4" fill="#065f46"/>
                    <text x="730" y="201" text-anchor="middle" fill="#a7f3d0" font-size="8" font-weight="700">Minta OTP &rarr;</text>
                """,
                "checkpoint": {
                    "q": "Mengapa reverse proxy seperti Evilginx disebut 'Adversary-in-the-Middle' (AitM)?",
                    "options": [
                        "Karena penyerang bertindak sebagai perantara transparan yang meneruskan data antara korban dan server asli secara langsung sambil menyalin seluruh kredensial.",
                        "Karena penyerang berada di tengah-tengah ruangan kantor bank.",
                        "Karena server penyerang hanya bisa beroperasi pada siang hari."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! AitM bertindak sebagai proxy di tengah-tengah alur lalu lintas data untuk meneruskan sekaligus menyadap kredensial secara transparan."
                }
            },
            {
                "title": "Intersepsi Kredensial & OTP Real-Time (Bypass 2FA SMS)",
                "status": {"text": "2FA Ditembus", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Server bank resmi mengirimkan kode OTP ke ponsel korban. Korban memasukkan OTP tersebut ke situs phishing. Evilginx langsung menangkap OTP tersebut dan meneruskannya ke server bank resmi dalam hitungan milidetik. Server bank menganggap permintaan tersebut sah dan mengonfirmasi autentikasi.",
                "terms": [
                    ["Kegagalan 2FA", "OTP Konvensional (SMS/Email) tidak origin-bound"],
                    ["Durasi Intersepsi", "Sub-detik (&lt; 500 ms) sebelum OTP kedaluwarsa"],
                    ["Status Keamanan", "Sistem autentikasi 2FA SMS bobol sepenuhnya"]
                ],
                "defenseInfo": "Migrasi wajib ke FIDO2 / WebAuthn Passkeys yang mengikat otentikasi secara kriptografis ke domain resmi.",
                "svg": """
                    <!-- Step 4 Layout -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="140" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">KORBAN MEMASUKKAN OTP</text>
                    <rect x="55" y="110" width="170" height="180" rx="6" fill="#020617"/>
                    <text x="140" y="135" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Menerima SMS OTP: 884019</text>
                    <rect x="70" y="150" width="140" height="35" rx="4" fill="#18181b" stroke="#f59e0b"/>
                    <text x="140" y="172" text-anchor="middle" fill="#fde047" font-size="12" font-weight="800">8 8 4 0 1 9</text>
                    <rect x="70" y="200" width="140" height="25" rx="4" fill="#dc2626"/>
                    <text x="140" y="217" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">Verifikasi OTP</text>

                    <!-- Forward Packet to Proxy -->
                    <path d="M 245 180 L 330 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <polygon points="330,174 344,180 330,186" fill="#ef4444"/>

                    <!-- Evilginx Capturing OTP -->
                    <rect x="345" y="60" width="210" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="450" y="88" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">EVILGINX MENYADAP OTP</text>
                    <rect x="360" y="105" width="180" height="185" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="370" y="128" fill="#4ade80" font-size="8.5" font-family="monospace">[+] INTERCEPTED CREDENTIALS:</text>
                    <text x="370" y="148" fill="#fde047" font-size="8.5" font-family="monospace">User: budi_finance</text>
                    <text x="370" y="168" fill="#f87171" font-size="9" font-weight="800" font-family="monospace">OTP: 884019 [CAPTURED]</text>
                    <text x="370" y="188" fill="#38bdf8" font-size="8" font-family="monospace">&gt; Relaying OTP to Bank...</text>
                    <rect x="370" y="205" width="160" height="30" rx="4" fill="#991b1b"/>
                    <text x="450" y="224" text-anchor="middle" fill="#fecaca" font-size="8.5" font-weight="800">OTP Diteruskan ke Bank</text>

                    <!-- Forward Packet to Bank -->
                    <path d="M 560 180 L 635 180" stroke="#f59e0b" stroke-width="3" class="flow-packet"/>
                    <polygon points="635,174 649,180 635,186" fill="#f59e0b"/>

                    <!-- Real Bank Accepts OTP -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="730" y="90" text-anchor="middle" fill="#38bdf8" font-size="10.5" font-weight="800">SERVER RESMI BANK</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="730" y="135" text-anchor="middle" fill="#4ade80" font-size="9" font-weight="700">OTP Valid!</text>
                    <text x="730" y="155" text-anchor="middle" fill="#cbd5e1" font-size="8">Membuat Token Sesi:</text>
                    <rect x="675" y="170" width="110" height="35" rx="4" fill="#0c4a6e" stroke="#38bdf8"/>
                    <text x="730" y="186" text-anchor="middle" fill="#7dd3fc" font-size="8">Set-Cookie:</text>
                    <text x="730" y="198" text-anchor="middle" fill="#fde047" font-size="7.5" font-family="monospace">session_token=xyz</text>
                """,
                "checkpoint": {
                    "q": "Mengapa SMS OTP tidak mampu mencegah serangan Reverse Proxy AitM?",
                    "options": [
                        "Karena SMS OTP tidak memiliki pengikatan asal domain (origin-bound), sehingga kode angka yang sama dapat langsung di-relay oleh proxy penyerang ke bank secara instan.",
                        "Karena semua operator seluler bekerja sama dengan penyerang.",
                        "Karena SMS OTP hanya bisa digunakan sekali dalam 24 jam."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! OTP berupa kode statis numerik yang tidak mengikat domain asal, sehingga proxy penyerang dapat langsung meneruskannya ke server asli secara instan."
                }
            },
            {
                "title": "Pembajakan Session Cookie & Account Takeover (ATO < 60s)",
                "status": {"text": "Account Takeover", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Ketika server bank mengembalikan HTTP Response berisi Set-Cookie (session token), Evilginx mencuri token sesi tersebut sebelum meneruskannya ke korban. Penyerang mengimpor cookie tersebut ke browser miliknya: Akun korban berhasil diambil alih sepenuhnya (ATO) kurang dari 60 detik tanpa perlu mengetahui password lagi, lalu mengubah rekening settlement pencairan dana.",
                "terms": [
                    ["Aset yang Dicuri", "Session Token / Authentication Bearer Cookie"],
                    ["Kecepatan Serangan", "Account Takeover (ATO) selesai dalam &lt; 60 detik"],
                    ["Dampak Fatal", "Penggantian rekening pencairan dana (settlement) merchant"]
                ],
                "defenseInfo": "Verifikasi ganda (maker-checker) untuk perubahan rekening settlement serta deteksi anomali geolokasi IP (Impossible Travel Detection).",
                "svg": """
                    <!-- Attacker Hijacks Session -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYERANG: ACCOUNT TAKEOVER</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="132" fill="#4ade80" font-size="9" font-family="monospace">[+] SESSION HIJACKED!</text>
                    <text x="65" y="150" fill="#fde047" font-size="8.5" font-family="monospace">Cookie: session_auth=a98bf2...</text>
                    <text x="65" y="168" fill="#38bdf8" font-size="8.5" font-family="monospace">Hak Akses: ADMIN MERCHANT</text>
                    <rect x="65" y="185" width="170" height="40" rx="4" fill="#991b1b"/>
                    <text x="150" y="202" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Ubah Rekening Pencairan</text>
                    <text x="150" y="217" text-anchor="middle" fill="#fca5a5" font-size="7.5">&rarr; Bank Penampung Rekening Pelaku</text>
                    <text x="150" y="245" text-anchor="middle" fill="#ef4444" font-size="9" font-weight="800">ATO SELESAI (&lt; 60 DETIK)</text>

                    <!-- Cookie Transfer from Bank -->
                    <path d="M 640 180 L 270 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <polygon points="270,174 256,180 270,186" fill="#ef4444"/>
                    <text x="450" y="168" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">Pencurian Session Cookie &larr;</text>

                    <!-- Victim Screen (Confused/Diverted) -->
                    <rect x="360" y="70" width="180" height="230" rx="10" fill="#0f172a" stroke="#64748b"/>
                    <text x="450" y="100" text-anchor="middle" fill="#94a3b8" font-size="10" font-weight="700">KORBAN (DIALIHKAN)</text>
                    <rect x="375" y="120" width="150" height="150" rx="6" fill="#020617"/>
                    <text x="450" y="150" text-anchor="middle" fill="#fde047" font-size="8.5">"Sedang memproses..."</text>
                    <circle cx="450" cy="180" r="14" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="20 10"/>
                    <text x="450" y="220" text-anchor="middle" fill="#64748b" font-size="7.5">Korban mengira sistem loading</text>

                    <!-- Bank Server Processed -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="730" y="90" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">SERVER RESMI BANK</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="730" y="140" text-anchor="middle" fill="#ef4444" font-size="8.5">Sesi Diberikan</text>
                    <text x="730" y="165" text-anchor="middle" fill="#cbd5e1" font-size="8">Rekening Settlement</text>
                    <text x="730" y="180" text-anchor="middle" fill="#fde047" font-size="8">Berhasil Diubah</text>
                    <rect x="675" y="200" width="110" height="25" rx="4" fill="#450a0a"/>
                    <text x="730" y="216" text-anchor="middle" fill="#fca5a5" font-size="7.5" font-weight="700">Kerugian Finansial</text>
                """,
                "checkpoint": {
                    "q": "Apa dampak paling fatal jika penyerang mencuri Session Cookie hasil reverse proxy?",
                    "options": [
                        "Penyerang dapat langsung mengakses akun korban tanpa perlu login ulang atau meminta kode OTP lagi.",
                        "Komputer penyerang akan otomatis terformat.",
                        "Bank akan memblokir nomor telepon seluruh Indonesia."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Session cookie merepresentasikan sesi yang telah lolos autentikasi, sehingga penyerang dapat langsung membajak akun tanpa meminta OTP ulang."
                }
            },
            {
                "title": "Mitigasi Pertahanan: FIDO2 / WebAuthn Passkeys (Origin-Bound)",
                "status": {"text": "Mitigasi FIDO2", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Pertahanan mutlak terhadap Reverse Proxy Phishing adalah migrasi ke autentikasi FIDO2 / WebAuthn Passkeys. Kunci kriptografis FIDO2 bersifat 'origin-bound'—artinya peramban dan authenticator hanya akan menandatangani tantangan jika domain situs yang diakses identik dengan domain resmi (m-ewallet.id). Saat korban mengakses domain typosquatting m-ewallet-login.id, authenticator menolak verifikasi secara otomatis.",
                "terms": [
                    ["Pilar Teknologi", "FIDO2 / WebAuthn Passkeys (Origin-Bound Cryptography) & mTLS"],
                    ["Pilar Operasional", "Impossible Travel Detection oleh SOC & Proaktif DNS Takedown"],
                    ["Pilar Tata Kelola", "Maker-Checker (Dual-Control) persetujuan perubahan rekening settlement"]
                ],
                "defenseInfo": "Standar FIDO2 memberikan kekebalan kriptografis mutlak terhadap seluruh toolkit phishing berbasis reverse proxy (Evilginx).",
                "svg": """
                    <!-- Phishing Proxy Blocked -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="url(#hackerGrad)" stroke="#475569" stroke-width="1.5"/>
                    <text x="140" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">REVERSE PROXY GAGAL</text>
                    <rect x="55" y="110" width="170" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="135" fill="#ef4444" font-size="8.5" font-family="monospace">[!] FIDO2 Challenge Refused</text>
                    <text x="65" y="155" fill="#ef4444" font-size="8.5" font-family="monospace">[!] Origin Mismatch Error</text>
                    <text x="65" y="175" fill="#64748b" font-size="8.5" font-family="monospace">Zero Credentials Captured</text>
                    <rect x="65" y="210" width="150" height="30" rx="4" fill="#18181b"/>
                    <text x="140" y="229" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="800">Phishing Lumpuh Total</text>

                    <!-- Protected Authenticator with FIDO2 -->
                    <rect x="330" y="45" width="280" height="290" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="345" y="60" width="250" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="470" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10.5" font-weight="800">&#128272; FIDO2 / WEBAUTHN PASSKEYS</text>
                    <text x="470" y="92" text-anchor="middle" fill="#d1fae5" font-size="8">Origin-Bound Public Key Cryptography</text>

                    <rect x="345" y="115" width="250" height="205" rx="8" fill="#020617" stroke="#22c55e"/>
                    <circle cx="470" cy="155" r="24" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="470" y="162" text-anchor="middle" fill="#86efac" font-size="18">&#10004;</text>

                    <text x="470" y="198" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">VALIDASI ASAL DOMAIN (ORIGIN)</text>
                    <rect x="360" y="208" width="220" height="45" rx="6" fill="#1e293b"/>
                    <text x="370" y="224" fill="#94a3b8" font-size="8">Domain Terdaftar: <tspan fill="#86efac">m-ewallet.id</tspan></text>
                    <text x="370" y="240" fill="#94a3b8" font-size="8">Domain Diakses: <tspan fill="#f87171">m-ewallet-login.id (DITOLAK!)</tspan></text>

                    <rect x="370" y="265" width="200" height="24" rx="4" fill="#15803d"/>
                    <text x="470" y="281" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Kunci Rahasia Tidak Dikirim</text>

                    <!-- Real Bank Protected -->
                    <rect x="640" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="725" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">BANK PROTECTED</text>
                    <rect x="655" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="725" y="135" text-anchor="middle" fill="#86efac" font-size="8.5">SOC Monitoring:</text>
                    <text x="725" y="155" text-anchor="middle" fill="#38bdf8" font-size="8">Impossible Travel OK</text>
                    <text x="725" y="175" text-anchor="middle" fill="#38bdf8" font-size="8">Maker-Checker OK</text>
                    <rect x="665" y="210" width="120" height="30" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="725" y="229" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Akun 100% Aman</text>
                """,
                "checkpoint": {
                    "q": "Mengapa teknologi FIDO2 / WebAuthn Passkeys kebal terhadap phishing reverse proxy?",
                    "options": [
                        "Karena kunci kriptografis terikat pada domain asal (origin-bound), sehingga browser otomatis menolak mengirimkan tanda tangan jika domain situs tidak cocok dengan domain resmi yang terdaftar.",
                        "Karena FIDO2 mematikan seluruh koneksi WiFi saat pengguna mengakses web.",
                        "Karena FIDO2 mewajibkan pengguna menghafal password 100 karakter."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Mekanisme origin-binding FIDO2 memastikan kunci hanya dapat digunakan pada domain resmi yang terdaftar, membuat reverse proxy otomatis gagal."
                }
            }
        ]
    },

    3: {
        "tag": "VEKTOR 3A &bull; MAN-IN-THE-MIDDLE &amp; ROGUE WIFI",
        "title": "Vektor 3A: Man-in-the-Middle (MitM) &amp; Rogue WiFi (Jalur Jaringan)",
        "badge": "V3A &bull; Network MitM",
        "desc_overview": "Serangan intersepsi jaringan fisik di mana penyerang memasang Access Point palsu (Rogue WiFi) di area publik untuk melakukan ARP spoofing, SSL stripping, menyadap paket transaksi finansial yang tidak terenkripsi dengan benar, dan melakukan replay attack.",
        "steps": [
            {
                "title": "Pemasangan Rogue Access Point (Evil Twin WiFi)",
                "status": {"text": "Jaringan Palsu Aktif", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Penyerang memasang perangkat WiFi palsu (seperti WiFi Pineapple) di kafe atau bandara dengan nama SSID yang memikat (misal: 'Free_Public_HighSpeed_WiFi'). Penyerang mengatur antena transmisi sinyal berkekuatan tinggi agar perangkat di sekitarnya otomatis terhubung.",
                "terms": [
                    ["Hardware Serangan", "WiFi Pineapple / Portable Rogue Access Point"],
                    ["Teknik", "Evil Twin AP / SSID Spoofing"],
                    ["Lokasi Rawan", "Tempat publik: Kafe, Bandara, Co-working space"]
                ],
                "defenseInfo": "Edukasi untuk tidak melakukan transaksi finansial di WiFi publik terbuka tanpa proteksi VPN korporat.",
                "svg": """
                    <!-- Rogue AP -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">ROGUE AP (WIFI PINEAPPLE)</text>
                    <!-- Antenna icon -->
                    <path d="M 150 140 L 150 115" stroke="#ef4444" stroke-width="3"/>
                    <circle cx="150" cy="115" r="4" fill="#ef4444"/>
                    <path d="M 135 125 A 20 20 0 0 1 165 125" stroke="#f59e0b" stroke-width="2" fill="none"/>
                    <path d="M 125 115 A 32 32 0 0 1 175 115" stroke="#f59e0b" stroke-width="2" fill="none"/>

                    <rect x="55" y="150" width="190" height="140" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="172" fill="#38bdf8" font-size="8.5" font-family="monospace">SSID: Free_Public_WiFi</text>
                    <text x="65" y="190" fill="#f87171" font-size="8.5" font-family="monospace">Security: NONE (Open)</text>
                    <text x="65" y="208" fill="#4ade80" font-size="8.5" font-family="monospace">Interface: wlan0 AP Mode</text>
                    <text x="65" y="226" fill="#eab308" font-size="8.5" font-family="monospace">Captive Portal: Inactive</text>
                    <rect x="65" y="240" width="170" height="25" rx="4" fill="#991b1b"/>
                    <text x="150" y="256" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Memancarkan Sinyal Palsu</text>

                    <!-- WiFi Wave to Phone -->
                    <path d="M 270 180 L 380 180" stroke="#f59e0b" stroke-width="2.5" class="flow-packet"/>
                    <text x="325" y="170" text-anchor="middle" fill="#fcd34d" font-size="9" font-weight="700">Broadcast SSID &rarr;</text>

                    <!-- Victim Phone Scanning WiFi -->
                    <rect x="400" y="45" width="200" height="290" rx="20" fill="url(#phoneGrad)" stroke="#38bdf8" stroke-width="1.5"/>
                    <rect x="412" y="65" width="176" height="250" rx="10" fill="url(#screenGrad)"/>
                    <rect x="475" y="52" width="50" height="5" rx="2" fill="#334155"/>

                    <rect x="420" y="80" width="160" height="25" rx="4" fill="#1e293b"/>
                    <text x="430" y="96" fill="#fff" font-size="9" font-weight="700">&larr; Pilih Jaringan WiFi</text>

                    <rect x="420" y="115" width="160" height="40" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
                    <text x="430" y="132" fill="#a5b4fc" font-size="8.5" font-weight="700">&#128246; Free_Public_WiFi</text>
                    <text x="430" y="146" fill="#22c55e" font-size="8">Sinyal Paling Kuat &bull; Terhubung</text>

                    <rect x="420" y="165" width="160" height="35" rx="6" fill="#18181b"/>
                    <text x="430" y="182" fill="#94a3b8" font-size="8">&#128246; Cafe_Kopi_Secure (WPA3)</text>
                    <text x="430" y="194" fill="#64748b" font-size="7.5">Perlu Password</text>

                    <!-- Real Internet Gateway -->
                    <rect x="640" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="720" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">INTERNET / BANK API</text>
                    <rect x="655" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="720" y="180" text-anchor="middle" fill="#64748b" font-size="8.5">Menunggu Koneksi</text>
                """,
                "checkpoint": {
                    "q": "Mengapa penyerang sering menggunakan nama SSID seperti 'Free_Public_WiFi' di tempat umum?",
                    "options": [
                        "Untuk memancing korban agar secara sukarela menghubungkan gawainya tanpa sandi, sehingga seluruh lalu lintas jaringan korban melewati router penyerang.",
                        "Karena nama tersebut merupakan standar internasional untuk internet satelit.",
                        "Agar kuota internet korban dialihkan ke ponsel penyerang."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Rogue AP memanfaatkan godaan 'WiFi gratis tanpa sandi' agar pengguna terhubung dan seluruh paket datanya dapat disadap."
                }
            },
            {
                "title": "ARP Poisoning & Upaya SSL Stripping (Downgrade Attack)",
                "status": {"text": "Serangan MitM", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Setelah korban terhubung, penyerang melancarkan ARP Poisoning untuk memposisikan mesinnya sebagai default gateway. Ketika korban membuka aplikasi atau web perbankan, alat penyerang (seperti sslstrip) mencegat handshake TLS dan mencoba menurunkan protokol dari HTTPS aman ke HTTP biasa tanpa enkripsi.",
                "terms": [
                    ["Protokol Serangan", "ARP Spoofing & SSL Stripping (HTTPS to HTTP Downgrade)"],
                    ["Tools", "arpspoof / sslstrip / Bettercap"],
                    ["Tujuan", "Mencegah enkripsi TLS terbentuk agar payload dapat dibaca telanjang"]
                ],
                "defenseInfo": "Penerapan HSTS (HTTP Strict Transport Security) Preload dan Certificate Pinning di dalam aplikasi seluler.",
                "svg": """
                    <!-- Attacker MitM Tool -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">MITM CONSOLE (BETTERCAP)</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="132" fill="#f87171" font-size="8.5" font-family="monospace">&gt; arp.spoof on</text>
                    <text x="65" y="150" fill="#fde047" font-size="8.5" font-family="monospace">&gt; sslstrip.start</text>
                    <text x="65" y="168" fill="#38bdf8" font-size="8" font-family="monospace">[!] Rewriting HTTPS -&gt; HTTP</text>
                    <text x="65" y="186" fill="#4ade80" font-size="8" font-family="monospace">[+] Target IP: 192.168.1.105</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#991b1b"/>
                    <text x="150" y="228" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">SSL Handshake Dicegat</text>
                    <text x="150" y="240" text-anchor="middle" fill="#fca5a5" font-size="7.5">Mencoba Downgrade ke HTTP</text>

                    <!-- Downgrade Packet Flow -->
                    <path d="M 270 180 L 370 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <text x="320" y="170" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="700">Downgrade HTTP &rarr;</text>

                    <!-- Smartphone -->
                    <rect x="380" y="45" width="220" height="290" rx="20" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <rect x="392" y="65" width="196" height="250" rx="10" fill="url(#screenGrad)"/>
                    <rect x="465" y="52" width="50" height="5" rx="2" fill="#334155"/>

                    <rect x="402" y="80" width="176" height="50" rx="6" fill="#450a0a" stroke="#ef4444"/>
                    <text x="490" y="100" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">&#9888; Enkripsi TLS Dilemahkan</text>
                    <text x="490" y="118" text-anchor="middle" fill="#fecaca" font-size="7.5">Aplikasi rentan mengirim data teks polos</text>

                    <rect x="402" y="145" width="176" height="150" rx="6" fill="#020617"/>
                    <text x="490" y="170" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="700">Permintaan Transaksi:</text>
                    <rect x="412" y="185" width="156" height="50" rx="4" fill="#18181b"/>
                    <text x="420" y="202" fill="#fde047" font-size="8" font-family="monospace">POST /api/transfer</text>
                    <text x="420" y="216" fill="#94a3b8" font-size="7.5" font-family="monospace">Authorization: Bearer xyz</text>
                    <text x="420" y="228" fill="#94a3b8" font-size="7.5" font-family="monospace">Amount: 5000000</text>

                    <!-- Real Server -->
                    <rect x="630" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="715" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">BANK API ORIGIN</text>
                    <rect x="645" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="715" y="180" text-anchor="middle" fill="#64748b" font-size="8.5">Menunggu Paket</text>
                """,
                "checkpoint": {
                    "q": "Apa tujuan utama penyerang melakukan teknik SSL Stripping?",
                    "options": [
                        "Menurunkan paksa protokol komunikasi dari HTTPS (terenkripsi) menjadi HTTP (teks polos) agar seluruh data transaksi dapat dibaca penyerang di jaringan.",
                        "Menghapus sertifikat tanah milik korban.",
                        "Membuat baterai ponsel korban cepat habis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! SSL Stripping memotong enkripsi HTTPS menjadi HTTP teks polos sehingga data sensitif seperti token otentikasi dapat disadap."
                }
            },
            {
                "title": "Intersepsi Paket Transaksi Finansial (Sniffing)",
                "status": {"text": "Paket Disadap", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Karena aplikasi tidak memvalidasi sertifikat TLS dengan ketat (tidak menerapkan Certificate Pinning), transaksi finansial terkirim melalui jalur yang dikompromikan. Penyerang membuka Wireshark dan membaca seluruh isi paket: nomor rekening, nominal transfer, token otentikasi, dan signature request secara telanjang.",
                "terms": [
                    ["Kerentanan Klien", "Ketiadaan SSL/TLS Certificate Pinning"],
                    ["Data Terbongkar", "Auth Bearer Token, Account Number, Transaction Amount"],
                    ["Alat Analisis", "Wireshark Packet Dissector / TCPdump"]
                ],
                "defenseInfo": "Penerapan Certificate Pinning di mobile app agar aplikasi menolak koneksi jika sertifikat tidak identik dengan public key bank.",
                "svg": """
                    <!-- Wireshark Sniffer -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">WIRESHARK SNIFFER (C2)</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="130" fill="#4ade80" font-size="8.5" font-family="monospace">[+] HTTP POST CAPTURED:</text>
                    <text x="65" y="148" fill="#fde047" font-size="8" font-family="monospace">Host: api.ewallet.id</text>
                    <text x="65" y="166" fill="#f87171" font-size="8" font-family="monospace">Auth: Bearer eyJhbGciOi...</text>
                    <text x="65" y="184" fill="#38bdf8" font-size="8" font-family="monospace">from: 10023412</text>
                    <text x="65" y="200" fill="#38bdf8" font-size="8" font-family="monospace">to: 88401920 (Merchant)</text>
                    <text x="65" y="216" fill="#f87171" font-size="8.5" font-weight="800" font-family="monospace">amount: Rp 5.000.000</text>
                    <rect x="65" y="235" width="170" height="25" rx="4" fill="#991b1b"/>
                    <text x="150" y="251" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">Payload Transaksi Terbuka</text>

                    <!-- Packet Arrow -->
                    <path d="M 400 180 L 270 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <text x="335" y="170" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="700">Cleartext Payload &rarr;</text>

                    <!-- Smartphone -->
                    <rect x="410" y="45" width="200" height="290" rx="20" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <rect x="422" y="65" width="176" height="250" rx="10" fill="url(#screenGrad)"/>
                    <rect x="485" y="52" width="50" height="5" rx="2" fill="#334155"/>
                    <text x="510" y="110" text-anchor="middle" fill="#fca5a5" font-size="9.5" font-weight="700">Nasabah Melakukan</text>
                    <text x="510" y="125" text-anchor="middle" fill="#fca5a5" font-size="9.5" font-weight="700">Pembayaran QRIS / Transfer</text>
                    <rect x="435" y="145" width="150" height="60" rx="6" fill="#18181b" stroke="#ef4444"/>
                    <text x="510" y="170" text-anchor="middle" fill="#fde047" font-size="10" font-weight="800">Rp 5.000.000</text>
                    <text x="510" y="190" text-anchor="middle" fill="#cbd5e1" font-size="8">Status: Mengirim...</text>

                    <!-- Bank Server -->
                    <rect x="640" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="720" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">BANK API</text>
                    <rect x="655" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="720" y="180" text-anchor="middle" fill="#64748b" font-size="8.5">Menerima Paket</text>
                """,
                "checkpoint": {
                    "q": "Mengapa aplikasi mobile banking rentan terhadap sniffing jika tidak menerapkan Certificate Pinning?",
                    "options": [
                        "Karena sistem operasi dapat dipaksa memercayai sertifikat root palsu milik penyerang di jaringan publik sehingga trafik dapat didekripsi.",
                        "Karena kabel fiber optic di jalanan bocor.",
                        "Karena nomor handphone nasabah bisa dibaca orang lain."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Tanpa Certificate Pinning, penyerang dapat memasang sertifikat CA perantara untuk mendekripsi dan membaca seluruh muatan paket."
                }
            },
            {
                "title": "Replay Attack (Pengulangan Transaksi Ilegal)",
                "status": {"text": "Replay Attack", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Dengan memegang paket transaksi valid beserta token otentikasinya, penyerang melakukan Replay Attack: mengirimkan ulang payload transaksi yang sama berulang kali (misal: 10 kali) ke server bank. Jika API tidak memvalidasi nonce kriptografis dan timestamp, server mengira korban melakukan 10 kali transfer dan mendebit saldo korban berulang kali.",
                "terms": [
                    ["Tipe Serangan", "Replay Attack (Duplikasi Permintaan Transaksi)"],
                    ["Kelemahan API", "Tidak ada validasi Nonce sekali pakai & Timestamp kadaluwarsa"],
                    ["Dampak", "Saldo nasabah terpotong berulang kali untuk satu transaksi sah"]
                ],
                "defenseInfo": "Pemberian nonce sekali pakai (one-time cryptographic nonce) dan jendela waktu timestamp ketat pada setiap request API finansial.",
                "svg": """
                    <!-- Attacker Replaying -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">REPLAY SCRIPT (ATTACKER)</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="135" fill="#f87171" font-size="8.5" font-family="monospace">&gt; for i in {1..5}; do</text>
                    <text x="65" y="155" fill="#fde047" font-size="8.5" font-family="monospace">  curl -X POST /api/transfer</text>
                    <text x="65" y="175" fill="#f87171" font-size="8.5" font-family="monospace">  --data [STOLEN_PAYLOAD]</text>
                    <text x="65" y="195" fill="#f87171" font-size="8.5" font-family="monospace">done</text>
                    <rect x="65" y="215" width="170" height="30" rx="4" fill="#991b1b"/>
                    <text x="150" y="234" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">5x Replay Terkirim!</text>

                    <!-- Multiple Replay Arrows -->
                    <path d="M 270 160 L 630 160" stroke="#ef4444" stroke-width="2.5" class="flow-packet"/>
                    <path d="M 270 180 L 630 180" stroke="#ef4444" stroke-width="2.5" class="flow-packet"/>
                    <path d="M 270 200 L 630 200" stroke="#ef4444" stroke-width="2.5" class="flow-packet"/>
                    <text x="450" y="150" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">&#9888; Replay Stream (Duplikasi) &rarr;</text>

                    <!-- Real Bank Server Processing Multi Debit -->
                    <rect x="640" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                    <text x="725" y="90" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">BANK CORE LEDGER</text>
                    <rect x="655" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#ef4444"/>
                    <text x="665" y="132" fill="#ef4444" font-size="8" font-family="monospace">Tx #1: -5.000.000 (OK)</text>
                    <text x="665" y="148" fill="#ef4444" font-size="8" font-family="monospace">Tx #2: -5.000.000 (OK)</text>
                    <text x="665" y="164" fill="#ef4444" font-size="8" font-family="monospace">Tx #3: -5.000.000 (OK)</text>
                    <text x="665" y="180" fill="#ef4444" font-size="8" font-family="monospace">Tx #4: -5.000.000 (OK)</text>
                    <text x="665" y="196" fill="#ef4444" font-size="8" font-family="monospace">Tx #5: -5.000.000 (OK)</text>
                    <rect x="665" y="215" width="120" height="35" rx="4" fill="#450a0a"/>
                    <text x="725" y="230" text-anchor="middle" fill="#fca5a5" font-size="7.5">Total Terkuras:</text>
                    <text x="725" y="244" text-anchor="middle" fill="#fde047" font-size="9" font-weight="800">Rp 25.000.000</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana cara kerja serangan Replay Attack pada transaksi keuangan?",
                    "options": [
                        "Penyerang mencegat paket transaksi sah yang telah ditandatangani, lalu mengirimkannya kembali berkali-kali ke server agar saldo terpotong berulang.",
                        "Penyerang memutar lagu MP3 di microphone ponsel korban.",
                        "Penyerang menekan tombol reset pada modem WiFi."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Replay attack menyalin paket transaksi yang valid lalu mengirimkannya ulang tanpa modifikasi untuk mengelabui server yang tidak memeriksa nonce."
                }
            },
            {
                "title": "Mitigasi Pertahanan: Certificate Pinning & Anti-Replay Nonce",
                "status": {"text": "Pinning & Nonce Aktif", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Pertahanan jaringan diterapkan secara berlapis: (1) Certificate Pinning (SSL Pinning) pada aplikasi seluler dompet digital: aplikasi hanya memercayai public key hash resmi milik bank dan menolak mutlak sertifikat proxy Rogue AP (koneksi diputus seketika). (2) Enkripsi payload end-to-end dengan Timestamp ketat dan Nonce acak satu kali pakai: jika ada upaya replay paket, API Gateway otomatis menolak dengan error HTTP 409 Conflict.",
                "terms": [
                    ["Pilar Teknologi", "SSL/TLS Certificate Pinning & Cryptographic Nonce + Timestamp"],
                    ["Pilar Operasional", "Pemantauan sertifikat kedaluwarsa & audit berkala konfigurasi TLS"],
                    ["Pilar Tata Kelola", "Kepatuhan standar PCI-DSS v4.0.1 Req 4 (Proteksi Data in-Transit)"]
                ],
                "defenseInfo": "Certificate Pinning menghentikan serangan MitM di tahap awal sebelum paket data dapat disadap atau di-replay.",
                "svg": """
                    <!-- Rogue AP Blocked -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="url(#hackerGrad)" stroke="#475569" stroke-width="1.5"/>
                    <text x="140" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">ROGUE AP DITOLAK</text>
                    <rect x="55" y="110" width="170" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="135" fill="#ef4444" font-size="8.5" font-family="monospace">[!] SSL Handshake Failed</text>
                    <text x="65" y="155" fill="#ef4444" font-size="8.5" font-family="monospace">[!] Pin Mismatch Error</text>
                    <text x="65" y="175" fill="#ef4444" font-size="8.5" font-family="monospace">[!] Replay Nonce Reused</text>
                    <text x="65" y="195" fill="#64748b" font-size="8" font-family="monospace">Traffic Aborted</text>
                    <rect x="65" y="215" width="150" height="30" rx="4" fill="#18181b"/>
                    <text x="140" y="234" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="800">Gagal Dekripsi Paket</text>

                    <!-- Smartphone with Certificate Pinning Shield -->
                    <rect x="330" y="45" width="280" height="290" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="345" y="60" width="250" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="470" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10.5" font-weight="800">&#128737; CERTIFICATE PINNING ACTIVE</text>
                    <text x="470" y="92" text-anchor="middle" fill="#d1fae5" font-size="8">Public Key Pinning &amp; Nonce Verification</text>

                    <rect x="345" y="115" width="250" height="205" rx="8" fill="#020617" stroke="#22c55e"/>
                    <circle cx="470" cy="155" r="24" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="470" y="162" text-anchor="middle" fill="#86efac" font-size="18">&#10004;</text>

                    <text x="470" y="198" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PIN VERIFIKASI COCOK</text>
                    <text x="470" y="215" text-anchor="middle" fill="#cbd5e1" font-size="8">SHA-256 Pin: 256-bit bank cert match</text>
                    <text x="470" y="230" text-anchor="middle" fill="#cbd5e1" font-size="8">Sertifikat Rogue AP ditolak seketika!</text>

                    <rect x="365" y="250" width="210" height="26" rx="4" fill="#15803d"/>
                    <text x="470" y="267" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Transmisi Aman Terenkripsi TLS 1.3</text>

                    <!-- Bank Core Server Protected -->
                    <rect x="640" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="725" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">BANK GATEWAY OK</text>
                    <rect x="655" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="725" y="135" text-anchor="middle" fill="#86efac" font-size="8.5">Anti-Replay Nonce:</text>
                    <text x="725" y="155" text-anchor="middle" fill="#38bdf8" font-size="8">Nonce: Unik Sekali Pakai</text>
                    <text x="725" y="175" text-anchor="middle" fill="#38bdf8" font-size="8">Timestamp: &lt; 30s Valid</text>
                    <rect x="665" y="210" width="120" height="30" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="725" y="229" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Transaksi Sah Saja</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana Certificate Pinning melindungi aplikasi e-wallet dari serangan Man-in-the-Middle?",
                    "options": [
                        "Aplikasi mengunci sidik jari kriptografis sertifikat asli bank, sehingga aplikasi langsung memutuskan koneksi jika sertifikat di jaringan tidak cocok dengan sidik jari tersebut.",
                        "Aplikasi mengirim pesan WhatsApp ke kantor pusat polisi.",
                        "Aplikasi mengubah nama hotspot WiFi secara otomatis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Certificate Pinning memastikan aplikasi hanya mau berkomunikasi dengan server yang memiliki public key resmi bank, menolak proxy pihak ketiga."
                }
            }
        ]
    },

    4: {
        "tag": "VEKTOR 3B &bull; API EXPLOITATION (BOLA / IDOR)",
        "title": "Vektor 3B: API Exploitation — Broken Object Level Authorization (Infrastruktur API)",
        "badge": "V3B &bull; API BOLA",
        "desc_overview": "Celah otorisasi level objek (OWASP API Top 10 #1) di mana penyerang mereverse-engineering endpoint API dan memanipulasi parameter ID akun (from_account_id) untuk menguras saldo rekening nasabah lain tanpa izin kepemilikan.",
        "steps": [
            {
                "title": "Dekompilasi APK & Reverse Engineering Endpoint API",
                "status": {"text": "Reconnaissance API", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Penyerang mendekomplikasi berkas APK dompet digital menggunakan alat seperti jadx-gui atau Bytecode Viewer. Dari kode sumber Java/Kotlin yang tidak diobfuskasi sempurna, penyerang menemukan pola endpoint API RESTful sensitif seperti /api/v2/wallet/balance/{id} dan /api/v2/wallet/transfer.",
                "terms": [
                    ["Alat Dekompilasi", "jadx-gui / apktool / Frida"],
                    ["Aset Ditemukan", "URL REST API Endpoint, struktur request JSON, header autentikasi"],
                    ["Kerentanan Awal", "Kurangnya proteksi code obfuscation (ProGuard/R8) pada berkas APK"]
                ],
                "defenseInfo": "Penerapan obfuscation kode tingkat lanjut (DexGuard / ProGuard), code shrinking, dan penyembunyian string endpoint.",
                "svg": """
                    <!-- Attacker Decompilation -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fde047" font-size="11" font-weight="800">REVERSE ENGINEERING (JADX)</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="130" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; jadx ewallet_v2.apk</text>
                    <text x="65" y="148" fill="#4ade80" font-size="8.5" font-family="monospace">[+] Found ApiService.java:</text>
                    <text x="65" y="166" fill="#fde047" font-size="8" font-family="monospace">@POST("/api/v2/wallet/transfer")</text>
                    <text x="65" y="184" fill="#cbd5e1" font-size="8" font-family="monospace">Body: { from_id, to_id, amt }</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#78350f"/>
                    <text x="150" y="228" text-anchor="middle" fill="#fef08a" font-size="8.5" font-weight="800">Endpoint Sensitif Terbuka</text>
                    <text x="150" y="240" text-anchor="middle" fill="#cbd5e1" font-size="7.5">Parameter ID akun teridentifikasi</text>

                    <!-- Arrow to Burp -->
                    <path d="M 270 180 L 370 180" stroke="#f59e0b" stroke-width="2.5" class="flow-packet"/>
                    <text x="320" y="170" text-anchor="middle" fill="#fcd34d" font-size="9" font-weight="700">Audit Endpoint &rarr;</text>

                    <!-- Burp Suite Proxy Console -->
                    <rect x="380" y="55" width="230" height="260" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
                    <rect x="380" y="55" width="230" height="35" rx="10" fill="#1e293b"/>
                    <text x="495" y="77" text-anchor="middle" fill="#fde047" font-size="10" font-weight="800">BURP SUITE REPEATER</text>

                    <rect x="395" y="105" width="200" height="190" rx="6" fill="#020617" stroke="#334155"/>
                    <text x="405" y="125" fill="#f87171" font-size="8" font-family="monospace">POST /api/v2/wallet/transfer</text>
                    <text x="405" y="142" fill="#38bdf8" font-size="8" font-family="monospace">Host: api.ewallet.id</text>
                    <text x="405" y="159" fill="#94a3b8" font-size="8" font-family="monospace">Authorization: Bearer [UserA]</text>
                    <rect x="405" y="175" width="180" height="50" rx="4" fill="#18181b"/>
                    <text x="415" y="193" fill="#cbd5e1" font-size="8" font-family="monospace">"from_account_id": 1004,</text>
                    <text x="415" y="208" fill="#cbd5e1" font-size="8" font-family="monospace">"amount": 100000</text>
                    <text x="495" y="250" text-anchor="middle" fill="#4ade80" font-size="8">Request Akun Sendiri (Valid)</text>

                    <!-- Real Backend -->
                    <rect x="640" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="720" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">API GATEWAY</text>
                    <rect x="655" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="720" y="180" text-anchor="middle" fill="#64748b" font-size="8.5">Menunggu Request</text>
                """,
                "checkpoint": {
                    "q": "Mengapa dekompilasi APK berbahaya jika kode aplikasi tidak diobfuskasi?",
                    "options": [
                        "Karena penyerang dapat membaca struktur kode sumber, nama endpoint API backend, format parameter JSON, dan logika bisnis aplikasi secara transparan.",
                        "Karena dekompilasi APK membuat ponsel pengguna meledak.",
                        "Karena dekompilasi mengubah bahasa Indonesia menjadi bahasa mesin."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Kode yang tidak diobfuskasi membocorkan seluruh arsitektur API dan memudahkan penyerang memetakan target eksploitasi."
                }
            },
            {
                "title": "Manipulasi Parameter Objek ID (Object ID Tampering)",
                "status": {"text": "Eksploitasi BOLA", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Penyerang login secara sah sebagai User A (Account ID: 1004). Menggunakan Burp Suite Repeater, penyerang mengganti parameter from_account_id dari 1004 menjadi 2088 (ID milik merchant / nasabah korban). Token autentikasi tetap milik User A yang sah, namun ID sumber dana dialihkan ke rekening korban.",
                "terms": [
                    ["Tipe Celah", "Broken Object Level Authorization (BOLA / IDOR)"],
                    ["OWASP Ranking", "OWASP API Security Top 10 - Peringkat #1"],
                    ["Teknik Manipulasi", "ID Parameter Tampering (1004 &rarr; 2088)"]
                ],
                "defenseInfo": "Penerapan validasi kepemilikan objek pada lapisan business logic: memastikan user_id pada token sama dengan owner_id dari account_id.",
                "svg": """
                    <!-- Burp Suite Tampering in Action -->
                    <rect x="40" y="55" width="250" height="265" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="165" y="85" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">BURP SUITE: PARAMETER TAMPERING</text>
                    <rect x="55" y="100" width="220" height="205" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="122" fill="#38bdf8" font-size="8.5" font-family="monospace">POST /api/v2/wallet/transfer HTTP/1.1</text>
                    <text x="65" y="138" fill="#94a3b8" font-size="8" font-family="monospace">Authorization: Bearer [Token User A]</text>
                    <rect x="65" y="150" width="200" height="60" rx="4" fill="#450a0a" stroke="#ef4444"/>
                    <text x="75" y="168" fill="#fca5a5" font-size="8.5" font-family="monospace">"from_account_id": <tspan fill="#fde047" font-weight="800">2088</tspan>,</text>
                    <text x="75" y="184" fill="#fca5a5" font-size="8" font-family="monospace">(Dimanipulasi: ID Rekening Korban!)</text>
                    <text x="75" y="200" fill="#cbd5e1" font-size="8" font-family="monospace">"amount": 10000000</text>
                    <rect x="65" y="225" width="200" height="30" rx="4" fill="#991b1b"/>
                    <text x="165" y="244" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Kirim Request BOLA Jahat &rarr;</text>

                    <!-- Forward Attack Arrow -->
                    <path d="M 300 180 L 400 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <polygon points="400,174 414,180 400,186" fill="#ef4444"/>
                    <text x="350" y="170" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="700">Tampered ID &rarr;</text>

                    <!-- API Gateway (Flawed) -->
                    <rect x="420" y="55" width="200" height="265" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
                    <text x="520" y="85" text-anchor="middle" fill="#fde047" font-size="11" font-weight="800">API GATEWAY (FLAWED)</text>
                    <rect x="435" y="100" width="170" height="205" rx="6" fill="#020617" stroke="#334155"/>
                    <text x="445" y="125" fill="#4ade80" font-size="8.5" font-family="monospace">[+] Token Check: VALID</text>
                    <text x="445" y="142" fill="#94a3b8" font-size="8" font-family="monospace">(User A terotentikasi)</text>
                    <rect x="445" y="158" width="150" height="50" rx="4" fill="#450a0a" stroke="#ef4444"/>
                    <text x="520" y="178" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">&#9888; Celah Otorisasi Objek:</text>
                    <text x="520" y="195" text-anchor="middle" fill="#fecaca" font-size="7.5">Tidak memvalidasi kepemilikan 2088!</text>
                    <rect x="445" y="225" width="150" height="25" rx="4" fill="#f59e0b"/>
                    <text x="520" y="241" text-anchor="middle" fill="#042f2e" font-size="8" font-weight="800">Request Diteruskan ke Core &rarr;</text>

                    <!-- Core Database -->
                    <rect x="645" y="55" width="165" height="265" rx="12" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="1.5"/>
                    <text x="727" y="85" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">DATABASE AKUN</text>
                    <rect x="655" y="100" width="145" height="205" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="665" y="130" fill="#94a3b8" font-size="8">Menerima Perintah:</text>
                    <text x="665" y="150" fill="#fde047" font-size="8" font-family="monospace">UPDATE accounts</text>
                    <text x="665" y="168" fill="#fde047" font-size="8" font-family="monospace">SET balance = -10M</text>
                    <text x="665" y="186" fill="#f87171" font-size="8.5" font-weight="700" font-family="monospace">WHERE id = 2088</text>
                """,
                "checkpoint": {
                    "q": "Mengapa celah Broken Object Level Authorization (BOLA) bisa terjadi padahal token login JWT penyerang valid?",
                    "options": [
                        "Karena API Gateway hanya memeriksa apakah pengguna sudah login, tetapi kode backend lalai memeriksa apakah pengguna yang login berhak atas data objek (rekening) yang diminta.",
                        "Karena token JWT kadaluwarsa setelah 5 tahun.",
                        "Karena database SQL tidak mendukung angka genap."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! BOLA terjadi karena perbedaan antara otentikasi (siapa Anda) dan otorisasi objek (apakah Anda berhak mengakses objek nomor 2088 tersebut)."
                }
            },
            {
                "title": "Pengurasan Dana Lintas Akun Tanpa Otorisasi",
                "status": {"text": "Kebocoran Saldo", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Backend memproses transfer uang dari rekening korban 2088 ke rekening penyerang 1004. Penyerang mengotomatisasi skrip Python untuk melakukan iterasi ID rekening dari 2001 hingga 2099, menguras miliaran rupiah saldo nasabah lain secara massal tanpa memerlukan password atau PIN korban!",
                "terms": [
                    ["Otomasi Eksploitasi", "Python Multi-threaded Request Loop (ID 2001 - 2099)"],
                    ["Kerugian Nasabah", "Saldo rekening terkuras tanpa interaksi korban sama sekali"],
                    ["Dampak Hukum", "Sanksi regulator OJK/BI & tuntutan hukum ganti rugi massal"]
                ],
                "defenseInfo": "Pemberian policy fine-grained authorization di API Gateway menggunakan Open Policy Agent (OPA) atau Spring Security Method Security.",
                "svg": """
                    <!-- Attacker Script Draining All Accounts -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">BOLA AUTOMATION SCRIPT</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="132" fill="#4ade80" font-size="8.5" font-family="monospace">[+] BOLA EXPLOIT SUCCESS:</text>
                    <text x="65" y="150" fill="#fde047" font-size="8.5" font-family="monospace">Draining acc_id: 2088 (+10M)</text>
                    <text x="65" y="168" fill="#fde047" font-size="8.5" font-family="monospace">Draining acc_id: 2089 (+10M)</text>
                    <text x="65" y="186" fill="#fde047" font-size="8.5" font-family="monospace">Draining acc_id: 2090 (+10M)</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#991b1b"/>
                    <text x="150" y="228" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Total Curian: Rp 50 Miliar</text>
                    <text x="150" y="240" text-anchor="middle" fill="#fca5a5" font-size="7.5">Eksfiltrasi Dana Selesai</text>

                    <!-- Drain Packet Flow -->
                    <path d="M 640 180 L 270 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <text x="450" y="168" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">Saldo Korban Tersedot &larr;</text>

                    <!-- Core Ledger Bleeding -->
                    <rect x="630" y="60" width="180" height="250" rx="12" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                    <text x="720" y="90" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">CORE BANKING DATABASE</text>
                    <rect x="645" y="110" width="150" height="180" rx="6" fill="#090e1a" stroke="#ef4444"/>
                    <text x="655" y="135" fill="#ef4444" font-size="8.5" font-family="monospace">acc_2088: Rp 0 (-10M)</text>
                    <text x="655" y="155" fill="#ef4444" font-size="8.5" font-family="monospace">acc_2089: Rp 0 (-10M)</text>
                    <text x="655" y="175" fill="#ef4444" font-size="8.5" font-family="monospace">acc_2090: Rp 0 (-10M)</text>
                    <rect x="655" y="200" width="130" height="35" rx="4" fill="#450a0a"/>
                    <text x="720" y="218" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">Pencurian Lintas Akun</text>
                    <text x="720" y="230" text-anchor="middle" fill="#fde047" font-size="7.5">Tanpa Diketahui Nasabah</text>
                """,
                "checkpoint": {
                    "q": "Mengapa BOLA menjadi ancaman nomor 1 pada OWASP API Security Top 10?",
                    "options": [
                        "Karena sangat mudah dieksploitasi (cukup mengganti ID objek) dan dapat menghasilkan kebocoran data atau pencurian dana massal tanpa memicu alarm login mencurigakan.",
                        "Karena BOLA merusak router WiFi di kantor pusat bank.",
                        "Karena BOLA hanya terjadi pada aplikasi yang dibuat dengan HTML statis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! BOLA sangat berbahaya karena penyerang hanya perlu mengubah ID objek pada request valid untuk mengakses aset orang lain tanpa memicu proteksi login."
                }
            },
            {
                "title": "Mitigasi Pertahanan: Open Policy Agent (OPA) Fine-Grained Authorization",
                "status": {"text": "Otorisasi OPA Aktif", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Pertahanan terhadap BOLA diimplementasikan menggunakan Open Policy Agent (OPA) pada API Gateway: (1) OPA mengevaluasi kebijakan deklaratif (Rego policy) yang mencocokkan klaim identitas pada JWT token dengan parameter ID akun di dalam request body. (2) Jika token.user_id != account.owner_id, request ditolak seketika dengan HTTP 403 Forbidden dan insiden dielevasikan ke SIEM.",
                "terms": [
                    ["Pilar Teknologi", "Open Policy Agent (OPA) & Context-Aware JWT Claims Validation"],
                    ["Pilar Operasional", "Automated DAST API Fuzzing & Pen-testing pra-rilis"],
                    ["Pilar Tata Kelola", "Implementasi prinsip Least Privilege & Zero Trust Data Access"]
                ],
                "defenseInfo": "Pemberian izin akses berbasis atribut (ABAC) menjamin pengguna hanya bisa memanipulasi data objek miliknya sendiri.",
                "svg": """
                    <!-- Attacker Denied -->
                    <rect x="40" y="60" width="200" height="250" rx="12" fill="url(#hackerGrad)" stroke="#475569" stroke-width="1.5"/>
                    <text x="140" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">PENYERANG BOLA DITOLAK</text>
                    <rect x="55" y="110" width="170" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="135" fill="#ef4444" font-size="8.5" font-family="monospace">&gt; HTTP/1.1 403 Forbidden</text>
                    <text x="65" y="155" fill="#f87171" font-size="8" font-family="monospace">{"error": "BOLA_VIOLATION"}</text>
                    <text x="65" y="175" fill="#94a3b8" font-size="8" font-family="monospace">Account 2088 not owned!</text>
                    <rect x="65" y="210" width="150" height="30" rx="4" fill="#18181b"/>
                    <text x="140" y="229" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="800">Eksploitasi Digagalkan</text>

                    <!-- OPA API Gateway Shield -->
                    <rect x="310" y="45" width="310" height="290" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="325" y="60" width="280" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="465" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10.5" font-weight="800">&#128737; OPEN POLICY AGENT (OPA) ENFORCER</text>
                    <text x="465" y="92" text-anchor="middle" fill="#d1fae5" font-size="8">Fine-Grained Attribute-Based Access Control</text>

                    <rect x="325" y="115" width="280" height="205" rx="8" fill="#020617" stroke="#22c55e"/>
                    <circle cx="465" cy="155" r="24" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="465" y="162" text-anchor="middle" fill="#86efac" font-size="18">&#10004;</text>

                    <text x="465" y="198" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">VALIDASI KEPEMILIKAN OBJEK (REGO)</text>
                    <rect x="340" y="208" width="250" height="45" rx="6" fill="#1e293b"/>
                    <text x="350" y="224" fill="#94a3b8" font-size="8">Token Subject: <tspan fill="#38bdf8">User A (1004)</tspan></text>
                    <text x="350" y="240" fill="#94a3b8" font-size="8">Target Object: <tspan fill="#f87171">Account 2088 (TIDAK COCOK!)</tspan></text>

                    <rect x="350" y="265" width="230" height="24" rx="4" fill="#15803d"/>
                    <text x="465" y="281" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Akses Ditolak &bull; Alert Dikirim ke SOC</text>

                    <!-- Real Database Safe -->
                    <rect x="650" y="60" width="160" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="730" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">CORE LEDGER SAFE</text>
                    <rect x="665" y="110" width="130" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="730" y="140" text-anchor="middle" fill="#86efac" font-size="8.5">Saldo Utuh:</text>
                    <text x="730" y="160" text-anchor="middle" fill="#38bdf8" font-size="8">acc_2088: Aman</text>
                    <text x="730" y="180" text-anchor="middle" fill="#38bdf8" font-size="8">acc_2089: Aman</text>
                    <rect x="675" y="210" width="110" height="30" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="730" y="229" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Zero Data Theft</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana Open Policy Agent (OPA) mencegah eksploitasi BOLA pada API?",
                    "options": [
                        "Dengan mengevaluasi kebijakan otorisasi pada setiap request: memastikan bahwa subjek di dalam token JWT memiliki hak kepemilikan sah atas ID akun yang diminta.",
                        "Dengan melarang semua pengguna mentransfer uang sama sekali.",
                        "Dengan menghapus file JSON dari server."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! OPA memastikan setiap request dievaluasi berdasarkan aturan kepemilikan objek, sehingga request dengan ID akun orang lain langsung ditolak."
                }
            }
        ]
    },

    5: {
        "tag": "VEKTOR 3C &bull; LAYER 7 API FLOODING / DDOS",
        "title": "Vektor 3C: Layer 7 API Flooding / DDoS (Infrastruktur Backend)",
        "badge": "V3C &bull; Layer 7 DDoS",
        "desc_overview": "Serangan penolakan layanan terdistribusi (DDoS) lapisan aplikasi di mana ribuan botnet membanjiri endpoint API sensitif dengan puluhan ribu request per detik, menghabiskan kuota connection pool database dan menyebabkan kelumpuhan total (service outage) pada ekosistem dompet digital.",
        "steps": [
            {
                "title": "Target Profiling Endpoint Komputasi Berat",
                "status": {"text": "Target Profiling", "cls": "warn"},
                "category": "ATTACK",
                "desc": "Penyerang memetakan endpoint API yang membutuhkan beban komputasi server paling tinggi (misal: /api/v1/auth/verify-pin yang menggunakan fungsi hash lambat Argon2id, atau /api/v1/reports/pdf-statement yang memicu query database kompleks dan render berkas berat).",
                "terms": [
                    ["Tipe Serangan", "Application-Layer (Layer 7) DDoS Flooding"],
                    ["Target Selektif", "Endpoint API yang asimetris: murah dikirim klien, sangat mahal diproses server"],
                    ["Metode Pemetaan", "Response Latency Profiling"]
                ],
                "defenseInfo": "Pemberian caching pada endpoint statis dan pembatasan konkurensi pada endpoint yang memicu beban CPU/database berat.",
                "svg": """
                    <!-- Attacker Profiling -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#f59e0b" stroke-width="2"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fde047" font-size="11" font-weight="800">BOTNET CONTROLLER</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="132" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; probe_endpoints.py</text>
                    <text x="65" y="150" fill="#cbd5e1" font-size="8" font-family="monospace">GET /api/v1/balance -&gt; 12ms</text>
                    <text x="65" y="168" fill="#f87171" font-size="8" font-family="monospace">POST /verify-pin -&gt; 350ms (CPU!)</text>
                    <text x="65" y="186" fill="#f87171" font-size="8" font-family="monospace">POST /export-pdf -&gt; 850ms (DB!)</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#78350f"/>
                    <text x="150" y="228" text-anchor="middle" fill="#fde047" font-size="8.5" font-weight="800">Target Asimetris Terpilih</text>
                    <text x="150" y="240" text-anchor="middle" fill="#fef08a" font-size="7.5">Siap Flooding ke Endpoint Berat</text>

                    <!-- Arrow to Gateway -->
                    <path d="M 270 180 L 400 180" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
                    <text x="335" y="170" text-anchor="middle" fill="#fcd34d" font-size="9">Probe Profiling</text>

                    <!-- API Gateway Normal -->
                    <rect x="420" y="60" width="180" height="250" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="510" y="90" text-anchor="middle" fill="#38bdf8" font-size="10.5" font-weight="800">API GATEWAY</text>
                    <rect x="435" y="110" width="150" height="180" rx="6" fill="#020617" stroke="#1e293b"/>
                    <text x="510" y="140" text-anchor="middle" fill="#4ade80" font-size="9">Trafik Normal</text>
                    <text x="510" y="160" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Volume: 120 RPS</text>
                    <circle cx="510" cy="190" r="14" fill="#065f46"/>
                    <text x="510" y="195" text-anchor="middle" fill="#a7f3d0" font-size="8">OK</text>

                    <!-- Core Database -->
                    <rect x="630" y="60" width="170" height="250" rx="12" fill="url(#serverGrad)" stroke="#334155" stroke-width="1.5"/>
                    <text x="715" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">DATABASE BACKEND</text>
                    <rect x="645" y="110" width="140" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="715" y="140" text-anchor="middle" fill="#38bdf8" font-size="8.5">Pool Koneksi: 5%</text>
                    <text x="715" y="165" text-anchor="middle" fill="#4ade80" font-size="8.5">CPU Usage: 8%</text>
                """,
                "checkpoint": {
                    "q": "Mengapa penyerang DDoS Layer 7 memilih menyerang endpoint berat seperti /verify-pin daripada homepage?",
                    "options": [
                        "Karena endpoint tersebut memaksa server menjalankan komputasi hashing yang intensif atau query database besar, sehingga sedikit request dapat melumpuhkan server secara cepat.",
                        "Karena endpoint tersebut memiliki nama yang lebih panjang.",
                        "Karena homepage dilindungi oleh password rahasia."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Serangan asimetris memanfaatkan perbedaan beban: klien hanya butuh beberapa byte untuk mengirim request, namun server harus menguras CPU dan I/O database."
                }
            },
            {
                "title": "Serangan Flooding 50.000 Requests/Detik dari Botnet Global",
                "status": {"text": "Flooding L7 Aktif", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Penyerang mengerahkan botnet global (ribuan perangkat IoT terinfeksi) untuk menembakkan 50.000 HTTP POST request per detik secara serentak ke endpoint verify-pin. Setiap request menggunakan IP dan User-Agent yang berbeda-beda untuk mengecoh rate limiting tradisional.",
                "terms": [
                    ["Volume Serangan", "50.000 Request per Detik (RPS)"],
                    ["Sumber Serangan", "10.000+ IP Botnet IoT Global Terdistribusi"],
                    ["Karakteristik Trafik", "HTTP Valid yang tampak seperti transaksi asli (evasive)"]
                ],
                "defenseInfo": "Penerapan Anycast Cloud Web Application Firewall (WAF) di jaringan global edge untuk menyaring botnet sebelum mencapai origin.",
                "svg": """
                    <!-- Global Botnet -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="88" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">GLOBAL BOTNET SWARM</text>
                    <rect x="55" y="105" width="190" height="190" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="128" fill="#f87171" font-size="9" font-weight="800" font-family="monospace">50.000 RPS INCOMING!</text>
                    <text x="65" y="148" fill="#fde047" font-size="8" font-family="monospace">Bot #1 (182.21.x.x) -&gt; /verify-pin</text>
                    <text x="65" y="164" fill="#fde047" font-size="8" font-family="monospace">Bot #2 (45.120.x.x) -&gt; /verify-pin</text>
                    <text x="65" y="180" fill="#fde047" font-size="8" font-family="monospace">Bot #3 (103.8.x.x)  -&gt; /verify-pin</text>
                    <text x="65" y="196" fill="#f87171" font-size="8" font-family="monospace">... +9.997 Bot Nodes Active</text>
                    <rect x="65" y="215" width="170" height="35" rx="4" fill="#991b1b"/>
                    <text x="150" y="235" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Pembanjiran Trafik L7</text>

                    <!-- Massive Red Attack Streams -->
                    <path d="M 270 140 L 410 140" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <path d="M 270 165 L 410 165" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <path d="M 270 190 L 410 190" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <path d="M 270 215 L 410 215" stroke="#ef4444" stroke-width="3" class="flow-packet"/>
                    <text x="340" y="130" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">50K RPS Flood &rarr;</text>

                    <!-- Overloaded API Gateway -->
                    <rect x="420" y="60" width="180" height="250" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="510" y="90" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">API GATEWAY KWALAHAN</text>
                    <rect x="435" y="110" width="150" height="180" rx="6" fill="#090e1a" stroke="#ef4444"/>
                    <text x="510" y="135" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">&#9888; OVERLOAD!</text>
                    <text x="510" y="155" text-anchor="middle" fill="#fca5a5" font-size="8">Worker Threads: 100%</text>
                    <text x="510" y="175" text-anchor="middle" fill="#fca5a5" font-size="8">Antrian Request Penuh</text>
                    <circle cx="510" cy="205" r="14" fill="#991b1b"/>
                    <text x="510" y="210" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">!</text>

                    <!-- Forwarding to DB -->
                    <path d="M 605 180 L 635 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>

                    <!-- Database -->
                    <rect x="640" y="60" width="165" height="250" rx="12" fill="url(#serverGrad)" stroke="#f59e0b" stroke-width="1.5"/>
                    <text x="722" y="90" text-anchor="middle" fill="#fde047" font-size="10.5" font-weight="800">DATABASE BACKEND</text>
                    <rect x="655" y="110" width="135" height="180" rx="6" fill="#090e1a" stroke="#334155"/>
                    <text x="722" y="140" text-anchor="middle" fill="#fde047" font-size="8.5">Menerima Banjir Query</text>
                    <text x="722" y="165" text-anchor="middle" fill="#ef4444" font-size="8.5">Koneksi Melonjak</text>
                """,
                "checkpoint": {
                    "q": "Mengapa DDoS Layer 7 (Application Layer) lebih sulit ditangkal dibanding DDoS Layer 3/4 (Network)?",
                    "options": [
                        "Karena trafik Layer 7 berupa HTTP request valid yang meniru perilaku pengguna asli, sehingga firewall jaringan tradisional menganggapnya sebagai koneksi sah.",
                        "Karena Layer 7 berjalan tanpa kabel.",
                        "Karena Layer 7 tidak menggunakan alamat IP."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Serangan Layer 7 tampak seperti transaksi biasa dengan jabat tangan TCP dan TLS yang sempurna, sehingga sulit dibedakan dengan pengguna asli tanpa WAF canggih."
                }
            },
            {
                "title": "Penipisan Kuota Database Connection Pool (Pool Exhaustion)",
                "status": {"text": "Pool Exhaustion", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Setiap worker API yang menerima flood request mencoba membuka koneksi ke database perbankan. Dalam hitungan detik, kuota connection pool database (maksimal 1.000 koneksi) habis terpakai (100% capacity). CPU server mencapai 99%, I/O wait melesat, dan database berhenti merespons permintaan baru.",
                "terms": [
                    ["Kondisi Kegagalan", "Database Connection Pool Exhaustion (1.000 / 1.000 Connections)"],
                    ["Beban Komputasi", "CPU 99%, Thread Starvation, I/O Wait Bottleneck"],
                    ["Dampak Primer", "Seluruh query database mengantre dan mengalami timeout"]
                ],
                "defenseInfo": "Penerapan pola Circuit Breaker untuk menolak request berlebih secara terkendali dan autoscaling connection pool.",
                "svg": """
                    <!-- Overwhelmed Server Stage -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">FLOODING TERUS MENERUS</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="140" fill="#f87171" font-size="9" font-family="monospace">&gt; Stress Rate: 50.000 RPS</text>
                    <text x="65" y="165" fill="#fde047" font-size="9" font-family="monospace">&gt; Target Server Degrading</text>
                    <text x="65" y="190" fill="#ef4444" font-size="9" font-weight="800" font-family="monospace">&gt; HTTP 504 Timeout Surge</text>
                    <rect x="65" y="215" width="170" height="35" rx="4" fill="#991b1b"/>
                    <text x="150" y="235" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Menghabisi Sumber Daya</text>

                    <!-- Connection Pool Meter (Center) -->
                    <rect x="300" y="55" width="280" height="260" rx="14" fill="#450a0a" stroke="#ef4444" stroke-width="2.5" filter="url(#glowRed)"/>
                    <text x="440" y="85" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">&#9888; CONNECTION POOL EXHAUSTION</text>
                    <rect x="315" y="100" width="250" height="200" rx="8" fill="#020617" stroke="#ef4444"/>
                    
                    <!-- Progress Bar Pool 100% -->
                    <text x="330" y="125" fill="#fca5a5" font-size="9" font-weight="700">Kapasitas Pool Basis Data: 1.000 / 1.000 (100%)</text>
                    <rect x="330" y="135" width="220" height="18" rx="4" fill="#18181b"/>
                    <rect x="330" y="135" width="220" height="18" rx="4" fill="#ef4444"/>
                    <text x="440" y="148" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">HABIS (EXHAUSTED)</text>

                    <!-- CPU Meter 99% -->
                    <text x="330" y="175" fill="#fca5a5" font-size="9" font-weight="700">Beban CPU Server Origin: 99.8%</text>
                    <rect x="330" y="185" width="220" height="18" rx="4" fill="#18181b"/>
                    <rect x="330" y="185" width="218" height="18" rx="4" fill="#ef4444"/>
                    <text x="440" y="198" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">99.8% CRITICAL</text>

                    <rect x="330" y="215" width="220" height="45" rx="6" fill="#1c1917" stroke="#ef4444"/>
                    <text x="440" y="233" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">PostgreSQL / Oracle Connection Refused</text>
                    <text x="440" y="248" text-anchor="middle" fill="#fed7aa" font-size="7.5">FATAL: remaining connection slots are reserved</text>

                    <!-- Crashed DB Server -->
                    <rect x="620" y="60" width="180" height="250" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
                    <text x="710" y="90" text-anchor="middle" fill="#fca5a5" font-size="10.5" font-weight="800">CORE DATABASE</text>
                    <rect x="635" y="110" width="150" height="180" rx="6" fill="#090e1a" stroke="#ef4444"/>
                    <circle cx="710" cy="150" r="22" fill="#991b1b"/>
                    <text x="710" y="157" text-anchor="middle" fill="#fff" font-size="18">&#9760;</text>
                    <text x="710" y="195" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">Layanan Lumpuh</text>
                    <text x="710" y="215" text-anchor="middle" fill="#cbd5e1" font-size="8">Tidak Merespons Query</text>
                """,
                "checkpoint": {
                    "q": "Apa akibat langsung dari kondisi 'Database Connection Pool Exhaustion'?",
                    "options": [
                        "Database tidak lagi menerima koneksi baru, sehingga transaksi nasabah yang sah pun ikut gagal dan mengalami error timeout.",
                        "Database secara otomatis mengirimkan uang ke semua nasabah.",
                        "Database berganti nama menjadi MySQL."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Saat slot connection pool habis, seluruh permintaan baru—termasuk transaksi sah nasabah—akan ditolak atau dibiarkan menggantung hingga timeout."
                }
            },
            {
                "title": "Kegagalan Berantai (Cascading Failure) Layanan E-Wallet",
                "status": {"text": "Cascading Failure", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Kelumpuhan pada database memicu kegagalan berantai (cascading failure) ke seluruh ekosistem: Layanan QRIS, Transfer P2P, Pembayaran Merchant, dan Notifikasi Webhook tumbang satu per satu. Nasabah sah di kasir toko atau aplikasi e-commerce tidak dapat melakukan pembayaran (HTTP 503 Service Unavailable).",
                "terms": [
                    ["Pola Kerusakan", "Cascading Failure (Kegagalan Berantai Antar-Microservice)"],
                    ["Status Kode API", "HTTP 503 Service Unavailable / HTTP 504 Gateway Timeout"],
                    ["Dampak Bisnis", "Transaksi QRIS Kasir Gagal, Kerugian Reputasi Massal"]
                ],
                "defenseInfo": "Pola Circuit Breaker dan isolasi bulkhead antar-microservice agar kegagalan satu komponen tidak merembet ke seluruh sistem.",
                "svg": """
                    <!-- Collapsed Microservices Grid -->
                    <rect x="40" y="55" width="220" height="260" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
                    <text x="150" y="85" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">MICROSERVICES CRASH</text>
                    <rect x="55" y="100" width="190" height="200" rx="6" fill="#030712" stroke="#ef4444"/>
                    
                    <rect x="65" y="115" width="170" height="35" rx="4" fill="#7f1d1d"/>
                    <text x="150" y="132" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">&#10060; Service QRIS: DEAD (503)</text>
                    <text x="150" y="143" text-anchor="middle" fill="#cbd5e1" font-size="7">Koneksi DB Timeout</text>

                    <rect x="65" y="155" width="170" height="35" rx="4" fill="#7f1d1d"/>
                    <text x="150" y="172" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">&#10060; Service P2P Transfer: DEAD (504)</text>
                    <text x="150" y="183" text-anchor="middle" fill="#cbd5e1" font-size="7">Queue Overflow</text>

                    <rect x="65" y="195" width="170" height="35" rx="4" fill="#7f1d1d"/>
                    <text x="150" y="212" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">&#10060; Service Payment API: DEAD (500)</text>
                    <text x="150" y="223" text-anchor="middle" fill="#cbd5e1" font-size="7">Thread Pool Starvation</text>

                    <!-- Real Legitimate Customer Trying to Pay -->
                    <rect x="300" y="45" width="240" height="280" rx="20" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2"/>
                    <rect x="312" y="65" width="216" height="240" rx="10" fill="url(#screenGrad)"/>
                    <rect x="395" y="52" width="50" height="5" rx="2" fill="#334155"/>
                    <text x="420" y="95" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">Nasabah Sah di Kasir Toko</text>
                    
                    <!-- Failed Payment Dialog -->
                    <rect x="325" y="115" width="190" height="110" rx="8" fill="#450a0a" stroke="#ef4444"/>
                    <circle cx="420" cy="145" r="16" fill="#991b1b"/>
                    <text x="420" y="152" text-anchor="middle" fill="#fff" font-size="14">&#10006;</text>
                    <text x="420" y="180" text-anchor="middle" fill="#fca5a5" font-size="9.5" font-weight="800">TRANSAKSI GAGAL!</text>
                    <text x="420" y="198" text-anchor="middle" fill="#cbd5e1" font-size="7.5">Server tidak merespons (HTTP 504)</text>
                    <text x="420" y="212" text-anchor="middle" fill="#fca5a5" font-size="7.5">Silakan coba beberapa saat lagi</text>
                    <text x="420" y="255" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="700">&#128557; Nasabah Tidak Dapat Membayar</text>

                    <!-- Total Service Down Stage -->
                    <rect x="580" y="55" width="220" height="260" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="690" y="85" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">TOTAL SERVICE OUTAGE</text>
                    <rect x="595" y="100" width="190" height="200" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="690" y="130" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">SLA KOMPROMI</text>
                    <text x="690" y="150" text-anchor="middle" fill="#fde047" font-size="8">Ribuan Transaksi Drop</text>
                    <text x="690" y="170" text-anchor="middle" fill="#fde047" font-size="8">Potensi Denda Regulasi OJK</text>
                    <rect x="605" y="190" width="170" height="40" rx="4" fill="#991b1b"/>
                    <text x="690" y="208" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">SISTEM DOWN TOTAL</text>
                    <text x="690" y="222" text-anchor="middle" fill="#fca5a5" font-size="7.5">Pilar Ketersediaan (Availability) Bobol</text>
                """,
                "checkpoint": {
                    "q": "Apa yang dimaksud dengan fenomena 'Cascading Failure' pada arsitektur microservices?",
                    "options": [
                        "Kegagalan satu komponen kritis (seperti database) yang merembet melumpuhkan layanan-layanan lain yang bergantung padanya hingga seluruh sistem padam.",
                        "Kegagalan kabel jaringan yang terputus karena bencana banjir.",
                        "Penurunan versi aplikasi ke rilis sebelumnya secara otomatis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Cascading failure adalah kegagalan berantai ketika satu layanan yang crash menarik jatuh layanan lainnya karena ketergantungan sumber daya."
                }
            },
            {
                "title": "Mitigasi Pertahanan: Anycast WAF, Rate Limiting & Circuit Breaker",
                "status": {"text": "Mitigasi Berlapis", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Pertahanan komprehensif defense-in-depth diaktifkan: (1) Anycast Cloud WAF menyerap puluhan ribu RPS di 200+ edge location global dan memblokir signature botnet sebelum mencapai origin server. (2) Adaptive Rate Limiting membatasi frekuensi request per token/IP. (3) Circuit Breaker Pattern langsung menolak beban berlebih (fail-fast) sehingga connection pool database tetap aman. (4) Message Queue (Kafka) menampung webhook transaksi secara asinkron tanpa data hilang.",
                "terms": [
                    ["Pilar Teknologi", "Anycast Cloud WAF, Adaptive Rate Limiter, & Circuit Breaker Pattern"],
                    ["Pilar Operasional", "Autoscaling connection pool & monitoring RPS real-time dengan alert kuota"],
                    ["Pilar Tata Kelola", "Runbook tanggap darurat DDoS dengan target RTO terukur & simulasi load testing"]
                ],
                "defenseInfo": "Kombinasi Edge WAF dan Circuit Breaker memastikan integritas sistem core banking tetap berjalan normal saat terjadi lonjakan trafik ekstrem.",
                "svg": """
                    <!-- Botnet Blocked at Edge -->
                    <rect x="40" y="60" width="180" height="250" rx="12" fill="url(#hackerGrad)" stroke="#475569" stroke-width="1.5"/>
                    <text x="130" y="90" text-anchor="middle" fill="#94a3b8" font-size="10.5" font-weight="800">BOTNET 50K RPS</text>
                    <rect x="55" y="110" width="150" height="180" rx="6" fill="#030712" stroke="#334155"/>
                    <text x="65" y="135" fill="#ef4444" font-size="8" font-family="monospace">[!] Edge Dropped: 98%</text>
                    <text x="65" y="155" fill="#ef4444" font-size="8" font-family="monospace">[!] Rate Limited: 429</text>
                    <text x="65" y="175" fill="#64748b" font-size="8" font-family="monospace">Traffic Scrubbed</text>
                    <rect x="65" y="210" width="130" height="30" rx="4" fill="#18181b"/>
                    <text x="130" y="229" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="800">DDoS Dinetralisir</text>

                    <!-- Edge WAF + Circuit Breaker Shield (Center) -->
                    <rect x="250" y="45" width="340" height="290" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="265" y="60" width="310" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="420" y="78" text-anchor="middle" fill="#6ee7b7" font-size="10.5" font-weight="800">&#128737; ANYCAST CLOUD WAF &amp; CIRCUIT BREAKER</text>
                    <text x="420" y="92" text-anchor="middle" fill="#d1fae5" font-size="8">Edge Scrubbing &bull; Adaptive Rate Limiting &bull; Message Queue Buffer</text>

                    <rect x="265" y="115" width="310" height="205" rx="8" fill="#020617" stroke="#22c55e"/>
                    <circle cx="420" cy="150" r="22" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="420" y="157" text-anchor="middle" fill="#86efac" font-size="16">&#10004;</text>

                    <text x="420" y="190" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PERTAHANAN BERLAPIS BERFUNGSI</text>
                    
                    <rect x="280" y="202" width="280" height="50" rx="6" fill="#1e293b"/>
                    <text x="290" y="220" fill="#94a3b8" font-size="8">&bull; Anycast WAF: <tspan fill="#86efac">Menyaring 49.000 RPS di Edge Global</tspan></text>
                    <text x="290" y="235" fill="#94a3b8" font-size="8">&bull; Circuit Breaker: <tspan fill="#86efac">Fail-fast lindungi kuota DB connection</tspan></text>
                    <text x="290" y="248" fill="#94a3b8" font-size="8">&bull; Kafka Buffer: <tspan fill="#86efac">Webhook transaksi diproses asinkron</tspan></text>

                    <rect x="280" y="262" width="280" height="24" rx="4" fill="#15803d"/>
                    <text x="420" y="278" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Trafik Sah Nasabah Tetap Berjalan Normal</text>

                    <!-- Real Database Safe & Healthy -->
                    <rect x="620" y="60" width="180" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="710" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">CORE LEDGER STABIL</text>
                    <rect x="635" y="110" width="150" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="710" y="135" text-anchor="middle" fill="#86efac" font-size="8.5">Kapasitas Pool DB:</text>
                    <text x="710" y="155" text-anchor="middle" fill="#38bdf8" font-size="8.5">140 / 1.000 (Aman 14%)</text>
                    <text x="710" y="180" text-anchor="middle" fill="#86efac" font-size="8.5">CPU Usage: 22% Normal</text>
                    <rect x="645" y="210" width="130" height="30" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="710" y="229" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Zero Downtime</text>
                """,
                "checkpoint": {
                    "q": "Bagaimana pola Circuit Breaker melindungi database saat terjadi banjir request?",
                    "options": [
                        "Ketika beban mendekati batas kapasitas, Circuit Breaker memutus alur ('trip open') dan langsung menolak request berlebih dengan error 429 secara instan tanpa membiarkannya menyentuh database.",
                        "Circuit Breaker mematikan listrik di seluruh gedung kantor.",
                        "Circuit Breaker menghapus semua akun pengguna yang sedang online."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Pola Circuit Breaker mencegah kegagalan total dengan menolak request berlebih secara fail-fast, sehingga connection pool database tidak habis terkuras."
                }
            }
        ]
    },

    6: {
        "tag": "KETAHANAN DATA &bull; SKEMA BACKUP 3-2-1",
        "title": "Ketahanan Data: Skema Backup 3-2-1 &amp; Immutable WORM Storage",
        "badge": "Resiliensi &bull; Backup WORM",
        "desc_overview": "Arsitektur pencadangan emas perbankan (3 salinan, 2 media berbeda, 1 salinan off-site terisolasi WORM) untuk menjamin data transaksi finansial tidak dapat diubah, dienkripsi ransomware, maupun dihapus pelaku kejahatan.",
        "steps": [
            {
                "title": "Topologi Operasional Normal Skema Backup 3-2-1",
                "status": {"text": "Topologi Normal", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Arsitektur dompet digital menerapkan prinsip emas 3-2-1: (1) 3 Salinan data ledger transaksi, (2) disimpan pada 2 Media teknologi berbeda (SSD SAN on-premise lokal dan Cloud Object Storage terenkripsi), dan (3) minimal 1 Salinan disimpan off-site di Disaster Recovery Center (DRC) terisolasi dengan proteksi Immutable WORM (Write Once, Read Many).",
                "terms": [
                    ["Salinan 1 (Utama)", "SSD SAN On-Premise High-IOPS (Primary Ledger Active)"],
                    ["Salinan 2 (Lokal)", "Encrypted Cloud Object Storage (Warm Standby / RPO &lt; 5 min)"],
                    ["Salinan 3 (Offsite)", "DRC Storage dengan Immutable WORM Lock (Ransomware Proof)"]
                ],
                "defenseInfo": "Standar kepatuhan POJK No. 11/POJK.03/2022 dan ISO 27001 mengenai kelangsungan bisnis dan pencadangan data finansial.",
                "svg": """
                    <!-- 3-2-1 Topology Diagram -->
                    <!-- Node 1: Primary SAN -->
                    <rect x="40" y="70" width="220" height="230" rx="12" fill="url(#serverGrad)" stroke="#38bdf8" stroke-width="2"/>
                    <text x="150" y="98" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="800">1. PRIMARY DATABASE (PROD)</text>
                    <rect x="55" y="115" width="190" height="165" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <circle cx="80" cy="140" r="10" fill="#0284c7"/>
                    <text x="80" y="144" text-anchor="middle" fill="#fff" font-size="10">&#128452;</text>
                    <text x="100" y="144" fill="#cbd5e1" font-size="9" font-weight="700">SSD SAN On-Premise</text>
                    <text x="65" y="170" fill="#94a3b8" font-size="8">&bull; Status: Baca / Tulis Aktif</text>
                    <text x="65" y="188" fill="#94a3b8" font-size="8">&bull; Lokasi: Data Center Utama</text>
                    <text x="65" y="206" fill="#94a3b8" font-size="8">&bull; Replikasi Real-Time Aktif</text>
                    <rect x="65" y="230" width="170" height="28" rx="4" fill="#0c4a6e"/>
                    <text x="150" y="248" text-anchor="middle" fill="#7dd3fc" font-size="8.5" font-weight="700">Salinan #1: Data Asli Aktif</text>

                    <!-- Arrow 1 to 2 -->
                    <path d="M 270 180 L 320 180" stroke="#38bdf8" stroke-width="2" class="flow-packet"/>

                    <!-- Node 2: Secondary Cloud -->
                    <rect x="330" y="70" width="220" height="230" rx="12" fill="url(#serverGrad)" stroke="#38bdf8" stroke-width="2"/>
                    <text x="440" y="98" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="800">2. SECONDARY BACKUP</text>
                    <rect x="345" y="115" width="190" height="165" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <circle cx="370" cy="140" r="10" fill="#0284c7"/>
                    <text x="370" y="144" text-anchor="middle" fill="#fff" font-size="10">&#9729;</text>
                    <text x="390" y="144" fill="#cbd5e1" font-size="9" font-weight="700">Cloud Object Storage</text>
                    <text x="355" y="170" fill="#94a3b8" font-size="8">&bull; Media: Berbeda (Cloud Tier)</text>
                    <text x="355" y="188" fill="#94a3b8" font-size="8">&bull; Enkripsi: AES-256 (KMS)</text>
                    <text x="355" y="206" fill="#94a3b8" font-size="8">&bull; RPO: &lt; 5 Menit Sinkron</text>
                    <rect x="355" y="230" width="170" height="28" rx="4" fill="#0c4a6e"/>
                    <text x="440" y="248" text-anchor="middle" fill="#7dd3fc" font-size="8.5" font-weight="700">Salinan #2: Media Berbeda</text>

                    <!-- Arrow 2 to 3 -->
                    <path d="M 560 180 L 610 180" stroke="#22c55e" stroke-width="2" class="flow-packet"/>

                    <!-- Node 3: Immutable WORM DRC -->
                    <rect x="620" y="70" width="220" height="230" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <text x="730" y="98" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">3. IMMUTABLE WORM (OFFSITE)</text>
                    <rect x="635" y="115" width="190" height="165" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <circle cx="660" cy="140" r="10" fill="#15803d"/>
                    <text x="660" y="144" text-anchor="middle" fill="#fff" font-size="10">&#128274;</text>
                    <text x="680" y="144" fill="#86efac" font-size="9" font-weight="700">DRC WORM Isolated Tier</text>
                    <text x="645" y="170" fill="#94a3b8" font-size="8">&bull; Lokasi: Terpisah &gt; 50 KM</text>
                    <text x="645" y="188" fill="#94a3b8" font-size="8">&bull; Sifat: Write Once, Read Many</text>
                    <text x="645" y="206" fill="#86efac" font-size="8">&bull; Anti-Hapus &amp; Anti-Enkripsi</text>
                    <rect x="645" y="230" width="170" height="28" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="730" y="248" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">Salinan #3: WORM Terisolasi</text>
                """,
                "checkpoint": {
                    "q": "Apa arti aturan '3-2-1' dalam strategi pencadangan data finansial?",
                    "options": [
                        "3 salinan data, disimpan pada 2 media teknologi berbeda, dengan minimal 1 salinan disimpan off-site dan bersifat immutable WORM.",
                        "Pencadangan dilakukan 3 kali sehari, selama 2 jam, oleh 1 orang teknisi.",
                        "Menghitung mundur 3, 2, 1 sebelum mematikan server komputer."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Formula 3-2-1 memastikan jika data center utama musnah, salinan di media lain dan lokasi offsite WORM tetap utuh menyelamatkan data."
                }
            },
            {
                "title": "Serangan Destruktif Ransomware Melumpuhkan Primary DB",
                "status": {"text": "Ransomware Menyerang", "cls": "bad"},
                "category": "ATTACK",
                "desc": "Ransomware tingkat lanjut (seperti LockBit / BlackCat) berhasil menginfeksi jaringan internal melalui kredensial administrator yang bocor. Ransomware mulai mengenkripsi storage SAN utama (Primary Database), menambahkan ekstensi .locked pada berkas database, dan menuntut uang tebusan $5.000.000.",
                "terms": [
                    ["Tipe Serangan", "Enterprise Ransomware Infiltration"],
                    ["Dampak Primer", "Penyanderaan & Enkripsi Total Primary Storage SAN"],
                    ["Tuntutan Tebusan", "Uang tebusan cryptocurrency untuk kunci dekripsi"]
                ],
                "defenseInfo": "Segmentasi jaringan ketat dan penerapan hak akses least-privilege untuk mencegah pergerakan lateral ransomware.",
                "svg": """
                    <!-- Ransomware Attacker -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowRed)"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">RANSOMWARE OPERATOR</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="132" fill="#ef4444" font-size="9" font-family="monospace">&gt; ./encrypt_san.sh</text>
                    <text x="65" y="150" fill="#fde047" font-size="8.5" font-family="monospace">[*] Target: /mnt/san/ledger.db</text>
                    <text x="65" y="168" fill="#f87171" font-size="8.5" font-family="monospace">[+] AES-256 Locking Active</text>
                    <text x="65" y="186" fill="#f87171" font-size="8.5" font-family="monospace">[+] Files: ledger.db.locked</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#991b1b"/>
                    <text x="150" y="228" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Tebusan: $5.000.000</text>
                    <text x="150" y="240" text-anchor="middle" fill="#fca5a5" font-size="7.5">Primary Storage Terkunci</text>

                    <!-- Attack Arrow to Node 1 -->
                    <path d="M 270 180 L 350 180" stroke="#ef4444" stroke-width="3" class="flow-packet"/>

                    <!-- Node 1: Primary SAN ENCRYPTED -->
                    <rect x="360" y="60" width="230" height="250" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2.5" filter="url(#glowRed)"/>
                    <text x="475" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">&#9760; PRIMARY DB: TERENKRIPSI!</text>
                    <rect x="375" y="110" width="200" height="180" rx="6" fill="#020617" stroke="#ef4444"/>
                    <circle cx="475" cy="145" r="20" fill="#991b1b"/>
                    <text x="475" y="152" text-anchor="middle" fill="#fff" font-size="16">&#128274;</text>
                    <text x="475" y="182" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">ledger.db.locked</text>
                    <text x="475" y="200" text-anchor="middle" fill="#fca5a5" font-size="8">Data Center Utama Lumpuh Total</text>
                    <rect x="390" y="220" width="170" height="30" rx="4" fill="#7f1d1d"/>
                    <text x="475" y="238" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">Primary SAN Tidak Bisa Dibaca</text>

                    <!-- Node 3: Immutable WORM Standing Strong -->
                    <rect x="630" y="60" width="190" height="250" rx="12" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="725" y="90" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">IMMUTABLE WORM DRC</text>
                    <rect x="645" y="110" width="160" height="180" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="725" y="140" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700">Terisolasi Off-site</text>
                    <text x="725" y="165" text-anchor="middle" fill="#cbd5e1" font-size="8">Ransomware belum bisa masuk</text>
                    <rect x="655" y="195" width="140" height="35" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="725" y="212" text-anchor="middle" fill="#86efac" font-size="8" font-weight="800">Salinan Bersih Tersimpan</text>
                    <text x="725" y="224" text-anchor="middle" fill="#d1fae5" font-size="7">Snapshot Konsisten</text>
                """,
                "checkpoint": {
                    "q": "Mengapa organisasi tidak boleh membayar uang tebusan kepada penyerang ransomware?",
                    "options": [
                        "Karena tidak ada jaminan penyerang memberikan kunci dekripsi yang valid, mendanai kejahatan siber lebih lanjut, dan melanggar etika perbankan.",
                        "Karena penyerang hanya menerima uang koin kuno.",
                        "Karena sistem Windows akan menolak kunci dari hacker."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Membayar uang tebusan tidak menjamin data pulih dan menyuburkan industri kejahatan siber. Satu-satunya solusi andal adalah pemulihan dari backup immutable."
                }
            },
            {
                "title": "Penyerang Mencoba Menghapus Backup WORM (Gagal Mutlak!)",
                "status": {"text": "WORM Menolak Hapus", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Menyadari bahwa bank memiliki cadangan data di DRC, penyerang menggunakan kredensial domain admin yang dicuri untuk menjalankan perintah penghapusan massal: rm -rf /backups atau API DELETE Object. Namun, teknologi Immutable WORM (Write Once, Read Many) dengan Object Lock menolak mutlak perintah tersebut di level kernel hardware!",
                "terms": [
                    ["Fitur Keamanan", "Immutable WORM / S3 Object Lock (Compliance Mode)"],
                    ["Penolakan Akses", "Bahkan user root / administrator domain DILARANG menghapus berkas"],
                    ["Masa Retensi", "Data terkunci secara fisik hingga periode retensi resmi (misal: 7 tahun) berakhir"]
                ],
                "defenseInfo": "Kepatuhan terhadap regulasi Bank Indonesia yang mewajibkan audit trail finansial disimpan dalam media WORM tahan manipulasi.",
                "svg": """
                    <!-- Attacker Denied Delete -->
                    <rect x="40" y="60" width="220" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2"/>
                    <text x="150" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYERANG COBA HAPUS WORM</text>
                    <rect x="55" y="110" width="190" height="180" rx="6" fill="#030712" stroke="#ef4444"/>
                    <text x="65" y="132" fill="#ef4444" font-size="8.5" font-family="monospace">&gt; aws s3 rm s3://drc-worm/*</text>
                    <text x="65" y="152" fill="#f87171" font-size="8.5" font-family="monospace">[ERROR] 403 AccessDenied:</text>
                    <text x="65" y="170" fill="#fde047" font-size="7.8" font-family="monospace">ObjectLockConfiguration: LOCKED</text>
                    <text x="65" y="188" fill="#f87171" font-size="8" font-family="monospace">RetainUntilDate: 2033-09-08</text>
                    <rect x="65" y="210" width="170" height="35" rx="4" fill="#18181b" stroke="#ef4444"/>
                    <text x="150" y="228" text-anchor="middle" fill="#ef4444" font-size="8.5" font-weight="800">PERINTAH HAPUS GAGAL</text>
                    <text x="150" y="240" text-anchor="middle" fill="#94a3b8" font-size="7.5">Root / Admin Tidak Berdaya</text>

                    <!-- Blocked Arrow -->
                    <path d="M 270 180 L 370 180" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 2"/>
                    <circle cx="380" cy="180" r="10" fill="#991b1b"/>
                    <text x="380" y="184" text-anchor="middle" fill="#fff" font-size="10">&#10006;</text>

                    <!-- WORM Storage Shield Center -->
                    <rect x="410" y="45" width="400" height="285" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2.5" filter="url(#glowGreen)"/>
                    <rect x="425" y="60" width="370" height="40" rx="8" fill="#064e3b" stroke="#10b981"/>
                    <text x="610" y="78" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="800">&#128737; IMMUTABLE WORM PROTECTION LOCK</text>
                    <text x="610" y="92" text-anchor="middle" fill="#d1fae5" font-size="8">Write Once, Read Many &bull; Compliance Retention Mode Enforced</text>

                    <rect x="425" y="115" width="370" height="200" rx="8" fill="#020617" stroke="#22c55e"/>
                    <circle cx="610" cy="155" r="26" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
                    <text x="610" y="163" text-anchor="middle" fill="#86efac" font-size="20">&#10004;</text>

                    <text x="610" y="200" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">DATA AMAN &amp; TIDAK BISA DIUBAH ATAU DIHAPUS</text>
                    <text x="610" y="220" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Kebijakan WORM ditegakkan di level hardware kontroler penyimpanan.</text>
                    <text x="610" y="235" text-anchor="middle" fill="#cbd5e1" font-size="8.5">Sekalipun ransomware memiliki hak akses root, salinan WORM kebal manipulasi.</text>

                    <rect x="450" y="255" width="320" height="28" rx="4" fill="#15803d"/>
                    <text x="610" y="273" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">Integritas 100% Terjaga &bull; Siap Failover Cepat</text>
                """,
                "checkpoint": {
                    "q": "Mengapa teknologi WORM (Write Once, Read Many) kebal terhadap upaya penghapusan oleh ransomware?",
                    "options": [
                        "Karena kebijakan immutability ditegakkan secara hardware/firmware, sehingga data yang sudah tertulis dilarang diubah atau dihapus oleh siapapun (termasuk user root) sampai masa retensi berakhir.",
                        "Karena data WORM disimpan di dalam disket floppy disk.",
                        "Karena penyerang tidak mengetahui password wifi kantor."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! WORM (Compliance Mode) mengunci data secara hardware sehingga hak akses administrator tertinggi sekalipun tidak memiliki izin menghapus atau mengenkripsi data tersebut."
                }
            },
            {
                "title": "Failover Bencana & Pemulihan Integritas Finansial (DRC Active)",
                "status": {"text": "Pemulihan Berhasil", "cls": "ok"},
                "category": "DEFENSE",
                "desc": "Tim Incident Response mengaktifkan Disaster Recovery Plan: (1) Mengalihkan lalu lintas transaksi ke DRC (Disaster Recovery Center), (2) Me-restore ledger transaksi bersih dari snapshot WORM immutable, dan (3) Sistem kembali online dalam waktu kurang dari target Recovery Time Objective (RTO < 60 min, RPO < 5 min) dengan ZERO DATA LOSS.",
                "terms": [
                    ["Target Pemulihan", "Recovery Time Objective (RTO &lt; 60 menit)"],
                    ["Kehilangan Data", "Recovery Point Objective (RPO &lt; 5 menit / Zero Data Loss)"],
                    ["Status Akhir", "Sistem Pembayaran Pulih Sepenuhnya &amp; Saldo Nasabah Utuh"]
                ],
                "defenseInfo": "Pelaksanaan tabletop exercise dan simulasi uji pemulihan bencana berkala setiap 6 bulan sesuai mandat Bank Indonesia.",
                "svg": """
                    <!-- DRC Restoring -->
                    <rect x="40" y="55" width="240" height="270" rx="14" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
                    <text x="160" y="85" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">DISASTER RECOVERY CENTER (DRC)</text>
                    <rect x="55" y="100" width="210" height="210" rx="6" fill="#020617" stroke="#22c55e"/>
                    <text x="65" y="125" fill="#4ade80" font-size="8.5" font-family="monospace">&gt; Orchestrating Failover...</text>
                    <text x="65" y="145" fill="#38bdf8" font-size="8.5" font-family="monospace">[+] WORM Snapshot Validated</text>
                    <text x="65" y="165" fill="#38bdf8" font-size="8.5" font-family="monospace">[+] Ledger Rebuilt: 100% OK</text>
                    <text x="65" y="185" fill="#22c55e" font-size="9" font-weight="700" font-family="monospace">RTO: 34 Menit (&lt; 60 Min)</text>
                    <text x="65" y="205" fill="#22c55e" font-size="9" font-weight="700" font-family="monospace">RPO: 2 Menit (&lt; 5 Min)</text>
                    <rect x="65" y="225" width="190" height="35" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="160" y="243" text-anchor="middle" fill="#86efac" font-size="9" font-weight="800">DRC AKTIF MENJADI PRIMARY</text>
                    <text x="160" y="255" text-anchor="middle" fill="#d1fae5" font-size="7.5">Zero Data Loss Tercapai</text>

                    <!-- Failover Traffic Arrow -->
                    <path d="M 300 180 L 390 180" stroke="#22c55e" stroke-width="3" class="flow-packet"/>
                    <text x="345" y="170" text-anchor="middle" fill="#86efac" font-size="9" font-weight="700">Trafik Dialihkan &rarr;</text>

                    <!-- E-Wallet App Normal Again -->
                    <rect x="410" y="45" width="200" height="290" rx="20" fill="url(#phoneGrad)" stroke="#22c55e" stroke-width="2" filter="url(#glowGreen)"/>
                    <rect x="422" y="65" width="176" height="250" rx="10" fill="url(#screenGrad)"/>
                    <rect x="485" y="52" width="50" height="5" rx="2" fill="#334155"/>
                    <text x="510" y="90" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">DOMPET DIGITAL AKTIF</text>
                    
                    <rect x="432" y="110" width="156" height="85" rx="6" fill="#064e3b" stroke="#10b981"/>
                    <text x="510" y="130" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Saldo Rekening Nasabah:</text>
                    <text x="510" y="152" text-anchor="middle" fill="#fde047" font-size="13" font-weight="800">Rp 25.480.000</text>
                    <text x="510" y="170" text-anchor="middle" fill="#86efac" font-size="8">&#10004; Integritas Data Pulih 100%</text>

                    <rect x="432" y="210" width="156" height="30" rx="4" fill="#0284c7"/>
                    <text x="510" y="228" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="700">Siap Bertransaksi QRIS</text>
                    <text x="510" y="260" text-anchor="middle" fill="#86efac" font-size="8" font-weight="700">Layanan Berjalan Normal</text>

                    <!-- Bank Ledger Fully Restored -->
                    <rect x="630" y="55" width="190" height="270" rx="14" fill="url(#serverGrad)" stroke="#22c55e" stroke-width="2"/>
                    <text x="725" y="85" text-anchor="middle" fill="#86efac" font-size="10.5" font-weight="800">CORE LEDGER RESTORED</text>
                    <rect x="645" y="100" width="160" height="210" rx="6" fill="#090e1a" stroke="#1e293b"/>
                    <text x="725" y="130" text-anchor="middle" fill="#86efac" font-size="8.5">Integritas Finansial:</text>
                    <text x="725" y="150" text-anchor="middle" fill="#38bdf8" font-size="8">Audit Trail Konsisten</text>
                    <text x="725" y="170" text-anchor="middle" fill="#38bdf8" font-size="8">Tidak Ada Data Hilang</text>
                    <text x="725" y="190" text-anchor="middle" fill="#38bdf8" font-size="8">Kepatuhan OJK/BI Terjaga</text>
                    <rect x="655" y="210" width="140" height="35" rx="4" fill="#065f46" stroke="#22c55e"/>
                    <text x="725" y="228" text-anchor="middle" fill="#86efac" font-size="8.5" font-weight="800">RESILIENSI TINGGI</text>
                    <text x="725" y="240" text-anchor="middle" fill="#d1fae5" font-size="7.5">Ketahanan Teruji</text>
                """,
                "checkpoint": {
                    "q": "Mengapa target RTO (Recovery Time Objective) dan RPO (Recovery Point Objective) penting dalam sistem perbankan?",
                    "options": [
                        "RTO menentukan seberapa cepat sistem harus pulih dari bencana, sedangkan RPO menentukan toleransi maksimal data transaksi yang boleh hilang.",
                        "RTO dan RPO adalah merek server komputer.",
                        "RTO digunakan untuk menghitung gaji karyawan bank."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! RTO mengukur waktu pemulihan (target < 60 menit) dan RPO mengukur toleransi kehilangan data (target < 5 menit / zero loss)."
                }
            }
        ]
    }
}
