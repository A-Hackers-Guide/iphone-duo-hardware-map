# `/System/Library/Filesystems/hfs.fs/newfs_hfs`

From the upgrade restore ramdisk (141-29011-104.dmg). 87,984 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1680)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
</dict>
</plist>
```

## Strings (121)

```
 HFS Plus volume
invalid access mask: %s
/dev/
\tcatalog clump size: %u\n
\t-J [journal-size] make this HFS+ volume journaled\n
 case-insensitive
%s: bad HFS Plus allocation block size (must be a power of two)
\tattributes b-tree node size: %u\n
\t\tc=size (catalog b-tree)\n
unknown group id: %s
 HFS Plus volume with a %uk journal\n
\ttotal blocks: %u\n
\t\te=blocks (extents file)\n
\t-i starting catalog node id\n
\t\te=size (extents b-tree)\n
%s: %s
  where hfsplus-options are:\n
Overlapped catalog extent at <%u, %u>\n
a=%ld: initial size is not a multiple of node size\n
\tgroup ID: %d\n
\t-D journal-dev use 'journal-dev' for an external journal\n
%s::pread(%d, %p, %zu, %lld)
cannot create filesystem on %s
a=%ld: initial size is less than clump size\n
\tinitial allocation file size: %u (%u blocks)\n
%d is an unsupported sector size\n
%ld TB
\tuser ID: %d\n
Overlapped extent at <0, 1> (%d)
WriteBuffer
%s: starting catalog node id too small (must be > 15)
Initialized %s as a 
\t\tc=blocks (catalog file)\n
BG:J:D:M:N:PU:hsb:c:i:I:n:v:
Warning:  extents overflow extent requested count %u exceeds maximum 8, capping at 8\n
e=%ld: clump size is not a multiple of node size\n
\t\ta=blocks (attributes file)\n
%ld KB
e=%ld: initial size is not a multiple of node size\n
\tcatalog b-tree node size: %u\n
\taccess mask: %o\n
\tfile system start block: %u\n
\t-N do not create file system, just print out parameters\n
\tblock-size: %u\n
\t-G group-id (for root directory)\n
untitled
%s: bad allocation block size (too large)
 case-sensitive
\tfirst free catalog node id: %u\n
\t%s -v Untitled -n c=4096,e=1024 /dev/rdisk0s7 \n
Overlapped extent at <0, 4> (%d)
Overlapped extent at <0, 2> (%d)
%s: getmntinfo: %s
\t-s use case-sensitive filenames (default is case-insensitive)\n
\t\tb=blocks (bitmap file)\n
Could not copy volume name %s
%s: invalid catalog b-tree node size
%s: invalid extents b-tree node size
%s: invalid atrribute b-tree node size
%s: partition is too small (minimum is %d KB)
%llu sectors (%u bytes per sector)\n
\textents clump size: %u\n
\t-I initial size list (comma separated)\n
c=%ld: initial size is less than clump size\n
\t-v volume name (in ascii or UTF-8)\n
  examples:\n
%ld GB
c=%ld: initial size is not a multiple of node size\n
\tattributes clump size: %u\n
\tinitial attributes file size: %u\n
\tresource fork clump size: %u\n
Warning: block size %u is less than extents b-tree node size %u
\tvolume name: \"%s\"\n
\tdata fork clump size: %u\n
=%ld: too many blocks for initial size!
invalid HFS+ name: \"%s\", using \"%s\" instead
,
  options:\n
\t-M octal access-mask (for root directory)\n
.journal
Warning: %u is a non-optimal block size (4096 would be a better choice)
\textents b-tree node size: %u\n
\tinitial extents file size: %u\n
\t%s -v Untitled /dev/rdisk0s7 \n
%sr%s
a=%ld: clump size is not a multiple of node size\n
\tinitial catalog file size: %u\n
%s: partition is too big (maximum is %llu KB)
usage: %s [-N [partition-size]] [hfsplus-options] special-device\n
\t-b allocation block size (4096 optimal)\n
Warning: %u is invalid file system start allocation block number, must be less than total allocation blocks (%u)
HFS Plus format parameters:
Overlapped extent at <%u, %u> (%d)\n
%s%s
%s: block size %d is too small for %lld sectors
b=%ld: bitmap clump size is too small\n
\t-U user-id (for root directory)\n
MarkExtentUsed
Overlapped extent for AVH at <%u, %u>\n
\tjournal-size: %uk\n
%ld MB
%s is mounted on %s
\t-c clump size list (comma separated)\n
\t\td=blocks (user data fork)\n
Overlapped extent for header at <%u, %u>\n
c=%ld: clump size is not a multiple of node size\n
Warning: block size %u is less than catalog b-tree node size %u
e=%ld: initial size is less than clump size\n
=%ld: too many blocks for clump size!
unknown user id: %s
.journal_info_block
%s: journal size %lldk too small.  Reset to %dk.\n
%s: bad allocation block size (too small)
\t-n b-tree node size list (comma separated)\n
\t%s -v Untitled -c b=64,c=1024 /dev/rdisk0s7 \n\n
%s:  pwrite(%d, %p, %zu, %lld)
read (sector %llu)
\t\ta=size (attributes b-tree)\n
write (sector %llu)
Warning: Resetting file system start block to zero
\t\tr=blocks (user resource fork)\n
```
