# `/usr/lib/system/libsystem_darwindirectory.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 96,016 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 30 (Size: 2448)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (13)

- `/usr/lib/system/libsystem_darwindirectory.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_darwin.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_notify.dylib (compatibility version 1.0.0, current version 368.40.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`

## Entitlements

```xml
  - no entitlements
```

## Strings (71)

```
assertion failure: \"xpc_get_type(value) == (&_xpc_type_uint64)\" -> %llu
assertion failure: \"bootUUIDFound\" -> %llu
assertion failure: \"xpc_get_type(object) == (&_xpc_type_dictionary)\" -> %llu
assertion failure: \"store->recordStoreLen == 0\" -> %llu
assertion failure: \"xpc_get_type(value) == (&_xpc_type_array)\" -> %llu
assertion failure: \"xpc_get_type(memberValue) == (&_xpc_type_string)\" -> %llu
assertion failure: \"store->notifyToken == -1\" -> %llu
assertion failure: \"store->recordStore != ((void*)0)\" -> %llu
assertion failure: \"store->recordStoreLen != 0\" -> %llu
assertion failure: \"store->recordStore == ((void*)0)\" -> %llu
assertion failure: \"data != ((void*)0)\" -> %llu
assertion failure: \"seData->type == (&_xpc_type_uuid)\" -> %llu
assertion failure: \"xpc_get_type(value) == (&_xpc_type_uuid)\" -> %llu
assertion failure: \"xpc_get_type(value) == (&_xpc_type_bool)\" -> %llu
assertion failure: \"munmapResult == 0\" -> %llu
assertion failure: \"seData->length == sizeof(uuid_t)\" -> %llu
assertion failure: \"aeData != ((void*)0)\" -> %llu
assertion failure: \"foundMap\" -> %llu
assertion failure: \"xpc_get_type(value) == (&_xpc_type_string)\" -> %llu
allocation failed: obj = %s, size = %lu, error = %s
Record store at path %s doesn't have the correct boot uuid, unloading
Failed to stat record store %s: %s [%d]
ddrsKeyBootUUID
UUID
memberNames
v8@?0
i16@?0[16C]8
i24@?0^v8Q16
libsystem_darwindirectory: Failed to load system record store
com.apple.darwindirectory.local
com.apple.DarwinDirectory
Failed to register for record store update notifications: %d
Record store has not yet been loaded
Record store has a NULL boot UUID
ddrsKeyUserUUIDMap
ddrsKeyGroupUUIDMap
libsystem_darwindirectory: Invalid record type
ddrsKeyUserIDMap
known-constant allocation
kern.bootsessionuuid
/private/var/db/DarwinDirectory/local/recordStore.data
Loaded local record store
libsystem_darwindirectory: Failed to load local record store on reload
Failed to get the current boot UUID: %s (%d)
ddrsKeyUserRecordList
libsystem_darwindirectory: Invalid filter type
name
primaryGroupID
Local record store has changed and needs to be reloaded
Failed to open record store %s: %s [%d]
I20@?0I8^v12
ID
isMutable
fullName
shell
i20@?0r*8i16
Record store boot UUID does not match the current boot session
ddrsKeyGroupRecordList
Loaded system record store
/System/Library/DarwinDirectory/system/recordStore.data
i12@?0i8
i20@?0i8^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}12
I24@?0r*8^i16
I20@?0i8^i12
Failed to mmap file %s: %s [%d]
%u
ddrsKeyGroupIDMap
ddrsKeyUserNameMap
ddrsKeyGroupNameMap
homeDirectory
^v28@?0Q8i16i20i24
```
