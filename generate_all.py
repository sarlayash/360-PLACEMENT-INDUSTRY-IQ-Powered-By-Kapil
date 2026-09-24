import json
import os
import sys

from questions_l1_l2 import get_level1_and_level2
from questions_l3_l4 import get_level3_and_part4
from questions_l5 import get_level4_part2_and_level5
from generate_base import DIMENSIONS

def main():
    q1 = get_level1_and_level2()
    q2 = get_level3_and_part4()
    q3 = get_level4_part2_and_level5()

    all_questions = q1 + q2 + q3

    print(f"Total questions collected: {len(all_questions)}")
    assert len(all_questions) == 100, f"Expected exactly 100 questions, got {len(all_questions)}"

    # Verification checks (Section 43 Question Quality Control)
    ids = set()
    scenarios = set()
    categories = set()
    difficulty_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    dimension_coverage = {dim: 0 for dim in DIMENSIONS}
    industries = set()

    for idx, q in enumerate(all_questions, 1):
        # 1. Unique IDs
        assert q["id"] == idx, f"Question ID mismatch at index {idx}: got {q['id']}"
        assert q["id"] not in ids, f"Duplicate ID: {q['id']}"
        ids.add(q["id"])

        # 2. Unique scenarios
        sc_clean = q["scenario"].strip().lower()
        assert sc_clean not in scenarios, f"Duplicate scenario in Q{q['id']}: {q['scenario'][:40]}"
        scenarios.add(sc_clean)

        # 3. Exactly 4 options with keys A, B, C, D
        assert len(q["options"]) == 4, f"Q{q['id']} must have 4 options"
        keys = [opt["key"] for opt in q["options"]]
        assert keys == ["A", "B", "C", "D"], f"Q{q['id']} options keys invalid: {keys}"

        # 4. Difficulty counts
        diff = q["difficulty"]
        assert diff in difficulty_counts, f"Invalid difficulty {diff} in Q{q['id']}"
        difficulty_counts[diff] += 1

        # Check difficulty bracket
        if 1 <= q["id"] <= 20:
            assert diff == 1, f"Q{q['id']} should be level 1, got {diff}"
        elif 21 <= q["id"] <= 40:
            assert diff == 2, f"Q{q['id']} should be level 2, got {diff}"
        elif 41 <= q["id"] <= 60:
            assert diff == 3, f"Q{q['id']} should be level 3, got {diff}"
        elif 61 <= q["id"] <= 80:
            assert diff == 4, f"Q{q['id']} should be level 4, got {diff}"
        elif 81 <= q["id"] <= 100:
            assert diff == 5, f"Q{q['id']} should be level 5, got {diff}"

        # 5. Dimension coverage
        for dim, weight in q["dimensionWeights"].items():
            dimension_coverage[dim] += weight

        # 6. Industries
        for ind in q["industryTags"]:
            industries.add(ind)

        # 7. Categories
        categories.add(q["category"])

    print("\n--- Validation Succeeded ---")
    print(f"[OK] Exactly 100 questions verified.")
    print(f"[OK] No duplicate questions or scenarios.")
    print(f"[OK] Difficulty levels: {difficulty_counts}")
    print(f"[OK] Industries represented ({len(industries)}): {sorted(list(industries))}")
    print(f"[OK] Categories represented ({len(categories)}): {sorted(list(categories))}")

    # Check that all 20 dimensions have significant weight representation
    print("\nDimension weight representation across 100 questions:")
    for dim, total_w in dimension_coverage.items():
        print(f"  - {dim}: {total_w} points")
        assert total_w >= 100, f"Dimension {dim} under-represented: {total_w}"

    print("[OK] All 20 dimensions receive meaningful coverage!")

    # Write data/questions.json
    out_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(out_dir, "data", "questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Written: {json_path}")

    # Write js/questions-data.js for foolproof offline local-file execution
    js_path = os.path.join(out_dir, "js", "questions-data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("// 360° PLACEMENT & INDUSTRY IQ - Offline Questions Dataset\n")
        f.write("// Powered by SarlaYash Mission\n")
        f.write("window.QUESTIONS_DATA = ")
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
        f.write(";\n")
    print(f"Written: {js_path}")

if __name__ == "__main__":
    main()
