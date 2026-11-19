import base64
import json
import pathlib
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
TMP = pathlib.Path("/tmp/ucsub")
PREFIX = "Telegram: @UCIRANIR"


def main():
    selected = json.loads((TMP / "selected.json").read_text(encoding="utf-8"))
    if not selected:
        print("[render] no healthy configs; keeping previous output")
        return

    lines = []
    for i, rec in enumerate(selected, 1):
        name = f"{PREFIX} {i}"
        if rec["proto"] == "vmess":
            obj = dict(rec["vmess"])
            obj["ps"] = name
            encoded = base64.b64encode(json.dumps(obj, ensure_ascii=False).encode("utf-8")).decode()
            lines.append("vmess://" + encoded)
        else:
            lines.append(rec["share"] + "#" + urllib.parse.quote(name, safe=""))

    text = "\n".join(lines) + "\n"
    (ROOT / "output" / "sub.txt").write_text(text, encoding="utf-8")
    (ROOT / "output" / "sub_base64.txt").write_text(
        base64.b64encode(text.encode("utf-8")).decode() + "\n", encoding="utf-8"
    )
    print(f"[render] wrote {len(lines)} configs")


if __name__ == "__main__":
    main()
