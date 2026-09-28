# -*- coding: utf-8 -*-
"""
Generator for detailed scenario data with SVG scenes and educational content
for all 4 vectors from Modul02_Kelompok05_Updated.pdf
"""

def get_scenarios():
    scenarios = {}

    # =========================================================================
    # VEKTOR 1: MOBILE BANKING TROJAN
    # =========================================================================
    scenarios["1"] = {
        "title": "Vektor 1: Mobile Banking Trojan",
        "subtitle": "Distribusi APK Palsu, Injeksi Overlay & Penyadapan Kredensial",
        "accentColor": "#ef4444",
        "accentBg": "rgba(239, 68, 68, 0.12)",
        "steps": [
            {
                "title": "Distribusi APK Palsu (Social Delivery)",
                "statusText": "Penyebaran Trojan",
                "statusCls": "warn",
                "desc": "Penyerang menyebarkan malware perbankan melalui pesan WhatsApp atau grup Telegram dengan menyamar sebagai dokumen penting (contoh: 'Undangan_Pernikahan.apk' atau 'Resi_Paket_J&T.apk'). Korban terpancing untuk mengunduh dan memasang aplikasi dari sumber tidak dikenal (sideloading).",
                "defenseDesc": "Mitigasi Pilar Tindakan & Teknologi: Sistem operasi secara default memblokir sideloading aplikasi dari luar Google Play Store. Fitur Google Play Protect memindai hash APK dan memblokir instalasi secara proaktif.",
                "analogy": "Seperti seseorang berpakaian kurir mengetuk pintu dan memberikan paket mencurigakan tanpa alamat pengirim yang jelas, meminta pemilik rumah membukanya.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Terganggu", "cls": "warn"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Vektor Masuk", "Rekayasa Sosial via WhatsApp / Telegram Blast"],
                    ["Metode Instalasi", "Sideloading APK di luar Google Play Store"],
                    ["Keluarga Malware", "Android Banking Trojan (Anatsa / Godfather / Hook)"]
                ],
                "quiz": {
                    "q": "Mengapa pelaku kejahatan siber menyebarkan malware perbankan melalui format APK di WhatsApp?",
                    "options": [
                        "Untuk menghindari proses kurasi ketat dan verifikasi keamanan otomatis di Google Play Store.",
                        "Karena aplikasi WhatsApp secara otomatis memberikan hak root pada file APK.",
                        "Karena ukuran file APK di WhatsApp otomatis terenkripsi oleh server."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Google Play Store memiliki pemeriksaan kode otomatis (Play Protect). Pengiriman APK lewat chat memanipulasi korban agar memasang secara manual."
                },
                "svg": '''
                  <!-- Attacker Node -->
                  <rect x="50" y="70" width="190" height="250" rx="12" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="1.8" filter="url(#glowV1)"/>
                  <text x="145" y="98" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYERANG (C2 BOT)</text>
                  <rect x="65" y="115" width="160" height="75" rx="6" fill="#030712" stroke="#334155"/>
                  <text x="75" y="135" fill="#38bdf8" font-size="9" font-family="monospace">&gt; blast_wa.py --auto</text>
                  <text x="75" y="152" fill="#f87171" font-size="9" font-family="monospace">[+] payload: Resi_Paket.apk</text>
                  <text x="75" y="169" fill="#4ade80" font-size="8" font-family="monospace">[+] blast: 10,000 target</text>
                  <rect x="65" y="200" width="160" height="50" rx="6" fill="#1e1b4b"/>
                  <text x="145" y="222" text-anchor="middle" fill="#c7d2fe" font-size="9" font-weight="700">Trik Rekayasa Sosial</text>
                  <text x="145" y="238" text-anchor="middle" fill="#94a3b8" font-size="8">Urgensi kurir / undangan digital</text>

                  <!-- Packet Delivery Arrow -->
                  <path d="M 245 190 L 390 190" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="390,185 402,190 390,195" fill="#f59e0b"/>
                  <text x="320" y="178" text-anchor="middle" fill="#fcd34d" font-size="9" font-weight="700">Kirim APK via WA</text>

                  <!-- Victim Phone -->
                  <rect x="420" y="40" width="220" height="320" rx="22" fill="url(#phoneGrad)" stroke="#38bdf8" stroke-width="2"/>
                  <rect x="432" y="60" width="196" height="280" rx="12" fill="url(#screenGrad)"/>
                  <rect x="495" y="46" width="70" height="7" rx="3.5" fill="#334155"/>
                  
                  <!-- WA Chat Bubble -->
                  <rect x="444" y="85" width="172" height="90" rx="8" fill="#064e3b" stroke="#059669"/>
                  <text x="454" y="105" fill="#a7f3d0" font-size="10" font-weight="800">Kurir Logistik J&amp;T</text>
                  <text x="454" y="122" fill="#ecfdf5" font-size="9">Paket tertahan di gudang kami:</text>
                  <rect x="454" y="132" width="152" height="30" rx="5" fill="#047857"/>
                  <text x="464" y="152" fill="#fef08a" font-size="10" font-weight="700">&#128230; Cek_Resi_Paket.apk</text>
                  
                  <!-- Warning Box -->
                  <rect x="444" y="195" width="172" height="70" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
                  <text x="530" y="215" text-anchor="middle" fill="#fca5a5" font-size="9" font-weight="800">&#9888; SUMBER TIDAK DIKENAL</text>
                  <text x="530" y="232" text-anchor="middle" fill="#fecaca" font-size="8">Izinkan instalasi APK luar?</text>
                  <rect x="490" y="242" width="80" height="18" rx="4" fill="#ef4444"/>
                  <text x="530" y="255" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">IZINKAN (Korban)</text>
                ''',
                "defenseSvg": '''
                  <!-- Defense Shield Active -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <circle cx="410" cy="140" r="40" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                  <text x="410" y="148" text-anchor="middle" fill="#34d399" font-size="28">&#10004;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#a7f3d0" font-size="14" font-weight="800">INSTALASI SIDELOADING DIBLOKIR</text>
                  <text x="410" y="235" text-anchor="middle" fill="#cbd5e1" font-size="10">Kebijakan MDM / Google Play Protect menolak file APK tidak terverifikasi.</text>
                  <rect x="260" y="255" width="300" height="35" rx="6" fill="#022c22" stroke="#059669"/>
                  <text x="410" y="277" text-anchor="middle" fill="#6ee7b7" font-size="9" font-weight="700">STATUS: Perangkat Klien Aman dari Infiltrasi Trojan</text>
                '''
            },
            {
                "title": "Eskalasi Izin Accessibility Service",
                "statusText": "Penyalahgunaan Izin",
                "statusCls": "bad",
                "desc": "Setelah APK terpasang, trojan memanipulasi korban agar mengaktifkan 'Accessibility Service' (Layanan Aksesibilitas). Izin ini memberikan trojan hak penuh untuk membaca seluruh teks di layar, memantau aplikasi lain, dan mengeklik tombol secara otomatis.",
                "defenseDesc": "Mitigasi Pilar Operasional & RASP: Aplikasi fintech mendeteksi keberadaan Accessibility Service dari package tidak tepercaya dan meminta pengguna mencabutnya sebelum aplikasi dapat dibuka.",
                "analogy": "Seperti tamu tak dikenal yang meminta kunci cadangan master rumah dengan dalih 'ingin membantu memeriksa instalasi listrik'.",
                "triad": {
                    "c": {"text": "Terancam", "cls": "warn"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Izin Kritis", "android.permission.BIND_ACCESSIBILITY_SERVICE"],
                    ["Bahaya Aksesibilitas", "Mampu membaca antarmuka (UI Tree) dan mensimulasikan tap tombol"],
                    ["Teknik Persistensi", "Malware menyembunyikan ikon dari launcher agar sulit di-uninstall"]
                ],
                "quiz": {
                    "q": "Mengapa izin Accessibility Service sangat berbahaya jika dikuasai oleh malware perbankan?",
                    "options": [
                        "Karena malware dapat membaca semua isi layar dan meniru sentuhan tombol tanpa perlu akses root.",
                        "Karena izin ini secara otomatis meretas server cloud bank.",
                        "Karena izin ini membuat baterai ponsel langsung habis."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Layanan aksesibilitas dirancang untuk pengguna disabilitas, sehingga memiliki hak istimewa membaca struktur UI dan mengeksekusi klik otomatis."
                },
                "svg": '''
                  <!-- Smartphone Showing Accessibility Menu -->
                  <rect x="290" y="35" width="240" height="330" rx="22" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2.5" filter="url(#glowV1)"/>
                  <rect x="304" y="55" width="212" height="290" rx="12" fill="url(#screenGrad)"/>
                  <rect x="375" y="43" width="70" height="7" rx="3.5" fill="#334155"/>
                  
                  <rect x="304" y="55" width="212" height="32" fill="#1e293b"/>
                  <text x="410" y="76" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="700">Pengaturan Aksesibilitas</text>
                  
                  <!-- Fake Service Item -->
                  <rect x="314" y="100" width="192" height="75" rx="8" fill="#1e1b4b" stroke="#6366f1"/>
                  <text x="324" y="122" fill="#e0e7ff" font-size="10" font-weight="700">Layanan: Paket Resi Update</text>
                  <text x="324" y="138" fill="#94a3b8" font-size="8">Izinkan memantau seluruh layar ponsel?</text>
                  
                  <!-- Switch Active -->
                  <rect x="450" y="145" width="46" height="22" rx="11" fill="#22c55e"/>
                  <circle cx="482" cy="156" r="8.5" fill="#fff"/>
                  
                  <!-- Danger Warning Card -->
                  <rect x="314" y="185" width="192" height="145" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5" class="shake-node"/>
                  <text x="410" y="208" text-anchor="middle" fill="#fecaca" font-size="10" font-weight="800">&#9888; HAK AKSES SISTEM DIBERIKAN</text>
                  <text x="324" y="228" fill="#fca5a5" font-size="8.5">&bull; Membaca semua teks di layar</text>
                  <text x="324" y="246" fill="#fca5a5" font-size="8.5">&bull; Mengetahui penekanan PIN/Password</text>
                  <text x="324" y="264" fill="#fca5a5" font-size="8.5">&bull; Membaca SMS masuk secara instan</text>
                  <text x="324" y="282" fill="#fca5a5" font-size="8.5">&bull; Menjalankan klik otomatis (ATS)</text>
                  <rect x="330" y="295" width="160" height="22" rx="4" fill="#ef4444"/>
                  <text x="410" y="310" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">MALWARE KONTROL SISTEM</text>
                ''',
                "defenseSvg": '''
                  <!-- Accessibility Revocation -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="110" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; AUDIT IZIN LAYANAN AKSESIBILITAS</text>
                  <rect x="180" y="130" width="460" height="110" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="160" fill="#a7f3d0" font-size="11" font-weight="700">Peringatan Keamanan E-Wallet:</text>
                  <text x="200" y="182" fill="#cbd5e1" font-size="9">Aplikasi mendeteksi 'Paket_Resi.apk' menyalahgunakan Accessibility Service.</text>
                  <text x="200" y="202" fill="#fef08a" font-size="9">Aplikasi dompet digital terkunci otomatis demi melindungi saldo Anda.</text>
                  <text x="200" y="224" fill="#6ee7b7" font-size="9" font-weight="800">&#10004; Tindakan: Buka Pengaturan &gt; Nonaktifkan Izin Mencurigakan</text>
                  <rect x="280" y="255" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="277" text-anchor="middle" fill="#fff" font-size="10" font-weight="700">SESI DILINDUNGI RASP</text>
                '''
            },
            {
                "title": "Serangan Layar Palsu (Overlay Attack)",
                "statusText": "Injeksi Jendela Overlay",
                "statusCls": "bad",
                "desc": "Ketika korban membuka aplikasi dompet digital resmi, trojan mendeteksi aktivitas tersebut dan memunculkan jendela tiruan (overlay window) tepat di atas antarmuka asli. Korban mengira sedang memasukkan PIN pada aplikasi resmi.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Penerapan filter Anti-Tapjacking (`android:filterTouchesWhenObscured=\"true\"`) dan `FLAG_SECURE` yang secara otomatis menolak sentuhan jika ada layer aplikasi lain menutupi layar.",
                "analogy": "Seperti menempelkan stiker tombol palsu di atas tombol mesin ATM asli sehingga stiker itulah yang merekam sidik jari dan kode rahasia Anda.",
                "triad": {
                    "c": {"text": "Kritis", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Teknik Serangan", "Android Overlay Injection (SYSTEM_ALERT_WINDOW)"],
                    ["Deteksi Foreground", "Trojan memantau Package Name aplikasi dompet digital asli"],
                    ["Tampilan Overlay", "Tiruan presisi form input PIN 6-digit dompet digital"]
                ],
                "quiz": {
                    "q": "Bagaimana aplikasi Android asli dapat melindungi antarmukanya dari serangan Overlay Attack?",
                    "options": [
                        "Mengaktifkan properti filterTouchesWhenObscured dan WindowManager.LayoutParams.FLAG_SECURE.",
                        "Menghapus database SQLite lokal aplikasi.",
                        "Mengubah resolusi layar ponsel menjadi lebih rendah."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Atribut filterTouchesWhenObscured mengabaikan sentuhan saat jendela tertutup view lain, dan FLAG_SECURE mencegah perekaman layar."
                },
                "svg": '''
                  <!-- Genuine App (Bottom) -->
                  <rect x="160" y="65" width="210" height="290" rx="16" fill="url(#phoneGrad)" stroke="#475569" stroke-width="1.5" opacity="0.6"/>
                  <rect x="172" y="80" width="186" height="260" rx="8" fill="#0284c7"/>
                  <text x="265" y="115" text-anchor="middle" fill="#fff" font-size="12" font-weight="800">E-WALLET ASLI</text>
                  <text x="265" y="135" text-anchor="middle" fill="#e0f2fe" font-size="9">Tertutup di Lapisan Bawah</text>
                  
                  <!-- Injection Arrow -->
                  <path d="M 380 190 L 440 190" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 3" class="dash-flow"/>
                  <polygon points="440,185 452,190 440,195" fill="#ef4444"/>
                  <text x="410" y="175" text-anchor="middle" fill="#f87171" font-size="9" font-weight="700">Injeksi Overlay</text>

                  <!-- Fake Overlay (Top) -->
                  <rect x="450" y="45" width="240" height="320" rx="18" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2.5" filter="url(#glowV1)" class="fade-pop"/>
                  <rect x="462" y="60" width="216" height="290" rx="10" fill="#0f172a"/>
                  <rect x="462" y="60" width="216" height="42" fill="#1e293b"/>
                  <text x="570" y="86" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="800">&#128091; Dompet Digital Pay</text>
                  
                  <rect x="478" y="118" width="184" height="140" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-dasharray="4 2"/>
                  <text x="570" y="140" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="700">MASUKKAN PIN TRANSAKSI</text>
                  
                  <!-- PIN Dots -->
                  <circle cx="530" cy="168" r="5.5" fill="#38bdf8"/>
                  <circle cx="550" cy="168" r="5.5" fill="#38bdf8"/>
                  <circle cx="570" cy="168" r="5.5" fill="#38bdf8"/>
                  <circle cx="590" cy="168" r="5.5" fill="#334155"/>
                  <circle cx="610" cy="168" r="5.5" fill="#334155"/>
                  
                  <!-- Keypad Mock -->
                  <rect x="500" y="195" width="35" height="22" rx="4" fill="#334155"/>
                  <rect x="552" y="195" width="35" height="22" rx="4" fill="#334155"/>
                  <rect x="604" y="195" width="35" height="22" rx="4" fill="#334155"/>
                  <text x="517" y="210" fill="#fff" font-size="9" text-anchor="middle">1</text>
                  <text x="570" y="210" fill="#fff" font-size="9" text-anchor="middle">2</text>
                  <text x="622" y="210" fill="#fff" font-size="9" text-anchor="middle">3</text>

                  <rect x="478" y="270" width="184" height="40" rx="6" fill="#450a0a" stroke="#ef4444"/>
                  <text x="570" y="288" text-anchor="middle" fill="#fecaca" font-size="8.5" font-weight="800">&#9888; JENDELA OVERLAY PALSU</text>
                  <text x="570" y="302" text-anchor="middle" fill="#fca5a5" font-size="7.5">PIN yang diketik disadap oleh malware</text>
                ''',
                "defenseSvg": '''
                  <!-- Anti Tapjacking Protection -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; PROTEKSI ANTI-TAPJACKING &amp; FLAG_SECURE</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Filter Keamanan Layar Aktif:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; filterTouchesWhenObscured = TRUE (Input sentuhan ditolak)</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; FLAG_SECURE aktif (Perekaman layar &amp; screenshot diblokir OS)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; RASP mendeteksi objek overlay dan menghentikan proses transaksi</text>
                  <rect x="260" y="260" width="300" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">KREDENSIAL PIN TERLINDUNGI</text>
                '''
            },
            {
                "title": "Perekaman PIN & Penyadapan SMS OTP",
                "statusText": "Pencurian Kredensial",
                "statusCls": "bad",
                "desc": "Korban yang tidak sadar memasukkan 6 digit PIN. Keylogger malware mencatat setiap sentuhan, sementara listener Accessibility Service secara diam-diam mengekstrak SMS kode OTP dari bank tanpa menyalakan notifikasi atau suara pada ponsel.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Beralih dari SMS OTP ke Autentikasi Biometrik lokal berbasis Hardware Keystore (Android KeyStore / iOS Secure Enclave) dan Device Binding kriptografis.",
                "analogy": "Seperti seseorang mengintip dari balik bahu saat Anda memasukkan PIN, lalu mencuri surat kode rahasia dari kotak pos sebelum Anda membukanya.",
                "triad": {
                    "c": {"text": "Bocor Total", "cls": "bad"},
                    "i": {"text": "Terkorup", "cls": "bad"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Data Tercuri", "Nomor HP, 6 Digit PIN, SMS OTP verifikasi bank"],
                    ["Penyadapan SMS", "Membaca teks dari bar notifikasi via Accessibility API"],
                    ["Kelemahan SMS", "Tidak terenkripsi end-to-end dan mudah disadap di perangkat"]
                ],
                "quiz": {
                    "q": "Mengapa SMS OTP dinilai tidak lagi memadai sebagai faktor autentikasi kedua pada aplikasi perbankan modern?",
                    "options": [
                        "Karena SMS dapat disadap dengan mudah oleh malware di perangkat dan rentan terhadap serangan SIM Swap.",
                        "Karena SMS membutuhkan koneksi WiFi publik.",
                        "Karena SMS hanya bisa dibaca jika ponsel di-charge."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! NIST dan OJK menganjurkan penggantian SMS OTP dengan otentikasi kriptografis perangkat (FIDO2 / Hardware Keystore) karena SMS rentan intersepsi."
                },
                "svg": '''
                  <!-- Phone Intercepting -->
                  <rect x="120" y="60" width="220" height="290" rx="16" fill="url(#phoneGrad)" stroke="#ef4444" stroke-width="2"/>
                  <rect x="132" y="75" width="196" height="260" rx="8" fill="#0f172a"/>
                  
                  <rect x="142" y="90" width="176" height="50" rx="6" fill="#1e293b"/>
                  <text x="152" y="110" fill="#94a3b8" font-size="9">PIN Disadap (Keylogger):</text>
                  <text x="152" y="130" fill="#f87171" font-size="14" font-weight="800" font-family="monospace">849201</text>
                  
                  <rect x="142" y="155" width="176" height="65" rx="6" fill="#312e81" stroke="#6366f1"/>
                  <text x="152" y="175" fill="#c7d2fe" font-size="8.5" font-weight="700">SMS OTP Bank Diterima:</text>
                  <text x="152" y="195" fill="#fef08a" font-size="13" font-weight="800" font-family="monospace">OTP: 583-912</text>
                  <text x="152" y="212" fill="#a5b4fc" font-size="7.5">&#9889; Notifikasi diredam oleh trojan</text>
                  
                  <rect x="142" y="235" width="176" height="40" rx="6" fill="#450a0a" stroke="#ef4444"/>
                  <text x="230" y="255" text-anchor="middle" fill="#fca5a5" font-size="8.5" font-weight="800">PAKET EXFILTRASI SIAP</text>
                  <text x="230" y="267" text-anchor="middle" fill="#fecaca" font-size="7.5">Mengirim ke C2 Server Attacker</text>

                  <!-- Stream Arrow -->
                  <path d="M 350 200 L 510 200" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="510,195 522,200 510,205" fill="#ef4444"/>
                  <text x="430" y="188" text-anchor="middle" fill="#f87171" font-size="9" font-weight="700">HTTPS POST /c2/harvest</text>

                  <!-- C2 Server Terminal -->
                  <rect x="530" y="60" width="240" height="290" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV1)"/>
                  <text x="650" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">C2 ADVERSARY CONSOLE</text>
                  <rect x="545" y="105" width="210" height="225" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="555" y="130" fill="#4ade80" font-size="8.5" font-family="monospace">[+] CREDENTIAL HARVESTED!</text>
                  <text x="555" y="150" fill="#38bdf8" font-size="8" font-family="monospace">Target: +628129988xxxx</text>
                  <text x="555" y="170" fill="#f87171" font-size="8" font-family="monospace">PIN: 849201 [VALIDATED]</text>
                  <text x="555" y="190" fill="#facc15" font-size="8" font-family="monospace">SMS OTP: 583912 [CAPTURED]</text>
                  <text x="555" y="215" fill="#e2e8f0" font-size="8" font-family="monospace">&gt; Triggering ATS Module...</text>
                  <text x="555" y="235" fill="#a855f7" font-size="8" font-family="monospace">&gt; Target Wallet: ID-9982</text>
                  <text x="555" y="255" fill="#ec4899" font-size="8" font-family="monospace">&gt; Preparing automated debit</text>
                ''',
                "defenseSvg": '''
                  <!-- Hardware Keystore Safe -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128272; AUTENTIKASI HARDWARE KEYSTORE &amp; BIOMETRIK</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Tidak Menggunakan SMS OTP Rentan Intersepsi:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Kunci privat tersimpan di Secure Enclave / Titan M Security Chip</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Verifikasi transaksi mewajibkan biometrik fisik (Sidik Jari / Wajah)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Kunci tidak dapat diekstrak oleh malware software apapun di memori</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">ZERO SMS INTERCEPT RISK</text>
                '''
            },
            {
                "title": "Eksfiltrasi & Eksekusi Fraud (ATS Transfer)",
                "statusText": "Eksekusi Penipuan",
                "statusCls": "bad",
                "desc": "Data kredensial dan OTP dikirim ke server C2 penyerang. Penyerang mengaktifkan modul Automated Transfer System (ATS) yang mengeksekusi transfer dana dari rekening korban ke rekening penampung (money mule) dalam hitungan detik.",
                "defenseDesc": "Mitigasi Pilar Operasional: Fraud Detection System (FDS) memantau perilaku anomali (device fingerprint baru, transfer saldo 100% instan) dan otomatis menahan (hold) transaksi sebelum settlement.",
                "analogy": "Seperti pencuri yang langsung menggunakan kartu ATM curian beserta PIN-nya untuk menguras uang di mesin terdekat dalam hitungan detik.",
                "triad": {
                    "c": {"text": "Bocor", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Terganggu", "cls": "warn"}
                },
                "terms": [
                    ["ATS (Automated Transfer System)", "Skrip otomatisasi transfer uang tanpa intervensi manual"],
                    ["Money Mule", "Rekening penampung atas nama orang lain untuk mencuci uang curian"],
                    ["C2 Server", "Command and Control server yang mengendalikan jaringan malware"]
                ],
                "quiz": {
                    "q": "Apa yang dimaksud dengan Automated Transfer System (ATS) pada malware perbankan?",
                    "options": [
                        "Skrip otomatis yang langsung mengeksekusi transfer saldo ke rekening penampung sesaat setelah kredensial diperoleh.",
                        "Fitur transfer gratis dari bank untuk pengguna setia.",
                        "Protokol komunikasi antara mesin ATM dan satelit."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! ATS memungkinkan trojan mengeksekusi transfer instan secara otomatis sebelum korban menyadari atau sempat memblokir rekeningnya."
                },
                "svg": '''
                  <!-- Core Ledger & Mule Visual -->
                  <rect x="70" y="60" width="220" height="280" rx="14" fill="url(#serverGrad)" stroke="#38bdf8" stroke-width="1.8"/>
                  <text x="180" y="90" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="800">SERVER BANK / E-WALLET</text>
                  <rect x="85" y="110" width="190" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="95" y="125" width="170" height="45" rx="4" fill="#450a0a" stroke="#ef4444"/>
                  <text x="105" y="145" fill="#fca5a5" font-size="8.5" font-weight="700">DEBIT REKENING KORBAN:</text>
                  <text x="105" y="162" fill="#f87171" font-size="11" font-weight="800">- Rp 25.000.000</text>
                  
                  <rect x="95" y="180" width="170" height="45" rx="4" fill="#064e3b" stroke="#22c55e"/>
                  <text x="105" y="200" fill="#a7f3d0" font-size="8.5" font-weight="700">KREDIT KE REKENING MULE:</text>
                  <text x="105" y="217" fill="#4ade80" font-size="11" font-weight="800">+ Rp 25.000.000</text>

                  <rect x="95" y="240" width="170" height="60" rx="4" fill="#1e1b4b"/>
                  <text x="180" y="260" text-anchor="middle" fill="#c7d2fe" font-size="8.5" font-weight="700">STATUS TRANSAKSI:</text>
                  <text x="180" y="280" text-anchor="middle" fill="#f87171" font-size="10" font-weight="800">&#10007; SUCCESS (ATS INTRUSION)</text>

                  <!-- Arrow to Mule -->
                  <path d="M 300 200 L 480 200" stroke="#ef4444" stroke-width="3.5" class="dash-flow"/>
                  <polygon points="480,195 492,200 480,205" fill="#ef4444"/>
                  <text x="390" y="190" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">Transfer ke Mule</text>

                  <!-- Money Mule Account -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV1)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">REKENING PENAMPUNG (MULE)</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="530" y="140" fill="#38bdf8" font-size="9" font-family="monospace">Bank: Bank Anonim X</text>
                  <text x="530" y="160" fill="#38bdf8" font-size="9" font-family="monospace">Rekening: 9011-xxxx-4412</text>
                  <text x="530" y="180" fill="#38bdf8" font-size="9" font-family="monospace">Pemilik: Identitas Palsu (KTP Bodong)</text>
                  <rect x="530" y="200" width="190" height="50" rx="6" fill="#7f1d1d"/>
                  <text x="625" y="222" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">DANA LANGSUNG DITARIK</text>
                  <text x="625" y="238" text-anchor="middle" fill="#fca5a5" font-size="8">Dikonversi ke Kripto / Tunai ATM</text>
                ''',
                "defenseSvg": '''
                  <!-- FDS Hold & Rollback -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; FRAUD DETECTION SYSTEM (FDS) ANOMALY HOLD</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Aturan Deteksi Penipuan Terpicu:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Anomali Device Fingerprint &amp; Perubahan Pola Jam Transaksi</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Mekanisme Hold Otomatis menghentikan settlement dana ke rekening mule</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Tim SOC menerima peringatan instan dan memverifikasi pemilik rekening</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">DANA NASABAH BERHASIL DITAHAN</text>
                '''
            },
            {
                "title": "Dampak Akhir Serangan (Impact Vektor 1)",
                "statusText": "Kerugian Finansial",
                "statusCls": "bad",
                "desc": "Saldo nasabah terkuras habis tanpa disadari, akun dibekukan karena aktivitas transaksi anomali, dan identitas pribadi (PII) bocor ke jaringan kejahatan siber.",
                "defenseDesc": "Evaluasi Resiliensi: Dengan kontrol pertahanan berlapis (Defense in Depth), serangan trojan dapat diputus di tahap 1 (sideloading block), tahap 3 (anti-tapjacking/RASP), atau tahap 5 (FDS hold).",
                "analogy": "Seperti tabungan di brankas ludes dicuri, dan korban baru menyadarinya saat ingin membayar belanjaan di kasir.",
                "triad": {
                    "c": {"text": "Bocor Parah", "cls": "bad"},
                    "i": {"text": "Hancur", "cls": "bad"},
                    "a": {"text": "Terkunci", "cls": "bad"}
                },
                "terms": [
                    ["Saldo Terkuras", "Kerugian materi langsung pada nasabah"],
                    ["Akun Terkunci", "Sistem membekukan akun untuk investigasi forensik"],
                    ["Kebocoran PII", "Data identitas pribadi dijual di pasar gelap cybercrime"]
                ],
                "quiz": {
                    "q": "Menurut dokumen Modul 02, mengapa Vektor 1 (Mobile Banking Trojan) diklasifikasikan dengan tingkat keparahan CRITICAL?",
                    "options": [
                        "Karena berpotensi menyebabkan kerugian finansial massal dan kebocoran data jutaan pengguna secara simultan.",
                        "Karena trojan hanya menyerang ponsel merk lama.",
                        "Karena trojan tidak membutuhkan jaringan internet."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! V1 memiliki kombinasi Likelihood Tinggi (tren 3x YoY) dan Dampak Kritis karena otomatisasi pencurian saldo."
                },
                "svg": '''
                  <!-- Impact Visual -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="#2d0a0a" stroke="#ef4444" stroke-width="2.5" filter="url(#glowV1)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#fca5a5" font-size="14" font-weight="800">DAMPAK SERANGAN VEKTOR 1 — MOBILE BANKING TROJAN</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#450a0a" stroke="#f87171"/>
                  <text x="210" y="145" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">SALDO TERKURAS</text>
                  <text x="210" y="180" text-anchor="middle" fill="#f87171" font-size="18" font-weight="800">Rp 0</text>
                  <text x="210" y="210" text-anchor="middle" fill="#fecaca" font-size="8.5">Ludes via ATS Money Mule</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#450a0a" stroke="#f87171"/>
                  <text x="410" y="145" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">AKUN TERKUNCI</text>
                  <text x="410" y="175" text-anchor="middle" fill="#f87171" font-size="24">&#128274;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#fecaca" font-size="8.5">Diblokir Sistem Anti-Fraud</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#450a0a" stroke="#f87171"/>
                  <text x="610" y="145" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PII BOCOR</text>
                  <text x="610" y="180" text-anchor="middle" fill="#f87171" font-size="13" font-weight="800">NIK, PIN, NO HP</text>
                  <text x="610" y="210" text-anchor="middle" fill="#fecaca" font-size="8.5">Dijual ke Sindikat Pinjol</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#1f0909" stroke="#ef4444"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fca5a5" font-size="10" font-weight="800">KESIMPULAN: KEGAGALAN PERTAHANAN KLIEN BERDAMPAK FATAL</text>
                  <text x="410" y="300" text-anchor="middle" fill="#cbd5e1" font-size="9">Diperlukan pendekatan Defense-in-Depth untuk memotong rantai kill chain sebelum tahap eksfiltrasi.</text>
                ''',
                "defenseSvg": '''
                  <!-- Resilient Defense Architecture -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="14" font-weight="800">&#128737; PERTAHANAN BERLAPIS (DEFENSE-IN-DEPTH) SUKSES</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="210" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">SALDO UTUH</text>
                  <text x="210" y="180" text-anchor="middle" fill="#34d399" font-size="16" font-weight="800">Rp 25.000.000</text>
                  <text x="210" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Tidak Berkurang Sedikitpun</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="410" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">RASP ACTIVE</text>
                  <text x="410" y="175" text-anchor="middle" fill="#34d399" font-size="24">&#10004;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Overlay Terdeteksi &amp; Diblokir</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="610" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">PII TERLINDUNGI</text>
                  <text x="610" y="180" text-anchor="middle" fill="#34d399" font-size="13" font-weight="800">BIOMETRIK ENCLAVE</text>
                  <text x="610" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Zero Data Exfiltration</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">KONTROL PERTAHANAN BERHASIL MEMOTONG RUKUN KILL CHAIN</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Keamanan berlapis melindungi nasabah di setiap tahap serangan trojan.</text>
                '''
            },
            {
                "title": "Rangkuman Kontrol Mitigasi Vektor 1",
                "statusText": "Pertahanan Holistik",
                "statusCls": "ok",
                "desc": "Implementasi 4 pilar kontrol mitigasi Vektor 1: RASP, Anti-Tapjacking, Hardware Keystore, Blokir Sideloading, Deteksi/Revoke Accessibility Service, Verifikasi Code Signing, dan WORM Immutable Transaction Logging.",
                "defenseDesc": "Defense in Depth menjamin apabila salah satu kontrol gagal (misal korban berhasil menginstal APK), kontrol berikutnya (RASP dan Anti-Tapjacking) tetap mampu mencegah pencurian kredensial.",
                "analogy": "Seperti rumah dengan pagar luar terkunci, sensor gerak di halaman, pintu baja berlapis pin, dan brankas tahan api di dalam kamar.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Pilar Teknologi", "RASP, Anti-Tapjacking, Hardware Keystore"],
                    ["Pilar Operasional", "Sideloading restriction, Revoke Accessibility Service"],
                    ["Pilar Tata Kelola", "Code signing verification, WORM audit trail logging"]
                ],
                "quiz": {
                    "q": "Mengapa satu kontrol keamanan tunggal (misal hanya edukasi pengguna) tidak memadai untuk mengatasi Vektor 1?",
                    "options": [
                        "Karena 74% insiden kebocoran melibatkan faktor kelalaian manusia; kontrol teknis mandiri (RASP) harus hadir sebagai jaring pengaman lapis kedua.",
                        "Karena edukasi pengguna membutuhkan biaya jutaan dolar per jam.",
                        "Karena virus trojan kebal terhadap semua undang-undang pemerintah."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Prinsip Defense in Depth memastikan kegagalan pada satu lapisan (human error) tidak langsung berakibat fatal pada breach total."
                },
                "svg": '''
                  <!-- Defense Matrix Visual -->
                  <rect x="80" y="60" width="660" height="280" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">MATRIKS KONTROL PERTAHANAN BERLAPIS — VEKTOR 1</text>
                  
                  <rect x="100" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="170" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TEKNOLOGI</text>
                  <text x="110" y="165" fill="#cbd5e1" font-size="8">&bull; RASP Engine</text>
                  <text x="110" y="185" fill="#cbd5e1" font-size="8">&bull; Anti-Tapjacking</text>
                  <text x="110" y="205" fill="#cbd5e1" font-size="8">&bull; Hardware Keystore</text>
                  <text x="110" y="225" fill="#cbd5e1" font-size="8">&bull; FLAG_SECURE</text>
                  <text x="110" y="245" fill="#cbd5e1" font-size="8">&bull; Biometric Auth</text>
                  <text x="110" y="265" fill="#cbd5e1" font-size="8">&bull; Root/Jailbreak Detect</text>

                  <rect x="260" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="330" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">OPERASIONAL</text>
                  <text x="270" y="165" fill="#cbd5e1" font-size="8">&bull; Blokir Sideloading</text>
                  <text x="270" y="185" fill="#cbd5e1" font-size="8">&bull; Audit Accessibility</text>
                  <text x="270" y="205" fill="#cbd5e1" font-size="8">&bull; FDS Anomaly Hold</text>
                  <text x="270" y="225" fill="#cbd5e1" font-size="8">&bull; Edukasi Sideloading</text>
                  <text x="270" y="245" fill="#cbd5e1" font-size="8">&bull; Threat Intelligence</text>
                  <text x="270" y="265" fill="#cbd5e1" font-size="8">&bull; SOC Fast Escalation</text>

                  <rect x="420" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="490" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TATA KELOLA</text>
                  <text x="430" y="165" fill="#cbd5e1" font-size="8">&bull; Code Signing SOP</text>
                  <text x="430" y="185" fill="#cbd5e1" font-size="8">&bull; Review Perizinan App</text>
                  <text x="430" y="205" fill="#cbd5e1" font-size="8">&bull; Audit Siklus Rilis</text>
                  <text x="430" y="225" fill="#cbd5e1" font-size="8">&bull; SOP Penanganan ATS</text>
                  <text x="430" y="245" fill="#cbd5e1" font-size="8">&bull; Pelaporan OJK/BI</text>
                  <text x="430" y="265" fill="#cbd5e1" font-size="8">&bull; Forensik Insiden</text>

                  <rect x="580" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="650" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PENCADANGAN</text>
                  <text x="590" y="165" fill="#cbd5e1" font-size="8">&bull; Immutable WORM Log</text>
                  <text x="590" y="185" fill="#cbd5e1" font-size="8">&bull; Real-time Audit Trail</text>
                  <text x="590" y="205" fill="#cbd5e1" font-size="8">&bull; Mekanisme Rollback</text>
                  <text x="590" y="225" fill="#cbd5e1" font-size="8">&bull; Hold Settlement</text>
                  <text x="590" y="245" fill="#cbd5e1" font-size="8">&bull; Rekonsiliasi Saldo</text>
                  <text x="590" y="265" fill="#cbd5e1" font-size="8">&bull; Evidensi Bukti Hukum</text>
                ''',
                "defenseSvg": None
            }
        ]
    }

    print("Vektor 1 built.")
    return scenarios

if __name__ == '__main__':
    sc = get_scenarios()
    print("Scenarios initialized:", list(sc.keys()))
