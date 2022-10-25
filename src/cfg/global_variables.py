def init(base_path):

    # Base Path
    global APP_PATH
    APP_PATH = base_path

    # Init
    global DEFAULT_URL
    global DEFAULT_FIELD1
    global DEFAULT_FIELD2
    global url
    global field1
    global field2
    global font
    global footer

    # Default values
    DEFAULT_URL = "https://url.com/default"
    DEFAULT_FIELD1 = "default value 1"
    DEFAULT_FIELD2 = "default value 2"

    # Variables
    url = DEFAULT_URL
    field1 = DEFAULT_FIELD1
    field2 = DEFAULT_FIELD2
    font = "arial 8"
    footer = "©2022 @probua technologies"
