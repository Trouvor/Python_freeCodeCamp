test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(dictSettings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in dictSettings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictSettings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictSettings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in dictSettings:
        dictSettings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(dictSettings, in_key):
    key = in_key.lower()

    if key in dictSettings:
        del dictSettings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    
def view_settings(dictSettings):
    if not dictSettings:
        return "No settings available."
    
    s = "Current User Settings:"
    for key, value in dictSettings.items():
        s += f"\n{key.capitalize()}: {value}"
    
    return s + "\n"