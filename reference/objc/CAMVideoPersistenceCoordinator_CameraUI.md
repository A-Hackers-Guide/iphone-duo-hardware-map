# `CAMVideoPersistenceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<CAMVideoPersistenceCoordinationDelegate>" _delegate;
@"NSString" _loggingIdentifier;
@"NSMutableDictionary" __receivedCoordinationInfos;
@"NSMutableDictionary" __pendingLocalPersistenceResults;
@"NSString" __loggingPrefix;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__receivedCoordinationInfos) _receivedCoordinationInfos;
@property (T@"NSMutableDictionary",R,N,V__pendingLocalPersistenceResults) _pendingLocalPersistenceResults;
@property (T@"NSString",R,N,V__loggingPrefix) _loggingPrefix;
@property (T@"<CAMVideoPersistenceCoordinationDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_loggingIdentifier) loggingIdentifier;
@property (TB,R,N) hasReceivedAllExpectedResponses;
```

## Instance methods

```
-[CAMVideoPersistenceCoordinator loggingIdentifier];
-[CAMVideoPersistenceCoordinator _loggingPrefix];
-[CAMVideoPersistenceCoordinator delegate];
-[CAMVideoPersistenceCoordinator _pendingLocalPersistenceResults];
-[CAMVideoPersistenceCoordinator hasReceivedAllExpectedResponses];
-[CAMVideoPersistenceCoordinator _debugStringForUnreceivedResultSpecifiersFromExpectedResultSpecifiers:receivedCoordinationInfos:];
-[CAMVideoPersistenceCoordinator _dispatchRemotePersistenceIfPossibleForResultSpecifiers:request:];
-[CAMVideoPersistenceCoordinator _powerAssertionReasonForResultSpecifiers:];
-[CAMVideoPersistenceCoordinator _receivedCoordinationInfos];
-[CAMVideoPersistenceCoordinator initWithDelegate:loggingIdentifier:];
-[CAMVideoPersistenceCoordinator updateForCoordinationInfo:localPersistenceResult:request:];
-[CAMVideoPersistenceCoordinator updateForTimeoutTimerFiredForCoordinationInfo:request:];
```
