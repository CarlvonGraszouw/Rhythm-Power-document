import base64
import pathlib
import re


def main() -> None:
    src = pathlib.Path(
        r"c:\CURSOR PROJECTS\1. RHYTM POWER DOC\GSM_Data_Logger_ime line and cost.html"
    )
    html = src.read_text(encoding="utf-8", errors="ignore")

    m = re.search(
        r'<img\s+src="data:image/png;base64,([A-Za-z0-9+/=\s]+)"\s+alt="G-Matrix Systems Logo"',
        html,
    )
    if not m:
        raise SystemExit("Could not find embedded logo <img> in source HTML")

    b64 = re.sub(r"\s+", "", m.group(1))
    out = pathlib.Path(r"c:\CURSOR PROJECTS\1. RHYTM POWER DOC\gmatrix-logo.png")
    out.write_bytes(base64.b64decode(b64))
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
