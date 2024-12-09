import torch

def get_gpu_memory_usage():
    """
    Get current GPU memory usage
    """
    if torch.cuda.is_available():
        return {
            i: torch.cuda.memory_allocated(i) for i in range(torch.cuda.device_count())
        }
    return {}

def clear_gpu_memory():
    """
    Clear GPU memory cache
    """
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
