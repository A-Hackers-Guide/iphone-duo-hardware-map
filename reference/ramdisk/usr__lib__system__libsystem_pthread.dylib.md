# `/usr/lib/system/libsystem_pthread.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 182,064 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 2240)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libmacho.dylib (compatibility version 1.0.0, current version 1040.0.0, upward)`

## Entitlements

```xml
  - no entitlements
```

## Strings (67)

```
BUG IN LIBPTHREAD: host_info() failed
BUG IN LIBPTHREAD: pthread_join() wake failure
warning: dynamic tsd keys dirty after static key cleanup loop.
BUG IN LIBPTHREAD: thread_set_tsd_base() wasn't called by the kernel
BUG IN LIBPTHREAD: Missing required kernel support
BUG IN LIBPTHREAD: jit config vm_protect() failed
BUG IN LIBPTHREAD: impossible cond signature
PTHREAD_MUTEX_USE_ULOCK
BUG IN CLIENT OF LIBPTHREAD: Fulfilled a dependency not owned by current thread
__pth_jit_func
PTHREAD_MUTEX_ADAPTIVE_SPIN
BUG IN CLIENT OF LIBPTHREAD: pthread_mutex corruption: mutex owner changed in the middle of lock/unlock
BUG IN LIBPTHREAD: qos_max_parallelism failed
PTHREAD_YIELD_TO_ZERO
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() called before pthread_jit_write_freeze_callbacks_np()
BUG IN LIBPTHREAD: PTHREAD_SELF TSD not initialized
BUG IN CLIENT OF LIBPTHREAD: Unable to allocate thread port, possible port leak
main_stack
BUG IN CLIENT OF LIBPTHREAD: pthread_join() state corruption
BUG IN LIBPTHREAD: ulock_wake failure
BUG IN LIBPTHREAD: ulock_wait failure
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() called but freeze-late entitlement is missing
PTHREAD_MUTEX_DEFAULT_POLICY
BUG IN CLIENT OF LIBPTHREAD: __ulock_wait() failed
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() callback not in allowlist
__DATA_CONST
BUG IN CLIENT OF LIBPTHREAD: Too many pthread jit write callbacks
BUG IN CLIENT OF LIBPTHREAD: Invalid kqwl setup
BUG IN LIBPTHREAD: kernel rwlock returned unknown error
BUG IN LIBPTHREAD: kernel rwunlock returned unknown error
BUG IN CLIENT OF LIBPTHREAD: Corrupted pthread_dependency_t
BUG IN CLIENT OF LIBPTHREAD: workgroup functions already installed
has_sec_transition
BUG IN LIBPTHREAD: Unable to deallocate stack
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() already called
BUG IN CLIENT OF LIBPTHREAD: pthread_exit() called from a thread not created by pthread_create()
BUG IN LIBPTHREAD: Token from the kernel is 0
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER_LOG
PTHREAD_PTR_MUNGE_TOKEN
BUG IN LIBPTHREAD: Missing priority
BUG IN LIBPTHREAD: Invalid pthread priority for the legacy interface
BUG IN LIBPTHREAD: failed to set thread_id
BUG IN CLIENT OF LIBPTHREAD: workgroup functions not yet installed
BUG IN CLIENT OF LIBPTHREAD: Stack size in attrs is too small
pthread_tsd
BUG IN LIBPTHREAD: __workq_kernreturn returned
BUG IN LIBPTHREAD: EALREADY from ulock_wake
BUG IN CLIENT OF LIBPTHREAD: Invalid priority
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_setspecific_np outside of a CREATE introspection hook
BUG IN LIBPTHREAD: thread didn't terminate
ptr_munge
BUG IN LIBPTHREAD: Mixed ulock and psych condvar use
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_getspecific_np outside of a DESTROY introspection hook
BUG IN CLIENT OF LIBPTHREAD: Waiting on orphaned dependency
BUG IN LIBPTHREAD: expected atfork to be inline
BUG IN LIBPTHREAD: __ulock_wake() failed
BUG IN LIBPTHREAD: libpthread has not been initialized
pthread_t was corrupted
BUG IN LIBPTHREAD: kernel without PTHREAD_START_SUSPENDED support
BUG IN LIBPTHREAD: jit config vm_map PERMANENT failed
BUG IN LIBPTHREAD: unlock_slow without orig_waiters
BUG IN CLIENT OF LIBPTHREAD: Fufilling pthread_dependency_t twice
BUG IN CLIENT OF LIBPTHREAD: Unaligned stack addr in attrs
th_port
BUG IN CLIENT OF LIBPTHREAD: Invalid kqworkq setup
BUG IN LIBPTHREAD: __psynch_mutexdrop failed
```
