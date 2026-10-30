# `/usr/lib/system/libsystem_sandbox.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 120,544 bytes.

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
sandbox_message_filter_retain
sandbox_compile_string
invalid
%s failed: %d (%s)
sandbox_check_message_filter_string
sandbox_compile_named
iokit-open
%s: open(%s): %s
%s: lchflags(%s): %s
%s: unsupported flags: %u
%s: failed for %s: %s (%d)
%s failed for %s: %d (%s)
unsupported flags passed to %s: 0x%0x
v8@?0
%s: fts_open(%s): %s
%s: fts_read: %s
%s: rootless_clear_storage_class(%s): %s
compilation failed
sandbox_extension_issue_related_file_to_process
%s: rootless_set_storage_class(%s): %s
/usr/lib/libsandbox.1.dylib
%s: failed to allocate
sandbox_message_filter_release
sandbox_register_app_container_package_exception
sandbox_register_app_data_protection_exception
sandbox_apply
file-write-data
sandbox_extension_issue_mach_to_process
sandbox_extension_issue_mach_to_process_by_pid
sandbox_extension_issue_iokit_registry_entry_class
sandbox_extension_issue_generic_to_process_by_pid
iokit-open-user-client
(platform)
%s: bad fts entity %d:%d at %s
%s: failed: %s not on same filesystem as parent
com.apple.app-sandbox.read-write
sandbox_register_app_container_exception
sandbox_free_profile
rootless_mkdir_protected
rootless_remove_in_favor_of_static_storage_class
%s: rootless_check_clear_storage_class(%s): %s
sandbox_set_param
sandbox_checkattr_alloc
sandbox_extension_issue_generic
rootless_convert_to_datavault
sandbox_create_params
bad flags
sandbox_check_finder_automation_for_path
kTCCServiceMediaLibrary-iMovie
fgetattrlist failed: #%d: %s
Sandbox
sandbox_extension_issue_file_to_self
%s%s-XXXXXX
%s: failed: %s storage class changed before protection
com.apple.libsystem.rootless
security.mac.sandbox.sentinel
sandbox_register_app_bundle_package_exception
sandbox_compile_file
com.apple.sandbox.application-group
sandbox_extension_issue_file_to_process
sandbox_register_app_data_protection_package_exception
com.apple.libsystem.sandbox
getattrlist failed for %s: #%d: %s
%s: failed: %s moved before protection
com.apple.app-sandbox.mach
com.apple.sandbox.container
signal
sandbox_extension_issue_file
sandbox_extension_issue_generic_to_process
sandbox operation \"%s\" is obsolete; replace with \"%s\"
invalid token passed to rootless_verify_trusted_by_self_token()
sandbox_extension_consume
sandbox_extension_update_file
sandbox_check_message_filter_integer
getattrlist failed: #%d: %s
com.apple.app-sandbox.read
network-
asr-parser-enter
sandbox_extension_issue_iokit_registry_entry_class_to_process_by_pid
com.apple.rootless
%s: failed: %s not protected
sandbox_free_params
sandbox_extension_issue_file_to_process_by_pid
sandbox_extension_update_file_by_fileid
%s failed on message filter #%llu: %d (%s)
sandbox_register_app_bundle_exception
%s\n
-telemetry-
%s failed for team-id=%s, signing-id=%s: #%d (%s)
com.apple.app-sandbox.iokit-client
%s
sandbox initialization failed: %s
sandbox_extension_issue_mach
sandbox_extension_issue_iokit_registry_entry_class_to_process
%s failed for %x/%llu: %d (%s)
```
