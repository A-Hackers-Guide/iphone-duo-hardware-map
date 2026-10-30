# `BKTouchEventServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDDomainServiceDelegate`, `BKHIDDomainIncomingServiceConnectionHandler`, `_BKHIDIncomingServiceConnectionHandler`, `BKSTouchEventServer_IPC`
- 3 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
@"<BKTouchEventServerClientActionAuthority>" _authority;
@"<BKTouchEventServerIncomingServiceConnectionHandler>" _incomingServiceConnectionHandler;
```

## Properties

```
@property (T@"<BKTouchEventServerIncomingServiceConnectionHandler>",R,N) incomingConnectionHandler;
@property (T@"<BKTouchEventServerClientActionAuthority>",R,W,N) authority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchEventServer connectionDidTerminate:];
-[BKTouchEventServer activate];
-[BKTouchEventServer authority];
-[BKTouchEventServer detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:initialTouchOffset:error:];
-[BKTouchEventServer setContextIDs:forHitTestContextCategory:];
-[BKTouchEventServer setDetachedTouchOffset:userIdentifier:];
-[BKTouchEventServer setDetachedTouchRoutingPolicy:userIdentifier:];
-[BKTouchEventServer setHitTestFilterParameters:];
-[BKTouchEventServer setSceneHostSettings:forContextID:];
-[BKTouchEventServer transform3DForDisplayUUID:layerID:contextID:];
-[BKTouchEventServer acceptIncomingServiceConnection:serviceQueue:clientCalloutContextualizer:];
-[BKTouchEventServer connectionWillBegin:];
-[BKTouchEventServer handleIncomingServiceConnection:];
-[BKTouchEventServer incomingConnectionHandler];
-[BKTouchEventServer rejectIncomingServiceConnection:];
-[BKTouchEventServer initWithIncomingServiceConnectionHandler:clientActionAuthority:];
-[BKTouchEventServer _clientRecordForEstablishedConnection:];
```
