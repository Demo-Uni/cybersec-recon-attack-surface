"""
Recon & Attack Surface Mapping Lab
Use Python tools to discover and map attack surfaces.
"""
import socket
import json


def scan_ports(host: str, ports: list[int]) -> dict[int, str]:
    """Scan given ports on a host and return {port: status} dict.

    Args:
        host: Target hostname or IP
        ports: List of port numbers to scan

    Returns:
        Dict mapping port numbers to 'open' or 'closed'
    """
    # TODO: Implement port scanning using socket.connect_ex()
    pass


def parse_banner(raw_banner: str) -> dict:
    """Parse a service banner string into structured data.

    Args:
        raw_banner: Raw banner text from a service (e.g. "SSH-2.0-OpenSSH_8.9")

    Returns:
        Dict with keys: 'service', 'version', 'extra'
    """
    # TODO: Parse the banner to extract service name and version
    pass


def classify_risk(open_ports: list[int]) -> str:
    """Classify risk level based on open ports.

    High risk ports: 21 (FTP), 23 (Telnet), 3389 (RDP)
    Medium risk ports: 22 (SSH), 3306 (MySQL), 5432 (PostgreSQL)
    Low risk: everything else

    Args:
        open_ports: List of open port numbers

    Returns:
        'high', 'medium', or 'low'
    """
    # TODO: Implement risk classification logic
    pass


def generate_report(host: str, scan_results: dict, risk_level: str) -> str:
    """Generate a JSON security report.

    Args:
        host: Scanned host
        scan_results: Dict of {port: status}
        risk_level: 'high', 'medium', or 'low'

    Returns:
        Pretty-printed JSON string report
    """
    # TODO: Build and return a JSON report
    pass
