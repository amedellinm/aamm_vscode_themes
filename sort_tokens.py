import json
import os
from collections import defaultdict


class TokenColorSettings(dict):
    def __hash__(self) -> int:
        return hash(self["fontStyle"] + ";" + self["foreground"])


def key(dictionary: dict) -> tuple:
    scope = dictionary["scope"]
    if flag := isinstance(scope, list):
        return (flag, len(scope), scope)
    return (flag, scope)


def format_tokens(tokens: list[dict]) -> tuple:
    storage = defaultdict(set)

    for token in tokens:
        stts: dict = token["settings"]
        stts["foreground"] = stts["foreground"].lower()
        stts.setdefault("fontStyle", "")

        if not isinstance(scope := token["scope"], list):
            scope = [scope]

        storage[TokenColorSettings(stts)].update(scope)

    sorted_tokens = [
        {"scope": scope.pop() if len(scope) == 1 else sorted(scope), "settings": stts}
        for stts, scope in storage.items()
    ]

    return sorted(sorted_tokens, key=key)


def main(themes_path: str) -> None:
    for file_path in os.listdir(themes_path):
        file_path = os.path.join(themes_path, file_path)
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                continue

        data["tokenColors"] = format_tokens(data["tokenColors"])

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    main(r".\themes")
