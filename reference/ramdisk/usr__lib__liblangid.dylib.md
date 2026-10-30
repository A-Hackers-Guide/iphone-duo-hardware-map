# `/usr/lib/liblangid.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 87,680 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1384)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/liblangid.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (17)

```
H(fileVersion)==1
env->objectCount>0
_langid_env_create
_langid_dispose_internal
%s/%s
stat(path, &stat_data) == 0
LanguageIdentifier cannot open file: [%s], errno: %d error: [%s]\n
--
env->numLanguages<=kMaxVectorWidth
APPLE_FRAMEWORKS_ROOT
_open_and_mmap_for_reading
addr != MAP_FAILED
LanguageIdentifier.c
env->trie
_langid_env_dispose
/usr/share/langid/langid.inv
env
```
