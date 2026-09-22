"""Phone Security - educational defensive security starter.

This module intentionally contains safe, local-only functionality.
"""

def security_checklist():
    """Return a short defensive phone-security checklist."""
    return [
        "Use a strong screen lock and enable biometric authentication where appropriate.",
        "Install operating-system and application security updates promptly.",
        "Review app permissions regularly and remove unnecessary access.",
        "Use multi-factor authentication for important accounts.",
        "Avoid installing applications from untrusted sources.",
        "Back up important data using a trusted backup method.",
    ]


def main():
    print("Phone Security — Defensive Checklist")
    print("-" * 40)
    for number, item in enumerate(security_checklist(), 1):
        print(f"{number}. {item}")


if __name__ == "__main__":
    main()
