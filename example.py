import torch
from torch.profiler import profile, record_function, ProfilerActivity


with profile(activities=[ProfilerActivity.CPU], record_shapes=True, with_stack=True) as prof:
    with record_function("model_inference"):
        a = torch.ones(5,5)


prof.export_chrome_trace("torchProfile.json")