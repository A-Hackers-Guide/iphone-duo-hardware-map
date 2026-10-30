# `/usr/lib/swift/libswiftXPC.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 834,976 bytes.

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
Insufficient bytes to decode XPCObject
Trying to get a decision before it was set
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/Listener.swift
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/PeerRequirement.swift
xpc_session_send_message_with_reply_async no reply and no error
XPC object does not represent valid Data: 
init(intValue:) should never be called
Cannot read a valid tag from buffer
Cannot read a valid UInt from buffer
Unexpected failure in casting 
xpc_listener_reject_peer(_:_:)
Cannot read a valid UInt32 from buffer
Cannot read a valid string from buffer
_CodableOutOfLine
Invalid encoding graph: Found 
Invalid encoding graph:: Found key, expected value
Null Listener and Null error
Unable to decode message 
Missing container metadata for _SingleValueDecodingContainer
Container is at end.
Bad index for XPC object: 
XPC object does not exist at index 
Cannot read a valid UInt64 from buffer
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/RichError.swift
Activation failed, but no error
 is not available in Swift. Use the equivalent Swift API instead.
, and unable to recover from encoded value: 
 elements, expected odd number
Missing container metadata for _UnkeyedDecodingContainer
XPCCodableObject (containing: 
xpc_listener_create(_:_:_:_:_:)
Received message from a process running old XPC coder
XPCReceivedMessage did not contain CodableObject contents
, and container size (
XPC/KeyedEncodingContainer.swift
_CodableCoderVersion
xpc_listener_cancel(_:)
(failed to generate debug description for XPCListener)
Peer requirement invalid: 
No response and no error
(failed to generate debug description for XPCSession)
/Library/Caches/com.apple.xbs/5443B275-EE4F-4C42-BC5F-40797359FA80/TemporaryDirectory.WyGDnN/Sources/XPC_swiftoverlay/XPC-swiftoverlay/Session.swift
Invalid encoding graph: Failed to find key
init(stringValue:) should never be called
Missing CodingUserInfoKey 
Cannot read a valid UInt8 from buffer
Expected XPC_TYPE_DICTIONARY but received 
 into a container
Cannot read a valid UInt16 from buffer
Failed to construct peer requirement: 
Null Session and Null Error
xpc_listener_activate(_:_:)
Container size mismatch for _SingleValueDecodingContainer
XPC/UnkeyedEncodingContainer.swift
Insufficient container in buffer
XPCDictionary did not contain a possibly-Codable value for specified key
XPCReceivedMessage did not contain Codable contents
Found malformed XPC Data for Codable contents
Found bad value for .containerMetadata: 
Found dangling container in buffer
xpc_listener_copy_description(_:)
_CodableOutOfLine4CodableObject
Invalid container metadata for 
IncomingSessionRequest already handled with decision 
XPC/XPC.swift
Container size mismatch for SingleValueDecodingContainer4OptionalPrimitive
Duplicate reference to node #
Fatal error
Unable to encode 
Missing container metadata for 
Failed to initialize 
 but found incorrect type: xpc object 
Receiver didn't call reply(_) or handoffReply(_) before returning from the message handler for this sync IPC message
OS_xpc_object
NSObject
_TtC3XPC25TopLevelGraphEncodingNode
_TtC3XPC23_KeyedGraphEncodingNode
_TtC3XPC28SingleValueGraphEncodingNode
_TtC3XPC24UnkeyedGraphEncodingNode
_TtC3XPC16DecodedContainer
_TtC3XPC11XPCListener
_TtCC3XPC11XPCListener22IncomingSessionRequest
_TtC3XPC10XPCSession
_TtCV3XPC18XPCReceivedMessage26XPCReceivedMessageMetadata
isKindOfClass:
wrappedNode
requiresHandoff
superclass
zone
debugDescription
T#,R
_session
decodedValues
keyToIndex
performSelector:withObject:
T@\"NSString\",?,R,C
description
performSelector:withObject:withObject:
isProxy
_listener
isEqual:
autorelease
class
isMemberOfClass:
retainCount
retain
_decision
hash
self
targetQueue
TQ,R
isSync
performSelector:
respondsToSelector:
values
release
T@\"NSString\",R,C
conformsToProtocol:
B24@0:8@16
@32@0:8:16@24
B24@0:8:16
v16@?0@\"<OS_xpc_object>\"8
v16@?0@\"OS_xpc_session\"8
@16@0:8
B24@0:8#16
@\"NSString\"16@0:8
Q16@0:8
v8@?0
B24@?0q8@\"<OS_xpc_object>\"16
#16@0:8
@24@0:8:16
B16@0:8
Vv16@0:8
B24@?0r*8@\"<OS_xpc_object>\"16
@40@0:8:16@24@32
v24@?0@\"<OS_xpc_object>\"8@\"<OS_xpc_object>\"16
^{_NSZone=}16@0:8
B24@0:8@\"Protocol\"16
```
