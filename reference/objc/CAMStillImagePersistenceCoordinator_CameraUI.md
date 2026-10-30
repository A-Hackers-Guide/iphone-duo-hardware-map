# `CAMStillImagePersistenceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<CAMStillImagePersistenceCoordinatorDelegate>" _delegate;
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
@property (T@"<CAMStillImagePersistenceCoordinatorDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_loggingIdentifier) loggingIdentifier;
@property (TB,R,N) hasReceivedAllExpectedResponses;
```

## Instance methods

```
-[CAMStillImagePersistenceCoordinator loggingIdentifier];
-[CAMStillImagePersistenceCoordinator _loggingPrefix];
-[CAMStillImagePersistenceCoordinator delegate];
-[CAMStillImagePersistenceCoordinator _pendingLocalPersistenceResults];
-[CAMStillImagePersistenceCoordinator hasReceivedAllExpectedResponses];
-[CAMStillImagePersistenceCoordinator _debugStringForUnreceivedResultSpecifiersFromExpectedResultSpecifiers:receivedCoordinationInfos:];
-[CAMStillImagePersistenceCoordinator _dispatchRemotePersistenceIfPossibleForPairWithOriginalResultSpecifiers:processedResultSpecifiers:request:shouldPersistAsSingleAsset:];
-[CAMStillImagePersistenceCoordinator _dispatchRemotePersistenceIfPossibleForResultSpecifiers:request:];
-[CAMStillImagePersistenceCoordinator _powerAssertionReasonForResultSpecifiers:];
-[CAMStillImagePersistenceCoordinator _receivedCoordinationInfos];
-[CAMStillImagePersistenceCoordinator initWithDelegate:loggingIdentifier:];
-[CAMStillImagePersistenceCoordinator updateForCoordinationInfo:localPersistenceResult:request:];
-[CAMStillImagePersistenceCoordinator updateForTimeoutTimerFiredForCoordinationInfo:request:];
```
