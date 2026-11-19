import pytest
from audio import reverb_zone as mod

CASES = [
    ("cross", 'm.crossfade(0.5, 1.0) == approx(0.5)'),
    ("bus", 'm.bus_route(True) == "indoor"'),
    ("ir", 'm.ir_duration(48000, 48000) == approx(1.0)'),
    ("send", 'm.send_curve(2.0, 4.0) == approx(0.5)'),
    ("overlap", 'm.overlap_normalize(3.0) == approx(1.0)'),
    ("tail_off", 'm.tail_flush(False, 0.5) == approx(0.0)'),
    ("tail_on", 'm.tail_flush(True, 0.5) == approx(0.5)'),
    ("hrtf", 'm.hrtf_route(True) == "spatial"'),
    ("listener", 'm.listener_position((0.0, 0.0), (1.0, 1.0)) == (1.0, 1.0)'),
    ("ir_missing", 'm.ir_source(False, "placeholder") == "placeholder"'),
    ("ir_loaded", 'm.ir_source(True, "placeholder") == "ir"'),
    ("occlusion", 'm.occlusion_filter(True, 1.0) == approx(0.5)'),
    ("thread", 'm.thread_weight(1.0, 2.0) == approx(2.0)'),
    ("cache", 'm.cache_version("scene", "v1") == "scene:v1"'),
    ("voice", 'm.voice_isolation("voice", "reverb") is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
