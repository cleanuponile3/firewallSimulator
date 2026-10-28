
import random# generate random IP addresses and check against firewall rules


def generate_random_ip() -> str:
    """Generates a random IP address in the 192.168.1.x range."""
    return f"192.168.1.{random.randint(0, 20)}"


def check_firewall_rules(ip_address: str, firewall_rules: dict[str, str]) -> str:
    """Checks firewall rules for an IP; defaults to 'allow' if not found."""
    return firewall_rules.get(ip_address, "allow")


def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.17": "block",
        "192.168.1.19": "block",
    }

    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random Number: {random_number}")


if __name__ == "__main__":
    main()
