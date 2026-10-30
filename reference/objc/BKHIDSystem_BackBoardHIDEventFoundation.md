# `BKHIDSystem`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventProcessor`, `BKHIDEventBufferingHIDSystem`, `BKHIDSystemInterfacing`
- 12 instance variables, 13 properties, 37 instance methods, 1 class methods

## Instance variables

```
^{__IOHIDEventSystem=} _HIDEventSystem;
^{__IOHIDEventSystemClient=} _HIDEventSystemClient;
@"NSObject<OS_dispatch_queue>" _gsEventQueue;
@"NSMutableArray" _pendingDeliveryManagerBlocks;
B _fullyInitialized;
@"<BKHIDSystemDelegate>" _delegate;
@"BKHIDEventDeliveryManager" _deliveryManager;
@"BKHIDEventSenderCache" _senderCache;
@"NSObject<OS_dispatch_mach>" _HIDSystemChannel;
@"<BKHIDEventProcessor><BKHIDBufferedEventProcessor>" _eventProcessor;
@"<BKHIDDisplayChangeObserving>" _mainDisplayObserver;
@"<BKHIDEventDispatcherProviding>" _dispatcherProvider;
```

## Properties

```
@property (TB,GisFullyInitialized,V_fullyInitialized) fullyInitialized;
@property (T@"NSObject<OS_dispatch_mach>",&,GHIDSystemChannel,V_HIDSystemChannel) HIDSystemChannel;
@property (T@"<BKHIDEventProcessor><BKHIDBufferedEventProcessor>",R,N,V_eventProcessor) eventProcessor;
@property (T@"<BKHIDDisplayChangeObserving>",&,N,V_mainDisplayObserver) mainDisplayObserver;
@property (T@"<BKHIDEventDispatcherProviding>",&,N,V_dispatcherProvider) dispatcherProvider;
@property (T@"<BKHIDSystemDelegate>",W,V_delegate) delegate;
@property (T@"BKHIDEventDeliveryManager",R,V_deliveryManager) deliveryManager;
@property (T@"BKHIDEventSenderCache",R,V_senderCache) senderCache;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BKHIDClientConnectionManager",R) clientConnectionManager;
```

## Class methods

```
+[BKHIDSystem sharedInstance];
```

## Instance methods

```
-[BKHIDSystem systemPropertyForKey:];
-[BKHIDSystem init];
-[BKHIDSystem dealloc];
-[BKHIDSystem processEvent:sender:dispatcher:];
-[BKHIDSystem clientConnectionManager];
-[BKHIDSystem setDelegate:];
-[BKHIDSystem delegate];
-[BKHIDSystem deliveryManager];
-[BKHIDSystem isFullyInitialized];
-[BKHIDSystem setFullyInitialized:];
-[BKHIDSystem HIDSystemChannel];
-[BKHIDSystem IOHIDServicesMatching:];
-[BKHIDSystem _asyncScheduleWithHIDEventQuue:];
-[BKHIDSystem injectHIDEvent:];
-[BKHIDSystem registerIOHIDServicesCallback:matchingDictionary:target:refCon:];
-[BKHIDSystem _beginHandlingEvents];
-[BKHIDSystem buffer:drainEvent:withContext:sender:sequence:toResolution:];
-[BKHIDSystem bufferDidFinishDraining:];
-[BKHIDSystem bufferWillBeginDraining:];
-[BKHIDSystem bufferingDidAddNewBuffers:];
-[BKHIDSystem dispatcherProvider];
-[BKHIDSystem eventProcessor];
-[BKHIDSystem injectGSEvent:];
-[BKHIDSystem mainDisplayObserver];
-[BKHIDSystem performWhenDeliveryManagerAvailable:];
-[BKHIDSystem requestBufferReevaluationWithContext:];
-[BKHIDSystem senderCache];
-[BKHIDSystem setDispatcherProvider:];
-[BKHIDSystem setHIDSystemChannel:];
-[BKHIDSystem setMainDisplayObserver:];
-[BKHIDSystem setSystemProperty:forKey:];
-[BKHIDSystem startEventProcessor:mainDisplayObserver:deliveryManager:dispatcherProvider:];
-[BKHIDSystem startEventRouting];
-[BKHIDSystem startHIDSystem];
-[BKHIDSystem startServerWithChannel:];
-[BKHIDSystem systemEventOfType:matchingEvent:options:];
-[BKHIDSystem unregisterIOHIDServicesCallback:matchingDictionary:target:refCon:];
```
