# `/usr/lib/system/libsystem_platform.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 187,344 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2192)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`

## Entitlements

```xml
  - no entitlements
```

## Strings (67)

```
 [PID 
\\]
security_config
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt
BUG IN CLIENT OF LIBPLATFORM: Lock was not held
unfair
BUG IN LIBPLATFORM: ulock_wait2 failure
BUG IN CLIENT OF LIBPLATFORM: Creating semaphore failed, possible port leak
%s
]
BUG IN LIBPLATFORM: Overflow in _simple_snprintf
.*s
BUG IN CLIENT OF LIBPLATFORM: os_lock is corrupt
spin
nospin
BUG IN LIBPLATFORM: ulock_wait failure
Could not parse security_config string
BUG IN CLIENT OF LIBPLATFORM: os_unfair_lock is corrupt, or owner thread exited without unlocking
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly not owned by current thread
BUG IN CLIENT OF LIBPLATFORM: Requested allocation size is invalid
BUG IN CLIENT OF LIBPLATFORM: Destroying semaphore failed
] [GID 
] [Time 
0123456789ABCDEF
0x
BUG IN CLIENT OF LIBPLATFORM: Signaling semaphore failed
] [TimeNanoSec 
unknown
0123456789abcdef
BUG IN CLIENT OF LIBPLATFORM: Failed to allocate memory for buffer
BUG IN LIBPLATFORM: Failed to freeze script config storage.
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_once_t not owned by current thread
BUG IN LIBPLATFORM: Failed to allocate in os_alloc_once
BUG IN CLIENT OF LIBPLATFORM: Allocating semaphore failed with MIG_REPLY_MISMATCH
 %s
\\s
has_sec_transition
BUG IN LIBPLATFORM: unlock_slow with no waiters
BUG IN LIBPLATFORM: ulock_wake failure
1
KB
BUG IN CLIENT OF LIBPLATFORM: Unlock of an os_unfair_lock not owned by current thread
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_lock
BUG IN CLIENT OF LIBPLATFORM: Invalid options
%lu
(null)
pfz
         0
\\[
BUG IN CLIENT OF LIBPLATFORM: asl fd already initialized
 [
\\n
\\\\
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_once_t
] [UID 
/var/run/syslog
handoff
ASL_DISABLE
BUG IN CLIENT OF LIBPLATFORM: Waiting on semaphore failed
Message
%u
]\n
MB
BUG IN CLIENT OF LIBPLATFORM: Trying to recursively lock an os_unfair_lock
BUG IN CLIENT OF LIBPLATFORM: Assertion failed: Lock unexpectedly owned by current thread
%d
BUG IN CLIENT OF LIBPLATFORM: os_once_t is corrupt
```
