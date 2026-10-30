# `/System/Library/Filesystems/apfs.fs/apfs_stats`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 73,536 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1952)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.apfs.omm.ctl</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleAPFSUserClient</string>
	</array>
</dict>
</plist>
```

## Strings (123)

```
could not get total memory allocated - %s\n
%s%s = %lld\n
\t\t\tNumber of directories = %llu\n
\t\t\tNumber of snapshots = %llu\n
\t\t\tNumber of fsroot tree nodes = %llu\n
inode range base
%sAPFS container stats:\n
Statistics
Number of extents
inode range length
\t\t\t\t\tGraft volume statistics:
\t\t\tNumber of extentref tree nodes = %llu\n
 (
IOBlockStorageDriver
global
Histogram for free extents sizes, number of buckets is
Extentref tree node count
\t\t\t\t\t
vfs.generic.apfs.allocated
BSD Name
APFSContainer: %s\n
Histogram for number of files of sizes in a specific range, number of buckets is
Root tree node count
\t\t\tSize of purgeable files = %llu\n
Histogram for number of files per directory, number of buckets is
epZ
File sizes histogram
\t\t\t\t\tino range: %llu+%llu\n
%sIn freeQ:         %llu MiB (%llu blocks) %.2f%%\n
%sReserved Data:    %llu MiB (%llu blocks) %.2f%%\n
IOMedia
\t%lld read requests, transfered %lld bytes\n
\t\tVolume %s %s on %s\n
\t\tAverage cache count during overcommit: %llu%s\n
\t\t\tNo statistics exported
.dmg
Bytes (Read)
Cannot open connection to APFS Container %s - %s
\t\t\t
Number of snapshots
\t\t\t\t\tCryptex: %s (ino %llu)\n
%s         Meta:    %llu MiB (%llu blocks) %.2f%%\n
Graft directory inode
System content
%sFree total:       %llu MiB (%llu blocks) %.2f%%\n
\tThe number of volumes is %d \n
%03llu
%s%llu.%.*s %cB%s
extended-statistics
\tAPFS Total Memory Allocated = %llu\n
Global:
Bytes (Write)
AppleAPFSMedia
Total Time (Read)
Number of directories
disk
Failed to create match dictionary - %s\n
Cannot fetch information about container '%s' - %s\n
IOService
Free extents histogram
\t\t\t\t\tGraft container statistics:
no-zeros
)
Object mapping tree node count
Device: %s, block size %lld\n
\t\t\t\t\t\tNo container statistics exported
%s%s
%s%llu%-*.*s %cB%s
privacy
\tContainer: size %lld blocks, %lld blocks free\n
Files per directory histogram
Volume statistics
\t\tNumber of occurrences: %llu\n
/dev/
Failed to get container name\n
\t\t\t\t\t\tNo volume statistics exported
rdisk
Whole
Totals for all %lld disks:\n
/
Preferred Block Size
.
<fsgetpath failed: error %d>
Container statistics
%sTotal size:       %llu MiB (%llu blocks)\n
Cryptex inode
\tAPFS maximum total memory for object caches: %llu (0x%llx, approx. %s)\n
\tEvent: Object cache overcommit (lowest total maximum surpassed APFS maximum)
/private/preboot/cryptex1/current/%s
AppleAPFSContainer
\t
APFSComposited
Operations (Write)
\t\t\tNumber of purgeable files = %llu\n
Number of purgeable files
\t\t\tNumber of omap tree nodes = %llu\n
%sr%s
Cannot find entries matching %s - %s\n
\t%lld read requests, transfered %lld bytes in %lld.%09lld seconds\n
\t%lld write requests, transfered %lld bytes in %lld.%09lld seconds\n
System 
usage: %s [-e] [-Z] \n\t-e include extended statistics\n\t-Z skip counters with zero value\n
AppleAPFSContainerScheme
Total Size of purgeable files
\tNo statistics exported
RoleValue
Operations (Read)
Total Time (Write)
\t%s%c%llu, %llu%c = %lld\n
%sAvailable now:    %llu MiB (%llu blocks) %.2f%%\n
%s%llu %cB%s
Number of files
\t\t\tNumber of extents = %llu\n
\t\t\t\t\t\t
\t\tAverage amount memory overcommitted: %llu%s\n
\t%lld write requests, transfered %lld bytes\n
Number of volumes
UUID
\t\t\tNumber of files = %llu\n
ERROR: Reported block size is zero, assuming 4K
%s%s:\n
\t\t\t\t%sGraft: %s (ino %llu)\n
%sOBJECT CACHE STATS:\n%s  VIRTUAL + PHYSICAL:\n%s    mem_max_current             = %#12llx\n%s    mem_max_lowest              = %#12llx\n%s    mem_max_highest             = %#12llx\n%s    mem_max_pos_change          = %#12llx\n%s    mem_ma
```
