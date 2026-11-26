#!/usr/bin/env python3
"""Check presentation characters, local links and decorative SVG contracts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import re, sys
root=Path(__file__).resolve().parents[1]
# Presentation symbols must use SVG or CSS; platform emoji fonts are not stable.
unstable=re.compile(r"[\u2190-\u21ff\u2600-\u27bf\uFE0F\u20E3\U0001F000-\U0001FAFF]")
errors=[]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=="h1":self.h1+=1
  if "id" in a:self.ids.append(a["id"])
  if tag=="img" and not a.get("alt"):errors.append("image without alt")
  if tag=="svg" and a.get("class","").startswith("glyph-"):
   if a.get("aria-hidden")!="true" or a.get("focusable")!="false":errors.append("decorative SVG must be hidden from assistive technology")
   if not a.get("viewbox") or not a.get("width") or not a.get("height"):errors.append("SVG needs viewBox and explicit dimensions")
  for k in ("href","src","data-day","data-night"):
   if k in a:self.refs.append(a[k])
pages=[]
for f in sorted(root.rglob("*")):
 if not f.is_file() or any(part.startswith(".") for part in f.relative_to(root).parts):continue
 if f.suffix.lower() not in (".html",".css",".js"):continue
 text=f.read_text()
 hit=unstable.search(text)
 if hit:errors.append(f"{f.relative_to(root)}: platform-dependent decorative character U+{ord(hit.group()):04X}; use SVG/CSS")
 if f.suffix!=".html":continue
 p=Page();p.feed(text);pages.append(f)
 if p.h1!=1:errors.append(f"{f.relative_to(root)}: expected one h1")
 if len(set(p.ids))!=len(p.ids):errors.append(f"{f.relative_to(root)}: duplicate IDs")
 for ref in p.refs:
  if ref.startswith("#"):
   if ref[1:] not in p.ids:errors.append(f"{f.relative_to(root)}: broken anchor {ref}")
  elif not urlparse(ref).scheme:
   dest=(f.parent/unquote(ref.split("#",1)[0].split("?",1)[0])).resolve()
   if not dest.is_relative_to(root) or not dest.exists():errors.append(f"{f.relative_to(root)}: missing local resource {ref}")
if errors:
 print("\n".join(errors),file=sys.stderr);sys.exit(1)
print(f"PASS: {len(pages)} pages, platform-stable decorations, SVG accessibility and local references")

