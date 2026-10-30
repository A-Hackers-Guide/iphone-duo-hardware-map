# `SBContinuousFoldSnapshotCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBDisplayContentModeTransitionObserver`, `SBWindowSceneAttachmentObserving`
- 13 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBDeviceContinuousFoldInteractionSettings" _settings;
@"NSHashTable" _providers;
@"NSMapTable" _overlayWindowsByScene;
@"NSMapTable" _cloakContentsViewsByScene;
@"NSMapTable" _zStackParticipantsByScene;
@"SBSecureWindow" _containerWindow;
@"SBSecureWindow" _cloakWindow;
@"UIView" _containerContentsView;
@"UIView" _cloakContentsView;
@"SBContinuousFoldSnapshotConfiguration" _configuration;
@"NSMutableArray" _pendingCloakRevealCompletions;
B _cloakIsRevealing;
```

## Properties

```
@property (TB,R,N) hasStandingCoverForTesting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuousFoldSnapshotCoordinator zStackParticipant:updatePreferences:];
-[SBContinuousFoldSnapshotCoordinator initWithDisplayContentModeCoordinator:];
-[SBContinuousFoldSnapshotCoordinator windowSceneDidDisconnect:];
-[SBContinuousFoldSnapshotCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBContinuousFoldSnapshotCoordinator dealloc];
-[SBContinuousFoldSnapshotCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBContinuousFoldSnapshotCoordinator zStackParticipantDidChange:];
-[SBContinuousFoldSnapshotCoordinator removeProvider:];
-[SBContinuousFoldSnapshotCoordinator zStackParticipant:updateZOrderPreferences:];
-[SBContinuousFoldSnapshotCoordinator addProvider:];
-[SBContinuousFoldSnapshotCoordinator windowSceneDidConnect:];
-[SBContinuousFoldSnapshotCoordinator isCloakInstalledForWindowScene:];
-[SBContinuousFoldSnapshotCoordinator _activationPolicyForParticipantsBelowWithSnapshotInstalled:cloakInstalled:cloakIsRevealing:];
-[SBContinuousFoldSnapshotCoordinator _arrivingWindowSceneToCloakForFadeWithContext:];
-[SBContinuousFoldSnapshotCoordinator _captureDepartingDisplayIfClaimed:context:continuationLockProvider:];
-[SBContinuousFoldSnapshotCoordinator _dropOverlaysAtTransitionEndIfClaimed:completion:];
-[SBContinuousFoldSnapshotCoordinator _fadesSnapshotOutAtPostflightOfTransitionInPhase:];
-[SBContinuousFoldSnapshotCoordinator _liftCloakAtDidChangeIfClaimed:continuationLockProvider:];
-[SBContinuousFoldSnapshotCoordinator _liftCloakIfNeededForReason:mode:completion:];
-[SBContinuousFoldSnapshotCoordinator anyProviderPrefersContinuousSnapshotForWindowScenes:];
-[SBContinuousFoldSnapshotCoordinator hasStandingCoverForTesting];
```
