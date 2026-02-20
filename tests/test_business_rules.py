from app.services.business_rules import apply_voice_limits

def test_apply_voice_limits():
    data = [{"id": i} for i in range(20)]
    limited = apply_voice_limits(data, limit=5)
    assert len(limited) == 5
