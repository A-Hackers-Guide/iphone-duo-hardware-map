# `/System/Library/Filesystems/apfs.fs/apfs_computedigest`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 72,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 20 (Size: 1712)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, PIE
```

## Linked libraries (3)

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

## Strings (25)

```
sha512_256
sha3_256_4k
sha3_384
authapfs_valid_hash_type
Cannot allocate %zd bytes for temporary buffer
where [options] are\n       -h             display usage\n       -a <algo>      calculate digest using hash algorithm (default is SHA-256)\n       -c <chunk>     calculate digest of each chunk\n       <file>         file name
sha256
sha3_384_4k
sha3_512_4k
sha3_256
%02hhx
%s:%d: Invalid or unknown hash type: %d\n
Unknown hashing algorithm %s
sha384
sha512
sha3_512
a:c:h
Cannot set chunk size to %s
Cannot map %zd bytes from %s
USAGE: %s [options] <file>\n
Unknown hash type
Cannot open %s
Cannot get information about %s
%s is not regular file
%-6zd at %-12lld %s(%s)\n
```
