import os
import src.config as config


def create(dir_name: config.Path | str):
    """Create directory if it doesn't exist."""
    
    create_status = False
    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        create_status = True
        
    relative_path = os.path.relpath(dir_name, config.BASE_DIR)
    log = f"Directory '{relative_path}' ".ljust(50, "=")

    if create_status:
        print(f"{log} was created successfully")
    else:
        print(f"{log} already exists")


create(config.DATA_DIR)
create(config.COOKIES_DIR)
