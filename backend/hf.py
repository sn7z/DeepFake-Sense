from huggingface_hub import hf_hub_download

def download_model(path):
    return hf_hub_download(
        repo_id="SyedNumaan/DeepSense",
        filename=path
    )