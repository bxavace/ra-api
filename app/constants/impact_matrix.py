# Impact matrix: category -> adverse effect -> value
IMPACT_MATRIX = {
    "Degradation": {
        "completely nonexistent": "none",
        "negligible": "-",
        "limited": "some",
        "serious": "significant",
        "severe or catastrophic": "severe",
        "multiple severe or catastrophic": "severe",
    },
    "Damage": {
        "completely nonexistent": "none",
        "negligible": "-",
        "limited": "minor",
        "serious": "significant",
        "severe or catastrophic": "severe",
        "multiple severe or catastrophic": "severe",
    },
    "Financial Loss": {
        "completely nonexistent": "none",
        "negligible": "-",
        "limited": "minor",
        "serious": "significant",
        "severe or catastrophic": "major",
        "multiple severe or catastrophic": "major",
    },
    "Reputation": {
        "completely nonexistent": "none",
        "negligible": "very low",
        "limited": "minor",
        "serious": "significant",
        "severe or catastrophic": "high",
        "multiple severe or catastrophic": "very high",
    },
}

ORDINAL_EFFECT_DESC = {
    "completely nonexistent": "The threat event could be expected to have no adverse effect whatsoever on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "limited": "The threat event could be expected to have a limited adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "negligible": "The threat event could be expected to have a negligible adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "serious": "The threat event could be expected to have a serious adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "severe or catastrophic": "The threat event could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "multiple severe or catastrophic": "The threat event could be expected to have multiple severe or catastrophic adverse effects on organizational operations, organizational assets, organizational reputation, or a client organization.",
}
