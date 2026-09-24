import json
import os
import re

DIMENSIONS = [
    "iq",
    "eq",
    "aiq",
    "programming_iq",
    "problem_solving_iq",
    "communication_iq",
    "critical_thinking_iq",
    "creativity_iq",
    "adaptability_iq",
    "job_readiness_iq",
    "interview_iq",
    "sales_iq",
    "marketing_iq",
    "leadership_iq",
    "teamwork_iq",
    "time_priority_iq",
    "business_iq",
    "promotion_readiness_iq",
    "learning_agility_iq",
    "ethics_judgment_iq"
]

def make_q(id_num, difficulty, category, scenario, question, options_data, weights, time_rec, explanation, dev_insight, industry_tags, micro_scenario=None):
    assert len(options_data) == 4, f"Question {id_num} must have 4 options"
    # validate weights
    w_sum = sum(weights.values())
    assert 95 <= w_sum <= 105, f"Weights sum for Q{id_num} should be ~100, got {w_sum}"
    for k in weights:
        assert k in DIMENSIONS, f"Invalid dimension {k} in Q{id_num}"
    
    options = []
    for idx, (label, text, scores, risk, action_type) in enumerate(options_data):
        options.append({
            "key": label,
            "text": text,
            "scores": scores,
            "risk": risk,
            "actionType": action_type
        })
        
    return {
        "id": id_num,
        "difficulty": difficulty, # 1: Foundation, 2: Professional, 3: Industry, 4: Advanced, 5: Executive
        "category": category,
        "scenario": scenario,
        "question": question,
        "options": options,
        "dimensionWeights": weights,
        "timeRecommendation": time_rec,
        "explanation": explanation,
        "developmentInsight": dev_insight,
        "industryTags": industry_tags,
        "ageSuitability": ["All"],
        "stageSuitability": ["All"],
        "microScenario": micro_scenario
    }

print("Generator module loaded")
