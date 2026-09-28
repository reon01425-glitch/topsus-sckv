# -*- coding: utf-8 -*-
"""
Compile index.html cleanly from template and scenario_data
"""
import json
import scenario_data

def compile():
    s_obj = json.loads(scenario_data.SCENARIOS_JSON)
    p_obj = json.loads(scenario_data.PANORAMA_JSON)
    d_obj = json.loads(scenario_data.DEFENSE_PILLARS_JSON)

    s_literal = json.dumps(s_obj, ensure_ascii=True)
    p_literal = json.dumps(p_obj, ensure_ascii=True)
    d_literal = json.dumps(d_obj, ensure_ascii=True)

    with open('build_interactive_app.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Isolate template part: between f.write(''' and ''')
    start_marker = "f.write('''"
    end_marker = "''')"
    start_pos = content.find(start_marker) + len(start_marker)
    end_pos = content.rfind(end_marker)

    html = content[start_pos:end_pos]

    # Replace placeholders
    target_data = """    const SCENARIOS = ''' + SCENARIOS_JSON + ''';
    const PANORAMA = ''' + PANORAMA_JSON + ''';
    const DEFENSE_PILLARS = ''' + DEFENSE_PILLARS_JSON + ''';"""

    replacement_data = f"""    const SCENARIOS = {s_literal};
    const PANORAMA = {p_literal};
    const DEFENSE_PILLARS = {d_literal};"""

    if target_data in html:
        html = html.replace(target_data, replacement_data)
        print("Replaced data targets successfully.")
    else:
        print("Warning: target_data exact match not found, looking for alternative markers.")
        html = html.replace("const SCENARIOS = ''' + SCENARIOS_JSON + ''';", f"const SCENARIOS = {s_literal};")
        html = html.replace("const PANORAMA = ''' + PANORAMA_JSON + ''';", f"const PANORAMA = {p_literal};")
        html = html.replace("const DEFENSE_PILLARS = ''' + DEFENSE_PILLARS_JSON + ''';", f"const DEFENSE_PILLARS = {d_literal};")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("index.html compiled successfully! File size:", len(html))

if __name__ == '__main__':
    compile()
