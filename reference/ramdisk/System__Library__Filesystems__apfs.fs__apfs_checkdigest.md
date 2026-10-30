# `/System/Library/Filesystems/apfs.fs/apfs_checkdigest`

From the upgrade restore ramdisk (141-29011-104.dmg). 72,448 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 1824)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
```

## Linked libraries (4)

- `/System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression (compatibility version 1.0.0, current version 182.40.4)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.apfs.sep.ramdisk</key>
	<true/>
	<key>com.apple.container.crypto.io</key>
	<true/>
	<key>com.apple.keystore.device</key>
	<true/>
	<key>com.apple.keystore.devicebackup</key>
	<true/>
	<key>com.apple.private.apfs.create-sealed-snapshot</key>
	<true/>
	<key>com.apple.private.apfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.apfs.get-dstreams</key>
	<true/>
	<key>com.apple.private.apfs.get-file-exts</key>
	<true/>
	<key>com.apple.private.apfs.revert-to-snapshot</key>
	<true/>
	<key>com.apple.private.iopol.case_sensitivity</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.system-async-io</key>
	<true/>
	<key>com.apple.private.vfs.dataless-manipulation</key>
	<true/>
	<key>com.apple.private.vfs.move-data-extents</key>
	<true/>
	<key>com.apple.private.vfs.snapshot</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<string>AppleAPFSUserClient</string>
</dict>
</plist>
```

## Strings (39)

```
Cannot get byte count in extended attribute %s of %s
Cannot get information about %s
Cannot extract data integrity record for offset %lld in extended attributes %s of %s
Cannot extract data integrity record for offset %lld of %s
Cannot allocate %lld bytes to check digest of data at offset %lld
Digest mismatch detected for the record of %lld bytes at offset %lld - calculated digest %s, expected %s
where [options] are\n       -h             display usage\n       -x <xattr>     check digest of named extended attribute\n       -q             do not print hash records\n       -C             decompress data from named extended attribute\n
sha3_384
%s is not regular file
sha3_256_4k
sha3_512
Cannot get size for compression header attribute of %s
Cannot decompress %zd bytes at offset %lld in %s
sha512_256
%02hhx
com.apple.ResourceFork
Cannot extract data stream number for extended attribute %s of %s
USAGE: %s [options] <file>\n
sha384
sha3_384_4k
sha3_512_4k
com.apple.decmpfs
Cannot allocate %zd bytes for compression header attribute of %s
Unknown hash type %d in the record at offset %lld
Digest mismatch detected for the record of %lld bytes at offset %lld - calculated digest %s
sha3_256
Cannot access compression header of %s
Digest type changed from %d to %d in the record at offset %lld
Unknown hash type
hqx:C
Cannot allocate %zd bytes for read data in the extended attribute %s of %s
Cannot access data in extended attribute %s of %s
%-6lld at %-12lld %s(%s)\n
Cannot read %zd bytes at offset %lld
sha256
sha512
Cannot open %s
Detected a gap between expected offset %lld and record offset %lld
i40@?0q8Q16^v24^Q32
```
