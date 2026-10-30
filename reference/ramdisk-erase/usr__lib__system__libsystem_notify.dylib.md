# `/usr/lib/system/libsystem_notify.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 149,696 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 31 (Size: 2680)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (13)

- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_collections.dylib (compatibility version 1.0.0, current version 1786.40.6)`

## Entitlements

```xml
  - no entitlements
```

## Strings (84)

```
notify_monitor_file
[%s] canceling notification: token=%d flags=0x%x
B16@?0^v8
com.apple.private.darwin-notification.introspect
apple.shm.notification_center
libnotify.simulate_crash
BUG IN CLIENT OF LIBNOTIFY: loopback mode enabled but process wants to IPC to notifyd
B24@?0Q8^v16
name
notify_register_check
notify_register_coalesced_registration
notify_register_mach_port_via_dispatch
[bug in libnotify] resurrecting name_node
notify_suspend
v12@?0i8
notify_post
user.uid.
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a *non-empty* array of strings
enabled logging for all notifications
notify_client.c
com.apple.notify
[%s] registered for notification: token=%d flags=0x%x
notify_register_mach_port
enabled logging for %s
[bug in libnotify] resurrecting registration_node
BUG IN CLIENT OF LIBNOTIFY: Unable to allocate port array: possible notification registration leak
notify_register_mach_port_no_dispatch
*notify_port == MACH_PORT_NULL
registration_node_delete_locked
Libnotify: %s failed with code %d (%d) on line %d
Libnotify: %s failed with code %d on line %d (fileport_status: %d)
com.apple.system.notification_center
com.apple.libnotify
_notify_register_dispatch_with_extra_mp
[%s] registered for notification token=%d flags=0x%x
shm_attach
<- %s [%d] _notify_server_cancel_2 failed: 0x%08x\n
notify_get_state
BUG IN CLIENT OF NOTIFYD: %s has not dequeued the last %d messages
LIBNOTIFY INTROSPECT: registering for non-exempt notification %s
notify_check
notify_dump_status
BUG IN LIBNOTIFY CLIENT: internal data structure corrupted [0x%04llx, 0x%llx, 0x%llx, 0x%llx]]
DarwinNotificationLogging
com.apple.developer.web-browser-engine.restrict.notifyd
Libnotify client using deprecated function notify_simple_post, use notify_post instead
_notify_lib_regenerate_registration
com.apple.notify.root_access
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a non-empty *array* of strings
Libnotify: %s failed on line %d with errno %d
notify_register_mach_port_self
_notification_introspection_init_block_invoke
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a non-empty array of *strings*
self.
notify_register_file_descriptor
Libnotify client using deprecated function notify_get_event; this function does nothing
notify_suspend_pid
v8@?0
,
[bug in libnotify] refcount underrun
notify_set_state
notify_register_signal
Notification
notify_register_plain
globals
notify_cancel
notify_resume_pid
exempt_notifications != NULL
notify name \"%s\" has been registered %d times - this may be a leak
_State
notify_peek
Libnotify: %s failed with code %d on line %d (errno: %d)
BUG IN LIBNOTIFY: Unsupported protocol version
Libnotify: _notify_server_regnerate failed for name %s with status %d (flags: %x, token %d)
%s%d
com.apple.notify.background.local.notification
strncmp(name, SELF_PREFIX, SELF_PREFIX_LEN)
Libnotify: %s failed with code %d on line %d
notify_resume
Libnotify: %s failed with code %d on line %d (kstatus: %d)
BUG IN LIBNOTIFY CLIENT: registration held for restricted name %s with process uid %d
kstatus == KERN_SUCCESS
BUG IN CLIENT OF LIBNOTIFY: exceeded registration limit. Last registration was for name %s
B16@?0^I8
```
