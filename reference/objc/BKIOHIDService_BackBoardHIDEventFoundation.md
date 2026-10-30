# `BKIOHIDService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BKHIDEventSenderInfo`, `BSDescriptionProviding`, `NSCopying`
- 19 instance variables, 18 properties, 53 instance methods, 0 class methods

## Instance variables

```
@"BKIOHIDService" _strongSelf;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _workQueueAccessLock;
@"NSObject<OS_dispatch_queue>" _workQueue_do_not_touch_directly;
^{__IOHIDNotification=} _workQueue_removalNotification;
^{__IOHIDNotification=} _workQueue_willTerminateNotification;
@"NSMutableArray" _workQueue_disappearanceObservers;
@"BKSHIDEventSenderDescriptor" _senderDescriptorForKeyboardEvents;
B _authenticated;
B _builtIn;
i _eventSource;
I _primaryUsagePage;
I _primaryUsage;
@"BKSHIDEventSenderDescriptor" _senderDescriptor;
q _serviceStatus;
@"NSString" _productName;
@"NSString" _transport;
^{__IOHIDService=} _IOHIDService;
@"NSString" _displayUUID;
Q _senderID;
```

## Properties

```
@property (T^{__IOHIDService=},N,V_IOHIDService) IOHIDService;
@property (T@"NSString",C,N,V_displayUUID) displayUUID;
@property (Ti,N,V_eventSource) eventSource;
@property (TQ,N,V_senderID) senderID;
@property (TI,N,V_primaryUsagePage) primaryUsagePage;
@property (TI,N,V_primaryUsage) primaryUsage;
@property (TB,N,GisAuthenticated,V_authenticated) authenticated;
@property (TB,N,GisBuiltIn,V_builtIn) builtIn;
@property (T@"BKSHIDEventSenderDescriptor",C,N,V_senderDescriptor) senderDescriptor;
@property (Tq,N,V_serviceStatus) serviceStatus;
@property (T@"NSString",R,N) uniqueProductIdentifier;
@property (T@"NSString",R,C,N,V_productName) productName;
@property (T@"NSString",R,C,N,V_transport) transport;
@property (TB,R,N) isVirtualService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKIOHIDService propertyForKey:];
-[BKIOHIDService setServiceStatus:];
-[BKIOHIDService isAuthenticated];
-[BKIOHIDService setAuthenticated:];
-[BKIOHIDService eventSource];
-[BKIOHIDService serviceStatus];
-[BKIOHIDService setProperty:forKey:];
-[BKIOHIDService succinctDescriptionBuilder];
-[BKIOHIDService _workQueue_stopIOServiceRemovalNotifications];
-[BKIOHIDService productName];
-[BKIOHIDService uniqueProductIdentifier];
-[BKIOHIDService hasSiblingFIDOInterface];
-[BKIOHIDService propertyOfClass:forKey:];
-[BKIOHIDService asyncSetProperties:];
-[BKIOHIDService setEventSource:];
-[BKIOHIDService displayUUID];
-[BKIOHIDService dealloc];
-[BKIOHIDService senderDescriptorForEventType:];
-[BKIOHIDService transport];
-[BKIOHIDService descriptionWithMultilinePrefix:];
-[BKIOHIDService setProperties:];
-[BKIOHIDService setElementValue:forUsagePage:usage:];
-[BKIOHIDService senderID];
-[BKIOHIDService setSenderDescriptor:];
-[BKIOHIDService succinctDescription];
-[BKIOHIDService setDisplayUUID:];
-[BKIOHIDService _setUpInitialProperties];
-[BKIOHIDService setBuiltIn:];
-[BKIOHIDService removeDisappearanceObserver:];
-[BKIOHIDService claimsToConformToUsagePage:usage:];
-[BKIOHIDService addDisappearanceObserver:queue:];
-[BKIOHIDService setIOHIDService:];
-[BKIOHIDService initForSimulatorWithDisplayUUID:];
-[BKIOHIDService isBuiltIn];
-[BKIOHIDService senderDescriptor];
-[BKIOHIDService description];
-[BKIOHIDService primaryUsagePage];
-[BKIOHIDService asyncSetProperty:forKey:];
-[BKIOHIDService appendDescriptionToStream:];
-[BKIOHIDService asyncSetProperty:forKey:andDelayForSeconds:];
-[BKIOHIDService setSenderID:];
-[BKIOHIDService _workQueue_startIOServiceRemovalNotifications];
-[BKIOHIDService _initForTestingWithSenderID:setUpInitialProperties:];
-[BKIOHIDService setPrimaryUsagePage:];
-[BKIOHIDService isVirtualService];
-[BKIOHIDService primaryUsage];
-[BKIOHIDService copyWithZone:];
-[BKIOHIDService setPrimaryUsage:];
-[BKIOHIDService initWithHIDServiceRef:];
-[BKIOHIDService _disappearanceObservers];
-[BKIOHIDService IOHIDService];
-[BKIOHIDService _serviceWasRemoved];
-[BKIOHIDService descriptionBuilderWithMultilinePrefix:];
```
