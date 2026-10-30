# `/usr/lib/liblangid.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 87,680 bytes.

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
--
_langid_dispose_internal
env->objectCount>0
stat(path, &stat_data) == 0
env->trie
_open_and_mmap_for_reading
LanguageIdentifier cannot open file: [%s], errno: %d error: [%s]\n
env
env->numLanguages<=kMaxVectorWidth
_langid_env_dispose
addr != MAP_FAILED
_langid_env_create
LanguageIdentifier.c
H(fileVersion)==1
APPLE_FRAMEWORKS_ROOT
%s/%s
/usr/share/langid/langid.inv
```
