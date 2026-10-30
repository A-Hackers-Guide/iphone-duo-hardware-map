# `/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`

iOS 27.2 dyld shared cache image. Version `500.2.0.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 14 classes, 0 protocols, 148 methods, 22 properties

### Class pages

Every class and protocol, with its methods: [`IOKConnection`](../objc/IOKConnection_IOKitten.md), [`IOKInterestNotification`](../objc/IOKInterestNotification_IOKitten.md), [`IOKInterestNotificationRef`](../objc/IOKInterestNotificationRef_IOKitten.md), [`IOKIterator`](../objc/IOKIterator_IOKitten.md), [`IOKMatchingNotification`](../objc/IOKMatchingNotification_IOKitten.md), [`IOKMatchingNotificationRef`](../objc/IOKMatchingNotificationRef_IOKitten.md), [`IOKNotificationPort`](../objc/IOKNotificationPort_IOKitten.md), [`IOKObject`](../objc/IOKObject_IOKitten.md), [`IOKPowerManager`](../objc/IOKPowerManager_IOKitten.md), [`IOKPowerManagerPowerAssertion`](../objc/IOKPowerManagerPowerAssertion_IOKitten.md), [`IOKPowerNotifier`](../objc/IOKPowerNotifier_IOKitten.md), [`IOKRegistryEntry`](../objc/IOKRegistryEntry_IOKitten.md), [`IOKService`](../objc/IOKService_IOKitten.md), [`IORegistryIterator`](../objc/IORegistryIterator_IOKitten.md)

### Classes

`IOKConnection`, `IOKInterestNotification`, `IOKInterestNotificationRef`, `IOKIterator`, `IOKMatchingNotification`, `IOKMatchingNotificationRef`, `IOKNotificationPort`, `IOKObject`, `IOKPowerManager`, `IOKPowerManagerPowerAssertion`, `IOKPowerNotifier`, `IOKRegistryEntry`, `IOKService`, `IORegistryIterator`

### Properties

```
@property (TI,R,N,V_connection) connection;
@property (T@"IOKService",R,C,N) service;
@property (T@?,C,N,V_handler) handler;
@property (TI,N,V_object) object;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"IOKInterestNotificationRef",R,N,V_notificationRef) notificationRef;
@property (T@"IOKInterestNotification",N,V_notification) notification;
@property (TB,R,N,GisValid) valid;
@property (T@?,C,N,V_handler) handler;
@property (T@"IOKIterator",&,N,V_iterator) iterator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"IOKMatchingNotificationRef",R,N,V_notificationRef) notificationRef;
@property (T@"IOKMatchingNotification",N,V_notification) notification;
@property (T^{IONotificationPort=},R,N,V_port) port;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (TI,R,N) machPort;
@property (T@"NSString",R,C,N) ioClassName;
@property (TI,R,N,V_object) object;
@property (T@"<IOKPowerNotifierDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N) name;
@property (TQ,R,N) entryID;
@property (T@"NSDictionary",C,N) properties;
```

## Strings (56)

```
PreventUserIdleDisplaySleep
-[IOKConnection setNotificationPort:ofType:withReference:error:]
-[IOKConnection setProperty:withKey:error:]
-[IOKConnection callMethodWithSelector:structInput:structInputSize:structOutput:structOutputSize:error:]
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:]
IODeviceTree
IOServicePublish
IOServiceWillTerminate
IOErrorDomain
PreventUserIdleSystemSleep
-[IOKConnection setProperties:error:]
-[IOKConnection trap:p1:error:]
-[IOKConnection trap:p1:p2:error:]
notificationPort.queue
handler
v16@?0@\"IOKIterator\"8
NetworkClientActive
-[IOKConnection init]
-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:]
-[IOKConnection callMethodWithSelector:scalarInputs:scalarInputCount:scalarOutputs:scalarOutputCount:error:]
-[IOKConnection trap:p1:p2:p3:error:]
IOAudio
IOUSB
IOServiceFirstPublish
notificationPort
iteratorEnumerationBlock
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:structInput:structInputSize:structOutput:structOutputSize:error:]
-[IOKConnection trap:error:]
IOService
IOServiceFirstMatch
IOServiceTerminate
IOGeneralInterest
IOPriorityPowerStateInterest
v8@?0
-[IOKConnection unmapMemory64OfType:atAddress:error:]
-[IOKConnection trap:p1:p2:p3:p4:error:]
-[IOKConnection trap:p1:p2:p3:p4:p5:error:]
-[IOKConnection trap:p1:p2:p3:p4:p5:p6:error:]
IOFireWire
IOServiceMatched
IOBusyInterest
IOAppPowerStateInterest
Do not call %@
-[IOKObject init]
/Library/Caches/com.apple.xbs/CDA3C3FC-D45B-4205-831C-0E4550611BFD/TemporaryDirectory.5oyFNs/Sources/AudioTransportFrameworks/IOKitten/IOKService.m
To use -enumerate you must initialise with the initWithIterator:enumerationBlock: method.
PreventDiskIdle
!
-[IOKConnection mapMemory64OfType:withOptions:atAddress:ofSize:error:]
-[IOKConnection callAsyncMethodWithSelector:wakePort:reference:referenceCount:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:structOutput:structOutputSize:error:]
-[IOKNotificationPort init]
IORegistryEntry
IOPower
%s %s failed with error 0x%08x
IOKConnection %s failed with error 0x%08x
Assert: %s (value 0x%lx %lu), %s file: %s, line: %d\n
```
