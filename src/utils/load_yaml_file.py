import yaml

yaml_path="config.yaml"
def load_yaml() -> dict:
    """
    Load a yaml file and return the contents as a dictionary
    """
    with open(yaml_path,'r') as file:
        config=yaml.safe_load(file)
    return config