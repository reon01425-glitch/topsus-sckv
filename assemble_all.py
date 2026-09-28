# -*- coding: utf-8 -*-
"""
Assembler script to combine all scenario modules and generate the final index.html
"""
import json
from generate_all_scenarios import get_scenarios
from build_vector2 import get_v2
from build_vector3a import get_v3a
from build_vector3b import get_v3b
from scenario_data import PANORAMA, DEFENSE_PILLARS

def assemble():
    print("Combining all 4 vectors...")
    scenarios = {}
    scenarios["1"] = get_scenarios()["1"]
    scenarios["2"] = get_v2()
    scenarios["3a"] = get_v3a()
    scenarios["3b"] = get_v3b()

    print("V1 steps:", len(scenarios["1"]["steps"]))
    print("V2 steps:", len(scenarios["2"]["steps"]))
    print("V3A steps:", len(scenarios["3a"]["steps"]))
    print("V3B steps:", len(scenarios["3b"]["steps"]))

    # Write scenario_data.py
    with open("scenario_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-generated scenario data"""\n\n')
        f.write(f"SCENARIOS_JSON = {json.dumps(json.dumps(scenarios, ensure_ascii=False))}\n\n")
        f.write(f"PANORAMA_JSON = {json.dumps(json.dumps(PANORAMA, ensure_ascii=False))}\n\n")
        f.write(f"DEFENSE_PILLARS_JSON = {json.dumps(json.dumps(DEFENSE_PILLARS, ensure_ascii=False))}\n\n")
    
    print("scenario_data.py updated.")

    # Run build_interactive_app
    import build_interactive_app
    build_interactive_app.generate_html()
    print("index.html successfully updated!")

if __name__ == '__main__':
    assemble()
