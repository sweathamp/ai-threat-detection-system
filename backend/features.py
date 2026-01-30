from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "secure", "account",
    "bank", "update", "free", "reward"
]

def extract_features(url: str):
    url = str(url).lower()
    parsed = urlparse(url)

    features = []

    # 1. URL length
    features.append(len(url))

    # 2. Count of dots
    features.append(url.count("."))

    # 3. Count of hyphens
    features.append(url.count("-"))

    # 4. @ symbol present
    features.append(1 if "@" in url else 0)

    # 5. HTTPS present
    features.append(1 if url.startswith("https") else 0)

    # 6. Suspicious keywords count
    keyword_count = sum(1 for k in SUSPICIOUS_KEYWORDS if k in url)
    features.append(keyword_count)

    # 7. IP-based URL
    host = parsed.netloc.replace(".", "")
    features.append(1 if host.isdigit() else 0)

    return features
