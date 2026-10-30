# `/usr/lib/system/libsystem_notify.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 149,696 bytes.

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
notify_post
LIBNOTIFY INTROSPECT: registering for non-exempt notification %s
BUG IN CLIENT OF LIBNOTIFY: loopback mode enabled but process wants to IPC to notifyd
com.apple.libnotify
B16@?0^v8
[bug in libnotify] refcount underrun
com.apple.private.darwin-notification.introspect
_notify_lib_regenerate_registration
notify_monitor_file
notify_suspend
Libnotify: %s failed with code %d on line %d (fileport_status: %d)
BUG IN LIBNOTIFY CLIENT: internal data structure corrupted [0x%04llx, 0x%llx, 0x%llx, 0x%llx]]
%s%d
[%s] registered for notification token=%d flags=0x%x
BUG IN CLIENT OF LIBNOTIFY: exceeded registration limit. Last registration was for name %s
<- %s [%d] _notify_server_cancel_2 failed: 0x%08x\n
notify_check
Libnotify: %s failed with code %d on line %d (errno: %d)
enabled logging for all notifications
_notify_register_dispatch_with_extra_mp
[%s] registered for notification: token=%d flags=0x%x
Libnotify: %s failed on line %d with errno %d
,
com.apple.notify
[bug in libnotify] resurrecting registration_node
notify_set_state
Libnotify: %s failed with code %d on line %d (kstatus: %d)
enabled logging for %s
notify_register_coalesced_registration
globals
BUG IN CLIENT OF LIBNOTIFY: Unable to allocate port array: possible notification registration leak
B16@?0^I8
com.apple.notify.root_access
self.
notify_register_check
notify_register_plain
kstatus == KERN_SUCCESS
name
notify name \"%s\" has been registered %d times - this may be a leak
strncmp(name, SELF_PREFIX, SELF_PREFIX_LEN)
libnotify.simulate_crash
notify_client.c
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a non-empty *array* of strings
shm_attach
*notify_port == MACH_PORT_NULL
notify_resume_pid
v12@?0i8
Libnotify client using deprecated function notify_simple_post, use notify_post instead
Notification
notify_peek
notify_cancel
notify_resume
notify_suspend_pid
notify_register_mach_port_no_dispatch
BUG IN CLIENT OF NOTIFYD: %s has not dequeued the last %d messages
v8@?0
notify_register_mach_port_via_dispatch
registration_node_delete_locked
Libnotify: %s failed with code %d on line %d
Libnotify: %s failed with code %d (%d) on line %d
notify_register_mach_port
notify_register_file_descriptor
DarwinNotificationLogging
user.uid.
exempt_notifications != NULL
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a non-empty array of *strings*
notify_register_signal
Libnotify client using deprecated function notify_get_event; this function does nothing
notify_get_state
com.apple.system.notification_center
Libnotify: _notify_server_regnerate failed for name %s with status %d (flags: %x, token %d)
[bug in libnotify] resurrecting name_node
notify_register_mach_port_self
apple.shm.notification_center
BUG IN LIBNOTIFY: Unsupported protocol version
com.apple.developer.web-browser-engine.restrict.notifyd
B24@?0Q8^v16
com.apple.notify.background.local.notification
_State
notify_dump_status
BUG IN LIBNOTIFY CLIENT: registration held for restricted name %s with process uid %d
BUG IN CLIENT OF LIBNOTIFY: entitlement com.apple.private.darwin-notification.introspect must be a *non-empty* array of strings
[%s] canceling notification: token=%d flags=0x%x
_notification_introspection_init_block_invoke
```
