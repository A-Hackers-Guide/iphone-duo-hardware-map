# `/System/Library/Filesystems/apfs.fs/apfs_boot_util`

From the upgrade restore ramdisk (141-29011-104.dmg). 92,784 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1792)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/APFS.framework/APFS (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.unlock</key>
	<true/>
	<key>com.apple.private.apfs.create-synthetic-symlink-folder</key>
	<true/>
	<key>com.apple.private.apfs.root-mount-update</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.tcc.allow</key>
	<array>
		<string>kTCCServiceSystemPolicyRemovableVolumes</string>
	</array>
	<key>com.apple.private.vfs.exclave-fs-register</key>
	<true/>
	<key>com.apple.private.vfs.graftdmg</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.rootless.restricted-block-devices</key>
	<true/>
	<key>com.apple.rootless.storage.apfs_boot_mount</key>
	<true/>
	<key>com.apple.rootless.storage.early_boot_mount</key>
	<true/>
	<key>com.apple.rootless.volume.Preboot</key>
	<true/>
	<key>com.apple.rootless.volume.Recovery</key>
	<true/>
	<key>com.apple.rootless.volume.iSCPreboot</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>
```

## Strings (191)

```
%s:%d: %s failed - error %s (%d). Ignoring...\n
%s:%d: failed to graftdmg: %d\n
%s:%d: failed to create path %s (%s)\n
%s:%d: failed to remove overprovisioning file: %d\n
conformance
61706673-7575-6964-0002-766f6c756d00
sha3_512_4k
%s:%d: unable to get fsindex for root device %s\n
%s:%d: failed to look up hw.osenvironment: %s(%d)\n
%s:%d: could not open container %s for volume creation: %d\n
IOMedia
encrypted
uid=
61706673-7575-6964-01c0-766f6c756d00
61706673-7575-6964-0240-766f6c756d00
%s:%d: %s failed - error %d (errno %d)\n
fs_quota
mount_apfs
Unrecognized mount phase
%s:%d: No volume with role %d present on %s.\n
%s:%d: invalid exclaves status: %d\n
/System/Cryptexes/ExclaveOS
Size
case=insensitive
gid=
61706673-7575-6964-0100-766f6c756d00
%s:%d: Failed to open %s - %s. Ignoring...\n
%s:%d: cannot create directory '%s' - %s(%d)\n
%s:%d: unable to get volumes in volume group of root device %s\n
create_and_register_exclave_path_if_needed
role=
case=sensitive
/private/var/logs
%s:%d: cannot resolve mount path for %s (%s): %s\n
%s:%d: volume %s with role = %x already mounted at %s in APFS container for root device %s\n
%s:%d: Found %d Data volume snapshots\n
%s:%d: failed to stat path %s (%s)\n
%s:%d: error while looking up overprovisioning volume: %d\n
fsindex=
AppleAPFSContainer
apfs
%s:%d: failed to open dmg: %d\n
uuid_from_role
%s:%d: Failed to get snapshot list - %s. Ignoring...\n
kern.exclaves_relaxed_requirements
Ap,ExclaveOSVolume.img4
/private/var/.overprovisioning_file
sha3_256_4k
AppleAPFSContainerScheme
%s:%d: Could not get filesystem information for root filesystem - %s\n
Overprovision
Ap,ExclaveOS.dmg
IODeviceTree:/filesystems/fstab
Executes the mount phase designated by the number provided.
sealed=yes
unwritten=no
perform_mount_phase
%s:%d: %s failed - error %s (%d)\n
iDiags volume mount
sha3_384
sha3_512
%ss%d
%s:%d: Couldn't get whole media size: %d\n
mount_by_role
get_volume_from_volume_group
fssize=
Overprovision setup
error: unable to find filesystems node in device tree plane
mount_phase_one
%s:%d: found volume %s with role = %x in APFS container for root device %s\n
%s:%d: failed to create graft dir: %d\n
%s:%d: Skipping the registration of the exclaves writable storage\n
%s:%d: Updating overprovisioning volume sizes\n
defragment=yes
Usage: %s (1|2)\n
%s:%d: Nothing to do.\n
%s:%d: unable to mount %s on %s (%s), failing bootstrap for root device %s\n
%s:%d: Cannot open directory on %s: %s\n
%s:%d: Skipping overprovisioning checks for recovery boot.\n
IOService
defragment=no
61706673-7575-6964-00c0-766f6c756d00
%s:%d: Unrecognized mount phase: %d\n
%s:%d: unable to find role for volume %s, error = %x, skipping it ...\n
%s:%d: Failed to delete snapshot %s (xid %lld) - %s. Ignoring...\n
%s:%d: failed to open boot object path [%s]: %d\n
%s:%d: failed to get ExclaveOS registration base path: %s (%d)\n
%s:%d: Skipping the registration of the exclaves writable storage because we're not running in regular OS environment\n
%s:%d: failed to create overprovisioning volume: %d\n
IOBlockStorageDriver
%s:%d: found another volume %s mounted at %s, failing bootstrap for root device %s\n
com.apple.mobilebackup
%s:%d: failed to open volume root hash: %d\n
%s:%d: failed to register graft dir: %d\n
volname=
61706673-7575-6964-0004-766f6c756d00
61706673-7575-6964-02c0-766f6c756d00
sha384
error: unable to find OS environment entry in device tree plane
mount_phase_two
/private/var
%s:%d: failed to get tag %d registration base path: %s (%d)\n
%s:%d: failed to open graft dir: %d\n
%s:%d: Creating overprovisioning volume\n
fsquota=
61706673-7575-6964-0010-766f6c756d00
%s:%d: %s failed - error %x (errno %d). Ignoring...\n
/
%s:%d: root device %s is not in a volume group\n
%s:%d: failed to open preboot volume mount dir: %d\n
omap=ephemeral
61706673-7575-6964-0001-766f6c756d00
61706673-7575-6964-0300-766f6c756d00
AppleAPFSSnapshot
AppleAPFSMedia
IOMatchCategory
/private/var/.exclave/
/private/preboot
%s:%d: successfully registered tag %d at %s\n
%s:%d: Using existing overprovisioning volume\n
fstree=btree
%s:%d: Deleted snapshot %s (xid %lld)\n
com.apple.filesystems.apfs
kern.bootobjectspath
%s:%d: failed to lstat ExclaveOS registration path: %s (%d)\n
%s:%d: Successfully grafted and registered ExclaveOS Cryptex [%s] on [%s]\n
hw.osenvironment
fsreserve=
61706673-7575-6964-0040-766f6c756d00
%s:%d: skipping exclaveOS graft for recovery boot\n
%s:%d: Found container size of %llu bytes\n
61706673-7575-6964-0020-766f6c756d00
61706673-7575-6964-0140-766f6c756d00
61706673-7575-6964-0180-766f6c756d00
os_env_type
kern.exclaves_status
usr/standalone/firmware/FUD/
sha3_384_4k
Boot device lookup
%s:%d: tag %d is already registered but at unexpected path %s (expected %s\n)
com.apple.root.cryptex
%s:%d: failed to open ExclaveOS directory [%s]: %d\n
handle_overprovisioning
%s:%d: Using reserve size of %llu\n
unwritten
61706673-7575-6964-0280-766f6c756d00
%s:%d: Mounting %s on %s\n
%s:%d: failed to get exclaves status: %d\n
%s:%d: failed to register the exclaves writable storage path %s for tag %d (%s)\n
fs_reserve
61706673-7575-6964-0080-766f6c756d00
sha256
sha3_256
lookup_boot_device
mount_by_role_if_present
%s:%d: cannot get filesystem information for %s: %s\n
Cryptexes/ExclaveOS
omap=btree
61706673-7575-6964-0008-766f6c756d00
Log volume mount
%s:%d: unable to get volume group for root device %s, error = %x\n
boot_is_darwinos_ramdisk
%s:%d: Cannot set protection class on %s: %s\n
/dev/
%s:%d: Found overprovisioning file. Removing...\n
omap=physical
%s:%d: failed to get graft dir path: %d\n
/AppleInternal/Diags
%s:%d: base path %s doesn't match graft path %s\n
password=
AppleAPFSVolume
Register exclave RW main tag
%s:%d: os environment is darwinos-ramdisk, skipping ExclaveOS grafting\n
graft_exclaveos
%s:%d: failed to find boot device: %d\n
%s:%d: no space to create overprovisioning volume of size %lu\n
61706673-7575-6964-0200-766f6c756d00
sha512_256
delete_MB_snapshots
%s:%d: tag %d is already registered, skipping exclaveOS graft\n
%s:%d: failed to get boot object path: %d\n
%s:%d: Register tag %d on path %s\n
%s:%d: failed to get space information about volume %s: %d\n
,
61706673-7575-6964-0000-766f6c756d00
ExclaveOS graft
%s:%d: failed to update overprovisioning sizes: %d\n
untitled
empty_password
hash=
sha512
```
