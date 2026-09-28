#!/usr/bin/env python3
"""
FINTECH THREAT MODELING & DEFENSE IN DEPTH PRESENTATION GENERATOR
Penyusun: Topik Khusus Sistem Cerdas/Komputasi Visual - Kelompok Cipta dkk.
Target: Executive & Academic Presentation (16:9 Widescreen, Dark Fintech Aesthetics)
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Color Palette Constants ---
BG_DARK = RGBColor(10, 15, 29)          # #0A0F1D Deep Navy
CARD_BG = RGBColor(19, 29, 54)          # #131D36 Slate Blue Card
CARD_BORDER = RGBColor(40, 56, 92)      # #28385C Subtle Border
TEXT_PRIMARY = RGBColor(248, 250, 252)  # #F8FAFC Pure White
TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8 Cool Gray
ACCENT_CYAN = RGBColor(14, 165, 233)    # #0EA5E9 Tech Cyan
ACCENT_EMERALD = RGBColor(16, 185, 129) # #10B981 Success Emerald
ACCENT_ROSE = RGBColor(244, 63, 94)     # #F43F5E Threat Rose / Red
ACCENT_AMBER = RGBColor(245, 158, 11)   # #F59E0B Warning Amber
CARD_ALT_BG = RGBColor(24, 36, 66)      # #182442

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank slide

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.color.rgb = BG_DARK
        return bg

    def add_header(slide, badge_text, title_text, subtitle_text=""):
        # Category Badge
        badge_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.4))
        tf_b = badge_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.text = badge_text.upper()
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = ACCENT_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.7))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_PRIMARY

        # Subtitle
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.45), Inches(11.7), Inches(0.45))
            tf_s = sub_box.text_frame
            tf_s.word_wrap = True
            tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle_text
            p_s.font.size = Pt(12)
            p_s.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, items, title_color=ACCENT_CYAN, bg_color=CARD_BG):
        # Card Background Shape
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1)

        # Card Title
        tb_title = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), Inches(0.4))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.color.rgb = title_color

        # Card Items / Bullets
        tb_content = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.65), width - Inches(0.5), height - Inches(0.8))
        tf_content = tb_content.text_frame
        tf_content.word_wrap = True
        tf_content.margin_left = tf_content.margin_top = tf_content.margin_right = tf_content.margin_bottom = 0

        for idx, item in enumerate(items):
            p = tf_content.paragraphs[0] if idx == 0 else tf_content.add_paragraph()
            p.space_after = Pt(8)
            p.space_before = Pt(2)
            
            if isinstance(item, tuple):
                header_txt, desc_txt = item
                run1 = p.add_run()
                run1.text = "• " + header_txt + ": "
                run1.font.bold = True
                run1.font.size = Pt(11)
                run1.font.color.rgb = TEXT_PRIMARY
                
                run2 = p.add_run()
                run2.text = desc_txt
                run2.font.bold = False
                run2.font.size = Pt(10.5)
                run2.font.color.rgb = TEXT_MUTED
            else:
                run = p.add_run()
                run.text = "• " + item
                run.font.size = Pt(10.5)
                run.font.color.rgb = TEXT_PRIMARY

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_background(slide1)

    # Accent decorative bar
    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(1.2), Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_CYAN
    bar.line.fill.background()

    # Title Box
    title_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.1), Inches(11.7), Inches(2.2))
    tf = title_box.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "THREAT MODELING, AUDIT VEKTOR ANCAMAN, &"
    p0.font.size = Pt(28)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_PRIMARY
    
    p1 = tf.add_paragraph()
    p1.text = "STRATEGI DEFENSE IN DEPTH APLIKASI E-WALLET"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_CYAN
    p1.space_after = Pt(14)

    p2 = tf.add_paragraph()
    p2.text = "Studi Kasus Sistem Dompet Digital B2C & Merchant (QRIS, P2P, Payment Gateway, Biometrik & HSM)"
    p2.font.size = Pt(14)
    p2.font.color.rgb = TEXT_MUTED

    # Meta Cards at Bottom
    card_w = Inches(3.7)
    add_card(slide1, Inches(0.8), Inches(4.8), card_w, Inches(1.8), "PENYUSUN & MATA KULIAH", [
        ("Tim Pengkaji", "Kelompok Cipta dkk."),
        ("Mata Kuliah", "Topik Khusus Sistem Cerdas / Komputasi Visual"),
        ("Fokus Regulasi", "POJK 11/2022, PADG BI SPPur, UU PDP")
    ], ACCENT_EMERALD)

    add_card(slide1, Inches(4.8), Inches(4.8), card_w, Inches(1.8), "FRAMEWORK STANDAR", [
        ("Threat Modeling", "STRIDE Framework & Attack Trees"),
        ("Defense Architecture", "NIST CSF 2.0 & Zero Trust (SP 800-207)"),
        ("Standar Industri", "PCI-DSS v4.0, ISO/IEC 27001, OWASP API")
    ], ACCENT_CYAN)

    add_card(slide1, Inches(8.8), Inches(4.8), card_w, Inches(1.8), "RINGKASAN OUTPUT", [
        ("Audit Ancaman", "Malware Overlay, OTP Phishing, API BOLA"),
        ("3 Pilar Pertahanan", "Teknologi, Tindakan (People), Proses"),
        ("Ketahanan Data", "Skema Backup 3-2-1 & Immutable WORM")
    ], ACCENT_AMBER)

    add_notes(slide1, 
        "Selamat pagi/siang kepada Bapak/Ibu Dosen Pengampu dan Rekan-rekan sekalian.\n"
        "Presentasi ini disusun oleh Kelompok Cipta dkk. untuk mata kuliah Topik Khusus Sistem Cerdas / Komputasi Visual. "
        "Kami membedah secara komprehensif analisis ancaman dan rancang bangun arsitektur Defense in Depth untuk aplikasi "
        "dompet digital (E-Wallet) modern. Pertahanan ini tidak hanya menjawab aspek teknis melainkan juga tata kelola operasional "
        "dan kepatuhan terhadap regulasi Bank Indonesia, OJK, dan UU Perlindungan Data Pribadi."
    )

    # =========================================================================
    # SLIDE 2: PROFIL STUDI KASUS & ARSITEKTUR SINGKAT
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_background(slide2)
    add_header(slide2, "1. PROFIL STUDI KASUS & ARSITEKTUR", 
               "Arsitektur Sistem Dompet Digital B2C & Merchant", 
               "Pemetaan Trust Boundaries, Komponen Kritis, dan Alur Finansial Inti")

    col_w = Inches(3.7)
    add_card(slide2, Inches(0.8), Inches(2.1), col_w, Inches(4.7), "Mobile Client (Android/iOS)", [
        ("Trust Boundary", "Untrusted Client Device Boundary"),
        ("Fitur Utama", "QRIS Payment, P2P Transfer, Top-up, Merchant Cashout"),
        ("Mekanisme Auth", "Biometrik (Fingerprint/FaceID), 6-Digit PIN, Dynamic OTP"),
        ("Local Storage", "Android Keystore / iOS Keychain untuk token sesi & cryptographic keys"),
        ("Risiko Kritis", "Reverse engineering, Accessibility abuse, rooting/jailbreak, hooking Frida/Xposed")
    ], ACCENT_CYAN)

    add_card(slide2, Inches(4.8), Inches(2.1), col_w, Inches(4.7), "API Gateway & Core Ledger", [
        ("Trust Boundary", "DMZ & Internal Microservices Mesh Boundary"),
        ("Edge Perimeter", "Cloud WAF, DDoS Protection, Rate Limiting & Bot Manager"),
        ("Gateway Layer", "API Gateway (OAuth 2.0 PKCE, JWT Validation, mTLS Ingress)"),
        ("Core Banking Services", "Financial Ledger Service, Settlement Engine, QRIS Switching (ASPI)"),
        ("Risiko Kritis", "Broken Object Level Auth (BOLA), Credential Stuffing, Race Conditions di balance")
    ], ACCENT_EMERALD)

    add_card(slide2, Inches(8.8), Inches(2.1), col_w, Inches(4.7), "Database Finansial & HSM/KMS", [
        ("Trust Boundary", "High-Security Zone (PCI-DSS Scoped CDE Zone)"),
        ("Hardware Security", "HSM FIPS 140-2 Level 3 (PIN encryption, PVK/CVK, Key Generation)"),
        ("Ledger Storage", "Relational ACID DB (PostgreSQL Cluster) + Double-Entry Bookkeeping"),
        ("Enkripsi Data", "Data-at-Rest (AES-256 via KMS), Data-in-Transit (TLS 1.3 mTLS)"),
        ("Risiko Kritis", "Ransomware encryption, database tampering, privileged insider threat")
    ], ACCENT_AMBER)

    add_notes(slide2,
        "Slide ini menguraikan batas kepercayaan (trust boundaries) pada ekosistem dompet digital kami.\n"
        "Di sisi kiri, Mobile Client beroperasi di lingkungan 'untrusted device' yang rentan terhadap malware dan overlay. "
        "Di lapisan tengah, API Gateway bertindak sebagai benteng perimeter yang memvalidasi setiap request sebelum menyentuh "
        "microservices core ledger. Di lapisan terdalam adalah Cardholder Data Environment (CDE) yang terisolasi ketat, "
        "di mana Hardware Security Module (HSM) bertugas mengelola kunci kriptografi dan PIN tanpa pernah mengeksposnya ke memori aplikasi."
    )

    # =========================================================================
    # SLIDE 3: THREAT LANDSCAPE FINTECH (EMPIRICAL DATA)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_background(slide3)
    add_header(slide3, "2. THREAT LANDSCAPE FINTECH 2024-2026", 
               "Lanskap Ancaman Finansial Global & Nasional", 
               "Fakta Empiris dari Verizon DBIR, BPSDM Kominfo/BSSN, dan Standar OWASP")

    add_card(slide3, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.2), "Verizon DBIR: Financial Sector Insights", [
        ("Motivasi Finansial", "86%+ pelanggaran pada sektor keuangan murni bermotif keuntungan finansial langsung."),
        ("Human Element", "68% insiden melibatkan faktor manusia melalui credential theft dan social engineering."),
        ("Vektor Dominan", "Web Application Attacks & Desktop/Mobile Sharing menempati 70% volume insiden.")
    ], ACCENT_CYAN)

    add_card(slide3, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.2), "BPSDM Kominfo & BSSN Report", [
        ("Anomali Trafik", "Peningkatan 140%+ serangan malware berbasis Android APK menyasar perbankan Indonesia."),
        ("Modus Kurir & Undangan", "Penyalahgunaan izin Accessibility Service untuk mencuri SMS OTP perbankan."),
        ("Regulasi Siber", "Peringatan kepatuhan terhadap ketahanan data nasabah sesuai UU PDP No. 27/2022.")
    ], ACCENT_ROSE)

    add_card(slide3, Inches(0.8), Inches(4.5), Inches(5.7), Inches(2.3), "OWASP API Security Top 10", [
        ("API1:2023 - BOLA", "Broken Object Level Authorization merupakan ancaman nomor 1 pada open banking."),
        ("API2:2023 - Broken Auth", "Kelemahan validasi token, credential stuffing, dan sesi OAuth yang tidak kedaluwarsa."),
        ("API8:2023 - Misconfiguration", "Kesalahan konfigurasi CORS, debugging endpoint terbuka, dan bypass gateway.")
    ], ACCENT_AMBER)

    add_card(slide3, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.3), "NIST CSF 2.0 & Regulasi OJK / BI", [
        ("NIST CSF 2.0 Core", "Govern, Identify, Protect, Detect, Respond, Recover diwajibkan secara berkesinambungan."),
        ("POJK 11/POJK.03/2022", "Kewajiban penerapan manajemen risiko ketahanan siber bagi penyelenggara TI keuangan."),
        ("PADG BI No. 24/7/2022", "Standar keamanan sistem pembayaran, audit pen-testing berkala, dan redundansi DRC.")
    ], ACCENT_EMERALD)

    add_notes(slide3,
        "Mengapa threat modeling ini sangat mendesak? Berdasarkan laporan Verizon DBIR terbaru, lebih dari 86% insiden di sektor "
        "finansial dimotivasi oleh keuntungan moneter cepat, dan faktor manusia menyumbang 68% kelemahan awal.\n"
        "Di Indonesia, BSSN dan Kominfo menyoroti maraknya malware APK berkedok surat tilang atau kurir paket yang memanfaatkan "
        "Accessibility Service Android untuk mem-bypass autentikasi OTP. Sementara itu, di level API, OWASP menempatkan BOLA "
        "sebagai risiko teratas. Regulasi OJK dan Bank Indonesia kini mewajibkan sanksi berat bagi kegagalan sistemik ini."
    )

    # =========================================================================
    # SLIDE 4: AUDIT VEKTOR 1 - MOBILE MALWARE / OVERLAY
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_background(slide4)
    add_header(slide4, "AUDIT VEKTOR ANCAMAN #1: MALWARE & OVERLAY", 
               "Mobile Banking Trojan & Accessibility Service Abuse", 
               "Penyusupan Trojan, Pencurian PIN/OTP, dan Background Illegal Transaction")

    add_card(slide4, Inches(0.8), Inches(2.1), Inches(7.6), Inches(4.7), "Attack Flow (Anatomi Serangan)", [
        ("Fase 1: Social Delivery", "Korban menerima file .APK manipulatif via WhatsApp/Telegram (misal: 'Undangan_Pernikahan.apk' atau 'Resi_Paket.apk')."),
        ("Fase 2: Permission Escalation", "Malware memandu korban mengaktifkan izin 'Accessibility Service' dengan alasan verifikasi sistem."),
        ("Fase 3: Overlay Attack Injection", "Saat korban membuka aplikasi dompet digital yang sah, Trojan mendeteksi package ID dan memunculkan Webview/Window palsu yang identik 100% di atas aplikasi asli."),
        ("Fase 4: Credential & OTP Harvesting", "Korban memasukkan nomor ponsel dan PIN ke dalam overlay palsu. Malware mencatat input dan menyadap SMS OTP secara real-time via Accessibility log."),
        ("Fase 5: Background Transaction", "Malware mengirim PIN & OTP ke server C2, lalu bot mengeksekusi transfer dana ilegal di background tanpa disadari korban.")
    ], ACCENT_ROSE)

    add_card(slide4, Inches(8.7), Inches(2.1), Inches(3.8), Inches(2.25), "Profil Adversary", [
        ("Aktor", "Sindikat Kriminal Siber Terorganisir"),
        ("Motivasi", "Finansial Murni (Monetisasi Cepat)"),
        ("Kapabilitas", "Advance (Evasion, Obfuscation, C2 Botnet)"),
        ("Sumber Daya", "Malware-as-a-Service (MaaS) & Rekening Penampung (Mule Accounts)")
    ], ACCENT_AMBER)

    add_card(slide4, Inches(8.7), Inches(4.55), Inches(3.8), Inches(2.25), "Dampak Bisnis & Finansial", [
        ("CIA Triad", "Integrity (transaksi ilegal) & Confidentiality (kebocoran PIN)"),
        ("Kerugian Finansial", "Direct Loss saldo nasabah & biaya reimbursement fraud"),
        ("Dampak Reputasi", "Viral loss-of-trust, rating app anjlok di Playstore"),
        ("Sanksi Regulasi", "Audit investigasi OJK & sanksi denda PADG BI")
    ], ACCENT_CYAN)

    add_notes(slide4,
        "Vektor pertama adalah ancaman mobile paling mematikan saat ini: Banking Trojan dengan Overlay Attack.\n"
        "Alurnya: Pengguna dikelabui untuk menginstal APK kurir atau undangan palsu. Begitu Accessibility Service aktif, "
        "malware dapat membaca seluruh isi layar dan bahkan melakukan klik otomatis. Saat pengguna membuka e-wallet, Trojan "
        "menggambar overlay palsu untuk mencuri PIN dan menyadap SMS OTP. Korban tidak sadar bahwa saldonya sedang ditransfer "
        "ke rekening 'mule' di latar belakang. Dari sudut pandang arsitektur, aplikasi e-wallet harus memiliki mekanisme self-defense "
        "yang mampu mendeteksi overlay dan memblokir eksekusi jika Accessibility Service aktif pada aplikasi yang tidak dikenal."
    )

    # =========================================================================
    # SLIDE 5: AUDIT VEKTOR 2 - PHISHING / SOCIAL ENGINEERING (ATO)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_background(slide5)
    add_header(slide5, "AUDIT VEKTOR ANCAMAN #2: REKAYASA SOSIAL & ATO", 
               "OTP Harvesting & SIM Swap / Vishing Customer Service", 
               "Eksploitasi Human Vulnerability Menuju Pengambilalihan Akun Penuh (ATO)")

    add_card(slide5, Inches(0.8), Inches(2.1), Inches(7.6), Inches(4.7), "Attack Flow (Anatomi Serangan)", [
        ("Fase 1: Profiling & OSINT", "Penyerang mengumpulkan nomor telepon korban dari database bocor atau media sosial."),
        ("Fase 2: Impersonasi & Vishing", "Penyerang menelepon korban menggunakan VoIP Caller ID Spoofing mengatasnamakan 'Divisi Fraud / CS Resmi' e-wallet."),
        ("Fase 3: Cognitive Overload & Urgensi", "Penyerang menciptakan rasa panik: 'Ada transaksi mencurigakan Rp 5.000.000 di akun Anda! Untuk membatalkannya, sebutkan kode pembatalan yang baru saja dikirim via SMS!'"),
        ("Fase 4: Real-time Device Provisioning", "Secara simultan, penyerang mencoba login di perangkat baru. Kode yang dikirim adalah OTP login perangkat baru."),
        ("Fase 5: SIM Swap Alternative", "Jika vishing gagal, penyerang mendatangi gerai operator menggunakan KTP palsu untuk menduplikasi SIM card (SIM Swap) demi membajak seluruh jalur OTP SMS."),
        ("Fase 6: Account Takeover (ATO)", "Penyerang berhasil login di perangkat baru, mereset PIN, dan menguras saldo serta limit Paylater.")
    ], ACCENT_ROSE)

    add_card(slide5, Inches(8.7), Inches(2.1), Inches(3.8), Inches(2.25), "Profil Adversary", [
        ("Aktor", "Social Engineering Fraud Rings"),
        ("Motivasi", "Finansial Langsung (Pencairan Saldo/Kredit)"),
        ("Kapabilitas", "Teknis Sedang, Keahlian Psikologis Manipulasi Tinggi"),
        ("Sumber Daya", "Spoofing Gateway, KTP Palsu, Tim Call Center Ilegal")
    ], ACCENT_AMBER)

    add_card(slide5, Inches(8.7), Inches(4.55), Inches(3.8), Inches(2.25), "Dampak Bisnis & Finansial", [
        ("CIA Triad", "Confidentiality (identitas akun) & Availability (korban terkunci)"),
        ("Kerugian Finansial", "Fraud chargeback, sengketa transaksi kredit paylater"),
        ("Dampak Hukum", "Gugatan konsumen dan pelanggaran UU PDP No. 27/2022"),
        ("Operasional", "Lonjakan tiket keluhan nasabah di Contact Center")
    ], ACCENT_CYAN)

    add_notes(slide5,
        "Vektor kedua mengeksploitasi titik terlemah dalam rantai keamanan: manusia. Rekayasa sosial melalui Vishing dan OTP Harvesting "
        "tidak memerlukan exploit software zero-day. Penyerang memanfaatkan rasa panik korban dengan berpura-pura menjadi staf keamanan "
        "resmi yang hendak membatalkan transaksi palsu. Korban dengan sukarela membacakan OTP yang sebenarnya adalah token otorisasi "
        "login di perangkat penyerang. Di samping itu, serangan SIM Swap memungkinkan penyerang mencegat OTP secara pasif. "
        "Arsitektur kami harus mengeliminasi ketergantungan pada SMS OTP semata dan beralih ke Device Binding kriptografis."
    )

    # =========================================================================
    # SLIDE 6: AUDIT VEKTOR 3 - API VULNERABILITY (BOLA / IDOR)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_background(slide6)
    add_header(slide6, "AUDIT VEKTOR ANCAMAN #3: API BOLA / IDOR", 
               "Broken Object Level Authorization pada Transfer Endpoint", 
               "Eksploitasi Celah Otorisasi Tingkat Objek untuk Memotong Saldo Pengguna Lain")

    add_card(slide6, Inches(0.8), Inches(2.1), Inches(7.6), Inches(4.7), "Attack Flow (Anatomi Serangan)", [
        ("Fase 1: API Interception & Mapping", "Penyerang menggunakan HTTP Proxy (Burp Suite) pada perangkat uji untuk memetakan endpoint transfer: POST /api/v1/wallet/transfer."),
        ("Fase 2: Parameter Inspection", "Payload request dianalisis: {'source_wallet_id': 'WAL-10029', 'target_wallet_id': 'WAL-99001', 'amount': 2500000} dengan Bearer JWT token milik penyerang."),
        ("Fase 3: Object ID Tampering", "Penyerang mengganti nilai 'source_wallet_id' menjadi dompet milik korban ('WAL-10001'), namun tetap mengirimkan Bearer JWT token milik akun penyerang."),
        ("Fase 4: Authorization Logic Failure", "API Gateway memvalidasi bahwa JWT valid dan belum kedaluwarsa (Autentikasi Berhasil). Namun, service backend tidak memeriksa apakah subjek JWT adalah pemilik sah dari 'WAL-10001' (Otorisasi Objek Gagal)."),
        ("Fase 5: Unauthorized Transfer", "Sistem core ledger memproses mutasi: Saldo dompet korban terpotong Rp 2.500.000 dan masuk ke akun penyerang secara sah di mata ledger.")
    ], ACCENT_ROSE)

    add_card(slide6, Inches(8.7), Inches(2.1), Inches(3.8), Inches(2.25), "Profil Adversary", [
        ("Aktor", "Malicious User / Rouge FinTech Tester"),
        ("Motivasi", "Finansial Sistemik & Eksploitasi Saldo"),
        ("Kapabilitas", "Tinggi (Web/API Reverse Engineering, Fuzzing)"),
        ("Sumber Daya", "Proxy Tools, Custom Python Exploit Scripts")
    ], ACCENT_AMBER)

    add_card(slide6, Inches(8.7), Inches(4.55), Inches(3.8), Inches(2.25), "Dampak Bisnis & Finansial", [
        ("CIA Triad", "Integrity (manipulasi saldo mutasi tanpa otorisasi)"),
        ("Dampak Finansial", "Pencurian dana langsung lintas akun secara masif & instan"),
        ("Kepatuhan PCI-DSS", "Pelanggaran serius PCI-DSS Req 6.5.8 (Access Control)"),
        ("Regulasi BI", "Pemberhentian sementara lisensi Payment Gateway oleh BI")
    ], ACCENT_CYAN)

    add_notes(slide6,
        "Vektor ketiga berada di layer backend: Broken Object Level Authorization (BOLA), yang merupakan ancaman nomor 1 dalam "
        "OWASP API Security Top 10. Bayangkan seorang pengguna resmi mengubah ID dompet asal di payload HTTP transfer dari akun miliknya "
        "ke akun korban. Banyak sistem fintech melakukan kesalahan fatal: API Gateway memeriksa apakah token JWT valid (autentikasi), "
        "tetapi tidak ada pengecekan di level kode apakah subjek pada JWT berhak melakukan mutasi atas objek dompet target (otorisasi). "
        "Akibatnya, penyerang dapat menguras saldo nasabah manapun hanya dengan menebak atau melakukan enumerasi ID dompet."
    )

    # =========================================================================
    # SLIDE 7: DEFENSE IN DEPTH ARCHITECTURE - 3 PILAR
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_background(slide7)
    add_header(slide7, "3. RANCANG BANGUN DEFENSE IN DEPTH", 
               "Arsitektur Pertahanan Berlapis (3 Pilar Holistik)", 
               "Sinergi Komprehensif Antara Teknologi Mutakhir, Kesiapan Insani, dan Tata Kelola Proses")

    col_w = Inches(3.7)
    add_card(slide7, Inches(0.8), Inches(2.1), col_w, Inches(4.7), "Pilar 1: TEKNOLOGI", [
        ("Fokus Utama", "Proteksi Teknis Otomatis & Kriptografi"),
        ("Mobile Client", "RASP (Anti-Hook, Anti-Overlay), Cert Pinning, Hardware Key Attestation"),
        ("Edge & API", "WAF dengan Bot ML, API Gateway OAuth 2.0 PKCE, mTLS, Rate Limiting"),
        ("Core Ledger", "Open Policy Agent (OPA) untuk BOLA, HSM FIPS 140-2 Level 3"),
        ("Monitoring", "SIEM/XDR 24/7 terintegrasi Real-time Behavioral Fraud Detection System")
    ], ACCENT_CYAN)

    add_card(slide7, Inches(4.8), Inches(2.1), col_w, Inches(4.7), "Pilar 2: TINDAKAN (PEOPLE)", [
        ("Fokus Utama", "Human Firewall & Operasional Tangguh"),
        ("Nasabah", "Edukasi 'Jaga OTP', In-App Warning deteksi remote tools (AnyDesk), Push Verify"),
        ("Internal Staf", "Security Awareness Training berkala, simulasi phishing adaptif"),
        ("Operasional IT", "Zero Trust Architecture, Least Privilege Access, Hardware FIDO2 MFA"),
        ("Security Teams", "Latihan rutin Red Team vs Blue Team (Purple Teaming exercises)")
    ], ACCENT_EMERALD)

    add_card(slide7, Inches(8.8), Inches(2.1), col_w, Inches(4.7), "Pilar 3: PROSES & TATA KELOLA", [
        ("Fokus Utama", "Siklus Hidup Aman, Standar & Ketahanan"),
        ("Secure SDLC", "Threat Modeling STRIDE berkala, integrasi SAST/DAST/SCA di CI/CD"),
        ("Incident Response", "IRP Finansial berbasis ISO 27035 & NIST SP 800-61 (SLA < 15 Menit)"),
        ("Audit Kepatuhan", "PCI-DSS v4.0, ISO/IEC 27001:2022, POJK 11/2022, PADG BI, UU PDP"),
        ("Resiliensi Data", "Skema Backup 3-2-1 dengan Salinan Immutable WORM Storage")
    ], ACCENT_AMBER)

    add_notes(slide7,
        "Untuk memitigasi ketiga vektor ancaman sebelumnya secara tuntas, kita tidak bisa hanya mengandalkan satu solusi teknologi. "
        "Kami merancang arsitektur Defense in Depth yang bertumpu pada Tiga Pilar: Teknologi, Tindakan (People), dan Proses.\n"
        "Pilar Teknologi memastikan tidak ada celah di client, API, maupun data storage. Pilar Tindakan memperkuat faktor manusia, "
        "baik nasabah maupun karyawan internal melalui Zero Trust. Pilar Proses menjamin bahwa siklus pengembangan sistem "
        "memiliki standar kepatuhan regulasi yang ketat dan memiliki kesiapan tanggap darurat serta pemulihan data bencana."
    )

    # =========================================================================
    # SLIDE 8: PILAR TEKNOLOGI - DETAILED MITIGATION
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_background(slide8)
    add_header(slide8, "PILAR 1: TEKNOLOGI - DETAIL IMPLEMENTASI", 
               "Proteksi Berlapis dari Mobile Client ke Core Banking", 
               "Mitigasi Spesifik Terhadap Malware Overlay, Serangan Man-in-the-Middle, dan BOLA")

    add_card(slide8, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.2), "Mobile Client Shield (Anti-Trojan)", [
        ("RASP Engine", "Mendeteksi & memblokir overlay injection (Window flag SECURE), mendeteksi Frida/Xposed hooks."),
        ("Accessibility Guard", "Memutus sesi jika ada aplikasi pihak ketiga mencurigakan mengaktifkan Accessibility."),
        ("Certificate Pinning", "HPKP / Network Security Config untuk mencegah dekripsi trafik via proxy/Burp."),
        ("Device Binding", "Kunci sesi diikat ke hardware KeyStore/Secure Enclave perangkat nasabah.")
    ], ACCENT_CYAN)

    add_card(slide8, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.2), "API Gateway & Fine-Grained Authorization", [
        ("Mitigasi BOLA (OPA)", "Open Policy Agent mengevaluasi: JWT.sub == Wallet.owner_id pada setiap request transfer."),
        ("Strict Rate Limiting", "Token Bucket algorithm: 10 req/menit per user ID untuk mencegah credential stuffing."),
        ("mTLS & OAuth 2.0 PKCE", "Komunikasi antar microservices terenkripsi penuh dengan mutual TLS autentikasi."),
        ("Schema Validation", "JSON Schema enforcement memblokir manipulasi parameter tak dikenal.")
    ], ACCENT_EMERALD)

    add_card(slide8, Inches(0.8), Inches(4.5), Inches(5.7), Inches(2.3), "HSM & Perlindungan Data Kritis", [
        ("Hardware Security Module", "HSM FIPS 140-2 Level 3 memproses enkripsi PIN, generate symmetric keys, dan PIN verification."),
        ("Envelope Encryption", "Data balance dan histori transaksi dienkripsi AES-256 GCM di database level."),
        ("Tokenization Engine", "PAN kartu debit/kredit diganti format-preserving token; data mentah tidak disimpan di DB aplikasi.")
    ], ACCENT_AMBER)

    add_card(slide8, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.3), "SIEM / XDR & Real-Time Behavioral FDS", [
        ("Behavioral Profiling", "FDS Machine Learning menganalisis profil transaksi (IP, velocity, jenis merchant, geolokasi)."),
        ("Risk-Based Stepped Auth", "Jika ada anomali (misal login dari IP baru), transaksi otomatis meminta re-autentikasi biometrik."),
        ("SIEM Threat Hunting", "Koleksi log terpusat dengan deteksi IOC (Indicators of Compromise) secara otomatis.")
    ], ACCENT_ROSE)

    add_notes(slide8,
        "Mari kita bedah implementasi pilar Teknologi secara mendalam.\n"
        "Pertama, di Mobile Client, kami mengimplementasikan RASP yang langsung mematikan aplikasi jika mendeteksi screen overlay, "
        "hooking Frida, atau root environment. Flag 'FLAG_SECURE' memastikan layar tidak dapat direkam oleh malware.\n"
        "Kedua, untuk menumpas BOLA, kami menanamkan policy engine (Open Policy Agent) di API Gateway yang secara ketat "
        "mencocokkan JWT subjek dengan ID dompet asal pada database sebelum request menyentuh controller.\n"
        "Ketiga, di core backend, operasi PIN wajib melewati Hardware Security Module (HSM), dan FDS berbasis ML secara aktif "
        "mengevaluasi kecepatan transaksi (velocity checks) untuk memblokir penarikan dana massal."
    )

    # =========================================================================
    # SLIDE 9: PILAR TINDAKAN (PEOPLE & OPERATIONAL)
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_background(slide9)
    add_header(slide9, "PILAR 2: TINDAKAN (PEOPLE & OPERASIONAL)", 
               "Membangun Human Firewall & Tata Kelola Operasional", 
               "Edukasi Nasabah, Pelatihan Internal, dan Implementasi Zero Trust Security")

    col_w = Inches(3.7)
    add_card(slide9, Inches(0.8), Inches(2.1), col_w, Inches(4.7), "Edukasi & Perlindungan Nasabah", [
        ("Kampanye 'Jaga OTP & PIN'", "Edukasi berkelanjutan bahwa CS resmi TIDAK PERNAH meminta OTP/PIN dalam kondisi apapun."),
        ("In-App Security Prompt", "Tampilan peringatan dinamis saat nasabah menerima OTP bertuliskan 'JANGAN BERIKAN KODE INI KEPADA SIAPAPUN TERMASUK PIHAK E-WALLET'."),
        ("Remote Access Detection", "Aplikasi memperingatkan nasabah jika aplikasi remote desktop (AnyDesk/TeamViewer) sedang berjalan di latar belakang."),
        ("Out-of-Band Notification", "Push notification verifikasi instan ke perangkat primer saat ada upaya login dari perangkat baru.")
    ], ACCENT_CYAN)

    add_card(slide9, Inches(4.8), Inches(2.1), col_w, Inches(4.7), "Budaya Keamanan Internal Staf", [
        ("Security Awareness Rutin", "Pelatihan wajib bulanan mengenai taktik rekayasa sosial, spear phishing, dan kebersihan siber."),
        ("Simulated Phishing Attacks", "Pengujian phishing internal berkala untuk mengidentifikasi staf yang rentan terkena manipulasi."),
        ("Customer Service Safeguards", "Staf CS tidak memiliki akses melihat data sensitif (Data Masking penuh pada nomor kartu, saldo, dan log OTP)."),
        ("Dual-Control Authorization", "Tindakan perubahan konfigurasi atau unblock akun wajib memerlukan otorisasi 2 personel (Maker-Checker).")
    ], ACCENT_EMERALD)

    add_card(slide9, Inches(8.8), Inches(2.1), col_w, Inches(4.7), "Operasional Zero Trust & Pen-testing", [
        ("Zero Trust Network Access", "Tidak ada akses langsung ke database produksi; seluruh akses melalui bastion host dengan perekaman sesi penuh."),
        ("Hardware-Based MFA", "Akses administratif engineer wajib menggunakan FIDO2 hardware security key (YubiKey)."),
        ("Red Team vs Blue Team", "Simulasi serangan siber terencana setiap kuartal (Purple Team) untuk menguji kesiapan FDS dan respons SOC."),
        ("Bug Bounty Program", "Program vulnerability disclosure bertanggung jawab dengan peretas etis untuk audit berkelanjutan.")
    ], ACCENT_AMBER)

    add_notes(slide9,
        "Pilar kedua adalah Tindakan (People & Operational). Teknologi tercanggih akan runtuh jika nasabah atau staf internal "
        "berhasil dimanipulasi oleh rekayasa sosial.\n"
        "Untuk nasabah, kami menyematkan peringatan kontekstual di dalam aplikasi saat OTP dikirimkan dan mendeteksi software remote access.\n"
        "Untuk internal perusahaan, kami menerapkan prinsip Maker-Checker: tidak ada satu staf pun yang bisa membuka blokir rekening "
        "atau mengubah limit transaksi secara sepihak. Selain itu, staf CS hanya melihat data yang ter-masking. Akses engineer "
        "ke sistem backend diwajibkan menggunakan hardware token FIDO2 dengan prinsip Zero Trust—tidak ada yang dipercaya secara default."
    )

    # =========================================================================
    # SLIDE 10: PILAR PROSES & TATA KELOLA (GOVERNANCE & IRP)
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_background(slide10)
    add_header(slide10, "PILAR 3: PROSES & TATA KELOLA REGULATORI", 
               "Secure SDLC, Incident Response Plan, & Kepatuhan", 
               "Integrasi Standar ISO/IEC 27001, PCI-DSS v4.0, POJK 11/2022, dan PADG BI")

    add_card(slide10, Inches(0.8), Inches(2.1), Inches(5.7), Inches(2.2), "Secure SDLC (S-SDLC) & DevSecOps", [
        ("Threat Modeling STRIDE", "Kewajiban analisis ancaman pada fase desain arsitektur sebelum coding dimulai."),
        ("Automated SAST & SCA", "Pipeline CI/CD otomatis memblokir build jika ada high/critical vulnerability pada kode atau library."),
        ("Pre-Release Pen-testing", "Penetration test independen setiap ada rilis mayor fitur transfer/payment.")
    ], ACCENT_CYAN)

    add_card(slide10, Inches(6.8), Inches(2.1), Inches(5.7), Inches(2.2), "Incident Response Plan (IRP) Finansial", [
        ("SLA Eskalasi Ketat", "Deteksi fraud -> isolasi akun penampung dalam < 15 menit; pemblokiran API key compromised < 5 menit."),
        ("Alur Komunikasi", "CS First Line -> Fraud Investigation Unit -> Security Incident Response Team (SIRT) -> Legal & CISO."),
        ("Pelaporan Regulator", "Notifikasi resmi ke Bank Indonesia, OJK, dan BSSN maksimal 1x24 jam sesuai ketentuan hukum.")
    ], ACCENT_ROSE)

    add_card(slide10, Inches(0.8), Inches(4.5), Inches(5.7), Inches(2.3), "Kepatuhan PCI-DSS v4.0 & ISO 27001", [
        ("PCI-DSS v4.0 Compliance", "Segmentasi Cardholder Data Environment (CDE), audit logging tamper-proof (Req 10), dan enkripsi transmisi."),
        ("ISO/IEC 27001:2022", "Audit Information Security Management System (ISMS) tahunan dan evaluasi manajemen risiko menyeluruh.")
    ], ACCENT_EMERALD)

    add_card(slide10, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.3), "Regulasi Perbankan & Privasi Data", [
        ("POJK No. 11/POJK.03/2022", "Penyelenggaraan teknologi informasi bank/fintech, disaster recovery test minimal 1 kali per tahun."),
        ("PADG BI No. 24/7/PADG/2022", "Ketahanan dan keamanan sistem pembayaran (SPPur), interoperabilitas QRIS aman."),
        ("UU PDP No. 27/2022", "Akuntabilitas pengendali data finansial dan kewajiban enkripsi data pribadi nasabah.")
    ], ACCENT_AMBER)

    add_notes(slide10,
        "Pilar ketiga adalah Proses dan Tata Kelola. Keamanan harus menjadi budaya siklus hidup sistem melalui DevSecOps.\n"
        "Kami menerapkan Threat Modeling berbasis STRIDE di tahap desain, diikuti pemindaian SAST otomatis pada pipeline CI/CD. "
        "Jika terjadi insiden fraud finansial, Incident Response Plan (IRP) kami memiliki SLA kritis: rekening penampung harus dibekukan "
        "dalam waktu kurang dari 15 menit untuk mencegah penarikan uang tunai.\n"
        "Secara hukum dan regulasi, arsitektur kami patuh penuh terhadap PCI-DSS v4.0, ISO 27001, POJK No. 11/2022, "
        "PADG Bank Indonesia mengenai Penyelenggaraan Sistem Pembayaran, serta UU Perlindungan Data Pribadi."
    )

    # =========================================================================
    # SLIDE 11: SKEMA BACKUP 3-2-1 & DATA RESILIENCE
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_background(slide11)
    add_header(slide11, "KETAHANAN DATA: SKEMA BACKUP 3-2-1", 
               "Strategi Pemulihan Bencana & Proteksi Ransomware", 
               "Menjamin Integritas Ledger Finansial Tanpa Kehilangan Data Transaksi")

    col_w = Inches(3.7)
    add_card(slide11, Inches(0.8), Inches(2.1), col_w, Inches(3.3), "Prinsip '3' : TIGA SALINAN DATA", [
        ("Salinan 1 (Primary)", "Database Produksi Aktif (High Availability Multi-AZ PostgreSQL Cluster)."),
        ("Salinan 2 (Local Replica)", "Continuous Snapshot Cadangan Lokal yang disimpan secara terpisah di storage on-premise."),
        ("Salinan 3 (Remote Backup)", "Cadangan arsip terenkripsi yang direplikasi secara asinkron ke fasilitas sekunder.")
    ], ACCENT_CYAN)

    add_card(slide11, Inches(4.8), Inches(2.1), col_w, Inches(3.3), "Prinsip '2' : DUA MEDIA BERBEDA", [
        ("Media 1: SSD SAN On-Prem", "Storage Enterprise SAN lokal dengan latensi ultra-rendah untuk pemulihan RTO instan."),
        ("Media 2: Cloud Object Storage", "Penyimpanan berbasis cloud terpisah (misal: S3 / Cloud Storage) dengan arsitektur software berbeda."),
        ("Tujuan Redudansi", "Menghindari kegagalan vendor hardware tunggal (Common-Mode Failure).")
    ], ACCENT_EMERALD)

    add_card(slide11, Inches(8.8), Inches(2.1), col_w, Inches(3.3), "Prinsip '1' : SATU SALINAN IMMUTABLE", [
        ("Off-Site & Air-Gapped", "Disimpan di Disaster Recovery Center (DRC) geografis berbeda (> 30 km dari DC Utama)."),
        ("Immutable WORM Storage", "Write-Once-Read-Many storage: Data terkunci secara kriptografis dan TIDAK BISA dihapus/dienkripsi ulang oleh ransomware."),
        ("Air-Gap Logis", "Akses jaringan diputus total kecuali selama jendela replikasi batch terverifikasi.")
    ], ACCENT_AMBER)

    # Bottom Target Metric Card
    bottom_w = Inches(11.7)
    add_card(slide11, Inches(0.8), Inches(5.6), bottom_w, Inches(1.35), "Target Metrik Disaster Recovery (DR) & Business Continuity", [
        ("Recovery Point Objective (RPO) < 5 Menit", "Maksimal selisih kehilangan data transaksi finansial tidak melebihi 5 menit terakhir."),
        ("Recovery Time Objective (RTO) < 60 Menit", "Sistem core banking dan e-wallet wajib pulih dan melayani transaksi penuh di DRC dalam 1 jam pasca bencana fatal."),
        ("Pengujian Rutin", "Disaster Recovery Drill (simulasi bencana & uji restore data) wajib dilaksanakan minimal 2 kali setahun sesuai audit regulator.")
    ], ACCENT_ROSE, CARD_ALT_BG)

    add_notes(slide11,
        "Ketahanan data adalah garis pertahanan terakhir. Bayangkan skenario terburuk: ransomware melumpuhkan data center utama.\n"
        "Kami menerapkan standar emas Skema Backup 3-2-1: 3 salinan data transaksi finansial, disimpan pada 2 media teknologi berbeda "
        "(SSD SAN lokal dan Cloud Object Storage), dan minimal 1 salinan disimpan off-site di DRC dengan proteksi Immutable WORM "
        "(Write Once, Read Many). Artinya, sekalipun ransomware memiliki hak akses administrator tertinggi, salinan WORM tersebut "
        "tidak dapat diubah, dienkripsi, maupun dihapus.\n"
        "Dengan skema ini, kami menetapkan target RPO kurang dari 5 menit dan RTO kurang dari 60 menit untuk failover sistem."
    )

    # =========================================================================
    # SLIDE 12: KESIMPULAN & REFERENSI STANDAR IEEE
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_background(slide12)
    add_header(slide12, "KESIMPULAN & DAFTAR REFERENSI", 
               "Ringkasan Eksekutif & Referensi Standar Industri", 
               "Daftar Pustaka Akademis & Standar Keamanan Finansial (Format IEEE)")

    add_card(slide12, Inches(0.8), Inches(2.1), Inches(5.7), Inches(4.7), "Kesimpulan & Rekomendasi Eksekutif", [
        ("Pertahanan Holistik", "Keamanan dompet digital tidak dapat mengandalkan solusi tunggal; ketiga pilar (Teknologi, Tindakan, Proses) harus saling mengunci."),
        ("Prioritas Quick Wins", "1. Terapkan RASP dan Accessibility Guard di Mobile Client untuk menekan penipuan trojan overlay."),
        ("Prioritas Arsitektur", "2. Integrasikan Open Policy Agent (OPA) pada API Gateway untuk mengeliminasi celah BOLA/IDOR."),
        ("Kesiapan Resiliensi", "3. Lakukan simulasi berkala pemulihan backup WORM 3-2-1 guna memastikan zero data loss pada kondisi darurat."),
        ("Kepercayaan Nasabah", "Kepercayaan nasabah adalah aset terbesar fintech; kepatuhan regulasi OJK & BI adalah pembeda kompetitif utama.")
    ], ACCENT_CYAN)

    add_card(slide12, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.7), "Daftar Referensi Standar (Format IEEE)", [
        ("[1]", "Verizon, '2024 Data Breach Investigations Report (DBIR),' Verizon Enterprise Solutions, Tech. Rep., 2024."),
        ("[2]", "BPSDM Kominfo & BSSN, 'Lanskap Ancaman Siber Sektor Keuangan Indonesia,' Badan Siber dan Sandi Negara, Jakarta, Laporan Tahunan, 2023/2024."),
        ("[3]", "OWASP Foundation, 'OWASP API Security Top 10 2023,' Open Web Application Security Project, Dec. 2023. [Online]. Available: https://owasp.org/API-Security/"),
        ("[4]", "National Institute of Standards and Technology (NIST), 'The NIST Cybersecurity Framework (CSF) 2.0,' NIST CSWP 29, Feb. 2024."),
        ("[5]", "Otoritas Jasa Keuangan, 'Penyelenggaraan Teknologi Informasi oleh Bank Umum dan Lembaga Keuangan,' POJK No. 11/POJK.03/2022, Jakarta, 2022."),
        ("[6]", "Bank Indonesia, 'Penyelenggaraan Jasa Sistem Pembayaran (SPPur),' Peraturan Anggota Dewan Gubernur BI No. 24/7/PADG/2022, 2022."),
        ("[7]", "PCI Security Standards Council, 'Payment Card Industry Data Security Standard (PCI-DSS) v4.0.1,' PCI SSC Standard, June 2024.")
    ], ACCENT_EMERALD)

    add_notes(slide12,
        "Sebagai penutup, pertahanan siber pada aplikasi dompet digital bukanlah proyek sekali selesai, melainkan postur ketahanan "
        "yang dinamis. Dengan mengimplementasikan RASP di sisi mobile, OPA di sisi API, edukasi serta Zero Trust di sisi operasional, "
        "dan replikasi data WORM 3-2-1, kita memastikan integritas sistem pembayaran terjaga secara menyeluruh.\n"
        "Seluruh kajian ini berlandaskan standar industri IEEE, Verizon DBIR, OWASP, NIST CSF 2.0, serta regulasi Bank Indonesia dan OJK. "
        "Terima kasih atas perhatian Dewan Penguji dan hadirin sekalian. Sesi tanya jawab kami buka."
    )

    output_path = "threat_defense_fintech_presentation.pptx"
    prs.save(output_path)
    print(f"[SUCCESS] Presentation successfully generated: {output_path}")
    print(f"[INFO] Total Slides: {len(prs.slides)}")

if __name__ == "__main__":
    create_presentation()
