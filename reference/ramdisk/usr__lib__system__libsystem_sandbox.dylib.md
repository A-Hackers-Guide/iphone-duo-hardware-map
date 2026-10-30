# `/usr/lib/system/libsystem_sandbox.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 120,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 2200)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/system/libsystem_sandbox.dylib (compatibility version 1.0.0, current version 3051.40.81)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (95)

```
com.apple.libsystem.rootless
asr-parser-enter
%s failed: %d (%s)
sandbox_extension_issue_related_file_to_process
%s failed on message filter #%llu: %d (%s)
sandbox_message_filter_retain
iokit-open-user-client
sandbox operation \"%s\" is obsolete; replace with \"%s\"
-telemetry-
%s%s-XXXXXX
%s: fts_open(%s): %s
%s: lchflags(%s): %s
%s: failed: %s moved before protection
com.apple.app-sandbox.read-write
sandbox_register_app_bundle_exception
sandbox_compile_named
getattrlist failed: #%d: %s
sandbox_check_finder_automation_for_path
sandbox_extension_issue_mach_to_process_by_pid
sandbox_extension_issue_iokit_registry_entry_class_to_process
sandbox_register_app_data_protection_exception
%s: open(%s): %s
%s: fts_read: %s
com.apple.rootless
%s: failed to allocate
sandbox_message_filter_release
com.apple.libsystem.sandbox
fgetattrlist failed: #%d: %s
com.apple.sandbox.application-group
sandbox_extension_issue_mach_to_process
sandbox_extension_issue_iokit_registry_entry_class
sandbox_extension_issue_iokit_registry_entry_class_to_process_by_pid
sandbox_extension_consume
sandbox_compile_string
sandbox_free_profile
kTCCServiceMediaLibrary-iMovie
%s: unsupported flags: %u
sandbox_extension_issue_generic_to_process_by_pid
security.mac.sandbox.sentinel
sandbox_check_message_filter_string
sandbox_register_app_container_package_exception
rootless_convert_to_datavault
%s: failed: %s not protected
rootless_remove_in_favor_of_static_storage_class
sandbox_extension_issue_mach
compilation failed
com.apple.app-sandbox.read
sandbox_set_param
unsupported flags passed to %s: 0x%0x
%s: rootless_set_storage_class(%s): %s
%s: failed: %s not on same filesystem as parent
bad flags
sandbox_extension_issue_file
sandbox_extension_issue_file_to_process_by_pid
sandbox_extension_update_file
sandbox_extension_update_file_by_fileid
%s: failed: %s storage class changed before protection
sandbox_free_params
sandbox initialization failed: %s
sandbox_extension_issue_file_to_process
invalid
sandbox_check_message_filter_integer
v8@?0
sandbox_compile_file
com.apple.app-sandbox.mach
network-
sandbox_extension_issue_generic
sandbox_extension_issue_generic_to_process
sandbox_register_app_container_exception
%s: rootless_clear_storage_class(%s): %s
/usr/lib/libsandbox.1.dylib
sandbox_create_params
sandbox_checkattr_alloc
iokit-open
(platform)
%s failed for team-id=%s, signing-id=%s: #%d (%s)
rootless_mkdir_protected
%s
Sandbox
signal
%s: failed for %s: %s (%d)
%s: bad fts entity %d:%d at %s
%s: rootless_check_clear_storage_class(%s): %s
%s failed for %s: %d (%s)
sandbox_register_app_bundle_package_exception
sandbox_register_app_data_protection_package_exception
com.apple.sandbox.container
sandbox_extension_issue_file_to_self
%s failed for %x/%llu: %d (%s)
sandbox_apply
%s\n
invalid token passed to rootless_verify_trusted_by_self_token()
getattrlist failed for %s: #%d: %s
file-write-data
com.apple.app-sandbox.iokit-client
```
