# -*- coding: utf-8 -*-
"""
Builder for Vektor 3B: API Exploitation (BOLA / IDOR & Mass Extraction)
From Modul02_Kelompok05_Updated.pdf
"""

def get_v3b():
    return {
        "title": "Vektor 3B: API Exploitation",
        "subtitle": "Decompile APK, Celah BOLA/IDOR & Kebocoran Massal Data Nasabah",
        "accentColor": "#a855f7",
        "accentBg": "rgba(168, 85, 247, 0.12)",
        "steps": [
            {
                "title": "Reconnaissance (Decompile APK & Endpoint Discovery)",
                "statusText": "Reverse Engineering APK",
                "statusCls": "warn",
                "desc": "Penyerang mengunduh berkas APK resmi dompet digital dari Play Store, lalu melakukan reverse engineering menggunakan tool decompiler seperti JADX atau Apktool. Penyerang membedah kode Java/Kotlin dan menemukan daftar endpoint REST API internal yang tidak terdokumentasi publik.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Penerapan Advanced Code Obfuscation (ProGuard / DexGuard), enkripsi string sensitif, dan deteksi dynamic hooking (Frida/Xposed) di sisi klien.",
                "analogy": "Seperti membongkar mesin brankas portable untuk mempelajari diagram cetak biru kabel dan menemukan saklar rahasia di bagian belakangnya.",
                "triad": {
                    "c": {"text": "Terancam", "cls": "warn"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["JADX / Apktool", "Perangkat lunak open-source untuk mendekompilasi bytecode APK menjadi kode sumber"],
                    ["Hidden API Endpoints", "Alamat URL backend internal yang tidak sengaja diekspos di kode aplikasi"],
                    ["Code Obfuscation", "Teknik mengaburkan nama kelas dan logika kode agar tidak dapat dibaca manusia"]
                ],
                "quiz": {
                    "q": "Apa yang dicari penyerang saat mendekompilasi berkas APK aplikasi perbankan?",
                    "options": [
                        "Daftar endpoint REST API internal, skema struktur request/response, dan kunci API rahasia yang tertanam di kode.",
                        "Wallpaper tampilan aplikasi untuk dijual kembali.",
                        "Nama programmer yang membuat tombol login."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Analisis kode statis APK sering kali mengungkap endpoint rahasia backend dan logika bisnis yang rentan."
                },
                "svg": '''
                  <!-- Decompiler Screen Node -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#serverGrad)" stroke="#a855f7" stroke-width="2" filter="url(#glowV3b)"/>
                  <text x="225" y="90" text-anchor="middle" fill="#d8b4fe" font-size="11" font-weight="800">JADX-GUI APK DECOMPILER</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <text x="95" y="132" fill="#c084fc" font-size="8.5" font-family="monospace">package com.fintech.ewallet.api;</text>
                  <text x="95" y="152" fill="#38bdf8" font-size="8" font-family="monospace">public interface WalletApiService {</text>
                  
                  <rect x="95" y="162" width="260" height="50" rx="4" fill="#3b0764" stroke="#a855f7"/>
                  <text x="105" y="180" fill="#facc15" font-size="8" font-family="monospace">  @GET(\"/api/v1/user/{user_id}/balance\")</text>
                  <text x="105" y="196" fill="#4ade80" font-size="8" font-family="monospace">  Call&lt;WalletProfile&gt; getProfile(...);</text>

                  <text x="95" y="228" fill="#38bdf8" font-size="8" font-family="monospace">}</text>
                  <rect x="95" y="240" width="260" height="65" rx="4" fill="#1e1b4b"/>
                  <text x="225" y="260" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="700">&#128270; ENDPOINT RAHASIA DITEMUKAN</text>
                  <text x="225" y="278" text-anchor="middle" fill="#cbd5e1" font-size="8">Format user_id berupa angka integer berurutan:</text>
                  <text x="225" y="294" text-anchor="middle" fill="#fca5a5" font-size="8">user_id = 1001, 1002, 1003...</text>

                  <!-- Flow Arrow -->
                  <path d="M 400 190 L 485 190" stroke="#a855f7" stroke-width="2.5" stroke-dasharray="6 4" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#a855f7"/>

                  <!-- Target Backend API Box -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#serverGrad)" stroke="#a855f7" stroke-width="1.8"/>
                  <text x="625" y="90" text-anchor="middle" fill="#d8b4fe" font-size="11" font-weight="800">TARGET API ENDPOINT</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="625" cy="160" r="32" fill="#3b0764"/>
                  <text x="625" y="168" text-anchor="middle" fill="#c084fc" font-size="20">&#127760;</text>
                  <text x="625" y="215" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700">api.dompetpay.com</text>
                  <text x="625" y="235" text-anchor="middle" fill="#94a3b8" font-size="8.5">Endpoint siap diuji kerentanannya</text>
                  <rect x="530" y="255" width="190" height="35" rx="4" fill="#4a044e"/>
                  <text x="625" y="277" text-anchor="middle" fill="#f5d0fe" font-size="8.5" font-weight="700">Langkah 2: Uji BOLA / IDOR</text>
                ''',
                "defenseSvg": '''
                  <!-- ProGuard DexGuard Obfuscation Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; ADVANCED CODE OBFUSCATION &amp; STRING ENCRYPTION</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Proteksi Binary APK:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; DexGuard mengaburkan nama kelas menjadi simbol acak tidak bermakna (a.b.c.a())</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Enkripsi URL endpoint dan sertifikat publik pada binary native (C++ / .so library)</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; RASP mendeteksi upaya dynamic instrumentation Frida dan langsung crash otomatis</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">REVERSE ENGINEERING GAGAL</text>
                '''
            },
            {
                "title": "Vulnerability Discovery (Identifikasi BOLA / IDOR)",
                "statusText": "Penemuan Celah Otorisasi",
                "statusCls": "bad",
                "desc": "Penyerang login secara sah menggunakan akun miliknya (User ID 1001). Menggunakan Burp Suite, penyerang mencegat request profil lalu mengubah parameter `user_id` menjadi `1002`. Server mengembalikan seluruh data nasabah 1002 karena backend tidak mengecek apakah pemohon adalah pemilik sah data tersebut (BOLA - Broken Object Level Authorization).",
                "defenseDesc": "Mitigasi Pilar Teknologi: Open Policy Agent (OPA) / Fine-Grained Authorization di API Gateway. Memverifikasi bahwa klaim identitas pada token JWT (`jwt.sub`) identik dengan ID objek yang diminta (`input.user_id`).",
                "analogy": "Seperti tamu hotel bernomor kamar 101 yang iseng menempelkan kunci kartunya ke kamar 102, dan pintu kamar tetangga terbuka lebar karena kunci tidak mencocokkan nomor identitas pemegang kartu.",
                "triad": {
                    "c": {"text": "Bocor Parah", "cls": "bad"},
                    "i": {"text": "Terancam", "cls": "warn"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["BOLA / IDOR", "Broken Object Level Authorization (OWASP API Security #1:2023)"],
                    ["Broken Auth Flow", "Kegagalan validasi kepemilikan objek pada layer backend microservices"],
                    ["Burp Suite Repeater", "Alat untuk memanipulasi parameter HTTP request secara manual"]
                ],
                "quiz": {
                    "q": "Mengapa celah BOLA (Broken Object Level Authorization) menduduki peringkat #1 dalam OWASP API Security Top 10?",
                    "options": [
                        "Karena request HTTP yang dikirim penyerang memiliki token login sah dan format valid, sehingga WAF tradisional tidak mendeteksinya sebagai serangan.",
                        "Karena BOLA merusak router internet kantor.",
                        "Karena celah BOLA hanya terjadi pada aplikasi yang tidak memiliki database."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! BOLA adalah celah logika otorisasi bisnis, bukan signature serangan klasik seperti SQLi, sehingga lolos dari saringan WAF standar."
                },
                "svg": '''
                  <!-- BOLA Discovery Visual -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                  <text x="225" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">BURP SUITE REPEATER (USER 1001)</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="132" fill="#38bdf8" font-size="8.5" font-family="monospace">GET /api/v1/user/1002/profile HTTP/1.1</text>
                  <text x="95" y="150" fill="#cbd5e1" font-size="8" font-family="monospace">Authorization: Bearer [Token_User_1001]</text>
                  <rect x="95" y="165" width="260" height="40" rx="4" fill="#450a0a" stroke="#ef4444" class="shake-node"/>
                  <text x="105" y="185" fill="#fca5a5" font-size="8" font-family="monospace">&#9888; ID Dimanipulasi: 1001 &rarr; 1002</text>
                  <text x="105" y="198" fill="#f87171" font-size="7.5" font-family="monospace">Token miliknya sendiri, objek milik orang lain</text>

                  <rect x="95" y="215" width="260" height="95" rx="6" fill="#1e1b4b"/>
                  <text x="225" y="235" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="700">EVALUASI OTORISASI BACKEND:</text>
                  <text x="225" y="255" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">&#10007; NO AUTHORIZATION CHECK!</text>
                  <text x="225" y="272" text-anchor="middle" fill="#cbd5e1" font-size="8">Backend hanya mengecek keabsahan token,</text>
                  <text x="225" y="288" text-anchor="middle" fill="#fca5a5" font-size="8">tidak mengecek kepemilikan user_id 1002.</text>

                  <!-- Stream Arrow to Leaked Response -->
                  <path d="M 400 190 L 485 190" stroke="#ef4444" stroke-width="3" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#ef4444"/>

                  <!-- Server Response Box -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV3b)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">SERVER RESPONSE (HTTP 200 OK)</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="525" y="132" fill="#4ade80" font-size="8.5" font-family="monospace">HTTP/1.1 200 OK</text>
                  <text x="525" y="150" fill="#a7f3d0" font-size="7.5" font-family="monospace">{</text>
                  <text x="535" y="165" fill="#a7f3d0" font-size="7.5" font-family="monospace">  \"id\": 1002,</text>
                  <text x="535" y="180" fill="#f87171" font-size="7.5" font-family="monospace">  \"name\": \"Siti Rahmawati\",</text>
                  <text x="535" y="195" fill="#f87171" font-size="7.5" font-family="monospace">  \"nik\": \"3301024500980001\",</text>
                  <text x="535" y="210" fill="#f87171" font-size="7.5" font-family="monospace">  \"balance\": 45000000</text>
                  <text x="525" y="225" fill="#a7f3d0" font-size="7.5" font-family="monospace">}</text>
                  <rect x="525" y="235" width="200" height="70" rx="6" fill="#7f1d1d"/>
                  <text x="625" y="258" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">&#9888; CELAH BOLA TERBUKTI!</text>
                  <text x="625" y="275" text-anchor="middle" fill="#fecaca" font-size="8">Data nasabah lain terekspos bebas</text>
                  <text x="625" y="290" text-anchor="middle" fill="#fca5a5" font-size="7.5">Siap di-automate skrip massal</text>
                ''',
                "defenseSvg": '''
                  <!-- OPA / Fine-Grained Authorization Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; OPEN POLICY AGENT (OPA) &amp; FINE-GRAINED AUTH GATEWAY</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Evaluasi Kebijakan Otorisasi Mandiri:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; OPA Rule: allow { input.jwt.sub == input.requested_user_id }</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Evaluasi Gagal: Token milik User 1001 != Target Objek User 1002</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Gateway memutus koneksi dan merespons: HTTP 403 Forbidden</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">AKSES OBJEK NASABAH LAIN DIBLOKIR</text>
                '''
            },
            {
                "title": "Exploitation (Iterasi User ID Skrip Massal)",
                "statusText": "Eksploitasi Otomasi Skrip",
                "statusCls": "bad",
                "desc": "Mengetahui celah BOLA ada, penyerang menulis skrip otomatisasi (Python multi-threading atau Burp Intruder). Skrip mengeksekusi puluhan ribu permintaan HTTP per detik dengan menaikkan angka `user_id` dari 1000 hingga jutaan, membypass perlindungan rate limiting yang lemah.",
                "defenseDesc": "Mitigasi Pilar Teknologi: Penerapan Anycast Cloud WAF di edge jaringan dan Adaptive Rate Limiting yang membatasi maksimal 20 request per menit per token/IP.",
                "analogy": "Seperti robot yang berlari menyusuri seluruh lorong apartemen dan membuka ribuan pintu kamar dalam beberapa jam menggunakan kunci master.",
                "triad": {
                    "c": {"text": "Bocor Total", "cls": "bad"},
                    "i": {"text": "Kritis", "cls": "bad"},
                    "a": {"text": "Tertekan", "cls": "warn"}
                },
                "terms": [
                    ["Burp Intruder", "Modul pengujian penetrasi untuk melancarkan serangan brute force parameter"],
                    ["Scripted Exploitation", "Penggunaan skrip multithread untuk mempercepat eksfiltrasi ribuan kali lipat"],
                    ["Rate Limiting Bypass", "Mengeksploitasi endpoint yang lupa dikonfigurasi pembatas kuota request"]
                ],
                "quiz": {
                    "q": "Mengapa perlindungan Rate Limiting sangat krusial dipasang pada endpoint API publik?",
                    "options": [
                        "Untuk mencegah penyerang melakukan pemindaian atau penyedotan data secara massal dan otomatis dalam waktu singkat.",
                        "Untuk menghemat kuota internet pengguna ponsel.",
                        "Untuk mempercepat loading foto profil nasabah."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Rate limiting membatasi frekuensi pemanggilan endpoint sehingga eksploitasi skrip otomatisasi massal terhenti seketika."
                },
                "svg": '''
                  <!-- Mass Script Intruder Node -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV3b)"/>
                  <text x="225" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">BURP INTRUDER / SCRIPT RUNNER</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <text x="95" y="132" fill="#38bdf8" font-size="8.5" font-family="monospace">&gt; python3 dump_all_users.py</text>
                  <text x="95" y="152" fill="#facc15" font-size="8" font-family="monospace">Threads: 100 parallel workers</text>
                  <text x="95" y="172" fill="#4ade80" font-size="8" font-family="monospace">Speed: 4,500 requests / second</text>
                  <rect x="95" y="190" width="260" height="115" rx="6" fill="#1e1b4b"/>
                  <text x="105" y="210" fill="#a7f3d0" font-size="7.5" font-family="monospace">[200 OK] id=1003 &rarr; Budi Santoso</text>
                  <text x="105" y="226" fill="#a7f3d0" font-size="7.5" font-family="monospace">[200 OK] id=1004 &rarr; Dewi Lestari</text>
                  <text x="105" y="242" fill="#a7f3d0" font-size="7.5" font-family="monospace">[200 OK] id=1005 &rarr; Ahmad Fauzi</text>
                  <text x="105" y="258" fill="#a7f3d0" font-size="7.5" font-family="monospace">[200 OK] id=1006 &rarr; Jessica Wijaya</text>
                  <text x="225" y="288" text-anchor="middle" fill="#f87171" font-size="9" font-weight="800">ITERASI PULUHAN RIBU REQ/DETIK</text>

                  <!-- Stream to Edge API Gateway -->
                  <path d="M 400 190 L 485 190" stroke="#ef4444" stroke-width="3" stroke-dasharray="6 3" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#ef4444"/>

                  <!-- Overloaded API Gateway -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">API GATEWAY (OVERWHELMED)</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="625" cy="155" r="30" fill="#7f1d1d" class="shake-node"/>
                  <text x="625" y="163" text-anchor="middle" fill="#fca5a5" font-size="18">&#9888;</text>
                  <text x="625" y="205" text-anchor="middle" fill="#f87171" font-size="10" font-weight="800">TRAFIK MEMUNCAK EKSTREM</text>
                  <text x="625" y="222" text-anchor="middle" fill="#cbd5e1" font-size="8">Tidak ada Rate Limiting aktif</text>
                  <rect x="525" y="240" width="200" height="65" rx="4" fill="#450a0a"/>
                  <text x="625" y="260" text-anchor="middle" fill="#fecaca" font-size="8.5" font-weight="700">STATUS DATABASE:</text>
                  <text x="625" y="278" text-anchor="middle" fill="#fca5a5" font-size="7.5">Data jutaan nasabah</text>
                  <text x="625" y="292" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">TERSEDOT KE ATTACKER</text>
                ''',
                "defenseSvg": '''
                  <!-- Anycast Cloud WAF & Adaptive Rate Limiting Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; ANYCAST CLOUD WAF &amp; ADAPTIVE RATE LIMITING</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Penyaringan Trafik Skala Masif di Jaringan Edge:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Cloud WAF mendeteksi pola scraping otomatis dan lonjakan request &gt; 50 req/menit</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Token penyerang di-blacklist seketika; IP asal diblokir di edge jaringan global</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Server database terlindungi dan beban CPU origin server tetap stabil normal</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">LONJAKAN SCRAPING OTOMATIS DIBATALKAN</text>
                '''
            },
            {
                "title": "Mass Data Extraction (Penyedotan Jutaan Data)",
                "statusText": "Pencurian Database Masif",
                "statusCls": "bad",
                "desc": "Dalam waktu beberapa jam saja, penyerang berhasil mengekstraksi seluruh profil jutaan nasabah ke file basis data lokal: NIK, nama lengkap, nomor rekening, histori mutasi transaksi, dan saldo aktif. Sistem backend tidak sempat memutus koneksi.",
                "defenseDesc": "Mitigasi Pilar Operasional: Autoscaling connection pool dan pola Circuit Breaker yang otomatis menutup kanal transaksi jika mendeteksi anomali volume query database yang mencurigakan.",
                "analogy": "Seperti truk tangki ilegal yang menyedot habis seluruh isi pipa kilang minyak nasional dalam semalam tanpa ada alarm keamanan yang berbunyi.",
                "triad": {
                    "c": {"text": "Bocor Total", "cls": "bad"},
                    "i": {"text": "Hancur", "cls": "bad"},
                    "a": {"text": "Kritis", "cls": "bad"}
                },
                "terms": [
                    ["Data Dumping", "Penyalinan database skala jutaan baris secara ilegal ke media penyimpanan luar"],
                    ["PII Leak", "Personally Identifiable Information (NIK, KTP, Nama Ibu Kandung) terekspos"],
                    ["Circuit Breaker", "Pola arsitektur software untuk menghentikan operasi saat beban di luar toleransi"]
                ],
                "quiz": {
                    "q": "Apa fungsi pola 'Circuit Breaker' dalam arsitektur backend fintech ketika terjadi scraping data skala masif?",
                    "options": [
                        "Memutus atau menolak request baru secara terkendali ketika beban query melebihi ambang batas agar database tidak kolaps dan data tidak terkuras habis.",
                        "Menghapus seluruh akun nasabah yang ada di database.",
                        "Mematikan pasokan listrik seluruh gedung kantor."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Circuit Breaker melindungi kesehatan sistem dan membatasi volume kebocoran dengan memutus sirkuit layanan secara elegan."
                },
                "svg": '''
                  <!-- Extraction Meter Diagram -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#serverGrad)" stroke="#ef4444" stroke-width="2"/>
                  <text x="225" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYEDOTAN DATABASE FINANSIAL</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="95" y="125" width="260" height="70" rx="6" fill="#450a0a" stroke="#ef4444"/>
                  <text x="225" y="145" text-anchor="middle" fill="#fecaca" font-size="9" font-weight="800">PROGRESS DUMP DATABASE:</text>
                  <text x="225" y="172" text-anchor="middle" fill="#f87171" font-size="16" font-weight="800">10,240,891 NASABAH</text>
                  <text x="225" y="188" text-anchor="middle" fill="#fca5a5" font-size="7.5">100% Selesai Terekstraksi (18.4 GB JSON Dump)</text>

                  <rect x="95" y="205" width="260" height="100" rx="6" fill="#1e1b4b"/>
                  <text x="105" y="225" fill="#38bdf8" font-size="8" font-family="monospace">Isi Data Tercuri:</text>
                  <text x="105" y="242" fill="#fca5a5" font-size="8" font-family="monospace">&bull; NIK KTP &amp; Nama Lengkap</text>
                  <text x="105" y="258" fill="#fca5a5" font-size="8" font-family="monospace">&bull; Nomor HP, Alamat, Email</text>
                  <text x="105" y="274" fill="#fca5a5" font-size="8" font-family="monospace">&bull; Saldo Aktif &amp; Riwayat Mutasi Transaksi</text>

                  <!-- Exfil Stream to Attacker Storage -->
                  <path d="M 400 190 L 485 190" stroke="#ef4444" stroke-width="3.5" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#ef4444"/>

                  <!-- Attacker Hard Drive Box -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#ef4444" stroke-width="2" filter="url(#glowV3b)"/>
                  <text x="625" y="90" text-anchor="middle" fill="#fca5a5" font-size="11" font-weight="800">PENYIMPANAN DATA ATTACKER</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="625" cy="155" r="28" fill="#7f1d1d"/>
                  <text x="625" y="163" text-anchor="middle" fill="#fff" font-size="18">&#128190;</text>
                  <text x="625" y="205" text-anchor="middle" fill="#f87171" font-size="11" font-weight="800">DATA TERSIMPAN LENGKAP</text>
                  <text x="625" y="225" text-anchor="middle" fill="#fca5a5" font-size="8">Siap dimonetisasi di Dark Web</text>
                  <rect x="525" y="245" width="200" height="60" rx="4" fill="#3b0764"/>
                  <text x="625" y="268" text-anchor="middle" fill="#fde68a" font-size="8.5" font-weight="800">Langkah 5: Dark Web Auction</text>
                  <text x="625" y="285" text-anchor="middle" fill="#d8b4fe" font-size="7.5">Jual ke sindikat penipuan &amp; pinjol</text>
                ''',
                "defenseSvg": '''
                  <!-- Circuit Breaker & Anomaly Query Alert Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; CIRCUIT BREAKER &amp; DATABASE CONNECTION ISOLATION</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Isolasi Otomatis Beban Basis Data:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Pola Circuit Breaker 'TRIPPED' (Beban pool koneksi database &gt; 85%)</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Query profiling otomatis memutus transaksi massal yang melompati rentang ID</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Database utama terisolasi sehingga hanya kurang dari 0.001% data yang sempat tersentuh</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">KEBOCORAN DATA MASIF DIGAGALKAN</text>
                '''
            },
            {
                "title": "Monetization (Penjualan Data di Dark Web)",
                "statusText": "Monetisasi Pasar Gelap",
                "statusCls": "bad",
                "desc": "Penyerang memposting sampel 10.000 data di forum peretasan Dark Web (seperti BreachForums / pasar gelap Telegram). Basis data lengkap 10 juta nasabah dilelang dengan mata uang kripto (Bitcoin/Monero) untuk disalahgunakan sebagai modal pinjol ilegal dan penipuan terarah.",
                "defenseDesc": "Mitigasi Pilar Tata Kelola & Pencadangan: Tim Forensik Siber mengaktifkan Incident Response Plan (IRP), berkoordinasi dengan BSSN dan regulator, serta memanfaatkan log audit WORM untuk identifikasi data terdampak.",
                "analogy": "Seperti pencuri yang menggelar lapak di pasar gelap untuk menjual salinan sertifikat rumah dan dokumen rahasia warga sekota kepada sindikat penjahat.",
                "triad": {
                    "c": {"text": "Terjual Gelap", "cls": "bad"},
                    "i": {"text": "Hancur", "cls": "bad"},
                    "a": {"text": "Terganggu", "cls": "warn"}
                },
                "terms": [
                    ["Dark Web Forum", "Situs forum terenkripsi Onion/Tor tempat jual beli data hasil peretasan"],
                    ["Cryptocurrency Ransom/Auction", "Pembayaran menggunakan Bitcoin / Monero yang sulit dilacak"],
                    ["Identity Theft", "Penyalahgunaan data korban untuk pengajuan kredit ilegal tanpa izin"]
                ],
                "quiz": {
                    "q": "Apa bahaya jangka panjang bagi nasabah jika data PII mereka dijual di Dark Web?",
                    "options": [
                        "Identitas mereka dapat digunakan orang lain untuk membuka rekening bodong, pinjaman online ilegal, atau menjadi target penipuan spear-phishing seumur hidup.",
                        "Warna kartu ATM mereka akan berubah otomatis.",
                        "Ponsel mereka tidak bisa dicas lagi."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Sekali data pribadi bocor ke Dark Web, data tersebut beredar permanen dan menjadi amunisi kejahatan identitas berkepanjangan."
                },
                "svg": '''
                  <!-- Dark Web Forum Marketplace Visual -->
                  <rect x="70" y="60" width="310" height="280" rx="14" fill="url(#hackerGrad)" stroke="#a855f7" stroke-width="2" filter="url(#glowV3b)"/>
                  <text x="225" y="90" text-anchor="middle" fill="#d8b4fe" font-size="11" font-weight="800">BREACHFORUMS DARK WEB LISTING</text>
                  <rect x="85" y="110" width="280" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  
                  <rect x="95" y="125" width="260" height="55" rx="4" fill="#3b0764"/>
                  <text x="105" y="145" fill="#facc15" font-size="9" font-weight="700">[LEAK] 10M INDONESIAN E-WALLET USERS</text>
                  <text x="105" y="162" fill="#cbd5e1" font-size="7.5">Includes: Full Name, NIK, Balance, Phone, Mutation</text>
                  
                  <rect x="95" y="190" width="260" height="60" rx="4" fill="#1e1b4b"/>
                  <text x="105" y="210" fill="#38bdf8" font-size="8.5" font-family="monospace">Price: 2.5 BTC (~$150,000 USD)</text>
                  <text x="105" y="228" fill="#4ade80" font-size="8.5" font-family="monospace">Escrow: Accepted | Seller: APT-Shadow</text>

                  <rect x="95" y="260" width="260" height="45" rx="4" fill="#7f1d1d"/>
                  <text x="225" y="280" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="800">&#128176; STATUS: TRANSAKSI BERHASIL</text>
                  <text x="225" y="295" text-anchor="middle" fill="#fca5a5" font-size="7.5">Data dibeli oleh 3 sindikat kejahatan siber</text>

                  <!-- Flow to Dark Web Buyers -->
                  <path d="M 400 190 L 485 190" stroke="#a855f7" stroke-width="3" class="dash-flow"/>
                  <polygon points="485,185 497,190 485,195" fill="#a855f7"/>

                  <!-- Fraud Syndicates Receiving Data -->
                  <rect x="500" y="60" width="250" height="280" rx="14" fill="url(#hackerGrad)" stroke="#a855f7" stroke-width="2"/>
                  <text x="625" y="90" text-anchor="middle" fill="#d8b4fe" font-size="11" font-weight="800">SINDIKAT PENIPUAN &amp; PINJOL</text>
                  <rect x="515" y="110" width="220" height="210" rx="8" fill="#020617" stroke="#334155"/>
                  <circle cx="625" cy="155" r="28" fill="#3b0764"/>
                  <text x="625" y="163" text-anchor="middle" fill="#fde68a" font-size="18">&#128101;</text>
                  <text x="625" y="205" text-anchor="middle" fill="#fff" font-size="10" font-weight="800">Eksploitasi Sekunder:</text>
                  <text x="625" y="225" text-anchor="middle" fill="#fca5a5" font-size="8">&bull; Pengajuan Pinjaman Ilegal</text>
                  <text x="625" y="242" text-anchor="middle" fill="#fca5a5" font-size="8">&bull; Pemerasan Berbasis Saldo</text>
                  <text x="625" y="260" text-anchor="middle" fill="#fca5a5" font-size="8">&bull; Spear-Phishing Akurat</text>
                  <rect x="525" y="275" width="200" height="30" rx="4" fill="#4a044e"/>
                  <text x="625" y="295" text-anchor="middle" fill="#f5d0fe" font-size="8" font-weight="700">BENCANA IDENTITAS MASSAL</text>
                ''',
                "defenseSvg": '''
                  <!-- Dark Web Scraper & Legal Threat Intel Shield -->
                  <rect x="150" y="70" width="520" height="260" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="105" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">&#128737; THREAT INTELLIGENCE &amp; AUDIT TRAIL FORENSIK</text>
                  <rect x="180" y="125" width="460" height="120" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="200" y="152" fill="#a7f3d0" font-size="11" font-weight="700">Mitigasi Dampak Forensik Pascainsiden:</text>
                  <text x="200" y="174" fill="#cbd5e1" font-size="9">&bull; Log WORM membuktikan secara legal integritas transaksi tidak diubah oleh pelaku</text>
                  <text x="200" y="194" fill="#cbd5e1" font-size="9">&bull; Kerja sama dengan BSSN dan aparat penegak hukum untuk melacak alamat wallet crypto</text>
                  <text x="200" y="214" fill="#cbd5e1" font-size="9">&bull; Notifikasi wajib kepada pemilik data dalam kurun 3 x 24 jam sesuai amanat UU PDP</text>
                  <rect x="280" y="260" width="260" height="35" rx="6" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="282" text-anchor="middle" fill="#fff" font-size="9.5" font-weight="700">RESPON FORENSIK CEPAT &amp; TRANSPARAN</text>
                '''
            },
            {
                "title": "Dampak Akhir Serangan (Impact Vektor 3B)",
                "statusText": "Sanksi UU PDP & Pencabutan Izin",
                "statusCls": "bad",
                "desc": "Kebocoran lebih dari 10 juta data pribadi nasabah, pencabutan sertifikasi kepatuhan transaksi kartu (PCI-DSS Revoked), dan ancaman sanksi hukum berat di bawah UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi (denda administratif hingga puluhan miliar rupiah dan sanksi pidana).",
                "defenseDesc": "Evaluasi Resiliensi: Penguatan validasi otorisasi di level API Gateway dan implementasi WAF dengan Adaptive Rate Limiting mampu memotong kill chain V3B sebelum terjadi ekstraksi data.",
                "analogy": "Seperti perusahaan yang dijatuhi vonis bangkrut, izin usahanya dicabut pemerintah, dan direksinya diproses hukum karena kelalaian fatal menjaga arsip rahasia jutaan warga.",
                "triad": {
                    "c": {"text": "10M+ Bocor", "cls": "bad"},
                    "i": {"text": "Terkorup", "cls": "bad"},
                    "a": {"text": "Izin Dicabut", "cls": "bad"}
                },
                "terms": [
                    ["UU PDP No. 27/2022", "Regulasi perlindungan data pribadi Indonesia dengan sanksi pidana & denda berat"],
                    ["PCI-DSS Revocation", "Pencabutan lisensi memproses pembayaran kartu kredit & transaksi finansial"],
                    ["Mass Breach Severity", "Kategori Severity CRITICAL karena dampak sistemik skala nasional"]
                ],
                "quiz": {
                    "q": "Menurut dokumen Modul 02, sanksi apa yang membayangi penyelenggara e-wallet jika terjadi kebocoran 10 juta data akibat celah API BOLA?",
                    "options": [
                        "Pencabutan sertifikasi PCI-DSS dan sanksi denda administratif miliaran rupiah berdasarkan UU PDP No. 27/2022.",
                        "Kewajiban membagikan saldo gratis kepada penyerang.",
                        "Penggantian nama aplikasi menjadi situs belajar mengetik."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Dokumen Modul 02 menegaskan dampak V3B mencakup '10M+ data bocor, PCI-DSS revoked, Sanksi UU PDP'."
                },
                "svg": '''
                  <!-- Impact Vector 3B Visual -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="#26082e" stroke="#a855f7" stroke-width="2.5" filter="url(#glowV3b)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#f5d0fe" font-size="14" font-weight="800">DAMPAK SERANGAN VEKTOR 3B — API EXPLOITATION (BOLA)</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#3b0764" stroke="#a855f7"/>
                  <text x="210" y="145" text-anchor="middle" fill="#f5d0fe" font-size="11" font-weight="800">10M+ DATA BOCOR</text>
                  <text x="210" y="180" text-anchor="middle" fill="#f87171" font-size="16" font-weight="800">MASS BREACH</text>
                  <text x="210" y="210" text-anchor="middle" fill="#fca5a5" font-size="8.5">NIK, Saldo, Mutasi Beredar</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#3b0764" stroke="#a855f7"/>
                  <text x="410" y="145" text-anchor="middle" fill="#f5d0fe" font-size="11" font-weight="800">PCI-DSS REVOKED</text>
                  <text x="410" y="175" text-anchor="middle" fill="#f87171" font-size="24">&#10008;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#fca5a5" font-size="8.5">Izin Pembayaran Dibekukan</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#3b0764" stroke="#a855f7"/>
                  <text x="610" y="145" text-anchor="middle" fill="#f5d0fe" font-size="11" font-weight="800">SANKSI UU PDP</text>
                  <text x="610" y="180" text-anchor="middle" fill="#f87171" font-size="13" font-weight="800">DENDA &amp; PIDANA</text>
                  <text x="610" y="210" text-anchor="middle" fill="#fca5a5" font-size="8.5">UU No. 27 Tahun 2022</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#4a044e" stroke="#a855f7"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">KESIMPULAN: CELAH LOGIKA API ADALAH ANCAMAN KRITIS TERTINGGI</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Otorisasi di level objek (BOLA mitigation) dan Anycast WAF wajib menjadi standar arsitektur backend.</text>
                ''',
                "defenseSvg": '''
                  <!-- Resilient Defense Matrix V3B -->
                  <rect x="100" y="55" width="620" height="290" rx="16" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2.5" filter="url(#glowGreen)"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="14" font-weight="800">&#128737; RESILIENSI ARSITEKTUR BACKEND DENGAN OPA &amp; CLOUD WAF</text>
                  
                  <rect x="130" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="210" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">DATA NASABAH</text>
                  <text x="210" y="180" text-anchor="middle" fill="#34d399" font-size="16" font-weight="800">100% AMAN</text>
                  <text x="210" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Zero Data Leaked</text>

                  <rect x="330" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="410" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">PCI-DSS COMPLIANT</text>
                  <text x="410" y="175" text-anchor="middle" fill="#34d399" font-size="24">&#10004;</text>
                  <text x="410" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Sertifikasi Utuh</text>

                  <rect x="530" y="115" width="160" height="120" rx="10" fill="#022c22" stroke="#10b981"/>
                  <text x="610" y="145" text-anchor="middle" fill="#86efac" font-size="11" font-weight="800">UU PDP COMPLIANT</text>
                  <text x="610" y="180" text-anchor="middle" fill="#34d399" font-size="13" font-weight="800">ZERO SANCTION</text>
                  <text x="610" y="210" text-anchor="middle" fill="#a7f3d0" font-size="8.5">Audit Governance Lolos</text>

                  <rect x="130" y="255" width="560" height="60" rx="8" fill="#064e3b" stroke="#10b981"/>
                  <text x="410" y="280" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="800">PERTUMBUHAN BISNIS FINTECH AMAN DARI RISIKO HUKUM SISTEMIK</text>
                  <text x="410" y="300" text-anchor="middle" fill="#fff" font-size="9">Keamanan API berlapis menjaga integritas dan privasi jutaan data masyarakat.</text>
                '''
            },
            {
                "title": "Rangkuman Kontrol Mitigasi Vektor 3B",
                "statusText": "Pertahanan Infrastruktur Backend",
                "statusCls": "ok",
                "desc": "Implementasi 4 pilar kontrol mitigasi Vektor 3B: Open Policy Agent (OPA) / ABAC, Anycast Cloud WAF, Adaptive Rate Limiting, Obfuscation & Dynamic Hook Detection, Circuit Breaker, Message Queue Buffering (Kafka), dan Multi-Region Database Replication.",
                "defenseDesc": "Mencegah eksfiltrasi data secara menyeluruh mulai dari proteksi binary aplikasi hingga ketahanan sistem terdistribusi pada basis data.",
                "analogy": "Seperti gedung perbankan dengan pintu brankas berkode otorisasi ganda di setiap laci nasabah, serta sistem pintu darurat otomatis yang mengunci diri saat ada gerakan mencurigakan.",
                "triad": {
                    "c": {"text": "Aman", "cls": "safe"},
                    "i": {"text": "Aman", "cls": "safe"},
                    "a": {"text": "Aman", "cls": "safe"}
                },
                "terms": [
                    ["Pilar Teknologi", "OPA Rego Authorization, Anycast Cloud WAF, Adaptive Rate Limiter"],
                    ["Pilar Operasional", "Circuit Breaker, Autoscaling connection pool, Load Testing"],
                    ["Pilar Tata Kelola", "DDoS Incident Runbook, Kepatuhan UU PDP No. 27/2022"]
                ],
                "quiz": {
                    "q": "Di tahap manakah serangan Vektor 3B (API Exploitation) paling efektif dihentikan sesuai dokumen Modul 02?",
                    "options": [
                        "Pada tahap Exploitation dengan menerapkan rate limiting dan proper authorization di API gateway.",
                        "Setelah database 10 juta nasabah terunggah di Dark Web.",
                        "Saat penyerang mengajukan cuti liburan."
                    ],
                    "correct": 0,
                    "feedback": "Tepat! Dokumen Modul 02 halaman 3 secara eksplisit menyatakan bahwa V3B bisa dihentikan di tahap Exploitation dengan rate limiting dan proper authorization di API gateway."
                },
                "svg": '''
                  <!-- Matrix V3B Controls Visual -->
                  <rect x="80" y="60" width="660" height="280" rx="14" fill="url(#serverGrad)" stroke="#10b981" stroke-width="2"/>
                  <text x="410" y="90" text-anchor="middle" fill="#86efac" font-size="13" font-weight="800">MATRIKS KONTROL PERTAHANAN BERLAPIS — VEKTOR 3B (BACKEND &amp; API)</text>
                  
                  <rect x="100" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="170" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TEKNOLOGI</text>
                  <text x="110" y="165" fill="#cbd5e1" font-size="8">&bull; OPA Policy Engine</text>
                  <text x="110" y="185" fill="#cbd5e1" font-size="8">&bull; Anycast Cloud WAF</text>
                  <text x="110" y="205" fill="#cbd5e1" font-size="8">&bull; Adaptive Rate Limit</text>
                  <text x="110" y="225" fill="#cbd5e1" font-size="8">&bull; UUID v4 Non-seq</text>
                  <text x="110" y="245" fill="#cbd5e1" font-size="8">&bull; Obfuscation Binary</text>
                  <text x="110" y="265" fill="#cbd5e1" font-size="8">&bull; Anti-Frida RASP</text>

                  <rect x="260" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="330" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">OPERASIONAL</text>
                  <text x="270" y="165" fill="#cbd5e1" font-size="8">&bull; Circuit Breaker</text>
                  <text x="270" y="185" fill="#cbd5e1" font-size="8">&bull; Autoscaling Pool</text>
                  <text x="270" y="205" fill="#cbd5e1" font-size="8">&bull; Real-time RPS Alert</text>
                  <text x="270" y="225" fill="#cbd5e1" font-size="8">&bull; Tabletop Exercises</text>
                  <text x="270" y="245" fill="#cbd5e1" font-size="8">&bull; Regular Load Testing</text>
                  <text x="270" y="265" fill="#cbd5e1" font-size="8">&bull; Red Team API Pen-test</text>

                  <rect x="420" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="490" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">TATA KELOLA</text>
                  <text x="430" y="165" fill="#cbd5e1" font-size="8">&bull; DDoS Runbook RTO</text>
                  <text x="430" y="185" fill="#cbd5e1" font-size="8">&bull; Kepatuhan UU PDP</text>
                  <text x="430" y="205" fill="#cbd5e1" font-size="8">&bull; Audit OWASP API Top 10</text>
                  <text x="430" y="225" fill="#cbd5e1" font-size="8">&bull; Prosedur Notifikasi 72h</text>
                  <text x="430" y="245" fill="#cbd5e1" font-size="8">&bull; SOP Eskalasi Insiden</text>
                  <text x="430" y="265" fill="#cbd5e1" font-size="8">&bull; Review Arsitektur</text>

                  <rect x="580" y="115" width="140" height="190" rx="8" fill="#022c22" stroke="#059669"/>
                  <text x="650" y="140" text-anchor="middle" fill="#86efac" font-size="10" font-weight="800">PENCADANGAN</text>
                  <text x="590" y="165" fill="#cbd5e1" font-size="8">&bull; Kafka Queue Buffer</text>
                  <text x="590" y="185" fill="#cbd5e1" font-size="8">&bull; Multi-Region DB Sync</text>
                  <text x="590" y="205" fill="#cbd5e1" font-size="8">&bull; Immutable WORM Audit</text>
                  <text x="590" y="225" fill="#cbd5e1" font-size="8">&bull; Automated Failover</text>
                  <text x="590" y="245" fill="#cbd5e1" font-size="8">&bull; RPO &lt; 5m, RTO &lt; 30m</text>
                  <text x="590" y="265" fill="#cbd5e1" font-size="8">&bull; Forensik Snapshots</text>
                ''',
                "defenseSvg": None
            }
        ]
    }

print("get_v3b defined.")
