# `/System/DriverKit/usr/lib/system/libsystem_pthread.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 164,096 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2256)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/System/DriverKit/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/System/DriverKit/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/System/DriverKit/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/System/DriverKit/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Strings (54)

```
BUG IN LIBPTHREAD: qos_max_parallelism failed
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_getspecific_np outside of a DESTROY introspection hook
BUG IN CLIENT OF LIBPTHREAD: Corrupted pthread_dependency_t
BUG IN CLIENT OF LIBPTHREAD: workgroup functions already installed
BUG IN CLIENT OF LIBPTHREAD: workgroup functions not yet installed
BUG IN LIBPTHREAD: expected atfork to be inline
PTHREAD_YIELD_TO_ZERO
BUG IN CLIENT OF LIBPTHREAD: Stack size in attrs is too small
BUG IN CLIENT OF LIBPTHREAD: Unaligned stack addr in attrs
BUG IN LIBPTHREAD: pthread_join() wake failure
BUG IN CLIENT OF LIBPTHREAD: Invalid kqworkq setup
BUG IN CLIENT OF LIBPTHREAD: pthread_join() state corruption
BUG IN LIBPTHREAD: EALREADY from ulock_wake
PTHREAD_MUTEX_DEFAULT_POLICY
BUG IN LIBPTHREAD: kernel without PTHREAD_START_SUSPENDED support
BUG IN LIBPTHREAD: thread_set_tsd_base() wasn't called by the kernel
BUG IN CLIENT OF LIBPTHREAD: Unable to allocate thread port, possible port leak
BUG IN LIBPTHREAD: Invalid pthread priority for the legacy interface
BUG IN LIBPTHREAD: impossible cond signature
PTHREAD_MUTEX_ADAPTIVE_SPIN
BUG IN LIBPTHREAD: __psynch_mutexdrop failed
BUG IN LIBPTHREAD: unlock_slow without orig_waiters
has_sec_transition
BUG IN LIBPTHREAD: __workq_kernreturn returned
pthread_t was corrupted
BUG IN CLIENT OF LIBPTHREAD: Invalid priority
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_setspecific_np outside of a CREATE introspection hook
BUG IN CLIENT OF LIBPTHREAD: Fufilling pthread_dependency_t twice
BUG IN LIBPTHREAD: __ulock_wake() failed
BUG IN LIBPTHREAD: PTHREAD_SELF TSD not initialized
BUG IN LIBPTHREAD: Missing required kernel support
PTHREAD_PTR_MUNGE_TOKEN
BUG IN LIBPTHREAD: Missing priority
BUG IN LIBPTHREAD: Mixed ulock and psych condvar use
BUG IN LIBPTHREAD: ulock_wait failure
BUG IN LIBPTHREAD: kernel rwlock returned unknown error
BUG IN LIBPTHREAD: kernel rwunlock returned unknown error
BUG IN CLIENT OF LIBPTHREAD: pthread_exit() called from a thread not created by pthread_create()
ptr_munge
BUG IN CLIENT OF LIBPTHREAD: Invalid kqwl setup
BUG IN LIBPTHREAD: ulock_wake failure
BUG IN CLIENT OF LIBPTHREAD: pthread_mutex corruption: mutex owner changed in the middle of lock/unlock
BUG IN CLIENT OF LIBPTHREAD: Fulfilled a dependency not owned by current thread
BUG IN LIBPTHREAD: Unable to deallocate stack
BUG IN LIBPTHREAD: failed to set thread_id
main_stack
PTHREAD_MUTEX_USE_ULOCK
BUG IN CLIENT OF LIBPTHREAD: Waiting on orphaned dependency
BUG IN CLIENT OF LIBPTHREAD: __ulock_wait() failed
BUG IN LIBPTHREAD: host_info() failed
BUG IN LIBPTHREAD: libpthread has not been initialized
BUG IN LIBPTHREAD: thread didn't terminate
BUG IN LIBPTHREAD: Token from the kernel is 0
th_port
```
