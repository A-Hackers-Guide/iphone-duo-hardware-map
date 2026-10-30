# `/System/DriverKit/usr/lib/system/libsystem_platform.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 185,056 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2240)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/System/DriverKit/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/System/DriverKit/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/System/DriverKit/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`

## Entitlements

```xml
  - no entitlements
```

## Strings (56)

```
has_sec_transition
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_once_t
BUG IN CLIENT OF LIBPLATFORM: Invalid options
BUG IN LIBPLATFORM: unlock_slow with no waiters
BUG IN LIBPLATFORM: Failed to allocate in os_alloc_once
BUG IN CLIENT OF LIBPLATFORM: Creating semaphore failed, possible port leak
handoff
BUG IN CLIENT OF LIBPLATFORM: Lock was not held
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_once_t not owned by current thread
BUG IN LIBPLATFORM: ulock_wait2 failure
BUG IN CLIENT OF LIBPLATFORM: Allocating semaphore failed with MIG_REPLY_MISMATCH
BUG IN CLIENT OF LIBPLATFORM: Signaling semaphore failed
\\n
(null)
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly owned by current thread
unfair
BUG IN LIBPLATFORM: ulock_wake failure
.*s
MB
pfz
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly not owned by current thread
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_lock
BUG IN CLIENT OF LIBPLATFORM: Requested allocation size is invalid
BUG IN CLIENT OF LIBPLATFORM: Waiting on semaphore failed
 %s
\\s
0123456789abcdef
nospin
BUG IN CLIENT OF LIBPLATFORM: os_once_t is corrupt
BUG IN CLIENT OF LIBPLATFORM: Destroying semaphore failed
%s
\\[
\\]
BUG IN LIBPLATFORM: Overflow in _simple_snprintf
0x
BUG IN CLIENT OF LIBPLATFORM: os_lock is corrupt
spin
BUG IN LIBPLATFORM: ulock_wait failure
BUG IN LIBPLATFORM: Invalid commpage pfz base.
Could not parse security_config string
         0
 [
Message
]
Sender
BUG IN CLIENT OF LIBPLATFORM: Failed to allocate memory for buffer
Facility
\\\\
KB
BUG IN LIBPLATFORM: Failed to freeze script config storage.
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_unfair_lock
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_unfair_lock not owned by current thread
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt, or owner thread exited without unlocking
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt
0123456789ABCDEF
security_config
```
