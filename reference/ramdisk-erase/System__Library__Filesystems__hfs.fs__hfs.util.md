# `/System/Library/Filesystems/hfs.fs/hfs.util`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 88,496 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1624)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (2)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
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

## Strings (128)

```
ParseArgs
failed to get block count. trying stat().\n
Volume %s is already journaled.\n
Error getting list of mounted filesystems\n
       required for Mount and Force Mount 
hfs.util
/dev/fd/
couldn't convert volume status database: %s
writable
mount_point_arg:
%s : is not contiguous!\n
Journal size %dk is not a multiple of volume %s block size (%d).\n
disk
hfs.util: ERROR: unrecognized flag (removable/fixed) argv[%d]='%s'\n
       -%c (Turn off journaling on a raw device)\n
       required for Mount, Force Mount and Probe
Volume %s does not appear to be an HFS+ volume.\n
failed to read the journal info block (%s).\n
-e=%d
device_arg:
Can't find out any info about the fs for path %s (%s)\n
failed to read volume header @ offset %d (%s)\n
%s is a device node.  Journal enable only works on a mounted HFS+ volume.\n
Failed to write journal info block on volume %s (%s)!\n
%s/%s
.journal_info_block
/.CFUserTextEncoding
Flags:
disable_journaling: %s is not journaled.\n
hfs.util: ERROR: unrecognized flag (dev/nodev) argv[%d]='%s'\n
       -%c (Enable the use of an external journal on a raw device)\n
%s/is_vol_hfs_plus
Journaling disabled on %s mounted at %s.\n
Can't create journal file (NC)  on volume %s (%s)\n
Failed to write %dk to journal on volume %s (%s)\n
       indicates removable or fixed (for example 'fixed')
hfs.util: ERROR: unrecognized flag (suid/nosuid) argv[%d]='%s'\n
       -%c (Adopt permissions)\n
Volume %s (%s) is not journaled.\n
RawDisableJournaling: failed to read volume header @ offset %lld (%s)\n
%s is not an HFS+ volume.  Journaling only works on HFS+ volumes.\n
Could not create journal info block (NC) file on volume %s (%s)\n
disable_journaling: volume is only regular HFS, not HFS+\n
__CFStringGetDefaultEncodingForHFSUtil
readonly
can't open: %s (%s)\n
Can't calculate the embedded offset (if any) for %s.\n
Journal creation failure.\n
/dev/%s
size < INT_MAX
       indicates dev or nodev (for example 'dev')
Can't locate volume %s to turn off journaling (%s).\n
Failed to remove the journal info block %s (%s)\n
SetJournalInFSState: Invalid Embedded Volume Signature 
-u=unknown,-g=unknown,-m=0777
       -%c (Get size & location of journaling on a file system)\n
Can't stat volume %s (%s).\n
       -%c (Turn off journaling on a file system)\n
Failed to get journal info for volume %s (%s)\n
get_journal_info: invalid embedded volume signature 
get_journal_info: invalid volume signature
hfsutil_main.c
       -%c (Force Mount)\n
       name of the file system we're to act on (for example, '/Volumes/foo' or '/')
encoding > -1 && encoding <= UINT_MAX
hfs.util: ERROR: unrecognized flag (readonly/writable) argv[%d]='%s'\n
suid
       device we are acting upon (for example, 'disk0s2')
%s : starting block is > 32bits!\n
Failed to make volume %s journaled (%s)\n
RawDisableJournaling: invalid embedded volume signature 
nosuid
       if '-%c' or '-%c' is specified, this should be the\n
Can't create journal file on volume %s (%s)\n
%s: external journal stored on partition with uuid %s on machine w/serial number %s\n
SetJournalInFSState: Invalid Volume Signature 
       -%c (Disable use of an external journal on a raw device)\n
       %s -m disk0s2 /my/hfs removable readonly nosuid nodev\n
/dev/rdisk
nodev
Unable to get fs info for %s\n
Update of super-block on %s failed! (%d != %d, %s)\n
failed to re-write the journal info block (%s).\n
get_embedded_offset: invalid volume signature 
removable
fixed
       indicates suid or nosuid (for example 'suid')
HFS Mount: embedded volume offset not a multiple of physical block size (%d); switching to 512\n
Not enough contiguous space for a %d k journal.  Retrying.\n
hfs
       %s -p disk0s2 fixed writable\n
Can't locate volume %s to make it journaled (%s).\n
Allocated %lldK for journal file.\n
Disk too fragmented to enable journaling.\n
/dev/
.journal
action_arg:
can't get the device block size (%s). assuming 512\n
%s : not journaled.\n
dev
Failed to get start block for %s (%s)\n
-t
rdisk
can't stat %s (%s)\n
Please run a defragmenter on %s.\n
Volume %s (%s) is not a HFS volume.\n
%s : journal size %lld k at offset 0x%llx\n
       -%c (Mount)\n
hide: %s is alreadly invisible\n
Could not create journal info block file on volume %s (%s)\n
Turned off the journaling bit for %s\n
-o
usage: %s action_arg device_arg [mount_point_arg] [Flags] \n
       -%c (Probe for mounting)\n
Could not access %s (%s)\n
Failed to make volume %s UN-journaled (%s)\n
%.*s
       -%c (Unmount)\n
       -%c (Make a file system journaled)\n
Could not allocate memory to write to the journal on volume %s (%s)\n
Failed to remove the journal %s (%s)\n
RawDisableJournaling: Invalid Volume Signature 
failed to get block count. trying stat().
/dev/r%s
       indicates readonly or writable (for example 'readonly')
Examples:
failed to read the embedded vhp @ offset %d\n
Volume %s is not journaled.\n
```
