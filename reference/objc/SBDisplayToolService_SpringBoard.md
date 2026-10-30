# `SBDisplayToolService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSDisplayToolServiceServerInterface`
- 6 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBFDevicePoseProvider" _devicePoseProvider;
@"SBDisplayToolServiceCoordinator" _swapCoordinator;
@"BSServiceConnectionListener" _listener;
@"NSMutableSet" _connections;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayToolService listener:didReceiveConnection:withContext:];
-[SBDisplayToolService unlockForTestingWithCompletion:];
-[SBDisplayToolService awaitSystemSpaceWithOptions:completion:];
-[SBDisplayToolService disableYoinkingFlipOverrideWithCompletion:];
-[SBDisplayToolService enableYoinkingFlipOverrideForDuration:completion:];
-[SBDisplayToolService lockForTestingWithCompletion:];
-[SBDisplayToolService replayHingeSamplesWithOptions:path:completion:];
-[SBDisplayToolService setBacklightState:displayUUID:completion:];
-[SBDisplayToolService setDynamicMarkPersistence:completion:];
-[SBDisplayToolService setPrimary:displayUUID:completion:];
-[SBDisplayToolService swapDisplayWithOptions:completion:];
-[SBDisplayToolService _sbWindowSceneForDisplayUUID:];
-[SBDisplayToolService initWithWindowSceneManager:displayContentModeCoordinator:devicePoseProvider:displayYoinkingCoordinator:];
```
