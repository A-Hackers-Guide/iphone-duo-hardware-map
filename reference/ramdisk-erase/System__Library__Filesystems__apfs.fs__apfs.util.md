# `/System/Library/Filesystems/apfs.fs/apfs.util`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 88,944 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 1920)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.apfs.revert-to-snapshot</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
</dict>
</plist>
```

## Strings (182)

```
get
set=yes
failed to get the absolute volume uuid for %s : %s\n
\n%s <option> [<verb>] path|dir [<optional parameter>]\n
   -C -type type volume_path : clear the purgeability of files of the specified 'type' on the volume referred to by 'path'.
-zero
Purgeable file info for %s:\nFile Flags:    0x%llx\nRelated Flags: 0x%llx\nFile acctime:  %llu\nGen count:     %llu\nSync root id:  %llu\nSize:          %llu\n
book
Failed to set revert-to-snap : %s\n
failed to set the sync-root flag on %s : %s\n
failed to get the path for fd: %s, error %s\n
   -s             : set container UUID and its volume(s) UUID(s) to new random values.
system-discarded
Failed to set embedded xattr limit control to %d for %s: %s\n
   -Z path                   : get the purgeable file flags for the specific file at 'path'.
-high
-keep-pristine
Purging files on %s returned %d (%s).  Deleted amount: %lld (%llu files)\n
podcast
Documents
Books
AppleAPFSSnapshot
Defragmentation %s\n
-clear
   -A set=yes/no             : enable / disable atime update for volume.
   -S dir                    : get the directory stats from dir.
-uoffline
-cancel
Movie
IOMatchCategory
Failed to mark %s as purgeable, errno: %d (%s) (flags 0x%llx supplemental 0x%llx)\n
failed to drop extents in first snap for %s : %s\n
Total num purgeable files: %lld   Total purgeable data size: %lld\n
Video
%s:\ndescendants: %llu\nphysical size: %llu\ngen-count: %llu\n
   -R SNAPSHOT    : set the volume to revert to the snapshot named by SNAPSHOT on next mount.
Messages
Test
the -maxage argument requires a unix timestamp value (numeric).
Set the fs typename override on %s to %s (fstname ptr %p)\n
Failed to set maintain-dir-stats on %s : %s\n
failed to stat fd: %s, error %s\n
   -E path                   : drop the extents for 'path' from the first snapshot.
Defragmentation enabled
Purgeable flags for %s are: 0x%llx\n
Marked %s purgeable with flags 0x%llx (supplemental 0x%llx)\n
sucontent
enabled
needs to be run as root
AppleAPFSMedia
All
Music
A path is required to get purgeable statistics for.
IOService
request has flags: 0x%x type: 0x%x min_size %lld max_age %lld desired_amt %lld (size: %zd)\n
request has flags: 0x%llx type: 0x%llx typelimit: %llu min_size %lld max_age %lld desired_amt %lld (size: %zd)\n
Cancelling offline purge on %s returned %d (%s).\n
fp-api-discarded
Invalid argument: expected purge reason
%s <option> [<verb>] /dev/diskXsY\n
-type
   type %10s: num purgeable files: %6lld purgeable data size: %10lld\n
-purge-reason
Photos
Urgency filtering is not supported for device files.
/dev/
\n%s <option>\n
Directory %s will now maintain dir-stats.\n
/dev/fd/
UUID
   -P <criteria> path        : purge files meeting the criteria specified on the volume referred to by 'path'.
OK
Purging the single file %s purged %lld bytes\n
%s has been made exempt from COW behavior for snapshots\n
Failed to set the fs typename override of %s on %s : (err %d) %s\n
atime update was %s\n
-ext
-residency
-typetotal
document
ru-discarded
/
failed to stitch firmlinks and/or create synthetics for root volume (%x) ...\n
-fault
Podcast
The -future argument requires a unix timestamp value (numeric, nsec).
Set embedded xattr limit control to %d (was %d) for %s\n
   -M dir                    : flag the named directory as \"maintain-dir-stats\".
