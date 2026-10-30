# `BKTouchDeliveryPolicyServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `NSXPCConnectionDelegate`, `BKSTouchDeliveryPolicyServerInterface`
- 4 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCListener" _listener;
@"NSMutableSet" _assertionConnections;
@"BKSTouchDeliveryPolicy" _policy;
```

## Properties

```
@property (T@"BKSTouchDeliveryPolicy",&,S_queue_setPolicy:,V_policy) _policy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKTouchDeliveryPolicyServer sharedServer];
```

## Instance methods

```
-[BKTouchDeliveryPolicyServer listener:shouldAcceptNewConnection:];
-[BKTouchDeliveryPolicyServer init];
-[BKTouchDeliveryPolicyServer connection:handleInvocation:isReply:];
-[BKTouchDeliveryPolicyServer _policy];
-[BKTouchDeliveryPolicyServer dealloc];
-[BKTouchDeliveryPolicyServer run];
-[BKTouchDeliveryPolicyServer ipc_addPolicy:];
-[BKTouchDeliveryPolicyServer _queue_setPolicy:];
-[BKTouchDeliveryPolicyServer filterDestinations:];
-[BKTouchDeliveryPolicyServer shouldCancelTouchesDeliveredToContextId:withInitialTouchTimestamp:];
```
