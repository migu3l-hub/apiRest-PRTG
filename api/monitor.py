import psutil

def dar_uso_memoria():
    return dict(psutil.virtual_memory()._asdict())['percent']

def dar_uso_cpu():
    return psutil.cpu_percent(interval=1)

def dar_uso_disco():
    return psutil.disk_usage('/').percent