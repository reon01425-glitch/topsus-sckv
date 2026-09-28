# DOKUMENTASI RIWAYAT PROMPT / QUERY PENGGUNA

**Mata Kuliah:** Topik Khusus Sistem Cerdas / Komputasi Visual  
**Kelompok:** Kelompok Cipta dkk.  
**Studi Kasus:** Threat Modeling & Defense in Depth Aplikasi E-Wallet FinTech  

---

## 1. Prompt #1: Analisis Kasus Mandiri FinTech, Threat Modeling, & Defense in Depth
*Waktu: 2026-09-07 19:49:13 WIB*

```markdown
Bertindaklah sebagai Senior Cybersecurity Architect dan Threat Modeling Specialist di industri Financial Technology (Fintech). 

Saya sedang mengerjakan tugas analisis kasus mandiri dengan rincian berikut:
- Studi Kasus: Aplikasi Dompet Digital (Fintech E-Wallet / Mobile Payment)
- Topik: Threat Modeling, Audit Vektor Ancaman, dan Strategi Defense in Depth
- Format Output: Konten presentasi (.pptx) dan kode visualisasi interaktif (.html)

Tolong susun analisis mendalam yang komprehensif, akademis, dan praktikal dengan struktur berikut:

---

### 1. PROFIL STUDI KASUS & ARSITEKTUR SINGKAT
- Nama/Konteks: Sistem Aplikasi Dompet Digital B2C & Merchant (Fitur: QRIS, P2P Transfer, Top-up, Payment Gateway API, dan Autentikasi Biometrik/PIN/OTP).
- Komponen Kritis: Mobile Client (Android/iOS), API Gateway & Core Banking/Ledger Services, Database Finansial & HSM/KMS.

### 2. THREAT LANDSCAPE & AUDIT 3 VEKTOR ANCAMAN
Analisis minimal 3 vektor serangan yang paling relevan dan sering terjadi pada Fintech:
1. Vektor Malware: Mobile Banking Trojan / Overlay Attack & Accessibility Service Abuse (misal: Trojan mencuri PIN/OTP dan melakukan transaksi ilegal di background).
2. Vektor Phishing / Social Engineering: OTP Harvesting & SIM Swap / Vishing mengatasnamakan CS resmi untuk pengambilalihan akun (Account Takeover - ATO).
3. Vektor Jaringan / Web / API: Broken Object Level Authorization (BOLA / IDOR) atau Credential Stuffing pada Payment/Transfer API Endpoint.

Untuk setiap vektor, sertakan:
- Deskripsi & Alur Serangan (Attack Flow)
- Profil Adversary (Motivasi, Kapabilitas teknis, Sumber daya)
- Dampak Bisnis & Finansial (CIA Triad impact, kerugian reputasi, kepatuhan regulasi OJK/BI)

### 3. RANCANG BANGUN DEFENSE IN DEPTH
Rumuskan strategi kontrol pertahanan berlapis pada 3 pilar:
1. Pilar Teknologi:
   - RASP (Runtime Application Self-Protection), Certificate Pinning, Anti-Tamper/Root Detection di sisi Mobile Client.
   - WAF, API Security Gateway (OAuth 2.0, Rate Limiting, mTLS), HSM untuk enkripsi data finansial.
   - SIEM / XDR dan Fraud Detection System (FDS) berbasis Behavior Analysis.
2. Pilar Tindakan (People & Operational):
   - Edukasi nasabah anti-phishing (kampanye "Jaga OTP").
   - Security Awareness Training untuk tim internal, simulasi phishing, dan latihan Red Team / Blue Team rutin.
   - Zero Trust privilege access (MFA berkala, Role-Based Access Control).
3. Pilar Proses & Tata Kelola:
   - Secure SDLC (Threat Modeling berkala dengan framework STRIDE, SAST/DAST, Pen-testing sebelum rilis).
   - Incident Response Plan (IRP) & SOP eskalasi fraud finansial sesuai standar ISO 27001 dan PCI-DSS.
   - Skema Backup 3-2-1: 
     * 3 salinan data transaksi/database.
     * 2 media penyimpanan berbeda (misal: SSD SAN on-premise + Cloud Object Storage).
     * 1 salinan off-site yang terisolasi / immutable (WORM storage) tahan ransomware.

### 4. OUTPUT 1: OUTLINE & KONTEN SLIDE PRESENTASI (.PPTX)
Buat struktur slide presentasi yang siap pakai (10–12 slide) lengkap dengan:
- Judul Slide & Poin-poin Kunci (Bullet points padat & berbobot)
- Speaker Notes (naskah penjelasan lisan presenter untuk setiap slide)
- Berikan script Python lengkap menggunakan library `python-pptx` agar saya bisa langsung menjalankan kodenya untuk men-generate file .pptx tersebut secara otomatis dengan desain visual yang rapi dan profesional.

### 5. OUTPUT 2: VISUALISASI INTERAKTIF (.HTML)
Buat satu file mandiri `index.html` (single-file HTML/CSS/JS tanpa dependensi luar yang rumit) yang memvisualisasikan:
- Diagram alur 3 Vektor Serangan (Attack Vector Flow).
- Matriks Pemetaan Ancaman vs Mitigasi Defense in Depth (Teknologi, Tindakan, Proses).
- Visualisasi interaktif Skema Backup 3-2-1.
- Tampilan modern, responsif, dark-mode/fintech tech style (menggunakan Tailwind CSS via CDN atau CSS murni).

### 6. DAFTAR REFERENSI (FORMAT STANDAR IEEE)
Sertakan daftar pustaka berformat IEEE yang relevan, termasuk:
- Dokumen BPSDM Kominfo terkait Threat Landscape
- Verizon DBIR (Data Breach Investigations Report) terbaru
- Standar OWASP API Security Top 10 & NIST Cybersecurity Framework
```

---

## 2. Prompt #2: Penyesuaian Visualisasi Mengikuti Style Course Folder
*Waktu: 2026-09-07 19:56:00 WIB*

```markdown
I want you to visualize it like in the drive-download-20260907T122854Z-1-001 dir. ( but be more specific on Fintech Application ).
```

---

## 3. Prompt #3: Penggantian Afiliasi & Penamaan Kelompok Tugas
*Waktu: 2026-09-07 20:01:38 WIB*

```markdown
ganti dari UNDIP Cybersecurity Education Series • Author: Senior Cybersecurity Architect menjadi Topik Khusus Sistem Cerdas/Komputasi Visual - Kelompok Cipta dkk.
```

---

## 4. Prompt #4: Permintaan Rekapitulasi Prompting
*Waktu: 2026-09-07 20:03:54 WIB*

```markdown
berikan seluruh text prompting / query saya dari awal hingga akhir dalam bentuk .md
```
