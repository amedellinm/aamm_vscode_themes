INSTRUCTIONS

1 - Clone this repo to wherever your VSC extensions are.
        Example:
            C:\Users\user\.vscode\extensions\
        Once cloned:
            C:\Users\user\.vscode\extensions\aamm_vscode_themes

2 - Update the extensions.json (the VSC extensions file) located in the
    same root folder where you cloned the repo by adding the following
    extension data:
        {
            "identifier": {
                "id": "undefined_publisher.aamm_vscode_themes"
            },
            "location": {
                "$mid": 1,
                "path": [REPO PATH],
                "scheme": "file"
            },
            "metadata": {
                "publisherDisplayName": "AAMM"
            },
            "relativeLocation": "aamm_vscode_themes",
            "version": "1.0.0"
        },

