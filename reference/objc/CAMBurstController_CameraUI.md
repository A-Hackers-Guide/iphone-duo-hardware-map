# `CAMBurstController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 15 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<CAMBurstDelegate>" _burstDelegate;
@"NSObject<OS_dispatch_queue>" __mutexQueue;
@"NSMutableDictionary" __sessionsByIdentifier;
@"NSMutableDictionary" __analyticsEventsIdByIdentifier;
@"NSCountedSet" __inflightRequestsByIdentifier;
@"NSCountedSet" __requestsPendingPersistenceByIdentifier;
@"NSMutableDictionary" __faceResultsByIdentifier;
@"CAMBurstSession" __activeSession;
@"NSObject<OS_dispatch_queue>" __analysisQueue;
@"CAMPersistenceController" __persistenceController;
@"CAMProtectionController" __protectionController;
@"CAMPowerController" __powerController;
@"CAMRemoteShutterController" __remoteShutterController;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__mutexQueue) _mutexQueue;
@property (T@"NSMutableDictionary",R,N,V__sessionsByIdentifier) _sessionsByIdentifier;
@property (T@"NSMutableDictionary",R,N,V__analyticsEventsIdByIdentifier) _analyticsEventsIdByIdentifier;
@property (T@"NSCountedSet",R,N,V__inflightRequestsByIdentifier) _inflightRequestsByIdentifier;
@property (T@"NSCountedSet",R,N,V__requestsPendingPersistenceByIdentifier) _requestsPendingPersistenceByIdentifier;
@property (T@"NSMutableDictionary",R,N,V__faceResultsByIdentifier) _faceResultsByIdentifier;
@property (T@"CAMBurstSession",&,N,S_setActiveSession:,V__activeSession) _activeSession;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__analysisQueue) _analysisQueue;
@property (T@"CAMPersistenceController",R,W,N,V__persistenceController) _persistenceController;
@property (T@"CAMProtectionController",R,N,V__protectionController) _protectionController;
@property (T@"CAMPowerController",R,N,V__powerController) _powerController;
@property (T@"CAMRemoteShutterController",R,N,V__remoteShutterController) _remoteShutterController;
@property (T@"NSString",R,C,N) currentBurstIdentifier;
@property (TQ,R,N) currentBurstCount;
@property (T@"<CAMBurstDelegate>",W,N,V_burstDelegate) burstDelegate;
```

## Instance methods

```
-[CAMBurstController _remoteShutterController];
-[CAMBurstController _powerController];
-[CAMBurstController init];
-[CAMBurstController _persistenceController];
-[CAMBurstController burstDelegate];
-[CAMBurstController currentBurstCount];
-[CAMBurstController _protectionController];
-[CAMBurstController setBurstDelegate:];
-[CAMBurstController _activeSession];
-[CAMBurstController setPersistenceController:];
-[CAMBurstController _analysisQueue];
-[CAMBurstController _analyticsEventsIdByIdentifier];
-[CAMBurstController _faceResultsByIdentifier];
-[CAMBurstController _inflightRequestsByIdentifier];
-[CAMBurstController _mutexQueue];
-[CAMBurstController _mutexQueueProcessCompleteBurstSessionWithIdentifier:device:];
-[CAMBurstController _requestsPendingPersistenceByIdentifier];
-[CAMBurstController _sessionsByIdentifier];
-[CAMBurstController _setActiveSession:];
-[CAMBurstController cancelBurstCapture];
-[CAMBurstController currentBurstIdentifier];
-[CAMBurstController estimatedCountForIdentifier:];
-[CAMBurstController finishBurstCaptureForDevice:];
-[CAMBurstController inflightCountForIdentifier:];
-[CAMBurstController initWithProtectionController:powerController:remoteShutterController:];
-[CAMBurstController processCapturedRequest:withResult:];
-[CAMBurstController processEnqueuedRequest:];
-[CAMBurstController processFaceResults:];
-[CAMBurstController processPersistedRequest:withResult:];
-[CAMBurstController startBurstCaptureWithPersistenceUUID:];
```
