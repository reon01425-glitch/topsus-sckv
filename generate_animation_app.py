#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script to build the complete, interactive, presentation-ready
FinTech E-Wallet Threat Modeling & Defense in Depth Animation (index.html).

Course: Topik Khusus Sistem Cerdas / Komputasi Visual
Departemen Informatika, Universitas Diponegoro
Dosen: Guruh Aryotejo, S.Kom., M.Sc.
Kelompok 05: Cipta dkk.
"""

import json
import os
import shutil
import vectors_data

def build_app():
    print("Serializing SCENARIOS data from vectors_data.py...")
    # Convert integer keys to string keys if necessary for clean JS serialization
    scenarios_data = {str(k): v for k, v in vectors_data.SCENARIOS.items()}
    scenarios_json = json.dumps(scenarios_data, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Animasi Alur Serangan & Pertahanan FinTech E-Wallet | Kelompok 05</title>
  
  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet" />

  <style>
    :root {{
      --bg-dark: #070b14;
      --bg-surface: #0e1526;
      --bg-elevated: #151f38;
      --bg-card: rgba(18, 27, 49, 0.75);
      
      --border-subtle: #1e2c4f;
      --border-bright: #2d4175;
      
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      /* Threat Vector Theme Colors */
      --v1-color: #ef4444;
      --v1-glow: rgba(239, 68, 68, 0.25);
      --v2-color: #f59e0b;
      --v2-glow: rgba(245, 158, 11, 0.25);
      --v3a-color: #06b6d4;
      --v3a-glow: rgba(6, 182, 212, 0.25);
      --v3b-color: #a855f7;
      --v3b-glow: rgba(168, 85, 247, 0.25);
      --v3c-color: #f97316;
      --v3c-glow: rgba(249, 115, 22, 0.25);
      --v6-color: #10b981;
      --v6-glow: rgba(16, 185, 129, 0.25);
      
      --accent-color: var(--v1-color);
      --accent-glow: var(--v1-glow);

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --shadow-elevation: 0 12px 32px -8px rgba(0, 0, 0, 0.65);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: radial-gradient(circle at 10% 10%, #151b38 0%, transparent 40%),
                  radial-gradient(circle at 90% 90%, #0d2238 0%, transparent 40%),
                  var(--bg-dark);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
      overflow-x: hidden;
    }}

    /* Container */
    .app-container {{
      width: 100%;
      max-width: 1540px;
      margin: 0 auto;
      padding: 12px 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex: 1;
    }}

    /* HEADER */
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 12px 20px;
      box-shadow: var(--shadow-elevation);
      flex-wrap: wrap;
    }}

    .header-brand {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand-logo-pill {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #1e3a8a, #0284c7);
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      color: #fff;
      font-weight: 800;
      font-size: 0.65rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
    }}

    .brand-titles h1 {{
      font-size: clamp(1rem, 1.6vw, 1.25rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-titles p {{
      font-size: 0.76rem;
      color: var(--text-muted);
      margin-top: 1px;
    }}

    .header-toolbar {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .btn-tool {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 20px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }}

    .btn-tool:hover {{
      color: #fff;
      border-color: var(--border-bright);
      background: #1c2a4a;
    }}

    .btn-tool.active {{
      background: rgba(56, 189, 248, 0.15);
      border-color: #38bdf8;
      color: #38bdf8;
    }}

    .speed-select {{
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      padding: 5px 10px;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      outline: none;
    }}
    .speed-select:hover {{
      border-color: var(--border-bright);
      color: #fff;
    }}

    /* VECTOR SWITCHER TABS */
    .vector-navigation {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 8px;
    }}

    .v-tab-btn {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 14px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      text-align: left;
      position: relative;
      overflow: hidden;
    }}

    .v-tab-btn::before {{
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: transparent;
      transition: background 0.2s;
    }}

    .v-tab-btn:hover {{
      background: var(--bg-elevated);
      color: #fff;
      transform: translateY(-1px);
      border-color: var(--border-bright);
    }}

    .v-tab-btn.active {{
      background: var(--bg-elevated);
      color: #fff;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.4);
      border-color: currentColor;
    }}

    .v-tab-btn[data-vec="1"].active {{ color: var(--v1-color); border-color: var(--v1-color); }}
    .v-tab-btn[data-vec="1"].active::before {{ background: var(--v1-color); }}
    
    .v-tab-btn[data-vec="2"].active {{ color: var(--v2-color); border-color: var(--v2-color); }}
    .v-tab-btn[data-vec="2"].active::before {{ background: var(--v2-color); }}
    
    .v-tab-btn[data-vec="3"].active {{ color: var(--v3a-color); border-color: var(--v3a-color); }}
    .v-tab-btn[data-vec="3"].active::before {{ background: var(--v3a-color); }}
    
    .v-tab-btn[data-vec="4"].active {{ color: var(--v3b-color); border-color: var(--v3b-color); }}
    .v-tab-btn[data-vec="4"].active::before {{ background: var(--v3b-color); }}
    
    .v-tab-btn[data-vec="5"].active {{ color: var(--v3c-color); border-color: var(--v3c-color); }}
    .v-tab-btn[data-vec="5"].active::before {{ background: var(--v3c-color); }}
    
    .v-tab-btn[data-vec="6"].active {{ color: var(--v6-color); border-color: var(--v6-color); }}
    .v-tab-btn[data-vec="6"].active::before {{ background: var(--v6-color); }}

    .v-tab-icon {{
      font-size: 1.1rem;
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .v-tab-info {{
      display: flex;
      flex-direction: column;
      min-width: 0;
    }}

    .v-tab-label {{
      font-size: 0.79rem;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .v-tab-sub {{
      font-size: 0.68rem;
      color: var(--text-dim);
    }}
    .v-tab-btn.active .v-tab-sub {{
      color: var(--text-muted);
    }}

    /* MAIN STAGE WORKSPACE (3-COLUMN LAYOUT) */
    .stage-layout {{
      display: grid;
      grid-template-columns: 290px 1fr 370px;
      gap: 12px;
      align-items: stretch;
    }}

    @media (max-width: 1200px) {{
      .stage-layout {{
        grid-template-columns: 260px 1fr;
      }}
      .panel-detail {{
        grid-column: 1 / -1;
      }}
    }}

    @media (max-width: 780px) {{
      .stage-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    /* CARDS & PANELS */
    .panel-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 14px;
      box-shadow: var(--shadow-elevation);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    /* LEFT: STEP TIMELINE LIST */
    .panel-timeline {{
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .panel-header-section {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .panel-tag {{
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.07em;
      text-transform: uppercase;
      color: var(--text-muted);
    }}

    .vector-badge-pill {{
      font-size: 0.65rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
    }}

    .scenario-overview-box {{
      font-size: 0.77rem;
      color: var(--text-muted);
      background: rgba(0, 0, 0, 0.25);
      border-left: 3px solid var(--accent-color);
      padding: 8px 10px;
      border-radius: 4px;
      line-height: 1.4;
    }}

    .steps-list-container {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      overflow-y: auto;
      max-height: 520px;
      padding-right: 4px;
    }}

    .steps-list-container::-webkit-scrollbar {{
      width: 4px;
    }}
    .steps-list-container::-webkit-scrollbar-thumb {{
      background: var(--border-bright);
      border-radius: 4px;
    }}

    .step-item-btn {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 9px 12px;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: left;
    }}

    .step-item-btn:hover {{
      background: var(--bg-elevated);
      color: #fff;
      border-color: var(--border-bright);
    }}

    .step-item-btn.active {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--accent-color);
      color: #fff;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }}

    .step-idx-num {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      font-size: 0.72rem;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 1px;
    }}

    .step-item-btn.active .step-idx-num {{
      background: var(--accent-color);
      color: #fff;
    }}

    .step-item-content {{
      display: flex;
      flex-direction: column;
      gap: 2px;
      min-width: 0;
    }}

    .step-item-title {{
      font-size: 0.77rem;
      font-weight: 600;
      line-height: 1.3;
      color: var(--text-main);
    }}

    .step-item-status {{
      font-size: 0.65rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .step-item-status.warn {{ color: #fbbf24; }}
    .step-item-status.bad {{ color: #f87171; }}
    .step-item-status.ok {{ color: #34d399; }}

    /* CENTER: ANIMATED SVG STAGE */
    .panel-stage {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: relative;
    }}

    .stage-top-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .stage-step-heading {{
      font-size: 1rem;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .status-badge-live {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .status-badge-live.warn {{
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fcd34d;
    }}
    .status-badge-live.bad {{
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
    }}
    .status-badge-live.ok {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
    }}

    .stage-canvas-frame {{
      flex: 1;
      min-height: 440px;
      background: #060913;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* SVG Styling & Animations */
    .svg-viewport {{
      width: 100%;
      height: 100%;
      display: block;
      max-height: 480px;
    }}

    .flow-packet {{
      stroke-dasharray: 6 6;
      animation: packetFlow 1.2s linear infinite;
    }}

    @keyframes packetFlow {{
      to {{
        stroke-dashoffset: -24;
      }}
    }}

    .pulse {{
      animation: pulseGlow 1.5s ease-in-out infinite alternate;
    }}

    @keyframes pulseGlow {{
      from {{ opacity: 0.5; }}
      to {{ opacity: 1; }}
    }}

    .shake {{
      animation: shakePhone 0.4s ease;
    }}

    @keyframes shakePhone {{
      0%, 100% {{ transform: translate(0, 0); }}
      25% {{ transform: translate(-3px, 2px); }}
      50% {{ transform: translate(3px, -2px); }}
      75% {{ transform: translate(-2px, 1px); }}
    }}

    .overlay-drop {{
      animation: dropOverlay 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    @keyframes dropOverlay {{
      0% {{ opacity: 0; transform: translateY(-30px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* RIGHT: DETAILS, TERMS & CHECKPOINT QUIZ */
    .panel-detail {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
      max-height: 600px;
      padding-right: 4px;
    }}

    .detail-section-title {{
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.07em;
      text-transform: uppercase;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .narrative-card {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      font-size: 0.82rem;
      line-height: 1.5;
      color: #e2e8f0;
    }}

    .terms-grid {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .term-row {{
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      font-size: 0.76rem;
    }}

    .term-key {{
      color: #38bdf8;
      font-weight: 700;
      margin-bottom: 2px;
    }}

    .term-val {{
      color: var(--text-muted);
      line-height: 1.35;
    }}

    .defense-box {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      font-size: 0.79rem;
      color: #d1fae5;
      line-height: 1.45;
    }}

    .defense-box strong {{
      color: #34d399;
    }}

    /* QUIZ COMPONENT */
    .quiz-card {{
      background: linear-gradient(175deg, #131b2e 0%, #0d1424 100%);
      border: 1px solid #2d4175;
      border-radius: var(--radius-md);
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
    }}

    .quiz-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .quiz-badge {{
      font-size: 0.65rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 3px 8px;
      border-radius: 12px;
      background: #f59e0b;
      color: #000;
    }}

    .quiz-question-txt {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.4;
    }}

    .quiz-choices-wrap {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .choice-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      color: var(--text-muted);
      font-size: 0.74rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
      line-height: 1.35;
    }}

    .choice-btn:hover:not(:disabled) {{
      background: var(--bg-elevated);
      color: #fff;
      border-color: #38bdf8;
    }}

    .choice-btn.correct {{
      background: rgba(16, 185, 129, 0.2) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 700;
    }}

    .choice-btn.wrong {{
      background: rgba(239, 68, 68, 0.2) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }}

    .quiz-result-msg {{
      font-size: 0.75rem;
      line-height: 1.4;
      padding: 8px 10px;
      border-radius: var(--radius-sm);
      display: none;
    }}

    .quiz-result-msg.show-ok {{
      display: block;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #6ee7b7;
    }}

    .quiz-result-msg.show-fail {{
      display: block;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #fca5a5;
    }}

    /* BOTTOM CONTROLS BAR */
    .controls-dock {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 10px 18px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-elevation);
      flex-wrap: wrap;
    }}

    .playback-btn-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
      user-select: none;
    }}

    .btn-action:hover:not(:disabled) {{
      background: #1e2c4f;
      border-color: var(--border-bright);
      color: #fff;
    }}

    .btn-action:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .btn-action.btn-primary {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border: none;
      color: #fff;
      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.35);
    }}

    .btn-action.btn-primary:hover:not(:disabled) {{
      background: linear-gradient(135deg, #0369a1, #1d4ed8);
    }}

    .dots-nav {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .step-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--border-bright);
      border: none;
      cursor: pointer;
      transition: all 0.25s;
    }}

    .step-dot.active {{
      width: 26px;
      border-radius: 10px;
      background: var(--accent-color);
      box-shadow: 0 0 10px var(--accent-glow);
    }}

    .shortcuts-help-note {{
      font-size: 0.7rem;
      color: var(--text-dim);
    }}
    .shortcuts-help-note kbd {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 4px;
      padding: 1px 4px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-muted);
    }}

    /* FOOTER */
    footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      font-size: 0.74rem;
      color: var(--text-dim);
      padding: 4px 10px 10px;
      flex-wrap: wrap;
    }}

    footer a {{
      color: #38bdf8;
      text-decoration: none;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}

    /* MODAL DIALOGS */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(4, 7, 15, 0.82);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      z-index: 1000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }}

    .modal-backdrop.open {{
      opacity: 1;
      pointer-events: auto;
    }}

    .modal-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-bright);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 820px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.8);
      overflow: hidden;
    }}

    .modal-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .modal-head h3 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #fff;
    }}

    .modal-close-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
      padding: 2px 6px;
      border-radius: 6px;
    }}
    .modal-close-btn:hover {{
      color: #fff;
      background: rgba(255, 255, 255, 0.08);
    }}

    .modal-body {{
      padding: 18px 20px;
      overflow-y: auto;
      font-size: 0.82rem;
      line-height: 1.6;
      color: var(--text-muted);
    }}

    .ref-entry {{
      margin-bottom: 14px;
      padding-left: 26px;
      text-indent: -26px;
      line-height: 1.5;
    }}
    .ref-entry a {{
      color: #38bdf8;
      text-decoration: underline;
      word-break: break-all;
    }}

    /* Progress bar for autoplay */
    .auto-progress-bar {{
      width: 100%;
      height: 3px;
      background: rgba(255, 255, 255, 0.05);
      position: relative;
      overflow: hidden;
      border-radius: 2px;
    }}
    .auto-progress-fill {{
      height: 100%;
      width: 0%;
      background: var(--accent-color);
      transition: width 0.1s linear;
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-container">
    <!-- HEADER -->
    <header>
      <div class="header-brand">
        <div class="brand-logo-pill">
          <span>Informatika</span>
          <span>Undip</span>
        </div>
        <div class="brand-titles">
          <h1>Threat Modeling &amp; Defense in Depth FinTech E-Wallet</h1>
          <p>Topik Khusus Sistem Cerdas / Komputasi Visual &bull; Kelompok 05 (Cipta dkk.) &bull; Dosen: Guruh Aryotejo, S.Kom., M.Sc.</p>
        </div>
      </div>

      <div class="header-toolbar">
        <button class="btn-tool" id="btnTeamModal" title="Informasi Kelompok dan Modul">
          <span>👥</span> Profil Tim
        </button>
        <button class="btn-tool" id="btnBiblioModal" title="Daftar Pustaka Paper Akademis IEEE">
          <span>📚</span> Daftar Pustaka IEEE
        </button>
        <button class="btn-tool active" id="btnAudioToggle" title="Audio Sound Effects">
          <span id="audioIcon">🔊</span> Audio SFX
        </button>
        <select class="speed-select" id="speedSelect" title="Kecepatan Putar Otomatis">
          <option value="4000">Kecepatan: 1x (4s)</option>
          <option value="2500">Kecepatan: 1.5x (2.5s)</option>
          <option value="6000">Kecepatan: 0.75x (6s)</option>
        </select>
        <button class="btn-tool" id="btnFullscreen" title="Tampilkan Layar Penuh">
          <span>⛶</span> Fullscreen
        </button>
      </div>
    </header>

    <!-- VECTOR TABS NAVIGATION -->
    <nav class="vector-navigation" id="vectorNav" aria-label="Pilih Vektor Serangan">
      <button class="v-tab-btn active" data-vec="1">
        <div class="v-tab-icon">📱</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Vektor 1: Mobile Trojan</span>
          <span class="v-tab-sub">Overlay &amp; Accessibility (Client)</span>
        </div>
      </button>

      <button class="v-tab-btn" data-vec="2">
        <div class="v-tab-icon">🎣</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Vektor 2: AitM Proxy</span>
          <span class="v-tab-sub">Evilginx &amp; 2FA Bypass (Identitas)</span>
        </div>
      </button>

      <button class="v-tab-btn" data-vec="3">
        <div class="v-tab-icon">📡</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Vektor 3A: Rogue WiFi</span>
          <span class="v-tab-sub">SSL Stripping &amp; Replay (Jaringan)</span>
        </div>
      </button>

      <button class="v-tab-btn" data-vec="4">
        <div class="v-tab-icon">🔓</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Vektor 3B: API BOLA / IDOR</span>
          <span class="v-tab-sub">Broken Object Authorization (API)</span>
        </div>
      </button>

      <button class="v-tab-btn" data-vec="5">
        <div class="v-tab-icon">⚡</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Vektor 3C: Layer 7 DDoS</span>
          <span class="v-tab-sub">API Flooding &amp; Cascading Fail</span>
        </div>
      </button>

      <button class="v-tab-btn" data-vec="6">
        <div class="v-tab-icon">🛡️</div>
        <div class="v-tab-info">
          <span class="v-tab-label">Ketahanan Data: 3-2-1</span>
          <span class="v-tab-sub">Immutable WORM &amp; DRC Failover</span>
        </div>
      </button>
    </nav>

    <!-- AUTO-PLAY PROGRESS BAR -->
    <div class="auto-progress-bar">
      <div class="auto-progress-fill" id="autoProgressFill"></div>
    </div>

    <!-- MAIN 3-COLUMN WORKSPACE -->
    <main class="stage-layout">
      <!-- LEFT: TIMELINE LIST -->
      <section class="panel-card panel-timeline">
        <div class="panel-header-section">
          <span class="panel-tag" id="timelineTag">ALUR TAHAPAN SERANGAN</span>
          <span class="vector-badge-pill" id="scenarioBadgePill">V1 &bull; Client Malware</span>
        </div>

        <div class="scenario-overview-box" id="scenarioOverviewBox">
          Memuat ringkasan vektor ancaman...
        </div>

        <div class="steps-list-container" id="stepsListContainer">
          <!-- Step items rendered dynamically via JS -->
        </div>
      </section>

      <!-- CENTER: ANIMATED SVG STAGE -->
      <section class="panel-card panel-stage">
        <div class="stage-top-meta">
          <h2 class="stage-step-heading" id="stageStepHeading">
            <span id="stepCounterBadge" style="color: var(--accent-color);">Langkah 1/6</span>
            <span id="stepTitleTxt">Inisialisasi...</span>
          </h2>
          <span class="status-badge-live warn" id="stageStatusBadge">
            <span class="status-dot">●</span>
            <span id="stageStatusTxt">Menganalisis</span>
          </span>
        </div>

        <div class="stage-canvas-frame">
          <svg class="svg-viewport" viewBox="0 0 820 380" id="mainSvgStage" role="img" aria-label="Visualisasi Arsitektur Serangan">
            <!-- SHARED SVG DEFINITIONS: GRADIENTS, GLOWS, AND MARKERS -->
            <defs>
              <!-- Gradients -->
              <linearGradient id="phoneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#1e293b"/>
                <stop offset="100%" stop-color="#0b1329"/>
              </linearGradient>
              <linearGradient id="screenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#0f172a"/>
                <stop offset="100%" stop-color="#020617"/>
              </linearGradient>
              <linearGradient id="walletHeaderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0284c7"/>
                <stop offset="100%" stop-color="#2563eb"/>
              </linearGradient>
              <linearGradient id="hackerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#3b0764"/>
                <stop offset="100%" stop-color="#090514"/>
              </linearGradient>
              <linearGradient id="serverGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#1e293b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
              <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#d97706"/>
              </linearGradient>

              <!-- Glowing Filters -->
              <filter id="glowRed">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
              <filter id="glowGreen">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
              <filter id="glowCyan">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>
              <filter id="glowAmber">
                <feGaussianBlur stdDeviation="4" result="blur"/>
                <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
              </filter>

              <!-- Arrow Markers -->
              <marker id="arrowRed" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
                <polygon points="0 0, 8 3, 0 6" fill="#ef4444"/>
              </marker>
              <marker id="arrowGreen" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
                <polygon points="0 0, 8 3, 0 6" fill="#10b981"/>
              </marker>
              <marker id="arrowCyan" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
                <polygon points="0 0, 8 3, 0 6" fill="#06b6d4"/>
              </marker>
              <marker id="arrowAmber" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
                <polygon points="0 0, 8 3, 0 6" fill="#f59e0b"/>
              </marker>
            </defs>

            <!-- Dynamic content injected here -->
            <g id="dynamicSvgLayers"></g>
          </svg>
        </div>
      </section>

      <!-- RIGHT: DETAILS, TERMS & CHECKPOINT QUIZ -->
      <aside class="panel-card panel-detail">
        <div class="detail-section-title">
          <span>📖</span> DESKRIPSI &amp; APA YANG TERJADI
        </div>
        <div class="narrative-card" id="stepDescNarrative">
          Memuat penjelasan langkah...
        </div>

        <div class="detail-section-title">
          <span>💡</span> KAMUS ISTILAH TEKNIS
        </div>
        <div class="terms-grid" id="termsListGrid">
          <!-- Terms injected here -->
        </div>

        <div class="detail-section-title">
          <span>🛡️</span> TITIK MITIGASI &amp; PERTAHANAN BERLAPIS
        </div>
        <div class="defense-box" id="defenseInfoBox">
          Memuat titik pertahanan...
        </div>

        <!-- CHECKPOINT QUIZ BOX -->
        <div class="quiz-card" id="quizCardBox">
          <div class="quiz-header">
            <span class="quiz-badge">⚡ Checkpoint Kuis Audiens</span>
            <span style="font-size: 0.68rem; color: var(--text-dim);">Uji Pemahaman</span>
          </div>
          <div class="quiz-question-txt" id="quizQuestionTxt">
            Pertanyaan checkpoint kuis?
          </div>
          <div class="quiz-choices-wrap" id="quizChoicesWrap">
            <!-- Choice buttons injected here -->
          </div>
          <div class="quiz-result-msg" id="quizResultMsg"></div>
        </div>
      </aside>
    </main>

    <!-- BOTTOM CONTROLS BAR -->
    <div class="controls-dock">
      <div class="playback-btn-group">
        <button class="btn-action" id="btnPrevStep" aria-label="Langkah sebelumnya">
          <span>◀</span> Sebelumnya
        </button>
        <button class="btn-action btn-primary" id="btnPlayAuto" aria-label="Putar otomatis alur">
          <span id="playIcon">▶</span> <span id="playTxt">Putar Otomatis</span>
        </button>
        <button class="btn-action" id="btnNextStep" aria-label="Langkah berikutnya">
          Selanjutnya <span>▶</span>
        </button>
      </div>

      <!-- Step Indicator Dots -->
      <div class="dots-nav" id="stepDotsNav" role="tablist" aria-label="Indikator langkah"></div>

      <div class="playback-btn-group">
        <button class="btn-action" id="btnResetFlow" title="Kembali ke langkah pertama">
          <span>↺</span> Reset Alur
        </button>
      </div>

      <div class="shortcuts-help-note">
        Pintasan: <kbd>→</kbd> Maju &bull; <kbd>←</kbd> Mundur &bull; <kbd>Space</kbd> Play/Pause &bull; <kbd>1-6</kbd> Pilih Vektor &bull; <kbd>F</kbd> Fullscreen
      </div>
    </div>

    <!-- FOOTER CITATIONS -->
    <footer>
      <div>
        <strong>Acuan Standar &amp; Regulasi:</strong> POJK 11/POJK.03/2022 &bull; PADG BI No. 24/7/PADG/2022 (SPPur) &bull; PCI-DSS v4.0.1 Req 6 &bull; OWASP API Security 2023 &bull; NIST CSF 2.0 &bull; UU PDP No. 27/2022
      </div>
      <div>
        Departemen Informatika &bull; Fakultas Sains dan Matematika &bull; Universitas Diponegoro &copy; 2024
      </div>
    </footer>
  </div>

  <!-- MODAL: PROFIL TIM & KURSUS -->
  <div class="modal-backdrop" id="modalTeam">
    <div class="modal-box">
      <div class="modal-head">
        <h3>👥 Profil Tim &amp; Mata Kuliah</h3>
        <button class="modal-close-btn" data-close="modalTeam">&times;</button>
      </div>
      <div class="modal-body">
        <p><strong>Mata Kuliah:</strong> Topik Khusus Sistem Cerdas / Komputasi Visual (Semester 7)</p>
        <p><strong>Dosen Pengampu:</strong> Guruh Aryotejo, S.Kom., M.Sc.</p>
        <p><strong>Program Studi:</strong> S1 Informatika, Universitas Diponegoro</p>
        <p><strong>Kelompok Tugas:</strong> Kelompok 05 (Kelompok Cipta dkk.)</p>
        <br />
        <p><strong>Topik Proyek:</strong> Analisis Model Ancaman (Threat Modeling) &amp; Arsitektur Pertahanan Berlapis (Defense in Depth) pada Sistem Pembayaran Elektronik (FinTech E-Wallet).</p>
        <br />
        <p><strong>Cakupan Vektor Serangan:</strong></p>
        <ul style="padding-left: 20px; margin-top: 6px;">
          <li><strong>Vektor 1:</strong> Mobile Banking Trojan, Sideloading APK, Overlay Cloak &amp; Dagger, Accessibility Service Hijacking (Sisi Client).</li>
          <li><strong>Vektor 2:</strong> Phishing &amp; Adversary-in-the-Middle (AitM) Reverse Proxy (Evilginx) untuk Bypass 2FA SMS &amp; Cookie Theft (Jalur Identitas).</li>
          <li><strong>Vektor 3A:</strong> Rogue Access Point, ARP Poisoning, SSL Stripping &amp; Replay Attack (Jalur Jaringan).</li>
          <li><strong>Vektor 3B:</strong> API Broken Object Level Authorization (BOLA / IDOR) &amp; OPA Rego Authorization (Infrastruktur API).</li>
          <li><strong>Vektor 3C:</strong> Layer 7 API Flooding / DDoS, Database Connection Pool Exhaustion, Anycast WAF &amp; Circuit Breaker (Backend).</li>
          <li><strong>Ketahanan Data:</strong> Skema Pencadangan 3-2-1, Immutable WORM Storage, &amp; DRC Failover (Resiliensi Ledger).</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODAL: DAFTAR PUSTAKA IEEE -->
  <div class="modal-backdrop" id="modalBiblio">
    <div class="modal-box">
      <div class="modal-head">
        <h3>📚 Daftar Pustaka Akademis (IEEE &amp; Top Venues)</h3>
        <button class="modal-close-btn" data-close="modalBiblio">&times;</button>
      </div>
      <div class="modal-body">
        <div class="ref-entry">
          [1] S. Bojjagani and V. N. Sastry, "VAPTAi: A Threat Model for Vulnerability Assessment and Penetration Testing of Android and iOS Mobile Banking Apps," in <em>Proc. 2017 IEEE 3rd International Conference on Collaboration and Internet Computing (CIC)</em>, San Jose, CA, USA, 2017, pp. 77–86. Tersedia: <a href="https://ieeexplore.ieee.org/document/8181483" target="_blank" rel="noopener">https://ieeexplore.ieee.org/document/8181483</a>.
        </div>
        <div class="ref-entry">
          [2] <a href="https://ieeexplore.ieee.org/author/37085364317" target="_blank" rel="noopener">Fadi Mohsen</a>, <a href="https://ieeexplore.ieee.org/author/37595743100" target="_blank" rel="noopener">Halil Bisgin</a>, <a href="https://ieeexplore.ieee.org/author/37085495197" target="_blank" rel="noopener">Zachary Scott</a>, and <a href="https://ieeexplore.ieee.org/author/37086275889" target="_blank" rel="noopener">Kyle Strait</a>, "Detecting Android Malwares by Mining Statically Registered Broadcast Receivers," in <em>Proc. 2017 IEEE 3rd International Conference on Collaboration and Internet Computing (CIC)</em>, San Jose, CA, USA, 2017, pp. 67–76. Tersedia: <a href="https://ieeexplore.ieee.org/document/8181482" target="_blank" rel="noopener">https://ieeexplore.ieee.org/document/8181482</a>.
        </div>
        <div class="ref-entry">
          [3] Y. Fratantonio, C. Qian, S. P. H. Chung, and W. Lee, "Cloak &amp; Dagger: From Two Permissions to Complete Control of the UI Feedback Loop," in <em>Black Hat USA 2017</em>, Tech. Rep. / White Paper, 2017. Tersedia: <a href="https://blackhat.com/docs/us-17/thursday/us-17-Fratantonio-Cloak-And-Dagger-From-Two-Permissions-To-Complete-Control-Of-The-UI-Feedback-Loop-wp.pdf" target="_blank" rel="noopener">https://blackhat.com/docs/us-17/thursday/us-17-Fratantonio-Cloak-And-Dagger...</a>.
        </div>
        <div class="ref-entry">
          [4] H. Xu, M. Yao, R. Zhang, M. M. Dawoud, J. Park, and B. Saltaformaggio, "DVa: Extracting Victims and Abuse Vectors from Android Accessibility Malware," in <em>Proc. 33rd USENIX Security Symposium (USENIX Security 24)</em>, Philadelphia, PA, USA, Aug. 2024, pp. 2611–2628. Tersedia: <a href="https://www.usenix.org/conference/usenixsecurity24/presentation/xu-haichuan" target="_blank" rel="noopener">https://www.usenix.org/conference/usenixsecurity24/presentation/xu-haichuan</a>.
        </div>
        <div class="ref-entry">
          [5] P. Čisar and S. M. Čisar, "The framework of runtime application self-protection technology," in <em>Proc. 2016 IEEE 17th International Symposium on Computational Intelligence and Informatics (CINTI)</em>, Budapest, Hungary, 2016, pp. 241–246. Tersedia: <a href="https://ieeexplore.ieee.org/document/7846383" target="_blank" rel="noopener">https://ieeexplore.ieee.org/document/7846383</a>.
        </div>
        <div class="ref-entry">
          [6] <a href="https://ieeexplore.ieee.org/author/37090018560" target="_blank" rel="noopener">Nina Bindel</a>, <a href="https://ieeexplore.ieee.org/author/37528785600" target="_blank" rel="noopener">Cas Cremers</a>, and <a href="https://ieeexplore.ieee.org/author/37088950907" target="_blank" rel="noopener">Mang Zhao</a>, "FIDO2, CTAP 2.1, and WebAuthn 2: Provable Security and Post-Quantum Instantiation," in <em>Proc. 2023 IEEE Symposium on Security and Privacy (SP)</em>, San Francisco, CA, USA, 2023, pp. 434–451. Tersedia: <a href="https://ieeexplore.ieee.org/document/10179454" target="_blank" rel="noopener">https://ieeexplore.ieee.org/document/10179454</a>.
        </div>
        <div class="ref-entry">
          [7] Y. Huang, C. Shi, J. Lu, H. Li, H. Meng, and L. Li, "Detecting Broken Object-Level Authorization Vulnerabilities in Database-Backed Applications," in <em>Proc. 2024 ACM SIGSAC Conference on Computer and Communications Security (CCS '24)</em>, Salt Lake City, UT, USA, Oct. 2024, pp. 3173–3187, doi: <a href="https://doi.org/10.1145/3658644.3690227" target="_blank" rel="noopener">10.1145/3658644.3690227</a>.
        </div>
        <div class="ref-entry">
          [8] S. T. Zargar, J. B. D. Joshi, and D. Tipper, "A Survey of Defense Mechanisms Against Distributed Denial of Service (DDoS) Flooding Attacks," <em>IEEE Communications Surveys &amp; Tutorials</em>, vol. 15, no. 4, pp. 2046–2069, Fourth Quarter 2013, doi: <a href="https://doi.org/10.1109/SURV.2013.031413.00127" target="_blank" rel="noopener">10.1109/SURV.2013.031413.00127</a>.
        </div>
        <div class="ref-entry">
          [9] F. Montesi and J. Weber, "From the Decorator Pattern to Circuit Breakers in Microservices," in <em>Proc. 10th ACM SIGPLAN International Conference on Software Language Engineering (SLE 2017)</em>, Vancouver, BC, Canada, Oct. 2017, pp. 230–234. Tersedia: <a href="https://www.fabriziomontesi.com/files/mw18.pdf" target="_blank" rel="noopener">https://www.fabriziomontesi.com/files/mw18.pdf</a>.
        </div>
        <div class="ref-entry">
          [10] N. Jeršič, M. Turkanović, and T. Beranič, "Towards a Sustainable Cybersecurity Governance: Threat Modelling with Large Language Models," <em>Sustainability</em>, vol. 17, no. 23, Art. no. 10569, Nov. 2025, doi: <a href="https://doi.org/10.3390/su172310569" target="_blank" rel="noopener">10.3390/su172310569</a>.
        </div>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT ENGINE -->
  <script>
    // Embedded Scenarios Data from vectors_data.py
    const SCENARIOS = {scenarios_json};

    // State Variables
    let currentVector = "1";
    let currentStepIdx = 0;
    let autoPlayTimer = null;
    let autoProgressTimer = null;
    let autoProgressVal = 0;
    let isAudioMuted = false;

    // Web Audio Synthesizer (Zero External Dependencies)
    let audioCtx = null;
    function initAudio() {{
      if (!audioCtx) {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) audioCtx = new AudioContext();
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
    }}

    function playTone(freq, type, duration, gainLevel = 0.08) {{
      if (isAudioMuted) return;
      try {{
        initAudio();
        if (!audioCtx) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(gainLevel, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      }} catch (e) {{
        // Ignore audio errors
      }}
    }}

    function sfxStep() {{
      playTone(480, 'sine', 0.09, 0.06);
    }}
    function sfxAlert() {{
      playTone(260, 'sawtooth', 0.16, 0.08);
      setTimeout(() => playTone(210, 'sawtooth', 0.2, 0.08), 90);
    }}
    function sfxSuccess() {{
      playTone(520, 'triangle', 0.12, 0.07);
      setTimeout(() => playTone(780, 'triangle', 0.22, 0.08), 110);
    }}
    function sfxWrong() {{
      playTone(180, 'sawtooth', 0.24, 0.1);
    }}

    // DOM Elements Cache
    const dom = {{
      vectorNav: document.getElementById('vectorNav'),
      timelineTag: document.getElementById('timelineTag'),
      scenarioBadgePill: document.getElementById('scenarioBadgePill'),
      scenarioOverviewBox: document.getElementById('scenarioOverviewBox'),
      stepsListContainer: document.getElementById('stepsListContainer'),
      stageStepHeading: document.getElementById('stageStepHeading'),
      stepCounterBadge: document.getElementById('stepCounterBadge'),
      stepTitleTxt: document.getElementById('stepTitleTxt'),
      stageStatusBadge: document.getElementById('stageStatusBadge'),
      stageStatusTxt: document.getElementById('stageStatusTxt'),
      dynamicSvgLayers: document.getElementById('dynamicSvgLayers'),
      stepDescNarrative: document.getElementById('stepDescNarrative'),
      termsListGrid: document.getElementById('termsListGrid'),
      defenseInfoBox: document.getElementById('defenseInfoBox'),
      quizCardBox: document.getElementById('quizCardBox'),
      quizQuestionTxt: document.getElementById('quizQuestionTxt'),
      quizChoicesWrap: document.getElementById('quizChoicesWrap'),
      quizResultMsg: document.getElementById('quizResultMsg'),
      btnPrevStep: document.getElementById('btnPrevStep'),
      btnNextStep: document.getElementById('btnNextStep'),
      btnPlayAuto: document.getElementById('btnPlayAuto'),
      playIcon: document.getElementById('playIcon'),
      playTxt: document.getElementById('playTxt'),
      btnResetFlow: document.getElementById('btnResetFlow'),
      stepDotsNav: document.getElementById('stepDotsNav'),
      autoProgressFill: document.getElementById('autoProgressFill'),
      speedSelect: document.getElementById('speedSelect'),
      btnAudioToggle: document.getElementById('btnAudioToggle'),
      audioIcon: document.getElementById('audioIcon'),
      btnFullscreen: document.getElementById('btnFullscreen'),
      modalTeam: document.getElementById('modalTeam'),
      modalBiblio: document.getElementById('modalBiblio'),
      btnTeamModal: document.getElementById('btnTeamModal'),
      btnBiblioModal: document.getElementById('btnBiblioModal')
    }};

    // Switch active Vector Scenario
    function switchVector(vKey) {{
      stopAutoPlay();
      currentVector = String(vKey);
      currentStepIdx = 0;

      // Update active nav button
      document.querySelectorAll('.v-tab-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('data-vec') === currentVector);
      }});

      // Update accent color theme
      const colors = {{
        "1": "#ef4444",
        "2": "#f59e0b",
        "3": "#06b6d4",
        "4": "#a855f7",
        "5": "#f97316",
        "6": "#10b981"
      }};
      const accent = colors[currentVector] || "#ef4444";
      document.documentElement.style.setProperty('--accent-color', accent);
      document.documentElement.style.setProperty('--accent-glow', accent + '40');

      buildStepList();
      buildDots();
      renderStep(0);
      sfxStep();
    }}

    // Build timeline list in left panel
    function buildStepList() {{
      const sc = SCENARIOS[currentVector];
      dom.timelineTag.innerHTML = sc.tag || 'ALUR TAHAPAN SERANGAN';
      dom.scenarioBadgePill.innerHTML = sc.badge || 'Vektor Ancaman';
      dom.scenarioOverviewBox.innerHTML = sc.desc_overview || '';

      dom.stepsListContainer.innerHTML = '';
      sc.steps.forEach((step, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'step-item-btn' + (idx === 0 ? ' active' : '');
        btn.innerHTML = `
          <span class="step-idx-num">${{idx + 1}}</span>
          <div class="step-item-content">
            <span class="step-item-title">${{step.title}}</span>
            <span class="step-item-status ${{step.status ? step.status.cls : 'warn'}}">
              ${{step.status ? step.status.text : ''}}
            </span>
          </div>
        `;
        btn.addEventListener('click', () => {{
          stopAutoPlay();
          goToStep(idx);
        }});
        dom.stepsListContainer.appendChild(btn);
      }});
    }}

    // Build progress dots in controls dock
    function buildDots() {{
      const sc = SCENARIOS[currentVector];
      dom.stepDotsNav.innerHTML = '';
      sc.steps.forEach((_, idx) => {{
        const dot = document.createElement('button');
        dot.className = 'step-dot' + (idx === 0 ? ' active' : '');
        dot.setAttribute('title', `Langkah ${{idx + 1}}`);
        dot.addEventListener('click', () => {{
          stopAutoPlay();
          goToStep(idx);
        }});
        dom.stepDotsNav.appendChild(dot);
      }});
    }}

    // Render specific step
    function renderStep(idx) {{
      const sc = SCENARIOS[currentVector];
      const step = sc.steps[idx];
      if (!step) return;

      currentStepIdx = idx;

      // Update Meta & Headings
      dom.stepCounterBadge.textContent = `Langkah ${{idx + 1}}/${{sc.steps.length}}`;
      dom.stepTitleTxt.textContent = step.title;
      
      const st = step.status || {{ text: 'Aktif', cls: 'warn' }};
      dom.stageStatusTxt.textContent = st.text;
      dom.stageStatusBadge.className = `status-badge-live ${{st.cls}}`;

      // Update Left Timeline Active Button
      Array.from(dom.stepsListContainer.children).forEach((el, i) => {{
        el.classList.toggle('active', i === idx);
        if (i === idx) {{
          el.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
        }}
      }});

      // Update Dots
      Array.from(dom.stepDotsNav.children).forEach((d, i) => {{
        d.classList.toggle('active', i === idx);
      }});

      // Inject SVG Layer
      dom.dynamicSvgLayers.innerHTML = step.svg || '';

      // Update Right Narrative & Terms
      dom.stepDescNarrative.textContent = step.desc || '';
      
      // Terms
      dom.termsListGrid.innerHTML = '';
      if (step.terms && step.terms.length > 0) {{
        step.terms.forEach(([k, v]) => {{
          const tRow = document.createElement('div');
          tRow.className = 'term-row';
          tRow.innerHTML = `<div class="term-key">${{k}}</div><div class="term-val">${{v}}</div>`;
          dom.termsListGrid.appendChild(tRow);
        }});
      }}

      // Defense Info
      dom.defenseInfoBox.innerHTML = `<strong>Prinsip Pertahanan:</strong> ${{step.defenseInfo || 'Mitigasi komprehensif defense-in-depth.'}}`;

      // Quiz Checkpoint
      renderQuiz(step.checkpoint);

      // Button Disable states
      dom.btnPrevStep.disabled = (idx === 0);
      dom.btnNextStep.disabled = (idx === sc.steps.length - 1);
    }}

    // Render Quiz Checkpoint Box
    function renderQuiz(cp) {{
      if (!cp) {{
        dom.quizCardBox.style.display = 'none';
        return;
      }}
      dom.quizCardBox.style.display = 'flex';
      dom.quizQuestionTxt.textContent = cp.q;
      dom.quizResultMsg.className = 'quiz-result-msg';
      dom.quizResultMsg.style.display = 'none';
      dom.quizResultMsg.textContent = '';
      dom.quizChoicesWrap.innerHTML = '';

      cp.options.forEach((optText, optIdx) => {{
        const btn = document.createElement('button');
        btn.className = 'choice-btn';
        btn.textContent = optText;
        btn.addEventListener('click', () => {{
          const isCorrect = (optIdx === cp.correct);
          Array.from(dom.quizChoicesWrap.children).forEach((b, i) => {{
            b.disabled = true;
            if (i === cp.correct) b.classList.add('correct');
            else if (i === optIdx) b.classList.add('wrong');
          }});

          if (isCorrect) {{
            dom.quizResultMsg.className = 'quiz-result-msg show-ok';
            dom.quizResultMsg.innerHTML = `<strong>✔ Tepat Sekali!</strong> ${{cp.feedback}}`;
            sfxSuccess();
          }} else {{
            dom.quizResultMsg.className = 'quiz-result-msg show-fail';
            dom.quizResultMsg.innerHTML = `<strong>✖ Kurang Tepat.</strong> ${{cp.feedback}}`;
            sfxWrong();
          }}
        }});
        dom.quizChoicesWrap.appendChild(btn);
      }});
    }}

    // Step Movement
    function goToStep(idx) {{
      const sc = SCENARIOS[currentVector];
      if (idx < 0 || idx >= sc.steps.length) return;
      renderStep(idx);
      sfxStep();
    }}

    function nextStep() {{
      const sc = SCENARIOS[currentVector];
      if (currentStepIdx < sc.steps.length - 1) {{
        goToStep(currentStepIdx + 1);
      }} else {{
        stopAutoPlay();
      }}
    }}

    function prevStep() {{
      if (currentStepIdx > 0) {{
        goToStep(currentStepIdx - 1);
      }}
    }}

    // Auto-Play Controls
    function toggleAutoPlay() {{
      if (autoPlayTimer) {{
        stopAutoPlay();
      }} else {{
        startAutoPlay();
      }}
    }}

    function startAutoPlay() {{
      stopAutoPlay();
      dom.playIcon.textContent = '⏸';
      dom.playTxt.textContent = 'Jeda Alur';

      const duration = parseInt(dom.speedSelect.value, 10) || 4000;
      autoProgressVal = 0;
      dom.autoProgressFill.style.width = '0%';

      const progressInterval = 50;
      const progressStep = (progressInterval / duration) * 100;

      autoProgressTimer = setInterval(() => {{
        autoProgressVal += progressStep;
        dom.autoProgressFill.style.width = Math.min(autoProgressVal, 100) + '%';
      }}, progressInterval);

      autoPlayTimer = setInterval(() => {{
        const sc = SCENARIOS[currentVector];
        if (currentStepIdx >= sc.steps.length - 1) {{
          stopAutoPlay();
          return;
        }}
        autoProgressVal = 0;
        dom.autoProgressFill.style.width = '0%';
        nextStep();
      }}, duration);
    }}

    function stopAutoPlay() {{
      if (autoPlayTimer) {{
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }}
      if (autoProgressTimer) {{
        clearInterval(autoProgressTimer);
        autoProgressTimer = null;
      }}
      dom.playIcon.textContent = '▶';
      dom.playTxt.textContent = 'Putar Otomatis';
      dom.autoProgressFill.style.width = '0%';
    }}

    // Modal helpers
    function openModal(modalEl) {{
      if (modalEl) modalEl.classList.add('open');
    }}
    function closeModal(modalEl) {{
      if (modalEl) modalEl.classList.remove('open');
    }}

    // Event Listeners Setup
    function initListeners() {{
      // Vector Tabs
      document.querySelectorAll('.v-tab-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const vec = btn.getAttribute('data-vec');
          if (vec) switchVector(vec);
        }});
      }});

      // Stepper Controls
      dom.btnPrevStep.addEventListener('click', () => {{
        stopAutoPlay();
        prevStep();
      }});
      dom.btnNextStep.addEventListener('click', () => {{
        stopAutoPlay();
        nextStep();
      }});
      dom.btnPlayAuto.addEventListener('click', toggleAutoPlay);
      dom.btnResetFlow.addEventListener('click', () => {{
        stopAutoPlay();
        goToStep(0);
      }});

      // Speed selection change
      dom.speedSelect.addEventListener('change', () => {{
        if (autoPlayTimer) startAutoPlay();
      }});

      // Audio Toggle
      dom.btnAudioToggle.addEventListener('click', () => {{
        isAudioMuted = !isAudioMuted;
        dom.btnAudioToggle.classList.toggle('active', !isAudioMuted);
        dom.audioIcon.textContent = isAudioMuted ? '🔇' : '🔊';
        if (!isAudioMuted) sfxSuccess();
      }});

      // Fullscreen
      dom.btnFullscreen.addEventListener('click', () => {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(() => {{}});
        }} else {{
          document.exitFullscreen().catch(() => {{}});
        }}
      }});

      // Modals
      dom.btnTeamModal.addEventListener('click', () => openModal(dom.modalTeam));
      dom.btnBiblioModal.addEventListener('click', () => openModal(dom.modalBiblio));

      document.querySelectorAll('.modal-close-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const modalId = btn.getAttribute('data-close');
          if (modalId) closeModal(document.getElementById(modalId));
        }});
      }});

      document.querySelectorAll('.modal-backdrop').forEach(modal => {{
        modal.addEventListener('click', (e) => {{
          if (e.target === modal) closeModal(modal);
        }});
      }});

      // Keyboard navigation
      document.addEventListener('keydown', (e) => {{
        // If modal is open, close with Esc
        if (e.key === 'Escape') {{
          closeModal(dom.modalTeam);
          closeModal(dom.modalBiblio);
          return;
        }}
        if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
          stopAutoPlay();
          nextStep();
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
          stopAutoPlay();
          prevStep();
        }} else if (e.key === ' ' || e.code === 'Space') {{
          e.preventDefault();
          toggleAutoPlay();
        }} else if (['1', '2', '3', '4', '5', '6'].includes(e.key)) {{
          switchVector(e.key);
        }} else if (e.key.toLowerCase() === 'f') {{
          dom.btnFullscreen.click();
        }} else if (e.key.toLowerCase() === 'm') {{
          dom.btnAudioToggle.click();
        }} else if (e.key.toLowerCase() === 'r' || e.key === 'Home') {{
          dom.btnResetFlow.click();
        }}
      }});
    }}

    // Bootstrap app
    window.addEventListener('DOMContentLoaded', () => {{
      initListeners();

      // Check URL hash for direct vector or modal navigation
      const hash = window.location.hash;
      if (hash.includes('biblio')) {{
        openModal(dom.modalBiblio);
      }} else if (hash.includes('team')) {{
        openModal(dom.modalTeam);
      }}

      let startVec = "1";
      const match = hash.match(/vec=([1-6])/);
      if (match) {{
        startVec = match[1];
      }}
      switchVector(startVec);

      window.addEventListener('hashchange', () => {{
        const h = window.location.hash;
        if (h.includes('biblio')) openModal(dom.modalBiblio);
        else if (h.includes('team')) openModal(dom.modalTeam);
        const m = h.match(/vec=([1-6])/);
        if (m) switchVector(m[1]);
      }});
    }});
  </script>
</body>
</html>
'''

    output_path = "/Users/driven/KULIAH/semester7/topsus SC:KV/index.html"
    print(f"Writing generated HTML to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Done writing index.html!")

    # Mirror copy
    mirror_path = "/Users/driven/KULIAH/semester7/topsus SC:KV/drive-download-20260907T122854Z-1-001/animasi/Fintech_EWallet_Threat_Defense_Step_by_Step.html"
    if os.path.exists(os.path.dirname(mirror_path)):
        shutil.copyfile(output_path, mirror_path)
        print(f"Mirrored successfully to {mirror_path}")

if __name__ == "__main__":
    build_app()
