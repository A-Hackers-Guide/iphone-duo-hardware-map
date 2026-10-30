# `/usr/lib/libxpc_datastores.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 115,376 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2888)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (4)

- `/usr/lib/libxpc_datastores.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (4 classes, 4 protocols)

Classes: `OS_xds_local_cache`, `OS_xpc_datastore_object`, `OS_xpc_datastore_publisher`, `OS_xpc_datastore_subscriber`

Protocols: `NSObject`, `XDS_xpc_datastore_object`, `XDS_xpc_datastore_publisher`, `XDS_xpc_datastore_subscriber`

## Strings (98)

```
request_type
ds_status
ds_type
ds_ool_data
Data from datastore failed to deserialize
max_size
Unexpected data on anonymous endpoint to datastored
Provided data has OOL types
B
com.apple.xpc.datastore
ds_data
ds_data_invalid
Data size exceeds datastore max size
v8@?0
v16@?0@\"NSObject<OS_xpc_object>\"8
ds_name
ds_data_invalid_notify
%s.pending_work_dq
endpoint
Failure with xpc pipe
com.apple.xpc.datastores.publish
OS_xpc_datastore_publisher
XDS_xpc_datastore_publisher
OS_xpc_datastore_subscriber
XDS_xpc_datastore_subscriber
OS_xds_local_cache
OS_xpc_datastore_object
XDS_xpc_datastore_object
NSObject
dq
init
lock
retain
self
isMemberOfClass:
local_data
T#,R
ds_type
T@\"NSString\",R,C
conn
ds_name
description
max_size
performSelector:withObject:
performSelector:withObject:withObject:
superclass
activated
conformsToProtocol:
copyCurrentStateWithReqType:
hash
isKindOfClass:
performSelector:
dealloc
.cxx_destruct
class
respondsToSelector:
zone
isProxy
autorelease
initWithName:
isEqual:
pending_work_dq
publish_data
recvp
size
T@\"NSString\",?,R,C
TQ,R
data
debugDescription
retainCount
release
@16@0:8
B24@0:8#16
@\"NSString\"16@0:8
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@?
^v
@24@0:8:16
@32@0:8:16@24
B16@0:8
Vv16@0:8
@24@0:8r*16
@\"NSObject<OS_xpc_object>\"
@\"NSObject<OS_dispatch_queue>\"
v16@0:8
#16@0:8
@40@0:8:16@24@32
B24@0:8:16
^{_NSZone=}16@0:8
b1
I
Q16@0:8
B24@0:8@\"Protocol\"16
@24@0:8Q16
*
@\"OS_xds_local_cache\"
Q
B24@0:8@16
```
