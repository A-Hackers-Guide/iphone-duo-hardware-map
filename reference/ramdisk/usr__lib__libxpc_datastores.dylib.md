# `/usr/lib/libxpc_datastores.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 115,376 bytes.

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
v8@?0
v16@?0@\"NSObject<OS_xpc_object>\"8
ds_data_invalid_notify
ds_type
ds_data
Data from datastore failed to deserialize
max_size
com.apple.xpc.datastore
ds_data_invalid
B
request_type
ds_name
%s.pending_work_dq
endpoint
Unexpected data on anonymous endpoint to datastored
Failure with xpc pipe
Provided data has OOL types
ds_status
ds_ool_data
com.apple.xpc.datastores.publish
Data size exceeds datastore max size
XDS_xpc_datastore_publisher
OS_xpc_datastore_subscriber
XDS_xpc_datastore_subscriber
OS_xds_local_cache
OS_xpc_datastore_object
XDS_xpc_datastore_object
NSObject
OS_xpc_datastore_publisher
hash
publish_data
T@\"NSString\",R,C
isEqual:
isKindOfClass:
max_size
performSelector:
zone
pending_work_dq
init
performSelector:withObject:
respondsToSelector:
retain
T@\"NSString\",?,R,C
local_data
.cxx_destruct
conn
initWithName:
retainCount
activated
ds_name
TQ,R
description
dq
superclass
isProxy
class
data
lock
performSelector:withObject:withObject:
self
dealloc
T#,R
ds_type
release
isMemberOfClass:
recvp
size
autorelease
conformsToProtocol:
copyCurrentStateWithReqType:
debugDescription
@24@0:8:16
B24@0:8:16
^{_NSZone=}16@0:8
@24@0:8r*16
@24@0:8Q16
@\"OS_xds_local_cache\"
^v
B24@0:8@16
B16@0:8
@\"NSString\"16@0:8
@\"NSObject<OS_dispatch_queue>\"
@?
b1
I
v16@0:8
#16@0:8
@32@0:8:16@24
@40@0:8:16@24@32
B24@0:8@\"Protocol\"16
B24@0:8#16
Vv16@0:8
Q16@0:8
*
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
@\"NSObject<OS_xpc_object>\"
Q
@16@0:8
```
