from urllib.parse import urlparse
import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    parsed = urlparse(url)
    netloc = parsed.netloc

    # Feature 1: length_url - length of the URL string
    features.append(len(url))

    # Feature 2: ip - presence of IP address in domain
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    features.append(1 if ip_pattern.fullmatch(netloc) else 0)

    # Feature 3: nb_underscore - count of underscores in URL
    features.append(url.count('_'))

    # Feature 4: nb_tilde - count of tildes in URL
    features.append(url.count('~'))

    # Feature 5: nb_percent - count of percent signs in URL
    features.append(url.count('%'))

    # Feature 6: abnormal_subdomain - heuristic: 1 if any subdomain part length > 10 else 0
    subdomains = netloc.split('.')
    abnormal = 0
    for sub in subdomains[:-2]:  # exclude domain and TLD
        if len(sub) > 10:
            abnormal = 1
            break
    features.append(abnormal)

    # Feature 7: nb_subdomains - count of subdomains (number of dots in netloc minus 1)
    features.append(len(subdomains) - 2 if len(subdomains) > 2 else 0)

    # Feature 8: phish_hints - presence of suspicious words in URL
    suspicious_words = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'signin', 'banking']
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    # Feature 9: login_form - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 10: links_in_tags - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 11: submit_email - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 12: ratio_intMedia - placeholder 0 (requires external data)
    features.append(0)

    # Feature 13: ratio_extMedia - placeholder 0 (requires external data)
    features.append(0)

    # Feature 14: iframe - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 15: popup_window - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 16: safe_anchor - placeholder 1 (assume safe)
    features.append(1)

    # Feature 17: domain_registration_length - placeholder 0 (requires WHOIS)
    features.append(0)

    # Feature 18: domain_age - placeholder 0 (requires WHOIS)
    features.append(0)

    # Removed Feature 19-21 placeholders to match model's expected 18 features

    return features

def extract_features_no_http(url):
    features = []

    parsed = urlparse(url)
    netloc = parsed.netloc

    # Feature 1: length_url - length of the URL string
    features.append(len(url))

    # Feature 2: ip - presence of IP address in domain
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    features.append(1 if ip_pattern.fullmatch(netloc) else 0)

    # Feature 3: nb_underscore - count of underscores in URL
    features.append(url.count('_'))

    # Feature 4: nb_tilde - count of tildes in URL
    features.append(url.count('~'))

    # Feature 5: nb_percent - count of percent signs in URL
    features.append(url.count('%'))

    # Feature 6: abnormal_subdomain - heuristic: 1 if any subdomain part length > 10 else 0
    subdomains = netloc.split('.')
    abnormal = 0
    for sub in subdomains[:-2]:  # exclude domain and TLD
        if len(sub) > 10:
            abnormal = 1
            break
    features.append(abnormal)

    # Feature 7: nb_subdomains - count of subdomains (number of dots in netloc minus 1)
    features.append(len(subdomains) - 2 if len(subdomains) > 2 else 0)

    # Feature 8: phish_hints - presence of suspicious words in URL
    suspicious_words = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'signin', 'banking']
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    # Feature 9: login_form - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 10: links_in_tags - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 11: submit_email - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 12: ratio_intMedia - placeholder 0 (requires external data)
    features.append(0)

    # Feature 13: ratio_extMedia - placeholder 0 (requires external data)
    features.append(0)

    # Feature 14: iframe - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 15: popup_window - placeholder 0 (requires HTML content)
    features.append(0)

    # Feature 16: safe_anchor - placeholder 1 (assume safe)
    features.append(1)

    # Feature 17: domain_registration_length - placeholder 0 (requires WHOIS)
    features.append(0)

    # Feature 18: domain_age - placeholder 0 (requires WHOIS)
    features.append(0)

    return features
