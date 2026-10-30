# `/usr/lib/system/libsystem_pthread.dylib`

iOS 27.2 dyld shared cache image. Version `553.40.2.0.0`. **[DSC]**

## Linked libraries (4)

- `/usr/lib/system/libsystem_kernel.dylib`
- `/usr/lib/system/libsystem_platform.dylib`
- `/usr/lib/system/libdyld.dylib`
- `/usr/lib/system/libmacho.dylib`

## Strings (67)

```
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() called before pthread_jit_write_freeze_callbacks_np()
BUG IN LIBPTHREAD: libpthread has not been initialized
BUG IN CLIENT OF LIBPTHREAD: Stack size in attrs is too small
BUG IN CLIENT OF LIBPTHREAD: workgroup functions not yet installed
PTHREAD_YIELD_TO_ZERO
ptr_munge
__DATA_CONST
PTHREAD_MUTEX_ADAPTIVE_SPIN
BUG IN LIBPTHREAD: Missing required kernel support
BUG IN LIBPTHREAD: Token from the kernel is 0
BUG IN LIBPTHREAD: impossible cond signature
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER
warning: dynamic tsd keys dirty after static key cleanup loop.
BUG IN CLIENT OF LIBPTHREAD: Corrupted pthread_dependency_t
pthread_t was corrupted
BUG IN LIBPTHREAD: jit config vm_map PERMANENT failed
__pth_jit_func
BUG IN LIBPTHREAD: ulock_wait failure
BUG IN LIBPTHREAD: kernel rwlock returned unknown error
BUG IN CLIENT OF LIBPTHREAD: Fufilling pthread_dependency_t twice
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() called but freeze-late entitlement is missing
BUG IN LIBPTHREAD: __workq_kernreturn returned
BUG IN CLIENT OF LIBPTHREAD: Unaligned stack addr in attrs
PTHREAD_MUTEX_DEFAULT_POLICY
pthread_tsd
BUG IN LIBPTHREAD: kernel without PTHREAD_START_SUSPENDED support
BUG IN LIBPTHREAD: thread_set_tsd_base() wasn't called by the kernel
BUG IN CLIENT OF LIBPTHREAD: Too many pthread jit write callbacks
BUG IN CLIENT OF LIBPTHREAD: workgroup functions already installed
BUG IN LIBPTHREAD: jit config vm_protect() failed
BUG IN LIBPTHREAD: Invalid pthread priority for the legacy interface
BUG IN LIBPTHREAD: EALREADY from ulock_wake
BUG IN LIBPTHREAD: __psynch_mutexdrop failed
PTHREAD_KEY_LEGACY_DESTRUCTOR_ORDER_LOG
BUG IN LIBPTHREAD: host_info() failed
BUG IN LIBPTHREAD: Missing priority
BUG IN LIBPTHREAD: qos_max_parallelism failed
BUG IN LIBPTHREAD: expected atfork to be inline
BUG IN CLIENT OF LIBPTHREAD: pthread_exit() called from a thread not created by pthread_create()
BUG IN LIBPTHREAD: pthread_join() wake failure
BUG IN CLIENT OF LIBPTHREAD: Waiting on orphaned dependency
BUG IN CLIENT OF LIBPTHREAD: __ulock_wait() failed
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() callback not in allowlist
has_sec_transition
PTHREAD_PTR_MUNGE_TOKEN
BUG IN LIBPTHREAD: __ulock_wake() failed
th_port
BUG IN LIBPTHREAD: Mixed ulock and psych condvar use
BUG IN LIBPTHREAD: Unable to deallocate stack
BUG IN CLIENT OF LIBPTHREAD: Invalid kqworkq setup
BUG IN CLIENT OF LIBPTHREAD: Invalid priority
BUG IN LIBPTHREAD: kernel rwunlock returned unknown error
BUG IN LIBPTHREAD: ulock_wake failure
BUG IN LIBPTHREAD: unlock_slow without orig_waiters
BUG IN CLIENT OF LIBPTHREAD: Fulfilled a dependency not owned by current thread
BUG IN CLIENT OF LIBPTHREAD: Unable to allocate thread port, possible port leak
BUG IN LIBPTHREAD: thread didn't terminate
main_stack
BUG IN LIBPTHREAD: PTHREAD_SELF TSD not initialized
BUG IN LIBPTHREAD: failed to set thread_id
BUG IN CLIENT OF LIBPTHREAD: Invalid kqwl setup
PTHREAD_MUTEX_USE_ULOCK
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_setspecific_np outside of a CREATE introspection hook
BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() already called
BUG IN CLIENT OF LIBPTHREAD: pthread_join() state corruption
BUG IN CLIENT OF LIBPTHREAD: pthread_mutex corruption: mutex owner changed in the middle of lock/unlock
BUG IN CLIENT OF LIBPTHREAD: Calling pthread_introspection_getspecific_np outside of a DESTROY introspection hook
```
