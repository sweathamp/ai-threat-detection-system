def get_risk_level(score: float):
    """
    score: probability between 0 and 1
    """
    percentage = int(score * 100)

    if percentage >= 75:
        return "HIGH", percentage
    elif percentage >= 40:
        return "MEDIUM", percentage
    else:
        return "LOW", percentage


def get_impact(risk_level: str):
    if risk_level == "HIGH":
        return [
            "Login details may be collected",
            "Your account could be accessed by someone else",
            "Sensitive data may be misused"
        ]

    if risk_level == "MEDIUM":
        return [
            "The link looks suspicious",
            "There is a chance of data exposure",
            "Proceeding may be unsafe"
        ]

    return [
        "No clear threat detected",
        "However, always stay cautious online"
    ]


def get_recommended_actions(risk_level: str):
    if risk_level == "HIGH":
        return [
            "Do not enter any information",
            "Close this page",
            "Open the official website directly"
        ]

    if risk_level == "MEDIUM":
        return [
            "Avoid entering personal information",
            "Double-check the website address",
            "Proceed only if you trust the source"
        ]

    return [
        "You may continue with caution",
        "Ensure the website address is correct"
    ]
