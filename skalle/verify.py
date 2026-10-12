"""Discord interaction signature checks.

Message listening uses the gateway. This verifier is for the optional HTTP
interactions endpoint, which Discord signs with the application's public key.
"""

from __future__ import annotations

import time

from nacl.exceptions import BadSignatureError, CryptoError
from nacl.signing import VerifyKey


def verify_discord_signature(
    public_key_hex: str,
    signature_hex: str,
    timestamp: str,
    body: bytes,
    *,
    max_age_seconds: int = 300,
    now: float | None = None,
) -> bool:
    try:
        sent_at = int(timestamp)
        signature = bytes.fromhex(signature_hex)
        verify_key = VerifyKey(bytes.fromhex(public_key_hex))
    except (TypeError, ValueError, CryptoError):
        return False
    if len(signature) != 64:
        return False
    current = time.time() if now is None else now
    if abs(current - sent_at) > max_age_seconds:
        return False
    try:
        verify_key.verify(timestamp.encode("utf-8") + body, signature)
    except (BadSignatureError, CryptoError, ValueError):
        return False
    return True
