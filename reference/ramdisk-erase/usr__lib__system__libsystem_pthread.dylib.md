# `/usr/lib/system/libsystem_pthread.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 182,064 bytes.

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
BUG IN CLIENT OF LIBPTHREAD: workgroup functions already installed
BUG IN LIBPTHREAD: Unable to deallocate stack
BUG IN LIBPTHREAD: pthread_join() wake failure
BUG IN LIBPTHREAD: thread didn't terminate
BUG IN LIBPTHREAD: failed to set thread_id
ptr_munge
BUG IN LIBPTHREAD: jit config vm_map PERMANENT failed
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER_LOG
BUG IN CLIENT OF LIBPTHREAD: Waiting on orphaned dependency
PTHREAD_MUTEX_ADAPTIVE_SPIN
BUG IN LIBPTHREAD: qos_max_parallelism failed
pthread_t was corrupted
BUG IN LIBPTHREAD: jit config vm_protect() failed
BUG IN CLIENT OF LIBPTHREAD: pthread_mutex corruption: mutex owner changed in the middle of lock/unlock
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_getspecific_np outside of a DESTROY introspection hook
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() callback not in allowlist
BUG IN CLIENT OF LIBPTHREAD: workgroup functions not yet installed
has_sec_transition
main_stack
BUG IN LIBPTHREAD: ulock_wake failure
BUG IN LIBPTHREAD: ulock_wait failure
__pth_jit_func
BUG IN CLIENT OF LIBPTHREAD: Invalid kqwl setup
BUG IN LIBPTHREAD: impossible cond signature
BUG IN LIBPTHREAD: __psynch_mutexdrop failed
BUG IN LIBPTHREAD: unlock_slow without orig_waiters
BUG IN CLIENT OF LIBPTHREAD: Invalid priority
BUG IN LIBPTHREAD: thread_set_tsd_base() wasn't called by the kernel
BUG IN LIBPTHREAD: host_info() failed
BUG IN LIBPTHREAD: Missing required kernel support
PTHREAD_PTR_MUNGE_TOKEN
BUG IN LIBPTHREAD: Missing priority
BUG IN LIBPTHREAD: Mixed ulock and psych condvar use
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER
warning: dynamic tsd keys dirty after static key cleanup loop.
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() already called
BUG IN LIBPTHREAD: __workq_kernreturn returned
BUG IN CLIENT OF LIBPTHREAD: Too many pthread jit write callbacks
BUG IN LIBPTHREAD: EALREADY from ulock_wake
BUG IN LIBPTHREAD: kernel rwunlock returned unknown error
BUG IN CLIENT OF LIBPTHREAD: Fufilling pthread_dependency_t twice
BUG IN LIBPTHREAD: __ulock_wake() failed
BUG IN CLIENT OF LIBPTHREAD: Unable to allocate thread port, possible port leak
__DATA_CONST
PTHREAD_MUTEX_DEFAULT_POLICY
PTHREAD_MUTEX_USE_ULOCK
BUG IN LIBPTHREAD: PTHREAD_SELF TSD not initialized
BUG IN CLIENT OF LIBPTHREAD: Stack size in attrs is too small
BUG IN CLIENT OF LIBPTHREAD: Unaligned stack addr in attrs
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_setspecific_np outside of a CREATE introspection hook
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() called before pthread_jit_write_freeze_callbacks_np()
PTHREAD_YIELD_TO_ZERO
BUG IN CLIENT OF LIBPTHREAD: Invalid kqworkq setup
BUG IN LIBPTHREAD: Invalid pthread priority for the legacy interface
BUG IN CLIENT OF LIBPTHREAD: pthread_join() state corruption
BUG IN LIBPTHREAD: kernel rwlock returned unknown error
BUG IN LIBPTHREAD: Token from the kernel is 0
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() called but freeze-late entitlement is missing
BUG IN LIBPTHREAD: libpthread has not been initialized
th_port
BUG IN LIBPTHREAD: expected atfork to be inline
BUG IN CLIENT OF LIBPTHREAD: Fulfilled a dependency not owned by current thread
BUG IN CLIENT OF LIBPTHREAD: Corrupted pthread_dependency_t
BUG IN LIBPTHREAD: kernel without PTHREAD_START_SUSPENDED support
BUG IN CLIENT OF LIBPTHREAD: pthread_exit() called from a thread not created by pthread_create()
pthread_tsd
BUG IN CLIENT OF LIBPTHREAD: __ulock_wait() failed
```
