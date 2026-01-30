from urllib.parse import urlparse

def extract_features(url):
    features = []

    features.append(len(url))                     # URL length
    features.append(url.count('.'))                # Dot count
    features.append(url.count('-'))                # Hyphen count
    features.append(url.count('@'))                # @ symbol
    features.append(url.count('?'))                # ?
    features.append(1 if 'https' in url else 0)    # HTTPS present
    features.append(
        1 if urlparse(url).netloc.replace('.', '').isdigit() else 0
    )  # IP-based URL

    return features
