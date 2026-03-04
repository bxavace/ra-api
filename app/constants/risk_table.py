RISK_TABLE =[
    {"Total Probability": "High", "Impact": "High", "Concat.": "HighHigh", "Risk": "High"},
    {"Total Probability": "High", "Impact": "Low", "Concat.": "HighLow", "Risk": "Low"},
    {"Total Probability": "High", "Impact": "Moderate", "Concat.": "HighModerate", "Risk": "Moderate"},
    {"Total Probability": "High", "Impact": "None", "Concat.": "HighNone", "Risk": "None"},
    {"Total Probability": "High", "Impact": "Very High", "Concat.": "HighVery High", "Risk": "Very High"},
    {"Total Probability": "High", "Impact": "Very Low", "Concat.": "HighVery Low", "Risk": "Very Low"},
    
    {"Total Probability": "Low", "Impact": "High", "Concat.": "LowHigh", "Risk": "Low"},
    {"Total Probability": "Low", "Impact": "Low", "Concat.": "LowLow", "Risk": "Low"},
    {"Total Probability": "Low", "Impact": "Moderate", "Concat.": "LowModerate", "Risk": "Low"},
    {"Total Probability": "Low", "Impact": "None", "Concat.": "LowNone", "Risk": "None"},
    {"Total Probability": "Low", "Impact": "Very High", "Concat.": "LowVery High", "Risk": "Moderate"},
    {"Total Probability": "Low", "Impact": "Very Low", "Concat.": "LowVery Low", "Risk": "Very Low"},
    
    {"Total Probability": "Moderate", "Impact": "High", "Concat.": "ModerateHigh", "Risk": "Moderate"},
    {"Total Probability": "Moderate", "Impact": "Low", "Concat.": "ModerateLow", "Risk": "Low"},
    {"Total Probability": "Moderate", "Impact": "Moderate", "Concat.": "ModerateModerate", "Risk": "Moderate"},
    {"Total Probability": "Moderate", "Impact": "None", "Concat.": "ModerateNone", "Risk": "None"},
    {"Total Probability": "Moderate", "Impact": "Very High", "Concat.": "ModerateVery High", "Risk": "High"},
    {"Total Probability": "Moderate", "Impact": "Very Low", "Concat.": "ModerateVery Low", "Risk": "Very Low"},
    
    {"Total Probability": "None", "Impact": "High", "Concat.": "NoneHigh", "Risk": "None"},
    {"Total Probability": "None", "Impact": "Low", "Concat.": "NoneLow", "Risk": "None"},
    {"Total Probability": "None", "Impact": "Moderate", "Concat.": "NoneModerate", "Risk": "None"},
    {"Total Probability": "None", "Impact": "None", "Concat.": "NoneNone", "Risk": "None"},
    {"Total Probability": "None", "Impact": "Very High", "Concat.": "NoneVery High", "Risk": "None"},
    {"Total Probability": "None", "Impact": "Very Low", "Concat.": "NoneVery Low", "Risk": "None"},
    
    {"Total Probability": "Very High", "Impact": "High", "Concat.": "Very HighHigh", "Risk": "High"},
    {"Total Probability": "Very High", "Impact": "Low", "Concat.": "Very HighLow", "Risk": "Low"},
    {"Total Probability": "Very High", "Impact": "Moderate", "Concat.": "Very HighModerate", "Risk": "Moderate"},
    {"Total Probability": "Very High", "Impact": "None", "Concat.": "Very HighNone", "Risk": "None"},
    {"Total Probability": "Very High", "Impact": "Very High", "Concat.": "Very HighVery High", "Risk": "Very High"},
    {"Total Probability": "Very High", "Impact": "Very Low", "Concat.": "Very HighVery Low", "Risk": "Very Low"},
    
    {"Total Probability": "Very Low", "Impact": "High", "Concat.": "Very LowHigh", "Risk": "Low"},
    {"Total Probability": "Very Low", "Impact": "Low", "Concat.": "Very LowLow", "Risk": "Very Low"},
    {"Total Probability": "Very Low", "Impact": "Moderate", "Concat.": "Very LowModerate", "Risk": "Very Low"},
    {"Total Probability": "Very Low", "Impact": "None", "Concat.": "Very LowNone", "Risk": "None"},
    {"Total Probability": "Very Low", "Impact": "Very High", "Concat.": "Very LowVery High", "Risk": "Low"},
    {"Total Probability": "Very Low", "Impact": "Very Low", "Concat.": "Very LowVery Low", "Risk": "Very Low"}
]


IMPACT_STATEMENT = {
    "high": "The threat event could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "low": "The threat event could be expected to have a limited adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "moderate": "The threat event could be expected to have a serious adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "very high": "The threat event could be expected to have multiple severe or catastrophic adverse effects on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "very low": "The threat event could be expected to have a negligible adverse effect on organizational operations, organizational assets, organizational reputation, or a client organization.",
    "none": "The threat event could be expected to have no adverse effect whatsoever on organizational operations, organizational assets, organizational reputation, or a client organization."
}