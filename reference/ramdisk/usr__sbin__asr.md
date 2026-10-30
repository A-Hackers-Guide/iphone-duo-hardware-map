# `/usr/sbin/asr`

From the upgrade restore ramdisk (141-29011-104.dmg). 380,176 bytes.

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
useInverter
\nCouldn't find partition of appropriate type to freeze\n
 loop
The target device for a device restore must be a device node
Data Rate
No Data Rate specified
--nocheck has been deprecated.  Use --noverify instead.
No data volume corresponding to unreadable system volume at %@
No snapshot on volume at %@ with UUID %@
target
Target for adjust mode must be a partition with no mounted volume
--splittarget can only be used with --recoveryPV
PSTP\t100\t100\tstop verify
Port
Could not determine disk image size: %d
Start Offset
Erase contents of %s? [ny]: 
hidden
./.journal
XVDG\tmissed stream data %ld packets at position %lld
Setup
Could not get mount information for volume %@
Block Count
/sbin/fsck_hfs
Short write (%ld, %ld)
--target, --targetblockcopy and --targetARVcopy are mutually exclusive.
Bom copy exited with error %d
com.apple.asr.%ld
Unknown response type
vectored://foo/bar.dmg
Restoring  
PV UUID
Couldn't unmount volume on %s, error %d
GetContainerWholeDisk
settype
Could not get mach time conversion
Could not use image for multicast operation. Please use \"asr imagescan\"
-o
Could not write FEC data
No client requests.  Suspending stream %s
There was data corruption in the transmission from the host.\n
No image hash to compare.  Either the image must be encrypted or asr must be passed an expected hash.
Invalid target for adjust mode: %s
Recovery
Include most
%llu
PSTT\t0\t100\tstart restore loop
SHA-512
-n
Erase these volumes? [ny]: 
IOFDiskPartitionScheme
\nServer data rate exceeds client capability, or packet loss exceeds\nerror correction ability.\nAdjust server data rate and/or verify network integrity and try again.\n
com.apple.Boot.plist
Locked
interface
image scan not supported
Could not get filesystem information from image
Cannot use socket %d
--splitoffset can only be used with --splittarget
Error finding volume with matching snapshots in container %@ - %d
.shadow
-F
Data Offset
Loop Suspend
%s: could not convert snapshot name to c string
/dev/rdisk
partnumber
Target Offset
New UUID
Yes
The source volume cannot be restored because it has a broken seal
fail: packet loss
Could not open disk image %@ for verification
PINF\t%d\t100\tverify
s1
expectedhash
the copy engine failed: %@
APFS
Physical size
Failed to get partition media: %d\n
Partition Loader
Can't specify both --target and --file
      --hidden          restore to the hidden customer software partition\n
-osuid
the --settype option cannot be used with --hide or --show.
Include loaders
Origin
[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}
/System/Library/Filesystems/ntfs.fs/Contents/Resources/ntfs.util
OOB Offset
Type
The source image is missing checksum/hash information.\nPlease rescan it.
Can't open file
%s is not a block or character device
partition
Error reading from device %s at offset %X\n
Could not write all the data
imagescan <options> are any of:\n      --filechecksum calculate file checksum\n      --nostream     don't reorder file for multicast streaming\n
Could not get mount information for device %@
UnmountPartition
Multicast server operation failed\n
Could not set the size for %@
Could not attach source image
Incompatible
Stream ID
The argument to --splitoffset must be a multiple of 512
Can't specify --file for non-Multicast restores
insecurehttp
no-personalization
Whole
Apple_Free
Could not resolve %s to DiskImage: %d
restore
WriteMedia
Missing restore target
Could not find a data partition to restore.
Metadata checksum failed
Can't specify both --nocheck and --noverify
CannotCreatePlist
YES
://disk
Can't do info verb with multicast source
Can't determine image size
csheader
GUID
done
TRUE
Source Offset
    %s partition --target <whole disk> [--testsize <size>]\n                           [--retestsize <size>] [--recoverysize <size>]\n
