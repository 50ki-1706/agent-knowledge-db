import pathlib, re, sys
root = pathlib.Path(".")
files = sorted(
    list(root.glob("agents-md/**/AGENTS.md")) + list(root.glob("skill/**/SKILL.md"))
)
readme = (root / "README.md").read_text()
linked = set(re.findall(r"\(((?:agents-md|skill)/[^)\s]+\.md)\)", readme))
actual = {str(p) for p in files}
missing = actual - linked
extra = linked - actual
errors = []
if missing or extra:
    errors.append(f"index mismatch missing={sorted(missing)} extra={sorted(extra)}")
for path in files:
    text = path.read_text()
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    headings = re.findall(r"^## .+$", body, flags=re.M)
    if headings != ["## 説明", "## 本文", "## 出典"]:
        errors.append(f"{path}: headings {headings}")
    if path.name == "SKILL.md":
        name = path.parent.name
        if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", text):
            errors.append(f"{path}: name must match {name}")
        if "description:" not in text.split("---", 2)[1]:
            errors.append(f"{path}: missing description")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok {len(files)} files")
