# `/usr/lib/swift/libswiftXPC.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 834,976 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 4336)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (9 classes, 2 protocols)

Classes: `_TtC3XPC10XPCSession`, `_TtC3XPC11XPCListener`, `_TtC3XPC16DecodedContainer`, `_TtC3XPC23_KeyedGraphEncodingNode`, `_TtC3XPC24UnkeyedGraphEncodingNode`, `_TtC3XPC25TopLevelGraphEncodingNode`, `_TtC3XPC28SingleValueGraphEncodingNode`, `_TtCC3XPC11XPCListener22IncomingSessionRequest`, `_TtCV3XPC18XPCReceivedMessage26XPCReceivedMessageMetadata`

Protocols: `NSObject`, `OS_xpc_object`

## Strings (138)

```
, and unable to recover from encoded value: 
Failed to initialize 
Unable to decode message 
Missing container metadata for _UnkeyedDecodingContainer
 into a container
 but found incorrect type: xpc object 
Null Listener and Null error
 is not available in Swift. Use the equivalent Swift API instead.
Missing container metadata for _SingleValueDecodingContainer
Container size mismatch for _SingleValueDecodingContainer
Insufficient container in buffer
XPCCodableObject (containing: 
Trying to get a decision before it was set
Invalid encoding graph: Failed to find key
No response and no error
xpc_listener_create(_:_:_:_:_:)
Invalid encoding graph: Found 
init(stringValue:) should never be called
Duplicate reference to node #
XPC object does not represent valid Data: 
Insufficient bytes to decode XPCObject
Missing container metadata for 
init(intValue:) should never be called
Expected XPC_TYPE_DICTIONARY but received 
Missing CodingUserInfoKey 
Cannot read a valid tag from buffer
Bad index for XPC object: 
Found dangling container in buffer
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/Session.swift
Invalid container metadata for 
XPC/UnkeyedEncodingContainer.swift
Cannot read a valid UInt16 from buffer
IncomingSessionRequest already handled with decision 
Fatal error
Received message from a process running old XPC coder
Container is at end.
XPCDictionary did not contain a possibly-Codable value for specified key
_CodableCoderVersion
XPCReceivedMessage did not contain Codable contents
XPC object does not exist at index 
(failed to generate debug description for XPCListener)
Peer requirement invalid: 
Cannot read a valid UInt from buffer
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/PeerRequirement.swift
xpc_listener_copy_description(_:)
xpc_listener_reject_peer(_:_:)
Invalid encoding graph:: Found key, expected value
Cannot read a valid UInt8 from buffer
Unexpected failure in casting 
XPC/KeyedEncodingContainer.swift
(failed to generate debug description for XPCSession)
xpc_session_send_message_with_reply_async no reply and no error
XPC/XPC.swift
_CodableOutOfLine
Null Session and Null Error
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/RichError.swift
Activation failed, but no error
Failed to construct peer requirement: 
xpc_listener_activate(_:_:)
Cannot read a valid UInt64 from buffer
xpc_listener_cancel(_:)
_CodableOutOfLine4CodableObject
 elements, expected odd number
Container size mismatch for SingleValueDecodingContainer4OptionalPrimitive
Found malformed XPC Data for Codable contents
XPCReceivedMessage did not contain CodableObject contents
Unable to encode 
, and container size (
Cannot read a valid UInt32 from buffer
Found bad value for .containerMetadata: 
Cannot read a valid string from buffer
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/Listener.swift
Receiver didn't call reply(_) or handoffReply(_) before returning from the message handler for this sync IPC message
_TtCC3XPC11XPCListener22IncomingSessionRequest
OS_xpc_object
_TtC3XPC10XPCSession
_TtCV3XPC18XPCReceivedMessage26XPCReceivedMessageMetadata
NSObject
_TtC3XPC25TopLevelGraphEncodingNode
_TtC3XPC23_KeyedGraphEncodingNode
_TtC3XPC28SingleValueGraphEncodingNode
_TtC3XPC24UnkeyedGraphEncodingNode
_TtC3XPC16DecodedContainer
_TtC3XPC11XPCListener
class
conformsToProtocol:
performSelector:
performSelector:withObject:withObject:
values
zone
_listener
autorelease
decodedValues
isKindOfClass:
respondsToSelector:
_session
description
hash
retainCount
targetQueue
release
performSelector:withObject:
isMemberOfClass:
keyToIndex
self
wrappedNode
TQ,R
_decision
debugDescription
isEqual:
retain
isProxy
T@\"NSString\",?,R,C
T#,R
T@\"NSString\",R,C
isSync
superclass
requiresHandoff
B24@?0q8@\"<OS_xpc_object>\"16
@16@0:8
@24@0:8:16
B24@0:8#16
Vv16@0:8
@\"NSString\"16@0:8
B24@0:8@16
@40@0:8:16@24@32
B24@0:8:16
Q16@0:8
v16@?0@\"<OS_xpc_object>\"8
v24@?0@\"<OS_xpc_object>\"8@\"<OS_xpc_object>\"16
#16@0:8
B16@0:8
B24@?0r*8@\"<OS_xpc_object>\"16
@32@0:8:16@24
^{_NSZone=}16@0:8
v16@?0@\"OS_xpc_session\"8
B24@0:8@\"Protocol\"16
v8@?0
```
