# -*- coding: utf-8 -*-
"""
Script to generate the interactive animated kill chain HTML application
from Modul02_Kelompok05_Updated.pdf
"""
import json

def generate_html():
    from scenario_data import SCENARIOS_JSON, PANORAMA_JSON, DEFENSE_PILLARS_JSON

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Animasi Diagram Alur Serangan (Kill Chain) — Fintech Dompet Digital | Kelompok 05</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Source+Sans+3:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #060913;
      --bg-alt: #0a0f1d;
      --panel: #0f172a;
      --panel-elevated: #162036;
      --line: #1e2c47;
      --line-bright: #30456e;
      --text: #e2e8f0;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --v1-crimson: #ef4444;
      --v1-crimson-bg: rgba(239, 68, 68, 0.12);
      --v2-amber: #f59e0b;
      --v2-amber-bg: rgba(245, 158, 11, 0.12);
      --v3a-cyan: #06b6d4;
      --v3a-cyan-bg: rgba(6, 182, 212, 0.12);
      --v3b-purple: #a855f7;
      --v3b-purple-bg: rgba(168, 85, 247, 0.12);
      --def-green: #10b981;
      --def-green-bg: rgba(16, 185, 129, 0.12);
      
      --accent: var(--v1-crimson);
      --accent-bg: var(--v1-crimson-bg);
      --shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      min-height: 100vh;
      font-family: 'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: var(--text);
      background: radial-gradient(ellipse at 15% 0%, #1e1b4b 0%, transparent 45%),
                  radial-gradient(ellipse at 85% 100%, #0f2e4a 0%, transparent 45%),
                  linear-gradient(175deg, #060913 0%, #090e1c 100%);
      line-height: 1.5;
      overflow-x: hidden;
    }

    .app {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0.75rem clamp(0.75rem, 2vw, 1.5rem) 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    /* HEADER */
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.85rem 1.25rem;
      background: rgba(15, 23, 42, 0.88);
      border: 1px solid var(--line);
      border-radius: 14px;
      backdrop-filter: blur(12px);
      box-shadow: var(--shadow);
      flex-wrap: wrap;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }
    .brand-badge {
      font-family: Montserrat, sans-serif;
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      padding: 0.35rem 0.65rem;
      background: linear-gradient(135deg, #1e3a8a, #0284c7);
      color: #fff;
      border-radius: 8px;
      text-transform: uppercase;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
      cursor: pointer;
    }
    .brand-title h1 {
      font-family: Montserrat, sans-serif;
      font-size: clamp(1rem, 1.8vw, 1.35rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.01em;
    }
    .brand-title p {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .header-ctrls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .toggle-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-alt);
      border: 1px solid var(--line);
      border-radius: 20px;
      padding: 0.3rem 0.65rem;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      user-select: none;
      transition: all 0.2s;
    }
    .toggle-pill:hover { border-color: var(--line-bright); color: #fff; }
    .toggle-pill.active { background: #162036; color: #38bdf8; border-color: #0284c7; }

    /* VECTOR NAVIGATION TABS */
    .vector-nav {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 0.5rem;
    }
    .v-tab {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      padding: 0.65rem 0.85rem;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid var(--line);
      border-radius: 10px;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.22s ease;
      text-align: left;
    }
    .v-tab:hover {
      background: var(--panel-elevated);
      color: #fff;
      transform: translateY(-1px);
    }
    .v-tab.active {
      color: #fff;
      box-shadow: 0 4px 16px rgba(0,0,0,0.35);
      border-color: currentColor;
    }
    .v-tab[data-v="matrix"].active { color: #38bdf8; border-color: #38bdf8; background: rgba(56, 189, 248, 0.12); }
    .v-tab[data-v="1"].active { color: var(--v1-crimson); border-color: var(--v1-crimson); background: var(--v1-crimson-bg); }
    .v-tab[data-v="2"].active { color: var(--v2-amber); border-color: var(--v2-amber); background: var(--v2-amber-bg); }
    .v-tab[data-v="3a"].active { color: var(--v3a-cyan); border-color: var(--v3a-cyan); background: var(--v3a-cyan-bg); }
    .v-tab[data-v="3b"].active { color: var(--v3b-purple); border-color: var(--v3b-purple); background: var(--v3b-purple-bg); }
    .v-tab[data-v="def"].active { color: var(--def-green); border-color: var(--def-green); background: var(--def-green-bg); }

    .v-tab-icon {
      font-size: 1.1rem;
      width: 30px;
      height: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 6px;
      background: rgba(255,255,255,0.06);
      flex-shrink: 0;
    }
    .v-tab-info {
      display: flex;
      flex-direction: column;
      min-width: 0;
    }
    .v-tab-name {
      font-family: Montserrat, sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .v-tab-sub {
      font-size: 0.68rem;
      color: var(--text-dim);
    }
    .v-tab.active .v-tab-sub { color: rgba(255,255,255,0.75); }

    /* VIEW SECTIONS */
    .view-container {
      position: relative;
      min-height: 580px;
    }
    .view-tab-content {
      display: none;
    }
    .view-tab-content.active {
      display: block;
    }

    /* INTERACTIVE STEPPER LAYOUT */
    .interactive-layout {
      display: grid;
      grid-template-columns: 270px 1fr 340px;
      gap: 0.85rem;
    }
    @media (max-width: 1100px) {
      .interactive-layout { grid-template-columns: 1fr; }
    }

    .panel {
      background: rgba(15, 23, 42, 0.88);
      border: 1px solid var(--line);
      border-radius: 14px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(8px);
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    /* LEFT TIMELINE */
    .timeline-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      border-bottom: 1px solid var(--line);
      padding-bottom: 0.5rem;
    }
    .steps-list {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      overflow-y: auto;
      max-height: 500px;
      padding-right: 0.2rem;
    }
    .step-item {
      display: grid;
      grid-template-columns: 28px 1fr;
      gap: 0.6rem;
      align-items: center;
      padding: 0.6rem 0.7rem;
      border-radius: 9px;
      background: transparent;
      border: 1px solid transparent;
      color: var(--text);
      cursor: pointer;
      text-align: left;
      transition: all 0.2s;
    }
    .step-item:hover {
      background: var(--panel-elevated);
      border-color: var(--line);
    }
    .step-item.active {
      background: var(--accent-bg);
      border-color: var(--accent);
      color: #fff;
    }
    .step-badge-no {
      width: 26px;
      height: 26px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.08);
      font-family: Montserrat, sans-serif;
      font-weight: 800;
      font-size: 0.75rem;
    }
    .step-item.active .step-badge-no {
      background: var(--accent);
      color: #000;
    }
    .step-item-body {
      display: flex;
      flex-direction: column;
      min-width: 0;
    }
    .step-item-title {
      font-family: Montserrat, sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .step-item-status {
      font-size: 0.68rem;
      color: var(--text-dim);
    }
    .step-item.active .step-item-status {
      color: var(--text-muted);
    }

    /* CENTER CANVAS STAGE */
    .stage-panel {
      padding: 0.85rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      position: relative;
    }
    .stage-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
    .stage-title-wrap h2 {
      font-family: Montserrat, sans-serif;
      font-size: 1.1rem;
      font-weight: 800;
      color: #fff;
    }
    .stage-meta {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .status-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      background: rgba(239, 68, 68, 0.2);
      color: #f87171;
      border: 1px solid rgba(239, 68, 68, 0.35);
    }
    .status-tag.ok {
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.35);
    }
    .status-tag.warn {
      background: rgba(245, 158, 11, 0.2);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.35);
    }

    .mode-switch-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.3rem 0.75rem;
      border-radius: 8px;
      cursor: pointer;
      border: 1px solid var(--line);
      background: var(--panel-elevated);
      color: var(--text-muted);
      transition: all 0.2s;
    }
    .mode-switch-btn:hover { color: #fff; border-color: var(--line-bright); }
    .mode-switch-btn.defense-active {
      background: var(--def-green-bg);
      color: #34d399;
      border-color: #10b981;
    }

    .canvas-container {
      flex: 1;
      min-height: 400px;
      background: radial-gradient(circle at 50% 50%, #0d1629 0%, #070c17 100%);
      border: 1px solid var(--line);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    .svg-scene {
      width: 100%;
      height: 100%;
      min-height: 380px;
      max-height: 420px;
      display: block;
    }

    /* CONTROLS BAR */
    .controls-strip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      padding-top: 0.45rem;
      border-top: 1px solid var(--line);
      flex-wrap: wrap;
    }
    .btn-group {
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }
    .ctrl-btn {
      font-family: Montserrat, sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      background: var(--panel-elevated);
      border: 1px solid var(--line);
      color: var(--text);
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }
    .ctrl-btn:hover:not(:disabled) {
      background: #202e4d;
      border-color: var(--line-bright);
      color: #fff;
    }
    .ctrl-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }
    .ctrl-btn.primary {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border-color: #38bdf8;
      color: #fff;
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.3);
    }
    .speed-select {
      background: var(--panel-elevated);
      border: 1px solid var(--line);
      color: var(--text-muted);
      border-radius: 8px;
      font-size: 0.72rem;
      padding: 0.4rem 0.5rem;
      cursor: pointer;
    }

    .dots-nav {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .dot-step {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--line);
      border: none;
      cursor: pointer;
      transition: all 0.25s;
    }
    .dot-step:hover { background: var(--text-muted); }
    .dot-step.active {
      background: var(--accent);
      transform: scale(1.3);
      box-shadow: 0 0 8px var(--accent);
    }

    /* RIGHT DETAIL DRAWER */
    .detail-panel {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      overflow-y: auto;
      max-height: 560px;
    }
    .detail-section-title {
      font-family: Montserrat, sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .explanation-box {
      font-size: 0.85rem;
      line-height: 1.55;
      color: #cbd5e1;
      background: var(--bg-alt);
      border-left: 3px solid var(--accent);
      padding: 0.65rem 0.85rem;
      border-radius: 0 8px 8px 0;
    }
    .analogy-box {
      font-size: 0.82rem;
      line-height: 1.5;
      color: #fed7aa;
      background: rgba(245, 158, 11, 0.1);
      border: 1px dashed rgba(245, 158, 11, 0.4);
      padding: 0.65rem 0.85rem;
      border-radius: 8px;
    }

    .triad-bar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.4rem;
    }
    .triad-item {
      padding: 0.4rem;
      border-radius: 6px;
      background: var(--bg-alt);
      border: 1px solid var(--line);
      text-align: center;
    }
    .triad-name {
      font-size: 0.65rem;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
    }
    .triad-status {
      font-family: Montserrat, sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      margin-top: 0.15rem;
    }
    .triad-status.bad { color: #f87171; }
    .triad-status.safe { color: #34d399; }
    .triad-status.warn { color: #fbbf24; }

    .terms-card {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      background: var(--bg-alt);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0.65rem 0.8rem;
    }
    .term-row {
      font-size: 0.76rem;
      display: flex;
      flex-direction: column;
      gap: 0.1rem;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      padding-bottom: 0.35rem;
    }
    .term-row:last-child { border-bottom: none; padding-bottom: 0; }
    .term-key { font-weight: 700; color: #38bdf8; }
    .term-val { color: var(--text-muted); font-size: 0.74rem; }

    /* CHECKPOINT QUIZ */
    .quiz-card {
      background: linear-gradient(145deg, #10192e, #0c1222);
      border: 1px solid var(--line-bright);
      border-radius: 10px;
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }
    .quiz-title {
      font-family: Montserrat, sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }
    .quiz-question {
      font-size: 0.8rem;
      color: #f1f5f9;
      font-weight: 600;
    }
    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .quiz-opt-btn {
      font-size: 0.74rem;
      padding: 0.45rem 0.65rem;
      border-radius: 6px;
      border: 1px solid var(--line);
      background: var(--bg-alt);
      color: var(--text);
      cursor: pointer;
      text-align: left;
      transition: all 0.2s;
    }
    .quiz-opt-btn:hover { background: #1e293b; border-color: var(--line-bright); }
    .quiz-opt-btn.correct { background: rgba(16, 185, 129, 0.25); border-color: #10b981; color: #a7f3d0; }
    .quiz-opt-btn.wrong { background: rgba(239, 68, 68, 0.25); border-color: #ef4444; color: #fecaca; }
    .quiz-feedback {
      font-size: 0.74rem;
      padding: 0.4rem;
      border-radius: 6px;
      display: none;
    }
    .quiz-feedback.show { display: block; }
    .quiz-feedback.ok { background: rgba(16, 185, 129, 0.15); color: #34d399; }
    .quiz-feedback.fail { background: rgba(239, 68, 68, 0.15); color: #f87171; }

    /* PANORAMA MATRIX VIEW */
    .panorama-view {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 1.25rem;
      box-shadow: var(--shadow);
    }

    .matrix-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.75rem;
      border-bottom: 1px solid var(--line);
      padding-bottom: 0.85rem;
    }
    .matrix-title h2 {
      font-family: Montserrat, sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #fff;
    }
    .matrix-title p {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    .matrix-row {
      background: var(--bg-alt);
      border-radius: 12px;
      border: 1px solid var(--line);
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      transition: all 0.3s ease;
      position: relative;
    }
    .matrix-row.highlighted {
      border-color: currentColor;
      box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    .row-v1 { color: var(--v1-crimson); border-left: 4px solid var(--v1-crimson); }
    .row-v2 { color: var(--v2-amber); border-left: 4px solid var(--v2-amber); }
    .row-v3a { color: var(--v3a-cyan); border-left: 4px solid var(--v3a-cyan); }
    .row-v3b { color: var(--v3b-purple); border-left: 4px solid var(--v3b-purple); }

    .row-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: Montserrat, sans-serif;
      font-size: 0.82rem;
      font-weight: 800;
    }
    .row-header span.pill-meta {
      font-size: 0.68rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      background: rgba(255,255,255,0.08);
      color: var(--text-muted);
    }

    .row-flow {
      display: grid;
      grid-template-columns: repeat(5, 1fr) 1.25fr;
      gap: 0.5rem;
      position: relative;
    }
    @media (max-width: 960px) {
      .row-flow { grid-template-columns: 1fr; }
    }

    .flow-card {
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0.65rem;
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }
    .flow-card:hover {
      background: rgba(255,255,255,0.08);
      transform: translateY(-2px);
      border-color: var(--line-bright);
    }
    .flow-card.flow-active {
      border-color: currentColor;
      box-shadow: 0 0 14px currentColor;
      background: rgba(255,255,255,0.12);
    }
    .flow-card-num {
      font-family: Montserrat, sans-serif;
      font-size: 0.72rem;
      font-weight: 800;
      color: #fff;
    }
    .flow-card-desc {
      font-size: 0.72rem;
      color: var(--text-muted);
      line-height: 1.35;
    }
    .flow-card-impact {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      border-radius: 8px;
      padding: 0.65rem;
      color: #fca5a5;
    }
    .flow-card-impact h4 {
      font-family: Montserrat, sans-serif;
      font-size: 0.75rem;
      font-weight: 800;
      color: #f87171;
      margin-bottom: 0.2rem;
    }

    /* DEFENSE VIEW */
    .defense-view {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .defense-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 0.85rem;
    }
    .def-card {
      background: var(--bg-alt);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }
    .def-card-head {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: Montserrat, sans-serif;
      font-size: 0.9rem;
      font-weight: 800;
      color: #34d399;
    }
    .def-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }
    .def-list li {
      font-size: 0.78rem;
      color: var(--text-muted);
      padding-left: 1.1rem;
      position: relative;
      line-height: 1.45;
    }
    .def-list li::before {
      content: '✔';
      position: absolute;
      left: 0;
      color: #10b981;
      font-weight: 800;
    }

    /* FOOTER */
    footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 0.6rem;
      padding: 0.8rem 1.25rem;
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid var(--line);
      border-radius: 12px;
      font-size: 0.75rem;
      color: var(--text-dim);
    }
    footer a { color: #38bdf8; text-decoration: none; }
    footer a:hover { text-decoration: underline; }

    /* SVG ANIMATION STYLES */
    .pulse-glow { animation: pulseAnim 1.6s infinite alternate; }
    @keyframes pulseAnim {
      0% { filter: drop-shadow(0 0 2px currentColor); opacity: 0.8; }
      100% { filter: drop-shadow(0 0 10px currentColor); opacity: 1; }
    }
    .dash-flow {
      stroke-dasharray: 6 6;
      animation: dashMove 1s linear infinite;
    }
    @keyframes dashMove {
      to { stroke-dashoffset: -24; }
    }
    .shake-node {
      animation: shakeAnim 0.35s ease;
    }
    @keyframes shakeAnim {
      0%, 100% { transform: translate(0, 0); }
      25% { transform: translate(-3px, 2px); }
      75% { transform: translate(3px, -2px); }
    }
    .fade-pop {
      animation: popIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    @keyframes popIn {
      0% { opacity: 0; transform: scale(0.92); }
      100% { opacity: 1; transform: scale(1); }
    }

    /* MODAL FOR TEAM INFO */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.75);
      backdrop-filter: blur(5px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }
    .modal-backdrop.open { display: flex; }
    .modal-box {
      background: var(--panel);
      border: 1px solid var(--line-bright);
      border-radius: 14px;
      max-width: 560px;
      width: 100%;
      padding: 1.5rem;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .modal-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-head h3 {
      font-family: Montserrat, sans-serif;
      font-size: 1.1rem;
      font-weight: 800;
      color: #fff;
    }
    .modal-close {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      line-height: 1;
    }
    .team-member-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.65rem;
    }
    @media(max-width: 500px) {
      .team-member-grid { grid-template-columns: 1fr; }
    }
    .member-item {
      background: var(--bg-alt);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0.5rem 0.75rem;
    }
    .member-name { font-weight: 700; font-size: 0.8rem; color: #fff; }
    .member-nim { font-family: monospace; font-size: 0.72rem; color: #38bdf8; }
  </style>
</head>
<body>

  <div class="app">
    <!-- HEADER -->
    <header>
      <div class="brand-group">
        <button class="brand-badge" id="btnTeamModal">Kelompok 05</button>
        <div class="brand-title">
          <h1>Diagram Alur Serangan (Kill Chain) FinTech</h1>
          <p>Visualisasi Interaktif Berdasarkan Modul 02 &bull; Topik Khusus SC &amp; KV UNDIP 2026</p>
        </div>
      </div>

      <div class="header-ctrls">
        <button class="toggle-pill" id="btnAnalogy" title="Beralih ke mode analogi perumpamaan sehari-hari">
          <span>💡</span> <span id="analogyLabel">Mode Analogi: Nonaktif</span>
        </button>
        <button class="toggle-pill active" id="btnAudio" title="Nyalakan efek suara sintetis">
          <span>🔊</span> <span id="audioLabel">Audio SFX: Aktif</span>
        </button>
        <button class="toggle-pill" id="btnFullscreen" title="Layar Penuh untuk Presentasi">
          <span>⛶</span> <span>Layar Penuh</span>
        </button>
      </div>
    </header>

    <!-- VECTOR SELECTOR TABS -->
    <nav class="vector-nav" aria-label="Navigasi Vektor">
      <button class="v-tab active" data-v="matrix">
        <div class="v-tab-icon">🗺️</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Overview Kill Chain</span>
          <span class="v-tab-sub">Matriks 4 Vektor Serentak</span>
        </div>
      </button>

      <button class="v-tab" data-v="1">
        <div class="v-tab-icon">📱</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Vektor 1: Banking Trojan</span>
          <span class="v-tab-sub">Overlay &amp; Accessibility Abuse</span>
        </div>
      </button>

      <button class="v-tab" data-v="2">
        <div class="v-tab-icon">🎣</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Vektor 2: Phishing &amp; ATO</span>
          <span class="v-tab-sub">Social Eng. &amp; Typosquatting</span>
        </div>
      </button>

      <button class="v-tab" data-v="3a">
        <div class="v-tab-icon">📡</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Vektor 3A: MitM Attack</span>
          <span class="v-tab-sub">Rogue WiFi &amp; SSL Stripping</span>
        </div>
      </button>

      <button class="v-tab" data-v="3b">
        <div class="v-tab-icon">⚡</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Vektor 3B: API Exploitation</span>
          <span class="v-tab-sub">BOLA/IDOR &amp; Mass Extraction</span>
        </div>
      </button>

      <button class="v-tab" data-v="def">
        <div class="v-tab-icon">🛡️</div>
        <div class="v-tab-info">
          <span class="v-tab-name">Defense in Depth</span>
          <span class="v-tab-sub">4 Pilar &amp; Backup 3-2-1 WORM</span>
        </div>
      </button>
    </nav>

    <!-- VIEWS CONTAINER -->
    <div class="view-container">

      <!-- VIEW 1: PANORAMA KILL CHAIN MATRIX (OVERVIEW) -->
      <div class="view-tab-content active" id="view-matrix">
        <div class="panorama-view">
          <div class="matrix-header">
            <div class="matrix-title">
              <h2>DIAGRAM ALUR SERANGAN (KILL CHAIN) — PER VEKTOR</h2>
              <p>Visualisasi tahapan serangan dari reconnaissance hingga impact pada Aplikasi Dompet Digital (Modul 02 Halaman 3)</p>
            </div>
            <div class="btn-group">
              <button class="ctrl-btn primary" id="btnRunPanoramaFlow">▶ Simulasikan Alur Serangan</button>
              <button class="ctrl-btn" id="btnResetPanorama">↺ Reset Alur</button>
            </div>
          </div>

          <div id="panoramaRows">
            <!-- Rendered by JS from PANORAMA_JSON -->
          </div>
        </div>
      </div>

      <!-- VIEW 2: INTERACTIVE STEPPER FOR VECTOR 1, 2, 3A, 3B -->
      <div class="view-tab-content" id="view-interactive">
        <div class="interactive-layout">
          
          <!-- LEFT TIMELINE -->
          <aside class="panel">
            <div class="timeline-title">
              <span>Tahapan Kill Chain</span>
              <span id="stepCounterBadge">1 / 7</span>
            </div>
            <div class="steps-list" id="stepListContainer">
              <!-- Rendered by JS -->
            </div>
          </aside>

          <!-- CENTER STAGE -->
          <section class="panel stage-panel">
            <div class="stage-header">
              <div class="stage-title-wrap">
                <h2 id="stageTitle">Memuat Tahap...</h2>
              </div>
              <div class="stage-meta">
                <button class="mode-switch-btn" id="btnToggleDefenseStage">
                  <span>🛡️</span> <span id="defenseToggleLabel">Lihat Titik Intervensi Mitigasi</span>
                </button>
                <span class="status-tag" id="stageStatusTag">TAHAP SERANGAN</span>
              </div>
            </div>

            <!-- SVG STAGE CANVAS -->
            <div class="canvas-container">
              <svg class="svg-scene" id="svgCanvas" viewBox="0 0 820 400" role="img" aria-label="Visualisasi Serangan">
                <defs>
                  <linearGradient id="phoneGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#1e293b"/>
                    <stop offset="100%" stop-color="#0b1329"/>
                  </linearGradient>
                  <linearGradient id="screenGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#0f172a"/>
                    <stop offset="100%" stop-color="#020617"/>
                  </linearGradient>
                  <linearGradient id="hackerGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#3b0764"/>
                    <stop offset="100%" stop-color="#090514"/>
                  </linearGradient>
                  <linearGradient id="serverGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#1e293b"/>
                    <stop offset="100%" stop-color="#0f172a"/>
                  </linearGradient>
                  <filter id="glowV1">
                    <feGaussianBlur stdDeviation="3.5" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="glowV2">
                    <feGaussianBlur stdDeviation="3.5" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="glowV3a">
                    <feGaussianBlur stdDeviation="3.5" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="glowV3b">
                    <feGaussianBlur stdDeviation="3.5" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                  <filter id="glowGreen">
                    <feGaussianBlur stdDeviation="3.5" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                </defs>
                <g id="svgContentLayer"></g>
              </svg>
            </div>

            <!-- CONTROLS STRIP -->
            <div class="controls-strip">
              <div class="btn-group">
                <button class="ctrl-btn" id="btnPrevStep">← Sebelumnya</button>
                <button class="ctrl-btn primary" id="btnPlayStep">▶ Putar Otomatis</button>
                <button class="ctrl-btn" id="btnNextStep">Selanjutnya →</button>
              </div>

              <div class="dots-nav" id="dotsContainer">
                <!-- Dots rendered by JS -->
              </div>

              <div class="btn-group">
                <select class="speed-select" id="speedSelect" title="Kecepatan Putar">
                  <option value="5000">Kecepatan: 1x (5s)</option>
                  <option value="3500">Kecepatan: 1.5x (3.5s)</option>
                  <option value="2500">Kecepatan: 2x (2.5s)</option>
                </select>
                <button class="ctrl-btn" id="btnResetStep">↺ Ulang</button>
              </div>
            </div>
          </section>

          <!-- RIGHT DETAIL DRAWER -->
          <aside class="panel detail-panel">
            <div class="detail-section-title">
              <span>📖 Penjelasan Teknis</span>
            </div>
            <div class="explanation-box" id="stepExplanation">
              Memuat penjelasan alur teknis...
            </div>

            <div class="analogy-box" id="stepAnalogy" style="display:none;">
              <strong>💡 Analogi Sederhana:</strong>
              <div id="stepAnalogyText">Analogi...</div>
            </div>

            <div class="detail-section-title">
              <span>🎯 Dampak CIA Triad</span>
            </div>
            <div class="triad-bar">
              <div class="triad-item">
                <div class="triad-name">Kerahasiaan (C)</div>
                <div class="triad-status" id="triadC">-</div>
              </div>
              <div class="triad-item">
                <div class="triad-name">Integritas (I)</div>
                <div class="triad-status" id="triadI">-</div>
              </div>
              <div class="triad-item">
                <div class="triad-name">Ketersediaan (A)</div>
                <div class="triad-status" id="triadA">-</div>
              </div>
            </div>

            <div class="detail-section-title">
              <span>🔑 Istilah &amp; Parameter Kunci</span>
            </div>
            <div class="terms-card" id="termsContainer">
              <!-- Rendered by JS -->
            </div>

            <!-- CHECKPOINT QUIZ -->
            <div class="quiz-card" id="quizContainer">
              <div class="quiz-title">
                <span>⚡ Checkpoint Evaluasi Audiens</span>
              </div>
              <div class="quiz-question" id="quizQuestionText">Pertanyaan kuis?</div>
              <div class="quiz-options" id="quizOptionsContainer"></div>
              <div class="quiz-feedback" id="quizFeedbackBox"></div>
            </div>
          </aside>

        </div>
      </div>

      <!-- VIEW 3: DEFENSE IN DEPTH & BACKUP 3-2-1 -->
      <div class="view-tab-content" id="view-defense">
        <div class="defense-view">
          <div class="matrix-header">
            <div class="matrix-title">
              <h2>RANCANGAN KONTROL PERTAHANAN BERLAPIS (DEFENSE-IN-DEPTH)</h2>
              <p>Strategi Pengamanan Holistik E-Wallet: Teknologi, Operasional, Tata Kelola &amp; Skema Pencadangan (Modul 02 Bab 3)</p>
            </div>
          </div>

          <div class="defense-grid" id="defensePillarsContainer">
            <!-- Rendered by JS -->
          </div>
        </div>
      </div>

    </div>

    <!-- FOOTER -->
    <footer>
      <div>
        <strong>Acuan Standar &amp; Regulasi:</strong> POJK 11/POJK.03/2022 &bull; UU PDP No. 27/2022 &bull; PCI-DSS v4.0.1 Req 4 &amp; 6 &bull; OWASP API Security 2023 &bull; NIST CSF 2.0
      </div>
      <div>
        <span>Topik Khusus SC &amp; KV &bull; Kelompok 05 UNDIP 2026</span>
      </div>
    </footer>
  </div>

  <!-- TEAM MEMBERS MODAL -->
  <div class="modal-backdrop" id="teamModal">
    <div class="modal-box">
      <div class="modal-head">
        <h3>Kelompok 05 — Anggota Tim</h3>
        <button class="modal-close" id="btnCloseTeamModal">&times;</button>
      </div>
      <p style="font-size: 0.8rem; color: var(--text-muted);">
        Tugas Analisis Kasus Mandiri: Threat Landscape, Diagram Alur Serangan (Kill Chain) &amp; Defense in Depth pada Aplikasi Dompet Digital.
      </p>
      <div class="team-member-grid">
        <div class="member-item">
          <div class="member-name">Christiano Bryan Budiiman</div>
          <div class="member-nim">24060123130079</div>
        </div>
        <div class="member-item">
          <div class="member-name">Cipta Fikri Wiratama</div>
          <div class="member-nim">24060123140172</div>
        </div>
        <div class="member-item">
          <div class="member-name">Khairiya Fatih Izzudin Emarin</div>
          <div class="member-nim">24060123140166</div>
        </div>
        <div class="member-item">
          <div class="member-name">Dewangga Ramadhan Halim</div>
          <div class="member-nim">24060124130118</div>
        </div>
        <div class="member-item" style="grid-column: span 2;">
          <div class="member-name">Moses Morell Yosefan</div>
          <div class="member-nim">24060124130094</div>
        </div>
      </div>
      <div style="font-size: 0.78rem; color: #cbd5e1; border-top: 1px solid var(--line); padding-top: 0.75rem;">
        <strong>Dosen Pengampu:</strong> Guruh Aryotejo, S.Kom., M.Sc.<br />
        Departemen Informatika &bull; Fakultas Sains dan Matematika &bull; Universitas Diponegoro 2026
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    const SCENARIOS = ''' + SCENARIOS_JSON + ''';
    const PANORAMA = ''' + PANORAMA_JSON + ''';
    const DEFENSE_PILLARS = ''' + DEFENSE_PILLARS_JSON + ''';

    // APP STATE
    let currentView = 'matrix'; // 'matrix', 'interactive', 'defense'
    let currentVectorKey = '1';
    let currentStepIdx = 0;
    let isDefenseMode = false;
    let isAnalogyMode = false;
    let isAudioEnabled = true;
    let autoPlayTimer = null;
    let panoramaTimer = null;
    let audioCtx = null;

    // AUDIO SYNTHESIS
    function playBeep(freq = 440, type = 'sine', duration = 0.08) {
      if (!isAudioEnabled) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {}
    }

    // DOM ELEMENTS
    const dom = {
      views: {
        matrix: document.getElementById('view-matrix'),
        interactive: document.getElementById('view-interactive'),
        defense: document.getElementById('view-defense')
      },
      vTabs: document.querySelectorAll('.v-tab'),
      panoramaRows: document.getElementById('panoramaRows'),
      btnRunPanoramaFlow: document.getElementById('btnRunPanoramaFlow'),
      btnResetPanorama: document.getElementById('btnResetPanorama'),
      stepCounterBadge: document.getElementById('stepCounterBadge'),
      stepListContainer: document.getElementById('stepListContainer'),
      stageTitle: document.getElementById('stageTitle'),
      stageStatusTag: document.getElementById('stageStatusTag'),
      btnToggleDefenseStage: document.getElementById('btnToggleDefenseStage'),
      defenseToggleLabel: document.getElementById('defenseToggleLabel'),
      svgCanvas: document.getElementById('svgCanvas'),
      svgContentLayer: document.getElementById('svgContentLayer'),
      btnPrevStep: document.getElementById('btnPrevStep'),
      btnPlayStep: document.getElementById('btnPlayStep'),
      btnNextStep: document.getElementById('btnNextStep'),
      btnResetStep: document.getElementById('btnResetStep'),
      dotsContainer: document.getElementById('dotsContainer'),
      speedSelect: document.getElementById('speedSelect'),
      stepExplanation: document.getElementById('stepExplanation'),
      stepAnalogy: document.getElementById('stepAnalogy'),
      stepAnalogyText: document.getElementById('stepAnalogyText'),
      triadC: document.getElementById('triadC'),
      triadI: document.getElementById('triadI'),
      triadA: document.getElementById('triadA'),
      termsContainer: document.getElementById('termsContainer'),
      quizContainer: document.getElementById('quizContainer'),
      quizQuestionText: document.getElementById('quizQuestionText'),
      quizOptionsContainer: document.getElementById('quizOptionsContainer'),
      quizFeedbackBox: document.getElementById('quizFeedbackBox'),
      defensePillarsContainer: document.getElementById('defensePillarsContainer'),
      btnAnalogy: document.getElementById('btnAnalogy'),
      analogyLabel: document.getElementById('analogyLabel'),
      btnAudio: document.getElementById('btnAudio'),
      audioLabel: document.getElementById('audioLabel'),
      btnFullscreen: document.getElementById('btnFullscreen'),
      teamModal: document.getElementById('teamModal'),
      btnTeamModal: document.getElementById('btnTeamModal'),
      btnCloseTeamModal: document.getElementById('btnCloseTeamModal')
    };

    // INIT
    function init() {
      buildPanoramaView();
      buildDefenseView();
      setupEventListeners();
      switchView('matrix');
    }

    // VIEW SWITCHER
    function switchView(viewName, vectorKey = null) {
      currentView = viewName;
      stopAutoPlay();
      stopPanoramaFlow();

      dom.vTabs.forEach(t => {
        const v = t.dataset.v;
        if (viewName === 'matrix' && v === 'matrix') t.classList.add('active');
        else if (viewName === 'defense' && v === 'def') t.classList.add('active');
        else if (viewName === 'interactive' && v === vectorKey) t.classList.add('active');
        else t.classList.remove('active');
      });

      dom.views.matrix.classList.toggle('active', viewName === 'matrix');
      dom.views.interactive.classList.toggle('active', viewName === 'interactive');
      dom.views.defense.classList.toggle('active', viewName === 'defense');

      if (viewName === 'interactive') {
        if (vectorKey) currentVectorKey = vectorKey;
        loadVector(currentVectorKey);
      }
      playBeep(520, 'sine', 0.05);
    }

    // BUILD PANORAMA MATRIX
    function buildPanoramaView() {
      dom.panoramaRows.innerHTML = '';
      PANORAMA.forEach(row => {
        const rowDiv = document.createElement('div');
        rowDiv.className = `matrix-row row-${row.key}`;
        rowDiv.id = `pano-row-${row.key}`;

        let cardsHtml = '';
        row.stages.forEach((st, idx) => {
          cardsHtml += `
            <div class="flow-card" id="flow-${row.key}-${idx}" onclick="jumpToStage('${row.key}', ${idx})">
              <span class="flow-card-num">${st.no}</span>
              <span class="flow-card-desc">${st.desc}</span>
            </div>
          `;
        });

        cardsHtml += `
          <div class="flow-card-impact" onclick="jumpToStage('${row.key}', 5)">
            <h4>💥 IMPACT</h4>
            <div style="font-size:0.75rem; font-weight:700;">${row.impact.title}</div>
            <div style="font-size:0.7rem; opacity:0.85; margin-top:2px;">${row.impact.desc}</div>
          </div>
        `;

        rowDiv.innerHTML = `
          <div class="row-header">
            <span>${row.title}</span>
            <div style="display:flex; gap:0.4rem;">
              <span class="pill-meta">${row.severity}</span>
              <span class="pill-meta">${row.actor}</span>
            </div>
          </div>
          <div class="row-flow">${cardsHtml}</div>
        `;
        dom.panoramaRows.appendChild(rowDiv);
      });
    }

    function jumpToStage(vKey, stepIdx) {
      switchView('interactive', vKey);
      renderStep(stepIdx);
    }

    // PANORAMA FLOW SIMULATION
    function runPanoramaSimulation() {
      stopPanoramaFlow();
      dom.btnRunPanoramaFlow.textContent = '⏸ Jeda Simulasi';
      playBeep(600, 'triangle', 0.1);

      let step = 0;
      const totalSteps = 6;
      panoramaTimer = setInterval(() => {
        document.querySelectorAll('.flow-card, .flow-card-impact').forEach(el => el.classList.remove('flow-active'));
        if (step >= totalSteps) {
          stopPanoramaFlow();
          return;
        }

        PANORAMA.forEach(row => {
          const card = document.getElementById(`flow-${row.key}-${step}`);
          if (card) card.classList.add('flow-active');
          else if (step === 5) {
            const imp = document.querySelector(`#pano-row-${row.key} .flow-card-impact`);
            if (imp) imp.classList.add('flow-active');
          }
        });
        playBeep(350 + step * 70, 'sine', 0.08);
        step++;
      }, 1000);
    }

    function stopPanoramaFlow() {
      if (panoramaTimer) {
        clearInterval(panoramaTimer);
        panoramaTimer = null;
      }
      dom.btnRunPanoramaFlow.textContent = '▶ Simulasikan Alur Serangan';
      document.querySelectorAll('.flow-card, .flow-card-impact').forEach(el => el.classList.remove('flow-active'));
    }

    // BUILD DEFENSE VIEW
    function buildDefenseView() {
      dom.defensePillarsContainer.innerHTML = '';
      DEFENSE_PILLARS.forEach(pillar => {
        const card = document.createElement('div');
        card.className = 'def-card';
        card.innerHTML = `
          <div class="def-card-head">
            <span>${pillar.icon}</span>
            <span>${pillar.title}</span>
          </div>
          <p style="font-size:0.75rem; color:var(--text-dim);">${pillar.subtitle}</p>
          <ul class="def-list">
            ${pillar.items.map(it => `<li><strong>${it.label}:</strong> ${it.desc}</li>`).join('')}
          </ul>
        `;
        dom.defensePillarsContainer.appendChild(card);
      });
    }

    // LOAD VECTOR IN INTERACTIVE STAGE
    function loadVector(key) {
      const scenario = SCENARIOS[key];
      if (!scenario) return;

      document.documentElement.style.setProperty('--accent', `var(--v${key.replace('.', '')}-accent, ${scenario.accentColor})`);
      document.documentElement.style.setProperty('--accent-bg', scenario.accentBg);

      // Render Steps in Left List
      dom.stepListContainer.innerHTML = '';
      scenario.steps.forEach((st, idx) => {
        const item = document.createElement('button');
        item.className = 'step-item' + (idx === 0 ? ' active' : '');
        item.innerHTML = `
          <div class="step-badge-no">${idx + 1}</div>
          <div class="step-item-body">
            <span class="step-item-title">${st.title}</span>
            <span class="step-item-status">${st.statusText}</span>
          </div>
        `;
        item.addEventListener('click', () => {
          stopAutoPlay();
          renderStep(idx);
        });
        dom.stepListContainer.appendChild(item);
      });

      // Render Progress Dots
      dom.dotsContainer.innerHTML = '';
      scenario.steps.forEach((_, idx) => {
        const dot = document.createElement('button');
        dot.className = 'dot-step' + (idx === 0 ? ' active' : '');
        dot.title = `Pindah ke langkah ${idx + 1}`;
        dot.addEventListener('click', () => {
          stopAutoPlay();
          renderStep(idx);
        });
        dom.dotsContainer.appendChild(dot);
      });

      isDefenseMode = false;
      dom.btnToggleDefenseStage.classList.remove('defense-active');
      dom.defenseToggleLabel.textContent = 'Lihat Titik Intervensi Mitigasi';

      renderStep(0);
    }

    // RENDER STEP IN STAGE
    function renderStep(idx) {
      const scenario = SCENARIOS[currentVectorKey];
      if (!scenario || !scenario.steps[idx]) return;

      currentStepIdx = idx;
      const step = scenario.steps[idx];

      // Left List & Dots Update
      document.querySelectorAll('.step-item').forEach((it, i) => {
        it.classList.toggle('active', i === idx);
        if (i === idx) it.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
      document.querySelectorAll('.dot-step').forEach((dt, i) => dt.classList.toggle('active', i === idx));

      dom.stepCounterBadge.textContent = `${idx + 1} / ${scenario.steps.length}`;
      dom.stageTitle.textContent = `${idx + 1}. ${step.title}`;
      dom.stageStatusTag.textContent = step.statusText;
      dom.stageStatusTag.className = `status-tag ${step.statusCls}`;

      // Explanation & Analogy
      dom.stepExplanation.textContent = isDefenseMode && step.defenseDesc ? step.defenseDesc : step.desc;
      if (step.analogy) {
        dom.stepAnalogy.style.display = isAnalogyMode ? 'block' : 'none';
        dom.stepAnalogyText.textContent = step.analogy;
      } else {
        dom.stepAnalogy.style.display = 'none';
      }

      // CIA Triad
      dom.triadC.textContent = step.triad.c.text;
      dom.triadC.className = `triad-status ${step.triad.c.cls}`;
      dom.triadI.textContent = step.triad.i.text;
      dom.triadI.className = `triad-status ${step.triad.i.cls}`;
      dom.triadA.textContent = step.triad.a.text;
      dom.triadA.className = `triad-status ${step.triad.a.cls}`;

      // Terms
      dom.termsContainer.innerHTML = step.terms.map(([k, v]) => `
        <div class="term-row">
          <span class="term-key">${k}</span>
          <span class="term-val">${v}</span>
        </div>
      `).join('');

      // Quiz
      renderQuiz(step.quiz);

      // SVG Scene Render
      dom.svgContentLayer.innerHTML = isDefenseMode && step.defenseSvg ? step.defenseSvg : step.svg;

      // Prev/Next button states
      dom.btnPrevStep.disabled = idx === 0;
      dom.btnNextStep.disabled = idx === scenario.steps.length - 1;

      playBeep(480 + idx * 30, 'sine', 0.05);
    }

    function renderQuiz(quiz) {
      if (!quiz) {
        dom.quizContainer.style.display = 'none';
        return;
      }
      dom.quizContainer.style.display = 'flex';
      dom.quizQuestionText.textContent = quiz.q;
      dom.quizFeedbackBox.className = 'quiz-feedback';
      dom.quizFeedbackBox.textContent = '';
      dom.quizOptionsContainer.innerHTML = '';

      quiz.options.forEach((opt, oIdx) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-opt-btn';
        btn.textContent = opt;
        btn.addEventListener('click', () => {
          const isCorrect = oIdx === quiz.correct;
          Array.from(dom.quizOptionsContainer.children).forEach((b, i) => {
            b.disabled = true;
            if (i === quiz.correct) b.classList.add('correct');
            else if (i === oIdx) b.classList.add('wrong');
          });

          if (isCorrect) {
            dom.quizFeedbackBox.textContent = '✔ Tepat! ' + quiz.feedback;
            dom.quizFeedbackBox.className = 'quiz-feedback show ok';
            playBeep(650, 'triangle', 0.12);
          } else {
            dom.quizFeedbackBox.textContent = '✖ Kurang tepat. ' + quiz.feedback;
            dom.quizFeedbackBox.className = 'quiz-feedback show fail';
            playBeep(220, 'sawtooth', 0.15);
          }
        });
        dom.quizOptionsContainer.appendChild(btn);
      });
    }

    // NAVIGATION CONTROLS
    function nextStep() {
      const scenario = SCENARIOS[currentVectorKey];
      if (currentStepIdx < scenario.steps.length - 1) {
        renderStep(currentStepIdx + 1);
      } else {
        stopAutoPlay();
      }
    }

    function prevStep() {
      if (currentStepIdx > 0) renderStep(currentStepIdx - 1);
    }

    function toggleAutoPlay() {
      if (autoPlayTimer) {
        stopAutoPlay();
        return;
      }
      dom.btnPlayStep.textContent = '⏸ Jeda Otomatis';
      const speed = parseInt(dom.speedSelect.value, 10) || 5000;
      autoPlayTimer = setInterval(() => {
        const scenario = SCENARIOS[currentVectorKey];
        if (currentStepIdx >= scenario.steps.length - 1) {
          stopAutoPlay();
          return;
        }
        nextStep();
      }, speed);
    }

    function stopAutoPlay() {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
      dom.btnPlayStep.textContent = '▶ Putar Otomatis';
    }

    // EVENT LISTENERS
    function setupEventListeners() {
      // Vector Tabs
      dom.vTabs.forEach(t => {
        t.addEventListener('click', () => {
          const v = t.dataset.v;
          if (v === 'matrix') switchView('matrix');
          else if (v === 'def') switchView('defense');
          else switchView('interactive', v);
        });
      });

      // Stepper Controls
      dom.btnNextStep.addEventListener('click', nextStep);
      dom.btnPrevStep.addEventListener('click', prevStep);
      dom.btnResetStep.addEventListener('click', () => {
        stopAutoPlay();
        renderStep(0);
      });
      dom.btnPlayStep.addEventListener('click', toggleAutoPlay);

      // Defense Toggle Button
      dom.btnToggleDefenseStage.addEventListener('click', () => {
        isDefenseMode = !isDefenseMode;
        dom.btnToggleDefenseStage.classList.toggle('defense-active', isDefenseMode);
        dom.defenseToggleLabel.textContent = isDefenseMode ? 'Kembali ke Alur Serangan' : 'Lihat Titik Intervensi Mitigasi';
        renderStep(currentStepIdx);
        playBeep(isDefenseMode ? 620 : 420, 'sine', 0.08);
      });

      // Analogy Mode Toggle
      dom.btnAnalogy.addEventListener('click', () => {
        isAnalogyMode = !isAnalogyMode;
        dom.btnAnalogy.classList.toggle('active', isAnalogyMode);
        dom.analogyLabel.textContent = isAnalogyMode ? 'Mode Analogi: Aktif' : 'Mode Analogi: Nonaktif';
        renderStep(currentStepIdx);
        playBeep(550, 'triangle', 0.06);
      });

      // Audio Toggle
      dom.btnAudio.addEventListener('click', () => {
        isAudioEnabled = !isAudioEnabled;
        dom.btnAudio.classList.toggle('active', isAudioEnabled);
        dom.audioLabel.textContent = isAudioEnabled ? 'Audio SFX: Aktif' : 'Audio SFX: Hening';
        if (isAudioEnabled) playBeep(500, 'sine', 0.08);
      });

      // Fullscreen Toggle
      dom.btnFullscreen.addEventListener('click', () => {
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        } else {
          document.exitFullscreen().catch(() => {});
        }
      });

      // Panorama Controls
      dom.btnRunPanoramaFlow.addEventListener('click', () => {
        if (panoramaTimer) stopPanoramaFlow();
        else runPanoramaSimulation();
      });
      dom.btnResetPanorama.addEventListener('click', stopPanoramaFlow);

      // Modal Controls
      dom.btnTeamModal.addEventListener('click', () => dom.teamModal.classList.add('open'));
      dom.btnCloseTeamModal.addEventListener('click', () => dom.teamModal.classList.remove('open'));
      dom.teamModal.addEventListener('click', (e) => {
        if (e.target === dom.teamModal) dom.teamModal.classList.remove('open');
      });

      // Keyboard navigation
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') dom.teamModal.classList.remove('open');
        if (currentView === 'interactive') {
          if (e.key === 'ArrowRight') nextStep();
          if (e.key === 'ArrowLeft') prevStep();
          if (e.key === ' ') {
            e.preventDefault();
            toggleAutoPlay();
          }
        }
      });
    }

    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
''')
    print("Successfully generated index.html")

if __name__ == '__main__':
    generate_html()
