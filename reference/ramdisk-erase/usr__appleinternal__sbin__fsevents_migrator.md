# `/usr/appleinternal/sbin/fsevents_migrator`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 70,240 bytes.

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
-dst
print_settings
%s: settings->dst_folder_path = '%s'\n
%s: settings->truncate_prefix_path = '%s'\n
<dst>
ab
Empty file! skip\n
Flags:\n
       -verbose                                  Verbose output\n
IsSymLink
%s: failed to write %zu bytes to log file %s (err: %s).
ERROR: Can't stat log file: %s (%s)\n
ERROR: Problem with log files.\n
Modified
XattrMod
%s/fseventsd-uuid
-truncatePrefix
       -truncatePrefix <substring>               Prefix to filter and truncate from contents of src folder\n
Removed
process_disk_event_buf: checksum mis-match: file 0x%.8x, calculated 0x%.8x\n
read_disk_log: failed to gzopen %s
Empty file %s \n
       -dst <path>                               Destination path of .fseventsd folder\n
%sRootChanged
IsHardlink
, mask = 0x%08x [
], fileId = %llu
ERROR: Log files out of order (%ld < %ld) in %s.\n
-src
%s - empty path error\n
%sUnmount
Created
FinderInfoMod
%s: out of space for disk logger buffer\n
%s/%.16llx
%s: can't open destination file %s\n
copy uuid error (%s)\n
--help
%sHistoryDone
flush_event_buffer
#### reading disk log: %s\n
processed %d bytes; copying down %d to the beginning of buf\n
save_dest_log_file
%s: disk buffer not allocated\n
ERROR: can't get dir list %s\n
-verbose
%sMustScanSubDirs
Cloned
    event %2d: id = %15llu, path = '%s'
process_disk_event_buf: magic is wrong (0x%.8x != (0x%.8x <OR> 0x%.8x <OR> 0x%.8x))\n
%s - (%s) path is not a directory\n
Usage: fsevents_migrate_tool <flags> -src <src_folder_path> -dst <dst_folder_path> -truncatePrefix <prefix to filter and truncate>\n
,
%sEventIdsWrapped
%sMount
%s%s
r
init_disk_buffer
ERROR: could not open <<%s>> (%s)\nmake sure you are running as root\n
FALSE
Renamed
, docId = %u
\n
fill_event_buffer
process_disk_event_buf: dealing with opposite endian disk buffer.
-usage
-help
%s: settings->src_folder_path = '%s'\n
%sUserDropped
ChangeOwner
read %d (total: %lld; offset: %d)\n
ERROR: can't open folder %s\nmake sure you are running as root\n
%s: settings->verbose = %s\n
src path is  equal to dst path\n
%s - (%s) path error (%s)\n
InodeMetaMod
IsDir
process_disk_event_buf: ptr out-of-bounds (%ld > max %d)\n
read_disk_log: cur_file_size is %lld but actual file size is zero for %s\n
\n--------------------- Destination file %s ---------------------\n
TRUE
%s: settings->print_settings = %s\n
       -src <path>                               Source path of .fseventsd folder\n
IsLastHardlink
read_disk_log: problems with history file: %s (fd %d, errno %d ; is_reg %d; uid %d/%d gid %d/%d)\n does your volume allow logging?\n
\nFound %d log files in %s\n
<src>
.docid/
%s: gzflush(%s) returned %d
\n--------------------- Processing file %s ---------------------\n
IsFile
buffer->nitems < EVENT_CHUNK
uuid: %s\n
%sKernelDropped
fsevents_migrate_tools.c
-print_settings
```
