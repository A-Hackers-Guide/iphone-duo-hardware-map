# `SBDisplayContentModeTransitionStyleCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBFZStackParticipantObserver`, `SBWindowSceneAttachmentObserving`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"NSHashTable" _windowScenes;
B _continuousFoldTransitionEnabled;
@"NSMapTable" _continuousFoldTransitionDisablingAssertions;
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
-[SBDisplayContentModeTransitionStyleCoordinator zStackParticipantWithIdentifier:settingsDidChange:];
-[SBDisplayContentModeTransitionStyleCoordinator initWithDisplayContentModeCoordinator:];
-[SBDisplayContentModeTransitionStyleCoordinator windowSceneDidDisconnect:];
-[SBDisplayContentModeTransitionStyleCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayContentModeTransitionStyleCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayContentModeTransitionStyleCoordinator windowSceneDidConnect:];
-[SBDisplayContentModeTransitionStyleCoordinator _setContinuousFoldTransitionEnabled:forWindowScene:];
-[SBDisplayContentModeTransitionStyleCoordinator _updateTransitionStyleForReason:];
```
