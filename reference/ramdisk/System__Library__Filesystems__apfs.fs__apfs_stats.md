# `/System/Library/Filesystems/apfs.fs/apfs_stats`

From the upgrade restore ramdisk (141-29011-104.dmg). 73,536 bytes.

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
\t\tVolume %s %s on %s\n
Number of snapshots
\tNo statistics exported
.
Device: %s, block size %lld\n
Extentref tree node count
/dev/
 (
IOMedia
System 
\t\t\t\t\t\tNo container statistics exported
Bytes (Read)
\t\t\tNumber of purgeable files = %llu\n
\t\tAverage cache count during overcommit: %llu%s\n
%s%llu%-*.*s %cB%s
System content
Cannot find entries matching %s - %s\n
Histogram for free extents sizes, number of buckets is
\t\tAverage amount memory overcommitted: %llu%s\n
rdisk
no-zeros
BSD Name
Preferred Block Size
\t%s%c%llu, %llu%c = %lld\n
\t\t\tNumber of omap tree nodes = %llu\n
<fsgetpath failed: error %d>
%s%llu.%.*s %cB%s
Whole
\t\t\t\t\tino range: %llu+%llu\n
Container statistics
AppleAPFSContainer
Total Time (Read)
\t%lld write requests, transfered %lld bytes\n
\t\t\tNumber of fsroot tree nodes = %llu\n
Histogram for number of files per directory, number of buckets is
%sOBJECT CACHE STATS:\n%s  VIRTUAL + PHYSICAL:\n%s    mem_max_current             = %#12llx\n%s    mem_max_lowest              = %#12llx\n%s    mem_max_highest             = %#12llx\n%s    mem_max_pos_change          = %#12llx\n%s    mem_ma
\t\t\tNo statistics exported
disk
)
Number of directories
\tAPFS maximum total memory for object caches: %llu (0x%llx, approx. %s)\n
\tEvent: Object cache overcommit (lowest total maximum surpassed APFS maximum)
%sFree total:       %llu MiB (%llu blocks) %.2f%%\n
/private/preboot/cryptex1/current/%s
vfs.generic.apfs.allocated
\t\t\t\t\tCryptex: %s (ino %llu)\n
IOBlockStorageDriver
%s%llu %cB%s
APFSComposited
Number of purgeable files
Cryptex inode
global
\tContainer: size %lld blocks, %lld blocks free\n
%sIn freeQ:         %llu MiB (%llu blocks) %.2f%%\n
Failed to create match dictionary - %s\n
\t
\t\t\tSize of purgeable files = %llu\n
Histogram for number of files of sizes in a specific range, number of buckets is
Volume statistics
%sTotal size:       %llu MiB (%llu blocks)\n
%s%s
epZ
Number of files
%sAPFS container stats:\n
usage: %s [-e] [-Z] \n\t-e include extended statistics\n\t-Z skip counters with zero value\n
\tThe number of volumes is %d \n
Free extents histogram
File sizes histogram
Bytes (Write)
\t\t\tNumber of extentref tree nodes = %llu\n
\t\t\t\t\tGraft container statistics:
Total Time (Write)
Number of volumes
could not get total memory allocated - %s\n
Cannot open connection to APFS Container %s - %s
\t\t\tNumber of files = %llu\n
Number of extents
\t\t\tNumber of snapshots = %llu\n
Global:
\t\t\tNumber of extents = %llu\n
inode range length
RoleValue
Graft directory inode
privacy
Failed to get container name\n
Operations (Read)
\t\t\t\t\t
%s         Meta:    %llu MiB (%llu blocks) %.2f%%\n
\t%lld write requests, transfered %lld bytes in %lld.%09lld seconds\n
\t\t\t
Object mapping tree node count
Root tree node count
%sReserved Data:    %llu MiB (%llu blocks) %.2f%%\n
.dmg
\tAPFS Total Memory Allocated = %llu\n
\t\t\tNumber of directories = %llu\n
\t\t\t\t\t\t
IOService
\t%lld read requests, transfered %lld bytes in %lld.%09lld seconds\n
UUID
\t\t\t\t\tGraft volume statistics:
\t\t\t\t\t\tNo volume statistics exported
%sr%s
Totals for all %lld disks:\n
\t%lld read requests, transfered %lld bytes\n
%s%s:\n
%03llu
Operations (Write)
AppleAPFSContainerScheme
Total Size of purgeable files
/
ERROR: Reported block size is zero, assuming 4K
APFSContainer: %s\n
%s%s = %lld\n
Files per directory histogram
\t\t\t\t%sGraft: %s (ino %llu)\n
inode range base
%sAvailable now:    %llu MiB (%llu blocks) %.2f%%\n
extended-statistics
Cannot fetch information about container '%s' - %s\n
\t\tNumber of occurrences: %llu\n
Statistics
AppleAPFSMedia
```
