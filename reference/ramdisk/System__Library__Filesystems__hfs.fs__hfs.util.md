# `/System/Library/Filesystems/hfs.fs/hfs.util`

From the upgrade restore ramdisk (141-29011-104.dmg). 88,496 bytes.

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
%s : starting block is > 32bits!\n
       indicates removable or fixed (for example 'fixed')
       indicates suid or nosuid (for example 'suid')
disable_journaling: %s is not journaled.\n
hfs.util: ERROR: unrecognized flag (readonly/writable) argv[%d]='%s'\n
can't open: %s (%s)\n
/dev/fd/
%s : is not contiguous!\n
Volume %s does not appear to be an HFS+ volume.\n
.journal_info_block
disk
ParseArgs
size < INT_MAX
nosuid
       %s -m disk0s2 /my/hfs removable readonly nosuid nodev\n
Journal size %dk is not a multiple of volume %s block size (%d).\n
failed to read the journal info block (%s).\n
Could not allocate memory to write to the journal on volume %s (%s)\n
RawDisableJournaling: Invalid Volume Signature 
hfs.util: ERROR: unrecognized flag (dev/nodev) argv[%d]='%s'\n
Can't find out any info about the fs for path %s (%s)\n
failed to read volume header @ offset %d (%s)\n
%s/is_vol_hfs_plus
RawDisableJournaling: failed to read volume header @ offset %lld (%s)\n
hfs.util
dev
       -%c (Adopt permissions)\n
Examples:
failed to get block count. trying stat().\n
failed to read the embedded vhp @ offset %d\n
usage: %s action_arg device_arg [mount_point_arg] [Flags] \n
Volume %s is not journaled.\n
writable
Could not access %s (%s)\n
Failed to remove the journal info block %s (%s)\n
Journaling disabled on %s mounted at %s.\n
-t
       -%c (Make a file system journaled)\n
       required for Mount, Force Mount and Probe
Volume %s is already journaled.\n
%s/%s
       -%c (Probe for mounting)\n
       indicates readonly or writable (for example 'readonly')
Journal creation failure.\n
Can't create journal file on volume %s (%s)\n
%s : not journaled.\n
get_journal_info: invalid embedded volume signature 
%.*s
hfs.util: ERROR: unrecognized flag (suid/nosuid) argv[%d]='%s'\n
       -%c (Turn off journaling on a file system)\n
can't get the device block size (%s). assuming 512\n
Failed to get start block for %s (%s)\n
Failed to get journal info for volume %s (%s)\n
Turned off the journaling bit for %s\n
.journal
readonly
Failed to make volume %s UN-journaled (%s)\n
disable_journaling: volume is only regular HFS, not HFS+\n
failed to re-write the journal info block (%s).\n
couldn't convert volume status database: %s
       required for Mount and Force Mount 
rdisk
       device we are acting upon (for example, 'disk0s2')
-u=unknown,-g=unknown,-m=0777
Failed to write %dk to journal on volume %s (%s)\n
get_embedded_offset: invalid volume signature 
-o
nodev
       -%c (Turn off journaling on a raw device)\n
Can't calculate the embedded offset (if any) for %s.\n
Please run a defragmenter on %s.\n
hfs.util: ERROR: unrecognized flag (removable/fixed) argv[%d]='%s'\n
Volume %s (%s) is not journaled.\n
       -%c (Enable the use of an external journal on a raw device)\n
can't stat %s (%s)\n
%s is not an HFS+ volume.  Journaling only works on HFS+ volumes.\n
Disk too fragmented to enable journaling.\n
Failed to remove the journal %s (%s)\n
Update of super-block on %s failed! (%d != %d, %s)\n
SetJournalInFSState: Invalid Volume Signature 
device_arg:
-e=%d
       -%c (Mount)\n
       -%c (Get size & location of journaling on a file system)\n
HFS Mount: embedded volume offset not a multiple of physical block size (%d); switching to 512\n
hfsutil_main.c
       name of the file system we're to act on (for example, '/Volumes/foo' or '/')
Can't stat volume %s (%s).\n
Can't create journal file (NC)  on volume %s (%s)\n
Volume %s (%s) is not a HFS volume.\n
get_journal_info: invalid volume signature
mount_point_arg:
       indicates dev or nodev (for example 'dev')
/dev/rdisk
/dev/
%s : journal size %lld k at offset 0x%llx\n
__CFStringGetDefaultEncodingForHFSUtil
%s is a device node.  Journal enable only works on a mounted HFS+ volume.\n
Could not create journal info block (NC) file on volume %s (%s)\n
failed to get block count. trying stat().
/dev/%s
       %s -p disk0s2 fixed writable\n
Can't locate volume %s to make it journaled (%s).\n
encoding > -1 && encoding <= UINT_MAX
Flags:
       -%c (Unmount)\n
       -%c (Disable use of an external journal on a raw device)\n
action_arg:
hide: %s is alreadly invisible\n
Not enough contiguous space for a %d k journal.  Retrying.\n
Can't locate volume %s to turn off journaling (%s).\n
SetJournalInFSState: Invalid Embedded Volume Signature 
/dev/r%s
Allocated %lldK for journal file.\n
Error getting list of mounted filesystems\n
RawDisableJournaling: invalid embedded volume signature 
hfs
       -%c (Force Mount)\n
       if '-%c' or '-%c' is specified, this should be the\n
Failed to write journal info block on volume %s (%s)!\n
suid
Failed to make volume %s journaled (%s)\n
Unable to get fs info for %s\n
/.CFUserTextEncoding
fixed
Could not create journal info block file on volume %s (%s)\n
%s: external journal stored on partition with uuid %s on machine w/serial number %s\n
removable
```