ro
Could not map UUIDs for APFS volumes in container %@
%sdisk%is%i
Kernel Flags
Initiate
XSTA\tpass %d
APFSImplementation error: requested slice not honored in APFSVolumeCreate
/dev/
PSTP\t100\t100\tstop fsck %s
The target must be a file/folder path for multicast copies
1
GetVolumeSizes
fs_used
failed to get properties for device %s, error = %d\n
s
parasite mode not supported
Erase option required for multicast restore
Sections
Time Threshold
-f
Exiting - all requests satisfied
Block restoring over an APFS container requires --erase.
HFS Variant
SHA-1
Could not determine execution mode
the --recoveryPV option can only be used with the --csheader option.
PV BSDName
UnmountVolumesInGroup
The given volume does not contain the given snapshots.
content-hint
Percent Threshold
PSTT\t0\t100\tstart restore
/System/Library/Lockdown/SBOOT_S5L8900.pem
Writing to two targets. Split point is %.1f GiB (%lld bytes).
Retain existing content
--inpartition is not valid with multicast restores
\nRestore canceled
config
Embedded Size
readonly
Waiting for server
inpartition
XSTA\tfinish
Verifying  
/System/Library/Filesystems/apfs.fs
PSTP\t100\t100\tstop replicate
Restored target device is %@.
No --target for partition mode
recoveryPV
./private/tmp/
%lld
csumbuffersize
Apple_Boot
Data Rate of 0 is invalid
Server responded with:
(NULL)\n
Server didn't send packet size
nocheck
Usage: %s <verb> <options>\n
server <options> are any of:\n      --interface <if> Use 'if' as the interface for the server's\n                       outgoing stream\n      --config <configuration> server configuration file in plist format\n\n
ASRDataVolume_%d
Can't specify both --device and --file
The customer partition is too full
Total Skip Size
Could not send payload data
version %s
Improperly encoded Metadata Multicast Address
v sector %qd-%qd p offset %qd-%qd\n
The error is caused by corruption in transit, probably due to a bad cable,\n
-onoexec
sourcevolumeUUID
./Volumes/
XSTA\tRetry %sm
buffersize
Preboot
Could not get target partition size
Ejecting the source image...
IOPartitionScheme
Got %s digest of disk image file of: 
bad memory on the device or corruption on the host prior to transmission.\n
Could not restore - %@
disk%ds%d
LCFD
udif-ordered-chunks
XSTA\tsetup
CopyAPFSVolumeUUIDs
bytes
Improperly encoded Multicast Address
shadow-url
asr
./private/var/db/dyld/dyld_shared_cache_ppc
FDisk_partition_scheme
newfs_apfs
data
read-only
/
Could not get seal information for volume at %@
/System/Library/Filesystems/hfs.fs/Contents/Resources/hfs.util
Could not change the partition size for %@
Retry %sm
Status
Could not find any scan information. The source image needs to be imagescanned before it can be restored.
Can't do a device restore to a device with a mounted volume
0x
close(%s)
Unmount
IOMedia
removable
Writing multicast metadata to %s
Read 1KB Zeroes
Only one additional physical store can be specificed with --extraPV.
toSnapshot
RepairDevice: not a legal dev entry: \"%s\"
No Multicast Address specified
-onobrowse
Multicast file copy failed - %@
-v
Can't interpret %s as a plist
OOB Length
There are no volumes in the container %@ with the given snapshots.
********* Unsupported offset %qd, length %ld\n
Inverting target volume...
debug
IODeviceTree
41504653-0000-11AA-AA11-00306543ECAC
Could not open resources for image
Could not maximize the payload socket buffer
All missing data is within %lld bytes\n
replicate
Couldn't reprobe device %s, error %d
FAT
XSTA\trestore
Forcing a volume to be unencrypted requires a sibling volume to be present
Could not validate source - %@
testsize
Error finding volume with appropriate role in container %@
Rebuilding catalog
Ran out of buffers
disk%d
BadParameter
Copying Blocks
This server is too new for this version of asr
timeout
execv: %s: %s\n
-A
Could not create payload socket
Ignoring bad URL
XSTA\tstart\t%s\tclient
Could not get volume geometry information - %@
%@%@
NO
Chunks:\n
  <size> is in bytes but may end with a scale factor (b, k, m, g)\n\ncommon <options> are any of:\n      --source <source> path or url to disk image file, mountpoint, or\n                        web accessible disk image\n      --puppetstri
