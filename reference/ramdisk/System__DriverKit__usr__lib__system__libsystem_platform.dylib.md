# `/System/DriverKit/usr/lib/system/libsystem_platform.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 185,056 bytes.

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
Message
BUG IN LIBPLATFORM: Failed to freeze script config storage.
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_unfair_lock
BUG IN CLIENT OF LIBPLATFORM: Lock was not held
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_once_t not owned by current thread
BUG IN CLIENT OF LIBPLATFORM: os_once_t is corrupt
BUG IN LIBPLATFORM: Failed to allocate in os_alloc_once
BUG IN CLIENT OF LIBPLATFORM: Allocating semaphore failed with MIG_REPLY_MISMATCH
\\\\
\\[
BUG IN CLIENT OF LIBPLATFORM: Failed to allocate memory for buffer
BUG IN LIBPLATFORM: Invalid commpage pfz base.
BUG IN CLIENT OF LIBPLATFORM: os_lock is corrupt
spin
handoff
BUG IN LIBPLATFORM: Overflow in _simple_snprintf
KB
BUG IN LIBPLATFORM: ulock_wake failure
         0
0123456789ABCDEF
has_sec_transition
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt, or owner thread exited without unlocking
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt
nospin
BUG IN CLIENT OF LIBPLATFORM: Invalid options
BUG IN CLIENT OF LIBPLATFORM: Creating semaphore failed, possible port leak
 %s
\\n
Sender
\\s
.*s
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly owned by current thread
BUG IN CLIENT OF LIBPLATFORM: Requested allocation size is invalid
BUG IN CLIENT OF LIBPLATFORM: Destroying semaphore failed
 [
Facility
0123456789abcdef
0x
security_config
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly not owned by current thread
unfair
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_lock
]
\\]
MB
pfz
Could not parse security_config string
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_unfair_lock not owned by current thread
BUG IN LIBPLATFORM: ulock_wait2 failure
BUG IN LIBPLATFORM: unlock_slow with no waiters
%s
(null)
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_once_t
BUG IN LIBPLATFORM: ulock_wait failure
BUG IN CLIENT OF LIBPLATFORM: Signaling semaphore failed
BUG IN CLIENT OF LIBPLATFORM: Waiting on semaphore failed
```
