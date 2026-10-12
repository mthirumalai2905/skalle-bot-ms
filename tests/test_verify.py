import time

from nacl.signing import SigningKey

from skalle.verify import verify_discord_signature


def test_accepts_a_current_discord_signature():
    signing_key = SigningKey.generate()
    body = b'{"type":1}'
    timestamp = str(int(time.time()))
    signature = signing_key.sign(timestamp.encode() + body).signature
    assert verify_discord_signature(
        signing_key.verify_key.encode().hex(),
        signature.hex(),
        timestamp,
        body,
    )


def test_rejects_bad_signature_stale_timestamp_and_tampered_body():
    signing_key = SigningKey.generate()
    body = b'{"type":1}'
    timestamp = "1700000000"
    signature = signing_key.sign(timestamp.encode() + body).signature
    public_key = signing_key.verify_key.encode().hex()
    assert verify_discord_signature(public_key, signature.hex(), timestamp, body, now=1700000000)
    assert not verify_discord_signature(public_key, "ab" * 64, timestamp, body, now=1700000000)
    assert not verify_discord_signature(public_key, signature.hex(), timestamp, body, now=1700000000 + 301)
    assert not verify_discord_signature(public_key, signature.hex(), timestamp, b'{"type":2}', now=1700000000)
    assert not verify_discord_signature(public_key, "", timestamp, body, now=1700000000)
