"""第 60 批：推门进山洞，脚步声的尾音在门口被硬切一半，退回走廊又整段消失：混..."""

def crossfade(distance, radius):
    """混响区边界交叉淡入。"""
    raise NotImplementedError("TODO: crossfade")

def bus_route(indoor):
    """室内外总线。"""
    raise NotImplementedError("TODO: bus_route")

def ir_duration(samples, rate):
    """IR 时长。"""
    raise NotImplementedError("TODO: ir_duration")

def send_curve(distance, max_distance):
    """混响发送曲线。"""
    raise NotImplementedError("TODO: send_curve")

def overlap_normalize(total):
    """重叠混响归一。"""
    raise NotImplementedError("TODO: overlap_normalize")

def tail_flush(playing, tail):
    """尾音 flush。"""
    raise NotImplementedError("TODO: tail_flush")

def hrtf_route(spatial):
    """HRTF 顺序。"""
    raise NotImplementedError("TODO: hrtf_route")

def listener_position(camera_pos, listener_pos):
    """听者位置。"""
    raise NotImplementedError("TODO: listener_position")

def ir_source(loaded, placeholder):
    """异步 IR 占位。"""
    raise NotImplementedError("TODO: ir_source")

def occlusion_filter(occluded, cutoff):
    """遮挡低通。"""
    raise NotImplementedError("TODO: occlusion_filter")

def thread_weight(game, audio):
    """线程权重一致。"""
    raise NotImplementedError("TODO: thread_weight")

def cache_version(scene, version):
    """混响缓存键。"""
    raise NotImplementedError("TODO: cache_version")

def voice_isolation(voice_bus, reverb_bus):
    """语音总线隔离。"""
    raise NotImplementedError("TODO: voice_isolation")
