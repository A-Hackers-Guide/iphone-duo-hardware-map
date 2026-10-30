# `/usr/lib/system/libsystem_coreservices.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 100,400 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 33 (Size: 2920)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (15)

- `/usr/lib/system/libsystem_coreservices.dylib (compatibility version 1.0.0, current version 129.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libsystem_info.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_containermanager.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_featureflags.dylib (compatibility version 1.0.0, current version 111.0.0)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libsystem_sandbox.dylib (compatibility version 1.0.0, current version 3051.40.81)`

## Entitlements

```xml
  - no entitlements
```

## Strings (62)

```
%s
v8@?0
/Applications/Utilities
/Users
/System
/var/tmp/
/tmp/
_dirhelper_relative_internal
CryptexSearchPaths
/Applications
/AppleInternal
%s/
/Library/Input Methods
validate_user_dir_suffix
/Library/Documentation
/Library/Autosave Information
/Library/PreferencePanes
/Network
/System/Cryptexes/OS/System
/var/mobile/tmp/
/Applications/Demos
/Pictures
~
%s%s
tmp/
com.apple.libcoreservices
libcoreservices
/Music
/Public
/System/AppleInternal
NEXT_ROOT
TMPDIR
_dirhelper_update_tmpdir
/
/Developer
/Downloads
/Library/Printers/PPDs
_dirhelper_relative_internal_block_invoke
/Movies
../
/Developer/Applications
/Desktop
/Library/Caches
/Library/Application Support
/System/Cryptexes/App/System
/System/iOSSupport/System
/Library
/Documents
/Library/CoreServices
/System/iOSSupport
NSGetNextSearchPathEnumerationStatic
%s: error for relativepath %s: %s (%d)
%s: '..' not allowed, suffix=%s
%s: getpwuid_r returned no results for uid %d
%s: sysconf(_SC_GETPW_R_SIZE_MAX) error: %{errno}d
mkdir: created %s
mkdir: path=%{public}s mode=%o: %s (%d
%s: old=%s, new=%s
%s: no result for relativepath %s, err=%s (%d)
%s: this process is sandboxed so will never return /var/tmp/ or /var/mobile/tmp. This message is only logged once per process.
%s: slash not allowed, suffix=%s
%s: getpwuid_r(%d) error: %{errno}d
```
