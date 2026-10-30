# `/System/Library/PrivateFrameworks/AccessoryDaemonSupport.framework/AccessoryDaemonSupport`

iOS 27.2 dyld shared cache image. Version `41.7.0.0.0`. **[DSC]**

## Linked libraries (13)

- `/System/Library/PrivateFrameworks/AccessoryTypes.framework/AccessoryTypes`
- `/System/Library/PrivateFrameworks/AccessoryXPCServices.framework/AccessoryXPCServices`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_Concurrency.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 3 classes, 0 protocols, 0 methods, 0 properties

### Class pages

Every class and protocol, with its methods: [`_TtC22AccessoryDaemonSupport21AccessoryStateManager`](../objc/_TtC22AccessoryDaemonSupport21AccessoryStateManager_AccessoryDaemonSupport.md), [`_TtC22AccessoryDaemonSupport22AccessoryConfigManager`](../objc/_TtC22AccessoryDaemonSupport22AccessoryConfigManager_AccessoryDaemonSupport.md), [`_TtC22AccessoryDaemonSupport23AccessoryServicesDaemon`](../objc/_TtC22AccessoryDaemonSupport23AccessoryServicesDaemon_AccessoryDaemonSupport.md)

### Classes

`_TtC22AccessoryDaemonSupport21AccessoryStateManager`, `_TtC22AccessoryDaemonSupport22AccessoryConfigManager`, `_TtC22AccessoryDaemonSupport23AccessoryServicesDaemon`

## Swift types (7)

`AccessoryDaemonSupport.AccessoryConfigControllerProtocol`, `AccessoryDaemonSupport.AccessoryConfigManager`, `AccessoryDaemonSupport.AccessoryPrefsManager`, `AccessoryDaemonSupport.AccessoryServicesDaemon`, `AccessoryDaemonSupport.AccessoryStateManager`, `AccessoryDaemonSupport.AccessoryStateManager.StreamSubscription`, `conformance`

## Strings (40)

```
Subscription %@ detected as terminated during yield, marking for cleanup
AccessoryStateManager initialized
Accessory %@ changed %d properties: [%@]
updateAccessory called with empty identifier - ignoring
Removed dead subscription %@, remaining subscriptions: %d
%@
' is not implemented
com.apple.AccessoryDaemonSupport
Unsubscribe called for unknown subscription %@
Evaluating subscription %@ for accessory %@ (isRemoval=%@, currentlyMatches=%@, wasKnown=%@)
Subscription %@ - new device %@ matches filter, sending update
Stream subscription %@ terminated during initial yield
New accessory %@ created with %d properties changed: [%@]
Subscription %@ - device %@ doesn't match filter and is unknown, ignoring
Notifying %d stream subscribers about %@ for accessory %@
Notified new stream subscription %@ about %d existing devices
Found accessory: %@
Subscription %@ - no relevant property changes for device %@, ignoring
Removing accessory: %@
Subscription %@ - removal ignored: device %@ was not previously known
onTermination fired for subscription %@, removing from tracking
Subscription %@ - sending update for device %@ with relevant changes: [%@]
Subscription %@ - sending removal event for device %@
Unable to find accessory '
Sending config over transport '
Getting accessories with filter: %@, total=%d, filtered=%d
Accessory %@ not found for removal
Subscription %@ - device %@ no longer matches filter, sending removal
Added stream subscription %@ interested in [%@], filter: %@, total subscriptions: %d
Removed stream subscription %@, remaining subscriptions: %d
Accessory not found: %@
Successfully removed accessory: %@
Subscription %@ no longer found, skipping
Getting accessory with identifier: %@
AccessoryServicesDaemon initialized with injected state manager
XPC listener started successfully
Starting AccessoryServicesDaemon XPC listener...
Stopping AccessoryServicesDaemon XPC listener
AccessoryStateManager initialized
Sending config %s over transport '%s' for '%s'
```
