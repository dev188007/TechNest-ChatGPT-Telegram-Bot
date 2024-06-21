import yaml
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

with open(config_dir / "chat_modes.yml", 'r', encoding='utf8') as f:
    chat_modes = yaml.safe_load(f)

print(chat_modes)