-umove
-total
user-discarded
set=no
   -D set=yes/no  : enable / disable defragmentation for volume or container.
dE:pkK:sthD:R:M:S:O:a:A:P:m:G:r:Y:y:C:X:Z:z:
Failed to get dir-stats info on %s : (err %d) %s\n
%s has sync root flag : 0x%x\n
fd conversion failed: %s\n
   -G [options] path         : get stats on the purgeable files on the volume specified by 'path'.
The -syncroot argument requires an inode number.
   -D get         : Get defragmentation setting for volume or container.
com.apple.filesystems.apfs
-med
will purge files >= %lld\n
music
mail
data
the -total argument requires a numeric value for the desired total amount to purge.
APFS Utility tool
-nodups
-maxage
hfs
                                                     -clear.
   -y path                   : get the sync-root flag from the first parent that has one for the item identified by 'path'.
need a path to a volume to purge files on.
foundation-api-discarded
Purging the single file %s failed: %s (%d)
-syncroot
Cancelling purge on %s returned %d (%s).\n
movie
message
the -minsize argument requires a numeric value argument.
                                                     -podcast -video -movie -message -book -sucontent -fault -pdir
-pdir
-minsize
Invalid purge reason specified: %s \n
the -typetotal argument requires numerical limit to purge
   -O path [fs name]         : override the fstypename for apfs to be \"hfs\" (or the optional name given).
   -Y dir                    : get the sync-root flag from the specified directory.
   -z path                   : make the file at path exempt from copy-on-write semantics for snapshots.
Defragmentation disabled
Data
mount_apfs
Getting purgeable file stats on %s returned %d (%s)\n
Purging files on %s (offline) returned %d (%s).  Deleted amount: %lld (%llu files)\n
dropped the extents from %s in the first snapshot\n
need a path to a volume to clear purgeable files on.
AppleAPFSContainerScheme
Mail
   -k             : get volume UUID.
failed to check whether item at %s is under sync-root : %s\n
video
The -residency argument requires a residency reason.
Opening file %s for single file purge failed: %s (%d)
   -p             : probe for volume name.
failed to make file %s COW-exempt : %s\n
%s has abs volume uuid: : %s\n
atime update %s\n
                               'verb' could be one of: -low -med -high -su -photo -music -mail -document -data
   -t  : stitches and creates synthetic objects on root volume group.
-offline
%s is under sync-root : #%llu\n
/dev/r
AppleAPFSVolume
   -h  : show this help menu.
-fixup
failed getting purgeable flags for %s : (%d) %s\n
SU Content
Volume will revert to snapshot %s on next mount.\n
disabled
Failed to get atime update setting for [%s] : %s\n
   -K path                   : purge(kill) the single file at 'path'
-su
the -type argument requires a type of file to purge
                                                     -umove -future <timestamp>
AppleAPFSContainer
need a path to a volume (or device, if offline) to purge files on.
Usage: %s <option> [<verb>] path|dir|device [<optional parameter>], as follows:\n\n
   -A get                    : get atime update setting for volume.
   -r dir                    : set the sync-root flag on the specified directory.
   -X set=yes|no path        : set/unset embedded xattr max size enforcement on volume specified by 'path'.
Failed to set atime update setting : %s\n
   -a path        : Get the absolute volume uuid for the volume at path.
   -m <verb> path            : mark the file at path as purgeable with the various options specified.
-low
-future
the -typetotal argument requires a type of file to purge
need a path to an apfs volume that should purge files
failed to get the sync-root flag on %s : %s\n
                               'options', if provided, could be one of: -low -med -high -su -uoffline -future -nodups
need a path to mark purgeable.
Purging files on %s returned %d (%s).  cleared purgeability on %lld files\n
photo
```
