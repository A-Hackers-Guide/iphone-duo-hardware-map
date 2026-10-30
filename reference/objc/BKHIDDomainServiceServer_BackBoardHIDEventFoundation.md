# `BKHIDDomainServiceServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_BKHIDDomainIncomingServiceConnectionHandler`, `BSInvalidatable`
- 12 instance variables, 4 properties, 13 instance methods, 12 class methods

## Instance variables

```
@"BSServiceConnectionListener" _connectionListener;
@"<BKHIDDomainServiceDelegate>" _delegate;
@"<BKHIDDomainIncomingServiceConnectionHandler>" _incomingConnectionHandler;
@"BSServiceInterface" _interface;
@ _serviceTarget;
@"BSServiceDispatchQueue" _queue;
@"NSObject<OS_os_log>" _log;
@"NSString" _entitlement;
@"NSString" _serviceName;
@"BSMutableIntegerMap" _lock_activeConnectionsByPID;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSAtomicSignal" _invalidSignal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDDomainServiceServer _currentHIDEventDeliveryManager];
+[BKHIDDomainServiceServer _currentClientEnvironmentObjectForKey:];
+[BKHIDDomainServiceServer _currentDirectTouchEventProcessor];
+[BKHIDDomainServiceServer _currentDisplayRenderSpace];
+[BKHIDDomainServiceServer _currentHIDEventDeliveryObserverService];
+[BKHIDDomainServiceServer _currentTouchDeliveryObservationManager];
+[BKHIDDomainServiceServer _setCurrentClientEnvironmentObject:forKey:];
+[BKHIDDomainServiceServer _setCurrentDirectTouchEventProcessor:];
+[BKHIDDomainServiceServer _setCurrentDisplayRenderSpace:];
+[BKHIDDomainServiceServer _setCurrentHIDEventDeliveryManager:];
+[BKHIDDomainServiceServer _setCurrentHIDEventDeliveryObserverService:];
+[BKHIDDomainServiceServer _setCurrentTouchDeliveryObservationManager:];
```

## Instance methods

```
-[BKHIDDomainServiceServer invalidate];
-[BKHIDDomainServiceServer currentConnection];
-[BKHIDDomainServiceServer activate];
-[BKHIDDomainServiceServer initWithDelegate:incomingServiceConnectionHandler:serverTarget:serverProtocol:clientProtocol:serviceName:queue:log:entitlement:];
-[BKHIDDomainServiceServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKHIDDomainServiceServer connectionForPID:];
-[BKHIDDomainServiceServer didRespondBlockForConnection:];
-[BKHIDDomainServiceServer enumerateUserInfoWithBlock:];
-[BKHIDDomainServiceServer rejectIncomingServiceConnection:];
-[BKHIDDomainServiceServer remoteTargetForServiceConnection:];
-[BKHIDDomainServiceServer responsePendingForConnection:];
-[BKHIDDomainServiceServer setUserInfo:forConnection:];
-[BKHIDDomainServiceServer userInfoForConnection:];
```
