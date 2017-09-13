import json

settings_json = json.dumps([

    {
        "type": "bool",
        "title": "Use local time",
        "section": "General",
        "key": "local"
    },
    {

        "type": "numeric",
        "title": "Update time",
        "desc": "Time in seconds. Set to 0 to disable autoupdate.",
        "section": "General",
        "key": "time"
    }
])