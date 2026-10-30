# `/System/Library/Filesystems/hfs.fs/newfs_hfs`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 87,984 bytes.

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
invalid HFS+ name: \"%s\", using \"%s\" instead
%s: invalid atrribute b-tree node size
\tcatalog clump size: %u\n
\t\tb=blocks (bitmap file)\n
%s: journal size %lldk too small.  Reset to %dk.\n
\textents b-tree node size: %u\n
  examples:\n
\ttotal blocks: %u\n
HFS Plus format parameters:
\t\te=blocks (extents file)\n
\t-i starting catalog node id\n
.journal
%s: bad HFS Plus allocation block size (must be a power of two)
Warning: %u is invalid file system start allocation block number, must be less than total allocation blocks (%u)
\tfirst free catalog node id: %u\n
\taccess mask: %o\n
\t-U user-id (for root directory)\n
,
Initialized %s as a 
e=%ld: initial size is less than clump size\n
\tvolume name: \"%s\"\n
\t-b allocation block size (4096 optimal)\n
\t\tr=blocks (user resource fork)\n
\t%s -v Untitled /dev/rdisk0s7 \n
unknown group id: %s
 HFS Plus volume with a %uk journal\n
b=%ld: bitmap clump size is too small\n
\tblock-size: %u\n
\tdata fork clump size: %u\n
\tresource fork clump size: %u\n
\t\ta=blocks (attributes file)\n
\t%s -v Untitled -c b=64,c=1024 /dev/rdisk0s7 \n\n
%s is mounted on %s
\tattributes b-tree node size: %u\n
\t-M octal access-mask (for root directory)\n
 HFS Plus volume
c=%ld: initial size is not a multiple of node size\n
\tinitial catalog file size: %u\n
\t-D journal-dev use 'journal-dev' for an external journal\n
%ld MB
untitled
e=%ld: initial size is not a multiple of node size\n
MarkExtentUsed
%s: %s
\tuser ID: %d\n
\tgroup ID: %d\n
\tfile system start block: %u\n
\t-I initial size list (comma separated)\n
%s: partition is too big (maximum is %llu KB)
 case-insensitive
\textents clump size: %u\n
\t-n b-tree node size list (comma separated)\n
%s:  pwrite(%d, %p, %zu, %lld)
read (sector %llu)
c=%ld: clump size is not a multiple of node size\n
e=%ld: clump size is not a multiple of node size\n
\tjournal-size: %uk\n
\tinitial attributes file size: %u\n
usage: %s [-N [partition-size]] [hfsplus-options] special-device\n
\t-s use case-sensitive filenames (default is case-insensitive)\n
\t\tc=blocks (catalog file)\n
%sr%s
/dev/
  where hfsplus-options are:\n
a=%ld: initial size is less than clump size\n
\tcatalog b-tree node size: %u\n
Overlapped catalog extent at <%u, %u>\n
unknown user id: %s
%ld GB
\tinitial extents file size: %u\n
=%ld: too many blocks for clump size!
=%ld: too many blocks for initial size!
%s::pread(%d, %p, %zu, %lld)
WriteBuffer
%s: starting catalog node id too small (must be > 15)
\tinitial allocation file size: %u (%u blocks)\n
\t\tc=size (catalog b-tree)\n
\t%s -v Untitled -n c=4096,e=1024 /dev/rdisk0s7 \n
%s: bad allocation block size (too large)
%s%s
%s: getmntinfo: %s
%ld TB
c=%ld: initial size is less than clump size\n
\t-v volume name (in ascii or UTF-8)\n
Overlapped extent for AVH at <%u, %u>\n
%s: partition is too small (minimum is %d KB)
%s: block size %d is too small for %lld sectors
Warning: block size %u is less than catalog b-tree node size %u
\tattributes clump size: %u\n
\t-c clump size list (comma separated)\n
BG:J:D:M:N:PU:hsb:c:i:I:n:v:
a=%ld: initial size is not a multiple of node size\n
\t-N do not create file system, just print out parameters\n
\t-G group-id (for root directory)\n
Overlapped extent at <0, 2> (%d)
Overlapped extent at <0, 1> (%d)
Overlapped extent for header at <%u, %u>\n
.journal_info_block
 case-sensitive
Warning: %u is a non-optimal block size (4096 would be a better choice)
\t-J [journal-size] make this HFS+ volume journaled\n
  options:\n
write (sector %llu)
Warning: Resetting file system start block to zero
Warning:  extents overflow extent requested count %u exceeds maximum 8, capping at 8\n
\t\td=blocks (user data fork)\n
Overlapped extent at <0, 4> (%d)
%s: invalid extents b-tree node size
%d is an unsupported sector size\n
Warning: block size %u is less than extents b-tree node size %u
%llu sectors (%u bytes per sector)\n
\t\te=size (extents b-tree)\n
Could not copy volume name %s
cannot create filesystem on %s
invalid access mask: %s
%ld KB
\t\ta=size (attributes b-tree)\n
%s: bad allocation block size (too small)
%s: invalid catalog b-tree node size
a=%ld: clump size is not a multiple of node size\n
Overlapped extent at <%u, %u> (%d)\n
```
