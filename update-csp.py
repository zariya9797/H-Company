#!/usr/bin/env python3
"""Refresh the CSP hashes after editing the website's inline CSS or scripts."""
import base64
import hashlib
import re
from pathlib import Path

page = Path(__file__).with_name("h-company-website.html")
html = page.read_text(encoding="utf-8")
styles = re.findall(r"<style>(.*?)</style>", html, re.DOTALL)
scripts = re.findall(r"<script(?: [^>]*)?>(.*?)</script>", html, re.DOTALL)
if not styles or not scripts:
    raise SystemExit("Expected inline styles and scripts in the website.")

def hashes(blocks):
    return " ".join(
        "'sha256-" + base64.b64encode(hashlib.sha256(block.encode()).digest()).decode() + "'"
        for block in blocks
    )

policy = (
    "default-src 'none'; img-src 'self' https://images.unsplash.com; "
    f"style-src {hashes(styles)}; script-src {hashes(scripts)}; "
    "base-uri 'none'; form-action 'none'; upgrade-insecure-requests"
)
html, count = re.subn(
    r'<meta http-equiv="Content-Security-Policy" content="[^"]*">',
    lambda match: '<meta http-equiv="Content-Security-Policy" content="' + policy + '">',
    html,
)
if count != 1:
    raise SystemExit("Expected exactly one Content-Security-Policy meta tag.")
page.write_text(html, encoding="utf-8")
