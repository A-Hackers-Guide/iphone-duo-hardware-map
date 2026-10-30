# `/usr/bin/sed`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 88,352 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1608)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (1)

- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (78)

```
%lu: %s: extra characters at the end of %c command
%lu: %s: extra characters after \\ at the end of %c command
%lu: %s: \\%c not defined in the RE
%lu: %s: \\%u not defined in the RE
process.c
\\%03o
w command
read command
%lu: %s: newline can not be used as a string delimiter
123456789
%lu: %s: no wfile specified
%lu: %s: unterminated transform source string
%lu\n
label
%lu: %s: more than one number or 'g' in substitute flags
r
strdup
%lu: %s: command %c expects up to %d address(es), found %d
%lu: %s: unexpected }
\\\n
%lu: %s: RE error: %s
%lu: %s: unescaped newline inside substitute pattern
%lu: %s: unterminated substitute in regular expression
%s\n
advance > 0
%lu: %s: empty label
rename()
\\abfrtv
%lu: %s: command expected
works for regular files
usage: %s script [-EHalnru] [-i extension] [file ...]\n\t%s [-EHalnu] [-i extension] [-e script] ... [-f script_file] ... [file ...]\n
substitute
%s: %s
COLUMNS
malloc
%lu: %s: invalid command code %c
%lu: %s: unterminated transform target string
\"%s\"
%s: name too long
\n
RE error: %s
%lu: %s: whitespace after %s
%lu: %s: unused label '%s'
setting unbuffered output failed
-I or -i may not be used with stdin
%lu: %s: unbalanced brackets ([])
%lu: %s: transform strings are not the same length
%s/.!%ld!%s
%lu: %s: unterminated regular expression
%lu: %s: expected context address
%lu: %s: transform pattern can not be delimited by newline or backslash
setting line buffered output failed
stdin
first RE may not be empty
%lu: %s: unterminated substitute pattern
wfile too long
stdout
fclose()
%lu: %s: unexpected EOF (pending }'s)
%lu: %s: \\ can not be used as a string delimiter
%lu: %s: bad flag in substitute command: '%c'
EHI:ae:f:i:lnru
%s
%lu: %s: substitute pattern can not be delimited by newline or backslash
%lu: %s: overflow in the 'N' substitute flag
%lu: %s: undefined label '%s'
%s: %s %s
\\%c
%lu: %s: command %c expects \\ followed by text
%lu: %s: filename expected
branch
%lu: %s: extra text at the end of a transform command
realloc
w
0123456789/\\$
%lu: %s: duplicate label '%s'
asprintf
in-place editing only
```
