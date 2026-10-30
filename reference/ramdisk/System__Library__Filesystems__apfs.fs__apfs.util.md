# `/System/Library/Filesystems/apfs.fs/apfs.util`

From the upgrade restore ramdisk (141-29011-104.dmg). 88,944 bytes.

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
%s:\ndescendants: %llu\nphysical size: %llu\ngen-count: %llu\n
   -R SNAPSHOT    : set the volume to revert to the snapshot named by SNAPSHOT on next mount.
Cancelling purge on %s returned %d (%s).\n
enabled
   -A get                    : get atime update setting for volume.
   -t  : stitches and creates synthetic objects on root volume group.
need a path to a volume to purge files on.
-low
fp-api-discarded
   -y path                   : get the sync-root flag from the first parent that has one for the item identified by 'path'.
mail
Books
Invalid purge reason specified: %s \n
need a path to a volume (or device, if offline) to purge files on.
failed to drop extents in first snap for %s : %s\n
fd conversion failed: %s\n
                               'verb' could be one of: -low -med -high -su -photo -music -mail -document -data
   -Z path                   : get the purgeable file flags for the specific file at 'path'.
%s has sync root flag : 0x%x\n
   -M dir                    : flag the named directory as \"maintain-dir-stats\".
Defragmentation enabled
AppleAPFSContainerScheme
Purging files on %s returned %d (%s).  cleared purgeability on %lld files\n
-uoffline
Getting purgeable file stats on %s returned %d (%s)\n
-pdir
   type %10s: num purgeable files: %6lld purgeable data size: %10lld\n
Volume will revert to snapshot %s on next mount.\n
%s is under sync-root : #%llu\n
   -K path                   : purge(kill) the single file at 'path'
   -X set=yes|no path        : set/unset embedded xattr max size enforcement on volume specified by 'path'.
   -Y dir                    : get the sync-root flag from the specified directory.
Documents
Movie
Directory %s will now maintain dir-stats.\n
Failed to get dir-stats info on %s : (err %d) %s\n
-nodups
atime update %s\n
mount_apfs
the -type argument requires a type of file to purge
   -P <criteria> path        : purge files meeting the criteria specified on the volume referred to by 'path'.
   -S dir                    : get the directory stats from dir.
needs to be run as root
dE:pkK:sthD:R:M:S:O:a:A:P:m:G:r:Y:y:C:X:Z:z:
Opening file %s for single file purge failed: %s (%d)
movie
message
\n%s <option> [<verb>] path|dir [<optional parameter>]\n
Set embedded xattr limit control to %d (was %d) for %s\n
Data
Purgeable file info for %s:\nFile Flags:    0x%llx\nRelated Flags: 0x%llx\nFile acctime:  %llu\nGen count:     %llu\nSync root id:  %llu\nSize:          %llu\n
-keep-pristine
Purging files on %s returned %d (%s).  Deleted amount: %lld (%llu files)\n
atime update was %s\n
failed getting purgeable flags for %s : (%d) %s\n
-clear
-offline
Podcast
A path is required to get purgeable statistics for.
   -E path                   : drop the extents for 'path' from the first snapshot.
                                                     -clear.
AppleAPFSContainer
Failed to mark %s as purgeable, errno: %d (%s) (flags 0x%llx supplemental 0x%llx)\n
com.apple.filesystems.apfs
\n%s <option>\n
failed to stat fd: %s, error %s\n
                                                     -umove -future <timestamp>
need a path to mark purgeable.
-minsize
-cancel
sucontent
Failed to set embedded xattr limit control to %d for %s: %s\n
AppleAPFSVolume
   -h  : show this help menu.
Defragmentation disabled
AppleAPFSMedia
the -maxage argument requires a unix timestamp value (numeric).
need a path to an apfs volume that should purge files
Failed to set revert-to-snap : %s\n
Failed to set maintain-dir-stats on %s : %s\n
%s has been made exempt from COW behavior for snapshots\n
-total
Purging the single file %s purged %lld bytes\n
Music
Messages
%s has abs volume uuid: : %s\n
   -p             : probe for volume name.
photo
book
hfs
AppleAPFSSnapshot
-future
Urgency filtering is not supported for device files.
   -a path        : Get the absolute volume uuid for the volume at path.
Test
the -total argument requires a numeric value for the desired total amount to purge.
/
failed to get the sync-root flag on %s : %s\n
dropped the extents from %s in the first snapshot\n
get
IOMatchCategory
-type
-ext
/dev/
will purge files >= %lld\n
-typetotal
podcast
Photos
SU Content
system-discarded
ru-discarded
failed to check whether item at %s is under sync-root : %s\n
IOService
   -A set=yes/no             : enable / disable atime update for volume.
                                                     -podcast -video -movie -message -book -sucontent -fault -pdir
   -r dir                    : set the sync-root flag on the specified directory.
-med
-purge-reason
the -minsize argument requires a numeric value argument.
OK
failed to make file %s COW-exempt : %s\n
   -O path [fs name]         : override the fstypename for apfs to be \"hfs\" (or the optional name given).
Failed to get atime update setting for [%s] : %s\n
/dev/r
UUID
Defragmentation %s\n
failed to get the absolute volume uuid for %s : %s\n
%s <option> [<verb>] /dev/diskXsY\n
Failed to set the fs typename override of %s on %s : (err %d) %s\n
set=yes
-fixup
set=no
-umove
-residency
-maxage
document
All
Mail
failed to stitch firmlinks and/or create synthetics for root volume (%x) ...\n
disabled
   -C -type type volume_path : clear the purgeability of files of the specified 'type' on the volume referred to by 'path'.
   -m <verb> path            : mark the file at path as purgeable with the various options specified.
Purgeable flags for %s are: 0x%llx\n
-fault
-syncroot
music
Set the fs typename override on %s to %s (fstname ptr %p)\n
failed to get the path for fd: %s, error %s\n
   -G [options] path         : get stats on the purgeable files on the volume specified by 'path'.
-high
Purging files on %s (offline) returned %d (%s).  Deleted amount: %lld (%llu files)\n
video
Video
user-discarded
failed to set the sync-root flag on %s : %s\n
Failed to set atime update setting : %s\n
-su
-zero
Purging the single file %s failed: %s (%d)
The -residency argument requires a residency reason.
the -typetotal argument requires a type of file to purge
                               'options', if provided, could be one of: -low -med -high -su -uoffline -future -nodups
Total num purgeable files: %lld   Total purgeable data size: %lld\n
Marked %s purgeable with flags 0x%llx (supplemental 0x%llx)\n
data
The -future argument requires a unix timestamp value (numeric, nsec).
the -typetotal argument requires numerical limit to purge
/dev/fd/
   -D set=yes/no  : enable / disable defragmentation for volume or container.
   -s             : set container UUID and its volume(s) UUID(s) to new random values.
   -z path                   : make the file at path exempt from copy-on-write semantics for snapshots.
Cancelling offline purge on %s returned %d (%s).\n
foundation-api-discarded
The -syncroot argument requires an inode number.
APFS Utility tool
   -D get         : Get defragmentation setting for volume or container.
   -k             : get volume UUID.
need a path to a volume to clear purgeable files on.
request has flags: 0x%x type: 0x%x min_size %lld max_age %lld desired_amt %lld (size: %zd)\n
request has flags: 0x%llx type: 0x%llx typelimit: %llu min_size %lld max_age %lld desired_amt %lld (size: %zd)\n
Invalid argument: expected purge reason
Usage: %s <option> [<verb>] path|dir|device [<optional parameter>], as follows:\n\n
```
