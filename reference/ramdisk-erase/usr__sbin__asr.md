# `/usr/sbin/asr`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 380,176 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 2632)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (9)

- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Bom.framework/Bom (compatibility version 2.0.0, current version 195.0.0)`
- `/System/Library/PrivateFrameworks/MediaKit.framework/MediaKit (compatibility version 302.0.0, current version 944.0.0)`
- `/System/Library/PrivateFrameworks/DiskImages.framework/DiskImages (compatibility version 1.0.8, current version 710.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.security.network.server</key>
	<true/>
</dict>
</plist>
```

## Strings (1,004)

```
Size
outPropertyList
No checksum present for metadata. Assuming valid...
Bad data received from server
Usage: %s <verb> <options>\n
Include loaders
Snapshots cannot be used with invert restores.  The --useInverter\noption cannot be used with snapshot options.
VolGroupUUID
Could not find any scan information - %s
Could not find a system volume in container at %@
Only one additional physical store can be specificed with --extraPV.
HFSX
/..namedfork/rsrc
OOB Ranges
Verification is supported only for block operations
GPT
reserve
Can't open file
No Minimum Size For Loader
%s: could not convert snapshot name to c string
Apple_HFS
41504653-0000-11AA-AA11-00306543ECAC
/sbin/fsck_hfs
This server is too new for this version of asr
Passphrase
-onodev
XSTA\tmetadata
split offset
disk%is%i
-g
All missing data is within %lld bytes\n
Could not finish mounting volumes on %@
Inverting target volume...
Ran out of buffers
Could not change the partition type for %@ - %@
--inpartition is not valid with multicast restores
Buffer Count
Filesystems:\n
%s%s
Couldn't get container for physical store %s
Could not get mount information for volume %@
Source must be a device node
fromSnapshot
-y
Port
Packet dropped
HFS
Apple_DMG
XSTA\t%s
Couldn't find system volume in container %s%s
DeleteAPFSVolume in loop
Could not initialize DiskArbitration - %s
Merge Adjacent Freespace Records
\nServer data rate exceeds client capability, or packet loss exceeds\nerror correction ability.\nAdjust server data rate and/or verify network integrity and try again.\n
Verify failed: the recovery partition is not set up correctly.
csumbuffersize
verify: checksum of %s is valid\n
AppleAPFSSnapshot
Total Skip Size
Image failed signature verification.
Out of read buffers.  Blocking for the stream buffer lock
Error looking up UUID for volume at %@
IOProviderClass
\tChecking disk
Could not use image for multicast operation. Please use \"asr imagescan\"
-oexec
%s is not a block or character device
The target must be a file/folder path for multicast copies
Initiate
Could not set the stream packet TTL
disk%ds%d
fail: checksum failure
Skip Instructions
The error is caused by corruption in transit, probably due to a bad cable,\n
XVDG\tforward error correction at %llu
plist
r
Could not initialize DiskImages framework - %s
.shadow
Could not open resources for image
FALSE
0
-onoexec
system-entities
\nMissing data: expected %lld, got %lld (%ld packets)\n
No BSD name found for IOMedia object with GUID %s.  That shouldn't happen.
No --target for partition mode
Remounting target volume...
DeleteMe
compressed
streambuffersize
fail: stream timed out
debug
CannotCreatePlist
Percent Threshold
DNS Service Discovery Status
Can't deserialize metadata information
format
./private/var/db/dyld/dyld_shared_cache_rosetta
Error communicating with server
Server didn't send packets per FEC
SHA-384
No Multicast Address specified
PSTT\t0\t100\tstart replicate
thread-safe
      --hidden          restore to the hidden customer software partition\n
mount-required
Couldn't write to target device %s, %s
chunkchecksum
Schemes
/usr/sbin/xartutil
High Tide Mark
  <verb> is one of the following:\n
CopyRegistryProperty in loop
GetContainerWholeDisk
Unable to convert blkx resource to copy instructions
Calculated %s checksum %llu bytes in %.2f seconds, %.2f KiB/s\n
%lld
--corestorageconvert cannot be used with --hidden.  Try --csheader instead.
The target must be a single APFS volume for a snapshot delta restore - %@
Adjust completed successfully
Missing a total of %lld bytes from the stream\n
Checksum calculation failed for image %@
Couldn't find partition record for device %s, with partition ID %d.
Data Offset
Block Count
-d
%s/
Checksum failed: expected 
XSTA\tstart\t%s\tclient
Error looking up snapshot on device %@
-v
SHA-256
Can't interpret %s as a plist
Verify failed: partitions are not set up correctly for Core Storage conversion.
Encrypted
IOMedia
Data Rate of 0 is invalid
%sdisk%i
Rounding Unit
\tVerifying  
IODeviceTree
The source must be an APFS container for ARV block restores
Forcing a volume to be unencrypted requires a sibling volume to be present
Improperly encoded Multicast Address
Ignoring bad URL
the argument to --recoveryPV must be a disk device (e.g. /dev/disk2s2).
/Volumes/%s
Setup
FEC packet dropped due to congestion.  Continuing.
%s failed to verify
\nAttempt to read() offset 0x%llX from socket failed with errno of %d
device
%d
Container has no recovery volume
Could not allocate data for request
Could not mount source image
Direct Mode
Error finding volume with appropriate role in container %@
Could not get mount info for %s
vectored://%@/Default.dmg
filechecksum
DevMountPartitionWithOptions failed inside CopyFirstUUIDFolderName with error %d
system-image
PV Seek
force-TDM
Sealed
dev-entry
Stream ID
csumbuffers
disk%d
Shared Writer
PSTP\t100\t100\tstop restore%s
Checksum
/System/Library/Filesystems/hfs.fs/Contents/Resources/hfs.util
XVDG\tmissed stream data %ld packets at position %lld
%s: could not create snapshot name from root hash
SHA256
-s
Error finding volume with matching snapshots in container %@ - %d
Total
Could not determine disk image size: %d
bs-cache-depth
buffersize
no-personalization
calculated optimal virtual start offset as %qd\n
group UUID
/System/Library/Lockdown/SBOOT_S5L8900.pem
Replicating 
-onoowners
/dev/rdisk%d
Could not get the uuid for the snapshot volume %@
used
\n\t%s\n
IOGUIDPartitionScheme
Copying Blocks
Starting stream %s
Failed to get partition media: %d\n
\"--%s\" option specified multiple times
puppetstrings
1
%llu
Validating sizes...
--pr-options-file argument must be a valid path
EF57347C-0000-11AA-AA11-00306543ECAC
newfs_apfs
w
Content
Restore canceled\n
vectored://Default.dmg
arguments to --extraPV must be disk devices (e.g. /dev/disk2s2).
\nKilled\n
./private/var/db/dyld/dyld_shared_cache_ppc
Local IPC path too long
CS Header
Checksum failed.\nExpected %lX\nbut got %lX
fs_used
r+
Ejecting the source image...
Source %s cannot be opened for reading - %s
Invalid OOB request
--erase must be used with the --inpartition flag
toSnapshot
IOAPFSPreBootDevice
fsindex=%d
msdos
Note: checksumming turned off due to format argument
HFS+ Extended
Origin
The target device for a device restore must be a device node
--target, --targetblockcopy and --targetARVcopy are mutually exclusive.
expectedhash
Scramble Active
Status
could not checksum %@
Couldn't read image backing store
/dev/disk%ds%d
%s (%s)
recoveryPV
Apple_KernelCoreDump
-orw
com.apple.os.update-
New UUID
Missing server configuration plist
Retrieving scan information...
DeleteFoldersFromContainerForUUID
pr-options-file
Received OOB request:\n
Unknown checksum type from server
mount-nobrowse
Could not erase target - %@
Could not find a data partition to restore.
FULL_USAGE
mount-attempted
GUID
Device restore failed - %s.\n
AppleAPFSContainer
removable
hfs
APFSImplementation error: requested slice not honored in APFSVolumeCreate
The argument to --splitoffset must be a multiple of 512
Bom copy exited with error %d
The Multicast TTL key must not be 0
buffers
://
block
Family
XVDG\tstreambuffer blocked
Type
--blockonly is deprecated.  By default only the block checksum is performed.
\nThe volume in the partition %s could not be frozen\nbecause it needs repair.\nRun fsck_hfs or another disk repair utility to diagnose the problem\n
XSTA\tfail: checksum failure
fs_reserve
/System/Library/Filesystems/exfat.fs/Contents/Resources/exfat.util
XSTA\twait
Can't specify both --device and --file
MaxDisk
The source and target cannot be the same
Read 1KB Zeroes
Container Bytes
High virtual tide is currently %qd\n
v
Subrange Offset
Instruction Code
\nError: %s\n
Broken
Could not validate device restore target - %s.\n
Waiting for connection attempt from server
Short write (%ld, %ld)
disk%i
partnumber
ID
VectoredBackingStoreCallbackData
decompression of chunk %d failed
Error waiting for container %@ to quiesce
error while scanning \"%s\".
ForceInvert
Include all
Ignore Shims
/System/Library/Filesystems/ntfs.fs/Contents/Resources/ntfs.util
Connect to client
Partition ID
Image Size
f
No IOMedia object found for GUID %s.  Device may have been open.
retestsize
-odev
-obrowse
Could not find a data volume in container at %@
com.apple.recovery.boot
Macintosh HD
CaseSensitive
Filesystems
partition
The given volume does not contain the given snapshots.
'%s' failed %s (File %s; Line %d)\n
Tidemark
Could not send payload data
The image %@ has no checksum to verify
ASRNewVolume_%d
Failed to read the stream
XSTA\tstart\t%s\tmulticast-client
Could not unmount partitions on %s
Writable
Incompatible
IOPartitionScheme
Boot OS X
 loop
Volume has no UUID, and no group UUID path present in special volume
    %s restore --source <source> --target <target> [<options>]\n
apfs_invert
IODeviceTree:/
Could not map UUIDs for APFS volumes in container %@
FormatDeviceAPFS
-c
UseGroupUUID
 retry
Could not resolve %s to DiskImage backing store: %d
Invalid argument \"%s\" for option %s
ntfs
Device %s is larger than 4 GB\n
Include patch
The customer partition is too full
\nCould not get data at position %llu (stream at %llu).  Returning EAGAIN\n
    %s info --source <source> [--plist]\n
      --partnumber <string>    add string to metadata during imagescan (key \"part number\")\n
help
--splittarget can only be used with --recoveryPV
    %s adjust --target <partition> [--settype <partType>]\n
suppress-uiagent
GetRoledVolume
AppleAPFSMedia
Checksum failure! Expected %lX but got %lX
Sending payload
Could not repartition target %s: %s
FormatDevice: not a legal dev entry: \"%s\"
Initialized communication with client
the --settype option cannot be used with --hide or --show.
bootroot
IOClass
Kernel Flags
Can't connect to client
Checksum Chunks
nocheck
close(%s)
embed
MBR
Writing to two targets. Split point is %.1f GiB (%lld bytes).
GUID_partition_scheme
Could not access device %s\n
%02hhx
sourcevolumeUUID
://disk
PV Size
targetblockcopy
./Volumes/
com.apple.Boot.plist
Maximum Transfer Sector Count
server
/ContainerToInvert
\nRestore canceled
file-checksum-3
-A
/sbin/mount
SHA-512
Applying FEC fix
factory
EBD0A0A2-B9E5-4433-87C0-68B6B72699C7
Include drivers
No --target for adjust mode
--streambuffersize only valid in Multicast Restore mode
Recovery HD
./private/var/vm/
%@%@
No Data Rate specified
Verifying  
adjust
Restore
Could not retrieve scan information - %@
Booter
-J
Include aux
0x
data-run-info-global
Apple_partition_scheme
newPlist
Record Runs
Could not mark APFS container as new/unique
Generate Freespace Records
Couldn't get partition ID from registry, error %d
Can't specify both --target and --file
PSTT\t0\t100\tstart fsck %s
Target Device
Cannot use socket %d: type is %d, not SOCK_STREAM
/sbin/umount
WaitForQuiescence
Couldn't unmount all volumes from %s, error %d
Erase option required for multicast restore
Reading retry data from server failed
Could not understand multicast server response
\nCleaning up...\n
useFilesystemCache
Record Tidemark
-q
sector-start
read-only
MS-DOS
Record On Bits
PSTT\t0\t100\tstart restore retry
Packets Per FEC
 %#02hhx
verify-peer
  <size> is in bytes but may end with a scale factor (b, k, m, g)\n\ncommon <options> are any of:\n      --source <source> path or url to disk image file, mountpoint, or\n                        web accessible disk image\n      --puppetstri
Recovery partition restores can only be done on GPT partition maps.
IOService
-R
Could not open disk image %@ for verification
Waiting for server
The following volumes will all be erased:
Recovery
\nCore Storage group must have exactly one LV in order to freeze.\n
(NULL)\n
--nocheck has been deprecated.  Use --noverify instead.
The source must be an image in order to verify
Could not reconcile volumes in container %@ - %@
SHA-224-digest
Couldn't write to secondary target device %s, %s
Restoring  
-F
replicate
Cannot use socket %d
%srdisk%d
IOFDiskPartitionScheme
SHA-224
Image format is not UDIF\n
No client requests.  Suspending stream %s
Could not access multicast stream information
The source must be an HFS volume when converting to Core Storage
Erase contents of %s? [ny]: 
Multicast Address
CopyRegistryProperty
HFS Variant
DIAG
Scramble Sectors
FEC packet dropped
Erasing target device %@...
noprompt
Restore completed successfully.
./System/Library/dyld/dyld_shared_cache_rosetta
 
Test
%s: %d
APFS inverter failed to invert the volume - %@
Options
newdevice
XSTA\tfail: packet loss
XSTA\tstart\t%s\tadjust
DOS_FAT_32
Erase these volumes? [ny]: 
/usr/standalone/OS.dmg.root_hash
v sector %qd-%qd p offset %qd-%qd\n
h
t
Multicast file copy failed - %@
./private/var/db/dyld/dyld_shared_cache_i386
NTFS
BadParameter
Restrict Freespace
BSD name
    %s help | version\n
server <options> are any of:\n      --interface <if> Use 'if' as the interface for the server's\n                       outgoing stream\n      --config <configuration> server configuration file in plist format\n\n
Locked
file
Apple_HFSX
%srdisk%i
Not enough space on %@ to restore
Replicating
s1
Sectors/Track Alignment
No Filesystems information\n
imagescan
Unmount
image scan not supported
%s
Apple_UFS
Can't determine image size
1.2.12
erase
./System/Library/dyld/dyld_shared_cache_i386
Could not get information about device \"%s\"
Could not restore - %@
Couldn't reprobe target device %s, %s
asr
PSTP\t100\t100\tstop verify
Can't do a device restore to a device with a mounted volume
Could not look up self: %s
recoverysize
Target for adjust mode must be a partition with no mounted volume
Failed to create source stream for replication
PINF\t%d\t100\tverify
port
</plist>
Buffer Size
PSTT\t0\t100\tstart restore loop
sourcevolumename
-o
Could not understand client request
Couldn't open device %s: %s\n
Ignoring preference setting of ForceInvert as it is\nincompatible with snapshot options.
Couldn't allocate restore state
PSTP\t100\t100\tstop fsck %s
Couldn't run \"%s\"
[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}
Only one of --usereplication and --useInverter can be used
Content Ephermeral
Partition Loader
unknown
./private/tmp/
SHA-256-digest
Could not determine execution mode
Could not change the partition size for %@
Length
\nCouldn't find partition of appropriate type to freeze\n
-S
Could not create metadata request
    %s server  --source <source> --config <plist> [<options>]\n
Start Offset
Data Runs
Checksum Type
YES
Partitions:\n
vectored://foo/bar.dmg
UnmountPartition
nostream
SHA1
./System/Library/dyld/dyld_shared_cache_ppc64
-C
/dev/r%s
Could not resize APFS container - %@
\nThe volume could not be frozen because\n it is a Core Storage volume with multiple physical volumes.\n
Block restoring over an APFS container requires --erase.
hide
--csheader can only be used with --hidden
Validating source...
LCFD
Physical size
Thread Count
-onobrowse
ASRDataVolume_%d
Include data
show
Couldn't reprobe secondary device %s, error %d
RepairDevice: not a legal dev entry: \"%s\"
Source volume format not yet supported in this version of macOS
blockonly
Metadata has incorrect size
Source image volume size is not an exact multiple of 1 MiB
UnmountAllPartitions
Copy
Container has no preboot volume
platform-name
Server didn't send packet size
force-outkernel
Verifying
\toffset %qd (%#qx) length %lu (%#lx)
-osuid
Error while looking up data volume in container %@: %@
source
TRUE
localhost
Could not write FEC data
%02x
--erase must be used with the restoreexact verb.
/dev/disk
nobrowse
XSTA\tfail: stream timed out
Untitled
apfs.util
XSTA\tpass %d
Target device %s couldn't be opened, %s
Time Threshold
fs_quota
/System/Library/Lockdown/SBOOT_S5L8900_DEV.pem
GetGroupListForVolume
Couldn't read device
Root Hash object too small (expected %d)
Unexpected path for block or character device: %s
SystemOuterSlice
Volume offset
%02X
Address
info
WriteMedia
426F6F74-0000-11AA-AA11-00306543ECAC
Open
Partitions
com.apple.asr.%ld
Can't interpret %s as a path
Multicast server configuration:\n
Could not get target partition size
DevUnmountPartition failed inside CopyFirstUUIDFolderName with error %d
Multicast TTL
Could not set outgoing interface to %s
slurp
Could not find APFS container disk for target - %@
Could not get mount information for device %@
Couldn't open device %s, error %d
copyResources
Could not get information about \"%s\"\n
GetVolumeWithRole
bytes
Can't interpret %s as a URL
The corruption did not occur in transit, so this is either caused by\n
      --erase           formats target volume\n      --format <HFS+|HFSX> target format when erasing (defaults to source)\n      --noprompt        don't require confirmation on erase\n      --noverify        don't checksum results\n      --
image-options
fail
%02hX
File copy is not supported anymore.  Use the --erase flag.
noverify
Unrecognized filesystem format \"%s\"
./.journal_info_block
/dev/null
\nCouldn't regrow the filesystem for volume %s.\nYou should immediately back up all data in the volume and reformat it.\n
Could not validate device restore source - %s.\n
asr multicast server must be run as root
size
<error getting string representation>
LVUUID
%@
XDBG\tOOB retransmit %qd length %ld
com.apple.asr
Could not find any scan information. The source image needs to be imagescanned before it can be restored.
Can't do a device restore from a mounted volume
Metadata File
Could not create payload socket
Could not maximize the payload socket buffer
Stream ID is %#.4x\n
Could not get mach time conversion
\t
Metadata checksum failed
Could not validate sizes - %@
/dev/disk%i
RestoreData
Couldn't set socket option
Exiting - all requests satisfied
shadow-url
AddAPFSVolumeToContainer
-ordonly
Secondary target device %s couldn't be opened, %s
Could not parse --expectedhash
/sbin/newfs_hfs
mount-point
Could not resolve %s to DiskImage: %d
imagescan <options> are any of:\n      --filechecksum calculate file checksum\n      --nostream     don't reorder file for multicast streaming\n
Restored target device is %@.
XSTA\tstart\t%s\tmulticast-server
MAP
Block Size
SHA-1
-p
GetVolumeSizes
Couldn't get UUID for device %s - %s
sector-count
Failed to bind server socket
Volume at %@ has no UUID
Yes
FEC Slice Stride
data
CopyAPFSVolumeUUIDs
timeout
/dev/%s
unknownfs
Payload
Max Retry
unsupported family
Got %s digest of disk image file of: 
fsck
/%s
runs
Could not get UUIDs for APFS volumes in container %@
Filesystem
New group UUID
Failed to listen on server socket
Copying    
%s%@
slurp operation failed - %s
Rebuilding catalog
bad memory on the device or corruption on the host prior to transmission.\n
Could not query APFS container for data volume
PV UUID
Couldn't get block size\n
NoURLSpecified
Instructions
Data Rate
--hide and --show are mutually exclusive
Missing source device
Processed
%s\n
\tRange %qd-%qd(%qd) has compression ratio %f, throttle factor is %f\n
Chunks
testsize
no-bless
ContainerToInvert
-r
ro
ioctl(%s, DKIOCEJECT)
Restore canceled
Apple_CoreStorage
Include most
fsck_hfs failed to convert the target to case-sensitive.
fail: packet loss
Client aborted connection
skip-verify
Image is not ordered
Embedded Offset
Could not establish connection
%s failed with error %d\n
The source must have a recovery partition when converting to Core Storage
ExtractPartitions
<?xml
/sbin/newfs_msdos
Invalid target for adjust mode: %s
\nHigh physical tide is currently %qd\n
Couldn't check writeability, error %@
Failed to realloc runs
The cable may be bad or insecurely attached.\n
Image passed signature verification
splitoffset
Error looking up system volume for data volume %@: %@.
/.vol/%u/%u
/dev/random
writeable
Could not validate source - %@
--splitoffset can only be used with --splittarget
/dev/r
Couldn't stat mount-point: %s
UUID
XSTA\tfinish
the copy engine failed: %@
Plan 9
Geometry
Client Data Rate of 0 is invalid
Writing multicast metadata to %s
Copying Files
usereplication
readonly
restore <options> are any of:\n      --target <target> path to volume or mountpoint\n
main-url
Retain existing content
csheader
PINF\t%d\t100\t%s
Image format is not UDIF
Could not write all the data
BSD Name
IOApplePartitionScheme
Could not get image resource information: %d
-t
PV Throughput
Unable to decode root hash as img4
./.Spotlight-V100/
%s/%s
Image Name
%sdisk%is%i
execv: %s: %s\n
-onosuid
-oowners
Could not get source partition size
OOB Chunk
Checksum Chunk Size
raw
Sector Count
PSTT\t0\t100\tstart restore
Image Size: %qd\n
inpartition
%s failed with error %d
Server didn't send FEC stride
The image data received on the device does not match what was expected\n
Unrecognized verb \"%s\"
Can't specify both --nocheck and --noverify
Could not get volume geometry information - %@
Volume replication failed - %@
config
HFS+
./private/var/db/dyld/dyld_shared_cache_x86_64
Could not get seal information for volume at %@
--erase-disk
%ss%d\n
useInverter
Starting to send payload
Source Offset
Version
open(%s)
target
DeleteAPFSVolume
There are no volumes in the container %@ with the given snapshots.
Job State
Cannot stream dual-fork files.  Try flattening the image.
Media Block Count
AppleAPFSVolume
The source image is missing checksum/hash information.\nPlease rescan it.
FAT
Copied %llu bytes in %.2f seconds, %.2f KiB/s\n
Metadata
corestorageconvert
version %s
Fsck %s 
Sections
Validating target...
Loop Suspend
No --source for imagescan mode
The device restore source must be an image or a device node
Improperly encoded Metadata Multicast Address
No snapshot on volume at %@ with UUID %@
Device %@ is busy
verify
    %s imagescan --source <source> [--filechecksum] [--nostream]\n
Could not repartition target device
./private/var/db/dyld/dyld_shared_cache_ppc64
Erase contents of %s (%s)? [ny]: 
Include unknowns
/Library/Caches/com.apple.xbs/31405251-D749-4DA7-B060-CD11593EDBEB/TemporaryDirectory.POnMCw/Sources/asr/Utilities/UtilitiesCoreFoundation.c
HFS+ Embedded
failed to get properties for device %s, error = %d\n
XSTA\tfail
finish
Name
Couldn't reprobe device %s, error %d
s
copy_arv_apfs_system_snapshot_name
Packet dropped due to congestion.  Continuing.
The stream timed out; no packets for %d seconds
7C3457EF-0000-11AA-AA11-00306543ECAC
SystemInnerSlice
./System/Library/dyld/dyld_shared_cache_ppc
FAT Variant
 for [%llu,%ld], got 
extraPV
Missing source image
    %s partition --target <whole disk> [--testsize <size>]\n                           [--retestsize <size>] [--recoverysize <size>]\n
Whole
Retry %sm
-e
/System/Library/Filesystems/msdos.fs/Contents/Resources/msdos.util
common <options> are any of:\n      --source <source> path or url to disk image file, mountpoint, or\n                        web accessible disk image\n      --puppetstrings   print out messages in format good for machine parsing\n      --
SHA-512-digest
APM
Retest
Could not write data
OpenTargetDevice
genchecksumranges
Apple_APFS
There was data corruption in the transmission from the host.\n
********* Unsupported offset %qd, length %ld\n
Couldn't run \"%s\"\n
UnmountVolumesInGroup
/dev/
XSTA\tverify
Source Device
Could not repartition the target for Core Storage
DataInnerSlice
DataOuterSlice
content-hint
Media size
XSTA\tRetry %sm
Unknown response type
Read failed
    %s restore --source asr://<host>/ --file <file> [<options>]\n
Apple_Boot
FDisk_partition_scheme
Finished
Could not validate target - %@
Can't do info verb with multicast source
force-live
00000000-0000-0000-0000-000000000000
./.hotfiles.btree
./System/Library/dyld/dyld_shared_cache_x86_64
Apple_Free
/System/Library/Filesystems/apfs.fs
OOB Error
interface
./.journal
Embedded Size
%ss%i
Could not set the size for %@
the --recoveryPV option can only be used with the --csheader option.
Couldn't attach source image for restore.
Client Data Rate
OOBData
GetRole in loop
Unmount in loop
PSTP\t100\t100\tstop replicate
Preboot
Missing restore target
Data Length
restore
Incorrectly formatted metadata
Checksum failed.\nExpected %s\nbut got %s
splittarget
/
Reading back the contents of storage after writing it failed to match\nwhat was expected. Either the image needs to be rescanned, or\ncorruption occurred on the device after transmission,\ndue to bad memory or bad storage hardware (NAND).\n
Throttle Data:\n
Server responded with:
Verification failed: partition types for source and target have different sizes.
GetVolumeName
Root Hash object too small (min %d)
Offset
udif-ordered-chunks
Error while looking up system volume in container %@: %@
Couldn't get block count\n
kernelcoresize
insecurehttp
useReplication
--extraPV can only be used with --hidden.
-n
Can't specify --file for non-Multicast restores
Volume adjustment failed: %s
Multicast server operation failed\n
block-checksum-2
XDBG\tfailed request for %lu bytes at position %llu
Couldn't unmount volume on %s, error %d
%@ %@
done
PSTT\t0\t100\tstart verify
Target Offset
launched
allowfragmentedcatalog
hidden
Bad data received from client
Could not get filesystem information from image
Iterating with min %d test %d max %d\n
Could not query APFS container for system volume
settype
APFS volume cannot be the target of restores unless the source is also APFS.
PV Array
PV BSDName
Windows_NTFS
targetARVcopy
No Partitions information\n
-u
Error reading from device %s at offset %X\n
SHA-256 checksumming was requested and the source does not contain a SHA-256 hash
Allow Skips
--blockonly and --filechecksum are mutually exclusive
version
XSTA\tsetup
waiting for server...
The source image is missing file checksum information.\nPlease rescan it with the --filechecksum option.
Command
Chunks:\n
Failed to malloc chunk
%ss%d
Macintosh HD - Data
XSTA\tError: %s
inURL
\"--%s\" is not valid for verb \"%s\"
Media Offset
/dev/rdisk
Could not access %s
XSTA\trestore
Packet Payload Size
OOB Length
restoreexact
Could not attach source image
passphrase
OOB Offset
No image hash to compare.  Either the image must be encrypted or asr must be passed an expected hash.
Repartitioning target device...
Could not fix UUIDs for APFS volumes in container %@
Opening device %s was tried %d times
Container has no system volume
SHA-1-digest
Apple_KFS
APFS
KernelCore
-f
verbose
parasite mode not supported
The source volume cannot be restored because it has a broken seal
NO
set_realtime() failed.
\nSocket unexpectedly closed while trying to read() offset 0x%llX
No data volume corresponding to unreadable system volume at %@
Invalid length for --expectedhash
Kernel Cache
```
