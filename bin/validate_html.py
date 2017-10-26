import sys
import html5lib

if len(sys.argv) < 2:
  print("Usage: {} html_files_to_validate".format(sys.argv[0]))
  sys.exit(0)

status = 0
for i in range(1, len(sys.argv)):
  with open(sys.argv[i], "rb") as f:
    parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("dom"), strict=True)
    try:
      document = parser.parse(f)
      print("  HTML5 validation ok: {}".format(sys.argv[i]))
    except:
      status = 1
      print("! HTML5 validation error: {}".format(sys.argv[i]))
      for e in parser.errors:
        print("! Error detected on line: {:d}".format(e[0][0]))
      print("Use http://validator.w3.org/#validate_by_input to check your html.")

sys.exit(status)