--blockonly is deprecated.  By default only the block checksum is performed.
-onodev
Could not find APFS container disk for target - %@
Container has no preboot volume
decompression of chunk %d failed
%s failed with error %d\n
KernelCore
SHA-256
Cannot stream dual-fork files.  Try flattening the image.
  <verb> is one of the following:\n
FAT Variant
info
IOProviderClass
BSD name
    %s restore --source asr://<host>/ --file <file> [<options>]\n
Validating source...
runs
Could not get UUIDs for APFS volumes in container %@
bootroot
%s\n
-odev
version
Allow Skips
\toffset %qd (%#qx) length %lu (%#lx)
Could not look up self: %s
no-bless
HFS+ Embedded
-oowners
The target must be a single APFS volume for a snapshot delta restore - %@
AppleAPFSVolume
The image data received on the device does not match what was expected\n
Applying FEC fix
Couldn't attach source image for restore.
w
Missing source device
Couldn't allocate restore state
Source Device
Could not write data
skip-verify
Apple_DMG
Couldn't get container for physical store %s
Record On Bits
genchecksumranges
Writable
Direct Mode
High Tide Mark
Bad data received from server
XDBG\tfailed request for %lu bytes at position %llu
f
Missing source image
./System/Library/dyld/dyld_shared_cache_ppc
Replicating 
\"--%s\" option specified multiple times
mount-required
Boot OS X
DeleteAPFSVolume
--streambuffersize only valid in Multicast Restore mode
Filesystem
Error communicating with server
Verification failed: partition types for source and target have different sizes.
Copy
Kernel Cache
Volume has no UUID, and no group UUID path present in special volume
The image %@ has no checksum to verify
adjust
-ordonly
%s (%s)
EBD0A0A2-B9E5-4433-87C0-68B6B72699C7
Ignore Shims
mount-point
XSTA\twait
Could not find a data volume in container at %@
extraPV
Ignoring preference setting of ForceInvert as it is\nincompatible with snapshot options.
SHA-256 checksumming was requested and the source does not contain a SHA-256 hash
Sending payload
Rounding Unit
-oexec
Total
-y
\tRange %qd-%qd(%qd) has compression ratio %f, throttle factor is %f\n
--blockonly and --filechecksum are mutually exclusive
-obrowse
Couldn't open device %s, error %d
No --source for imagescan mode
-p
Options
pr-options-file
SystemInnerSlice
Checksum failed.\nExpected %lX\nbut got %lX
-q
DNS Service Discovery Status
1.2.12
/dev/disk%ds%d
erase
APM
Apple_CoreStorage
RestoreData
%@
\tChecking disk
/sbin/mount
OpenTargetDevice
Unexpected path for block or character device: %s
file
Shared Writer
XSTA\tfail: stream timed out
/System/Library/Filesystems/exfat.fs/Contents/Resources/exfat.util
SHA256
%srdisk%d
/usr/sbin/xartutil
fs_quota
Version
Family
Could not set the stream packet TTL
vectored://%@/Default.dmg
Could not unmount partitions on %s
Retrieving scan information...
ForceInvert
HFS+
Opening device %s was tried %d times
Unrecognized verb \"%s\"
Command
--pr-options-file argument must be a valid path
XSTA\tstart\t%s\tadjust
Media size
allowfragmentedcatalog
Checksum failed.\nExpected %s\nbut got %s
Could not get mount info for %s
Image failed signature verification.
FULL_USAGE
Plan 9
\nCore Storage group must have exactly one LV in order to freeze.\n
/dev/random
useReplication
Error while looking up data volume in container %@: %@
Checksum
apfs_invert
Verify failed: partitions are not set up correctly for Core Storage conversion.
Couldn't write to secondary target device %s, %s
Offset
Could not find any scan information - %s
WaitForQuiescence
raw
Could not validate sizes - %@
%s%@
fsindex=%d
The cable may be bad or insecurely attached.\n
buffers
Could not set outgoing interface to %s
DeleteAPFSVolume in loop
/dev/disk
main-url
Volume at %@ has no UUID
/ContainerToInvert
%s failed with error %d
waiting for server...
NTFS
Couldn't read image backing store
Reading retry data from server failed
ntfs
SHA-224-digest
CaseSensitive
block-checksum-2
OOB Error
-g
Could not access multicast stream information
Content Ephermeral
nostream
\nError: %s\n
Error looking up system volume for data volume %@: %@.
Could not query APFS container for system volume
Couldn't get block count\n
Error waiting for container %@ to quiesce
Metadata File
Packets Per FEC
XVDG\tstreambuffer blocked
/Volumes/%s
 retry
Restore canceled\n
Passphrase
Out of read buffers.  Blocking for the stream buffer lock
common <options> are any of:\n      --source <source> path or url to disk image file, mountpoint, or\n                        web accessible disk image\n      --puppetstrings   print out messages in format good for machine parsing\n      --
Copying    
Target device %s couldn't be opened, %s
Copied %llu bytes in %.2f seconds, %.2f KiB/s\n
AppleAPFSSnapshot
Merge Adjacent Freespace Records
%s: could not create snapshot name from root hash
Partitions
localhost
 %#02hhx
Could not validate target - %@
-r
Multicast TTL
/dev/r%s
Broken
'%s' failed %s (File %s; Line %d)\n
Record Runs
Couldn't run \"%s\"\n
Verification is supported only for block operations
VolGroupUUID
Data Length
device
sourcevolumename
GPT
</plist>
\nThe volume in the partition %s could not be frozen\nbecause it needs repair.\nRun fsck_hfs or another disk repair utility to diagnose the problem\n
DevMountPartitionWithOptions failed inside CopyFirstUUIDFolderName with error %d
Could not resolve %s to DiskImage backing store: %d
\nKilled\n
The source must be an APFS container for ARV block restores
Apple_UFS
%s/%s
Metadata
The source must be an HFS volume when converting to Core Storage
Couldn't read device
MaxDisk
Can't connect to client
Could not understand client request
puppetstrings
426F6F74-0000-11AA-AA11-00306543ECAC
./private/var/db/dyld/dyld_shared_cache_i386
Buffer Size
Max Retry
targetblockcopy
Embedded Offset
./System/Library/dyld/dyld_shared_cache_ppc64
Job State
XSTA\tfail
Failed to bind server socket
Validating target...
No Minimum Size For Loader
Couldn't get UUID for device %s - %s
Record Tidemark
\nAttempt to read() offset 0x%llX from socket failed with errno of %d
Skip Instructions
compressed
Error looking up UUID for volume at %@
DeleteFoldersFromContainerForUUID
splittarget
Could not initialize DiskImages framework - %s
sector-count
server
DIAG
SHA-224
Data Runs
Multicast Address
%02x
XVDG\tforward error correction at %llu
-t
source
r
./.Spotlight-V100/
copyResources
XSTA\tverify
No Filesystems information\n
-onoowners
Secondary target device %s couldn't be opened, %s
Apple_APFS
%srdisk%i
Device %@ is busy
slurp operation failed - %s
./System/Library/dyld/dyld_shared_cache_i386
%sdisk%i
verify-peer
%ss%d\n
The Multicast TTL key must not be 0
bs-cache-depth
Could not establish connection
launched
blockonly
kernelcoresize
Iterating with min %d test %d max %d\n
factory
system-image
-c
Cannot use socket %d: type is %d, not SOCK_STREAM
Device restore failed - %s.\n
disk%i
Could not access device %s\n
No --target for adjust mode
AppleAPFSMedia
Restrict Freespace
Windows_NTFS
\nCleaning up...\n
Apple_KernelCoreDump
-R
com.apple.recovery.boot
Local IPC path too long
Checksum Chunks
Verify failed: the recovery partition is not set up correctly.
embed
/sbin/umount
XSTA\tstart\t%s\tmulticast-client
Restore
Not enough space on %@ to restore
verify
New group UUID
Could not get information about device \"%s\"
FEC packet dropped due to congestion.  Continuing.
Client Data Rate of 0 is invalid
XSTA\tstart\t%s\tmulticast-server
/usr/standalone/OS.dmg.root_hash
block
Bad data received from client
Copying Files
Packet dropped due to congestion.  Continuing.
Server didn't send FEC stride
Couldn't find partition record for device %s, with partition ID %d.
PV Throughput
Client aborted connection
The source image is missing file checksum information.\nPlease rescan it with the --filechecksum option.
Address
unknownfs
Volume replication failed - %@
hfs
Unmount in loop
sector-start
\nSocket unexpectedly closed while trying to read() offset 0x%llX
Couldn't get partition ID from registry, error %d
Initialized communication with client
%s failed to verify
Apple_HFSX
0
Include aux
Retest
Block Size
Packet Payload Size
High virtual tide is currently %qd\n
%ss%d
Include patch
AppleAPFSContainer
outPropertyList
Volume offset
finish
%ss%i
Client Data Rate
t
restore <options> are any of:\n      --target <target> path to volume or mountpoint\n
chunkchecksum
XSTA\tfail: checksum failure
Could not understand multicast server response
Include unknowns
Snapshots cannot be used with invert restores.  The --useInverter\noption cannot be used with snapshot options.
file-checksum-3
The source must have a recovery partition when converting to Core Storage
/sbin/newfs_msdos
useFilesystemCache
OOB Chunk
\"--%s\" is not valid for verb \"%s\"
Could not repartition target device
port
nobrowse
Chunks
msdos
Validating sizes...
Could not find a system volume in container at %@
targetARVcopy
./System/Library/dyld/dyld_shared_cache_rosetta
split offset
disk%is%i
suppress-uiagent
/dev/r
r+
the argument to --recoveryPV must be a disk device (e.g. /dev/disk2s2).
Recovery HD
Source %s cannot be opened for reading - %s
HFSX
thread-safe
-e
data-run-info-global
The stream timed out; no packets for %d seconds
hide
Apple_KFS
Could not get the uuid for the snapshot volume %@
Metadata has incorrect size
Failed to read the stream
/sbin/newfs_hfs
/dev/%s
Include all
Failed to realloc runs
Couldn't reprobe target device %s, %s
DevUnmountPartition failed inside CopyFirstUUIDFolderName with error %d
Sectors/Track Alignment
%02hX
    %s adjust --target <partition> [--settype <partType>]\n
Invalid length for --expectedhash
csumbuffers
Remounting target volume...
Starting stream %s
OOB Ranges
\nHigh physical tide is currently %qd\n
--erase must be used with the restoreexact verb.
XSTA\tError: %s
Verifying
PV Size
--erase must be used with the --inpartition flag
MBR
Target Device
Image Size: %qd\n
Can't deserialize metadata information
GetRoledVolume
PSTT\t0\t100\tstart fsck %s
The device restore source must be an image or a device node
calculated optimal virtual start offset as %qd\n
reserve
SHA-384
APFS inverter failed to invert the volume - %@
IOGUIDPartitionScheme
inURL
v
-orw
SHA-512-digest
PV Seek
streambuffersize
com.apple.asr
Subrange Offset
Image passed signature verification
Could not get source partition size
The following volumes will all be erased:
Erasing target device %@...
-C
Incorrectly formatted metadata
PSTT\t0\t100\tstart replicate
FormatDevice: not a legal dev entry: \"%s\"
-u
MS-DOS
Apple_partition_scheme
newPlist
Tidemark
%s/
unsupported family
Connect to client
Failed to create source stream for replication
ioctl(%s, DKIOCEJECT)
SHA1
\tVerifying  
apfs.util
-S
Multicast server configuration:\n
Include data
./.journal_info_block
IOService
plist
 
NoURLSpecified
Test
XSTA\tfail: packet loss
Invalid argument \"%s\" for option %s
FEC packet dropped
Missing a total of %lld bytes from the stream\n
    %s server  --source <source> --config <plist> [<options>]\n
Encrypted
No BSD name found for IOMedia object with GUID %s.  That shouldn't happen.
\nThe volume could not be frozen because\n it is a Core Storage volume with multiple physical volumes.\n
fail: checksum failure
HFS
Replicating
--csheader can only be used with --hidden
Could not reconcile volumes in container %@ - %@
SHA-256-digest
No IOMedia object found for GUID %s.  Device may have been open.
CopyRegistryProperty in loop
FALSE
<?xml
Throttle Data:\n
Couldn't reprobe secondary device %s, error %d
OOBData
Source volume format not yet supported in this version of macOS
force-TDM
Generate Freespace Records
Couldn't set socket option
Fsck %s 
Couldn't unmount all volumes from %s, error %d
/dev/disk%i
Name
Length
-d
IODeviceTree:/
    %s info --source <source> [--plist]\n
Could not resize APFS container - %@
CopyRegistryProperty
retestsize
%02X
Macintosh HD
Could not create metadata request
restoreexact
    %s help | version\n
Could not retrieve scan information - %@
Could not finish mounting volumes on %@
Couldn't get block size\n
Unable to decode root hash as img4
%s
error while scanning \"%s\".
Container Bytes
Could not repartition the target for Core Storage
Apple_HFS
could not checksum %@
Could not validate device restore target - %s.\n
Failed to listen on server socket
Could not mount source image
./private/var/vm/
writeable
Content
UseGroupUUID
mount-attempted
BSD Name
Device %s is larger than 4 GB\n
Unrecognized filesystem format \"%s\"
Unable to convert blkx resource to copy instructions
asr multicast server must be run as root
--hide and --show are mutually exclusive
AddAPFSVolumeToContainer
GetVolumeWithRole
Instruction Code
Read failed
Can't do a device restore from a mounted volume
%s: %d
open(%s)
fsck
/dev/null
used
--corestorageconvert cannot be used with --hidden.  Try --csheader instead.
Could not erase target - %@
LVUUID
Scramble Active
Can't interpret %s as a path
XDBG\tOOB retransmit %qd length %ld
Include drivers
copy_arv_apfs_system_snapshot_name
newdevice
fromSnapshot
ContainerToInvert
Sealed
Could not validate device restore source - %s.\n
vectored://Default.dmg
Couldn't find system volume in container %s%s
7C3457EF-0000-11AA-AA11-00306543ECAC
filechecksum
Adjust completed successfully
./private/var/db/dyld/dyld_shared_cache_rosetta
ID
Size
PSTP\t100\t100\tstop restore%s
/System/Library/Filesystems/msdos.fs/Contents/Resources/msdos.util
Finished
Could not change the partition type for %@ - %@
PV Array
help
\nCouldn't regrow the filesystem for volume %s.\nYou should immediately back up all data in the volume and reformat it.\n
Stream ID is %#.4x\n
DataInnerSlice
--erase-disk
/.vol/%u/%u
Filesystems
No checksum present for metadata. Assuming valid...
com.apple.os.update-
Could not access %s
Missing server configuration plist
fail: stream timed out
Volume adjustment failed: %s
Restore completed successfully.
Checksum Chunk Size
DataOuterSlice
Reading back the contents of storage after writing it failed to match\nwhat was expected. Either the image needs to be rescanned, or\ncorruption occurred on the device after transmission,\ndue to bad memory or bad storage hardware (NAND).\n
Waiting for connection attempt from server
%s%s
XSTA\t%s
-s
DOS_FAT_32
Image Name
    %s imagescan --source <source> [--filechecksum] [--nostream]\n
arguments to --extraPV must be disk devices (e.g. /dev/disk2s2).
image-options
Couldn't open device %s: %s\n
h
IOClass
%d
dev-entry
IOAPFSPreBootDevice
Image Size
Maximum Transfer Sector Count
GetRole in loop
force-live
usereplication
GUID_partition_scheme
Untitled
Starting to send payload
slurp
    %s restore --source <source> --target <target> [<options>]\n
Couldn't check writeability, error %@
VectoredBackingStoreCallbackData
No Partitions information\n
\nMissing data: expected %lld, got %lld (%ld packets)\n
Recovery partition restores can only be done on GPT partition maps.
Could not mark APFS container as new/unique
Macintosh HD - Data
splitoffset
Couldn't run \"%s\"
PINF\t%d\t100\t%s
verify: checksum of %s is valid\n
./private/var/db/dyld/dyld_shared_cache_x86_64
fsck_hfs failed to convert the target to case-sensitive.
Partitions:\n
The source must be an image in order to verify
Could not query APFS container for data volume
Media Offset
%02hhx
-J
IOApplePartitionScheme
Checksum failure! Expected %lX but got %lX
Calculated %s checksum %llu bytes in %.2f seconds, %.2f KiB/s\n
platform-name
Restore canceled
/Library/Caches/com.apple.xbs/31405251-D749-4DA7-B060-CD11593EDBEB/TemporaryDirectory.POnMCw/Sources/asr/Utilities/UtilitiesCoreFoundation.c
Thread Count
group UUID
Checksum failed: expected 
Could not fix UUIDs for APFS volumes in container %@
Could not parse --expectedhash
Could not initialize DiskArbitration - %s
HFS+ Extended
://
UUID
./private/var/db/dyld/dyld_shared_cache_ppc64
SHA-1-digest
size
Packet dropped
The source and target cannot be the same
Error while looking up system volume in container %@: %@
/dev/rdisk%d
Source image volume size is not an exact multiple of 1 MiB
UnmountAllPartitions
Root Hash object too small (min %d)
Source must be a device node
./System/Library/dyld/dyld_shared_cache_x86_64
Sector Count
fail
/..namedfork/rsrc
fs_reserve
Payload
Repartitioning target device...
./.hotfiles.btree
EF57347C-0000-11AA-AA11-00306543ECAC
Buffer Count
FEC Slice Stride
GetGroupListForVolume
corestorageconvert
Invalid OOB request
Server didn't send packets per FEC
Only one of --usereplication and --useInverter can be used
Erase contents of %s (%s)? [ny]: 
Media Block Count
Couldn't write to target device %s, %s
system-entities
CS Header
ASRNewVolume_%d
00000000-0000-0000-0000-000000000000
Filesystems:\n
Schemes
Image format is not UDIF
Scramble Sectors
PSTT\t0\t100\tstart verify
unknown
<error getting string representation>
Geometry
Instructions
 for [%llu,%ld], got 
Open
Unknown checksum type from server
Root Hash object too small (expected %d)
--extraPV can only be used with --hidden.
Partition ID
DeleteMe
Checksum Type
The corruption did not occur in transit, so this is either caused by\n
XSTA\tmetadata
File copy is not supported anymore.  Use the --erase flag.
Processed
      --erase           formats target volume\n      --format <HFS+|HFSX> target format when erasing (defaults to source)\n      --noprompt        don't require confirmation on erase\n      --noverify        don't checksum results\n      --
mount-nobrowse
APFS volume cannot be the target of restores unless the source is also APFS.
show
\nCould not get data at position %llu (stream at %llu).  Returning EAGAIN\n
Note: checksumming turned off due to format argument
verbose
noverify
%@ %@
recoverysize
SystemOuterSlice
Couldn't stat mount-point: %s
Could not repartition target %s: %s
MAP
/System/Library/Lockdown/SBOOT_S5L8900_DEV.pem
set_realtime() failed.
Checksum calculation failed for image %@
-onosuid
Error looking up snapshot on device %@
FormatDeviceAPFS
noprompt
\n\t%s\n
imagescan
      --partnumber <string>    add string to metadata during imagescan (key \"part number\")\n
GetVolumeName
passphrase
Container has no system volume
Image is not ordered
PSTT\t0\t100\tstart restore retry
ExtractPartitions
Image format is not UDIF\n
Received OOB request:\n
Could not get image resource information: %d
force-outkernel
Could not get information about \"%s\"\n
Can't interpret %s as a URL
\t
Failed to malloc chunk
Booter
Container has no recovery volume
Could not allocate data for request
format
/%s
```
