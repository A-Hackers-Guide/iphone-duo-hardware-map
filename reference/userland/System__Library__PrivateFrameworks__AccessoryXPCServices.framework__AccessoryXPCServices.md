# `/System/Library/PrivateFrameworks/AccessoryXPCServices.framework/AccessoryXPCServices`

iOS 27.2 dyld shared cache image. Version `41.7.0.0.0`. **[DSC]**

## Linked libraries (15)

- `/usr/lib/libbsm.0.dylib`
- `/System/Library/PrivateFrameworks/AccessoryTypes.framework/AccessoryTypes`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Security.framework/Security`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_Concurrency.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 4 classes, 0 protocols, 0 methods, 0 properties

### Class pages

Every class and protocol, with its methods: [`_TtC20AccessoryXPCServices18AccessoryXPCClient`](../objc/_TtC20AccessoryXPCServices18AccessoryXPCClient_AccessoryXPCServices.md), [`_TtC20AccessoryXPCServices19AccessoryXPCHandler`](../objc/_TtC20AccessoryXPCServices19AccessoryXPCHandler_AccessoryXPCServices.md), [`_TtC20AccessoryXPCServices20AccessoryXPCListener`](../objc/_TtC20AccessoryXPCServices20AccessoryXPCListener_AccessoryXPCServices.md), [`_TtC20AccessoryXPCServices23AccessoryXPCPeerHandler`](../objc/_TtC20AccessoryXPCServices23AccessoryXPCPeerHandler_AccessoryXPCServices.md)

### Classes

`_TtC20AccessoryXPCServices18AccessoryXPCClient`, `_TtC20AccessoryXPCServices19AccessoryXPCHandler`, `_TtC20AccessoryXPCServices20AccessoryXPCListener`, `_TtC20AccessoryXPCServices23AccessoryXPCPeerHandler`

## Swift types (28)

`AccessoryXPCServices.AccessoryClientXPCMessage`, `AccessoryXPCServices.AccessoryClientXPCMessage.CodingKeys`, `AccessoryXPCServices.AccessoryClientXPCMessage.GetAccessoriesCodingKeys`, `AccessoryXPCServices.AccessoryClientXPCMessage.GetAccessoryCodingKeys`, `AccessoryXPCServices.AccessoryClientXPCMessage.SendDeviceConfigCodingKeys`, `AccessoryXPCServices.AccessoryClientXPCMessage.SubscribeCodingKeys`, `AccessoryXPCServices.AccessoryClientXPCMessage.UnsubscribeCodingKeys`, `AccessoryXPCServices.AccessoryConfigManagerProtocol`, `AccessoryXPCServices.AccessoryPeerEvent`, `AccessoryXPCServices.AccessoryPeerEvent.AccessoryEventCodingKeys`, `AccessoryXPCServices.AccessoryPeerEvent.CodingKeys`, `AccessoryXPCServices.AccessoryStateManagerProtocol`, `AccessoryXPCServices.AccessoryXPCClient`, `AccessoryXPCServices.AccessoryXPCConstants`, `AccessoryXPCServices.AccessoryXPCHandler`, `AccessoryXPCServices.AccessoryXPCListener`, `AccessoryXPCServices.AccessoryXPCMessageBase`, `AccessoryXPCServices.AccessoryXPCPeerHandler`, `AccessoryXPCServices.AccessoryXPCResult.CodingKeys<A:`, `AccessoryXPCServices.AccessoryXPCResult.FailureCodingKeys<A:`, `AccessoryXPCServices.AccessoryXPCResult.SuccessCodingKeys<A:`, `AccessoryXPCServices.AccessoryXPCResult<A:`, `AccessoryXPCServices.VoidResult`, `AccessoryXPCServices.VoidResult.CodingKeys`, `AccessoryXPCServices.XPCError`, `__C.CFBooleanRef`, `__C.os_unfair_lock_s`, `conformance`

## Strings (70)

```
com.apple.AccessoryXPCServices
Connection invalidated
com.apple.AccessoryServices
sendAndWaitForReply(_:as:)
com.apple.AccessoryXPCServices.listener
Invalid number of keys found, expected one.
config identifier 
com.apple.AccessoryXPCServices.peerhandler
Client invalidate
properties filter 
XPC request failed: 
XPC connection not established. Call activate() first.
Missing required entitlement: com.apple.AccessoryServices
com.apple.AccessoryXPCServices.client
sendDeviceConfig
AccessoryXPCClient initialized
XPC connection not active, nothing to invalidate
Starting XPC listener on service: %s
Stopping XPC listener and disconnecting all clients
Connection authorized: client has required entitlement
Created peer handler %s for new connection
AccessoryXPCPeerHandler initialized for peer: %s
Cleaning up peer handler: %s
New subscription active for peer %s
Received subscribe request from peer %s
Note: This service requires AccessoryFeatures.AAFRefactor feature flag to be enabled
Activating XPC connection to %s
Invalidating XPC connection
Requesting accessories with filter: %s
Sending device config to accessory: %s
AccessoryXPCListener initialized (inactive)
XPC listener started successfully, waiting for connections
Entitlement not found: %@
Entitlement has wrong type: expected Boolean
Peer %s cleanup completed
Received message from peer %s: %s
Received request from peer %s for accessory: %s
Returning %ld accessories to peer %s
Received sendDeviceConfig request from peer %s for accessory: %s
XPC connection already active
XPC connection invalidated
Sending unsubscribe message
Peer %s connection cancelled: %s
Cleaning up existing subscription (if any) for peer %s
Failed to send event to peer %s: %s
XPC client initialized
Rejecting connection: client lacks com.apple.AccessoryServices entitlement
Peer handler %s deallocated - XPC framework released reference
Received request from peer %s for accessories with filter: %s
Event stream ended for peer %s
Subscription task cancelled for peer %s, stopping event forwarding
Failed to establish XPC connection to %s: %@
Cancelling XPC session
Subscribing to accessory events
XPC connection cancelled: %s
Failed to send unsubscribe: %s
XPC listener stopped
Failed to create SecTask from audit token
Failed to copy entitlement: %@
Entitlement has value false, expected true
Forwarded event to peer %s
Successfully sent device config to accessory %s
Requesting accessory: %s
Received %ld accessories
Subscription active, returning event stream
Device config sent successfully
Failed to decode incoming message: %s
Received accessory event from daemon
Failed to decode message from peer %s: %s
Error handling request: %s
```
