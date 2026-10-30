# `/usr/lib/libcryptex_trampoline.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 88,032 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1856)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/usr/lib/libcryptex_trampoline.dylib (compatibility version 1.0.0, current version 761.40.23)`
- `/usr/lib/libcryptex_interface.dylib (compatibility version 1.0.0, current version 761.40.23)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (15)

```
com.apple.libcryptex
kern.proc_rsr_in_progress
trampoline
761.40.23
Monitor Cryptex Upgrades Version 2.0.0: Sat Oct  3 17:50:22 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_trampoline/RELEASE_ARM64E
RELEASE
@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sat Oct  3 17:50:22 PDT 2026; root:libcryptex-761.40.23~881/libcryptex_trampoline/RELEASE_ARM64E
/Library/Caches/com.apple.xbs/27778A89-67E4-4654-83F9-E0180CE73777/TemporaryDirectory.RUocNv/Binaries/libcryptex/install/Symbols/libcryptex_trampoline
known-constant allocation
v8@?0
Error encountered blocking on cryptex upgrade.: %{darwin.errno}d
Unblocked after upgrade for cryptex '%{public}s.
allocation failed: obj = %s, size = %lu, error = %s
Failed to read upgrade sysctl.: %{darwin.errno}d
Blocking on upgrade for cryptex '%{public}s.
```
