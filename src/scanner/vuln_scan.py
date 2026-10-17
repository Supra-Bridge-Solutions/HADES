"""Small wrapper around the Nmap command line scanner."""

import shutil
import subprocess


def run_nmap_scan(target, timeout=300):
    """Run a basic Nmap scan and return its output.

    Args:
        target: A single host name or IP address accepted by Nmap.
        timeout: Maximum scan duration in seconds.

    Raises:
        FileNotFoundError: If Nmap is not installed or not on PATH.
        subprocess.TimeoutExpired: If the scan exceeds ``timeout``.
        RuntimeError: If Nmap exits with an error.
    """
    if not target or not target.strip():
        raise ValueError("Enter a target host or IP address.")

    nmap_path = shutil.which("nmap")
    if nmap_path is None:
        raise FileNotFoundError("Nmap was not found. Install Nmap and ensure it is on PATH.")

    try:
        result = subprocess.run(
            [nmap_path, target.strip()],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError(f"Nmap scan exceeded the {timeout}-second time limit.") from exc

    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown error"
        raise RuntimeError(f"Nmap scan failed: {detail}")

    return result.stdout.strip()
