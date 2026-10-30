# `BKTouchStreamServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDTouchStreamServerInterface`, `BKHIDDomainServiceDelegate`, `BKHIDDomainIncomingServiceConnectionHandler`, `_BKHIDIncomingServiceConnectionHandler`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
@"<BKTouchStreamIncomingServiceConnectionHandler>" _incomingServiceConnectionHandler;
@? _clientEntitlementExemptionValidator;
```

## Properties

```
@property (T@?,C,N,V_clientEntitlementExemptionValidator) clientEntitlementExemptionValidator;
@property (T@"<BKTouchStreamIncomingServiceConnectionHandler>",R,N) incomingConnectionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchStreamServer connectionDidTerminate:];
-[BKTouchStreamServer activate];
-[BKTouchStreamServer newTouchStreamForContextID:displayUUID:identifier:shouldSendAmbiguityRecommendations:];
-[BKTouchStreamServer updateDispatchMode:ambiguityRecommendation:timestamp:];
-[BKTouchStreamServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKTouchStreamServer handleIncomingServiceConnection:];
-[BKTouchStreamServer incomingConnectionHandler];
-[BKTouchStreamServer initWithIncomingServiceConnectionHandler:];
-[BKTouchStreamServer rejectIncomingServiceConnection:];
-[BKTouchStreamServer clientEntitlementExemptionValidator];
-[BKTouchStreamServer setClientEntitlementExemptionValidator:];
```
