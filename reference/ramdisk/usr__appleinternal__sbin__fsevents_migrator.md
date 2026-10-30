# `/usr/appleinternal/sbin/fsevents_migrator`

From the upgrade restore ramdisk (141-29011-104.dmg). 70,240 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 1808)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (3)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (96)

```
%s: out of space for disk logger buffer\n
read_disk_log: failed to gzopen %s
, mask = 0x%08x [
%sMount
%s%s
InodeMetaMod
ERROR: can't get dir list %s\n
%s - empty path error\n
ChangeOwner
XattrMod
ERROR: can't open folder %s\nmake sure you are running as root\n
Empty file! skip\n
ERROR: Log files out of order (%ld < %ld) in %s.\n
%s - (%s) path is not a directory\n
       -dst <path>                               Destination path of .fseventsd folder\n
%sEventIdsWrapped
FinderInfoMod
process_disk_event_buf: ptr out-of-bounds (%ld > max %d)\n
read_disk_log: problems with history file: %s (fd %d, errno %d ; is_reg %d; uid %d/%d gid %d/%d)\n does your volume allow logging?\n
<dst>
,
Cloned
uuid: %s\n
-truncatePrefix
print_settings
], fileId = %llu
%sHistoryDone
processed %d bytes; copying down %d to the beginning of buf\n
copy uuid error (%s)\n
--help
%s: settings->verbose = %s\n
%sUserDropped
%sKernelDropped
fsevents_migrate_tools.c
\nFound %d log files in %s\n
ERROR: Problem with log files.\n
%s/fseventsd-uuid
ERROR: could not open <<%s>> (%s)\nmake sure you are running as root\n
%s: settings->src_folder_path = '%s'\n
%sRootChanged
%s: can't open destination file %s\n
save_dest_log_file
-dst
%s: settings->truncate_prefix_path = '%s'\n
<src>
Flags:\n
init_disk_buffer
Created
Modified
IsSymLink
ab
%s: failed to write %zu bytes to log file %s (err: %s).
-help
-verbose
%sMustScanSubDirs
IsDir
.docid/
, docId = %u
FALSE
%s: settings->dst_folder_path = '%s'\n
%s: settings->print_settings = %s\n
%s - (%s) path error (%s)\n
%sUnmount
IsFile
\n
flush_event_buffer
process_disk_event_buf: dealing with opposite endian disk buffer.
process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x))\n
process_disk_event_buf: checksum mis-match: file 0x%.8x, calculated 0x%.8x\n
read %d (total: %lld; offset: %d)\n
buffer->nitems < EVENT_CHUNK
#### reading disk log: %s\n
read_disk_log: cur_file_size is %lld but actual file size is zero for %s\n
-usage
TRUE
IsLastHardlink
fill_event_buffer
%s: disk buffer not allocated\n
-print_settings
-src
IsHardlink
ERROR: Can't stat log file: %s (%s)\n
src path is  equal to dst path\n
Renamed
\n--------------------- Destination file %s ---------------------\n
       -verbose                                  Verbose output\n
Removed
%s: gzflush(%s) returned %d
\n--------------------- Processing file %s ---------------------\n
Empty file %s \n
Usage: fsevents_migrate_tool <flags> -src <src_folder_path> -dst <dst_folder_path> -truncatePrefix <prefix to filter and truncate>\n
    event %2d: id = %15llu, path = '%s'
r
%s/%.16llx
       -src <path>                               Source path of .fseventsd folder\n
       -truncatePrefix <substring>               Prefix to filter and truncate from contents of src folder\n
```
