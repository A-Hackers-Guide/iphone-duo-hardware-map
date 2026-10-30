# `SBDisplayContentModeCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDevicePoseProviderObserver`, `SBFDevicePoseLikelyTransitionDelegate`, `SBFDisplayContentModeResolverDelegate`, `SBWindowSceneAttachmentObserving`
- 16 instance variables, 8 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _connectedWindowScenes;
@"SBFDisplayContentModeResolver" _resolver;
@"SBFDevicePoseProvider" _devicePoseProvider;
@"SBDeviceContinuousFoldInteractionSettings" _continuousFoldSettings;
@"NSUserDefaults" _springBoardDefaults;
@"NSMapTable" _observersToProxies;
@"NSMapTable" _windowScenesToContexts;
@"NSMutableArray" _preventBacklightActivationAssertions;
@"SBContinuousFoldSnapshotCoordinator" _continuousFoldSnapshotCoordinator;
d _lastHingeMotionIdleTimerResetTime;
d _lastInteractiveProgressIdleTimerResetTime;
@"NSMutableDictionary" _prewarmAssertionsBySurfaceType;
@"NSMutableDictionary" _prewarmAttemptsBySurfaceType;
d _prewarmStartTime;
@"SBWindowScene" _activeWindowScene;
@"SBDisplayUpdateLinkSourceProvider" _updateLinkProvider;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_activeWindowScene) activeWindowScene;
@property (T@"SBDisplayUpdateLinkSourceProvider",R,N,V_updateLinkProvider) updateLinkProvider;
@property (T@"SBFDisplayContentModeTransitionContext",R,N) currentTransitionContext;
@property (T@"SBWindowScene",R,N) primaryWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayContentModeCoordinator primaryWindowScene];
-[SBDisplayContentModeCoordinator removeTransitionObserver:];
-[SBDisplayContentModeCoordinator activeWindowScene];
-[SBDisplayContentModeCoordinator addTransitionObserver:];
-[SBDisplayContentModeCoordinator windowSceneDidDisconnect:];
-[SBDisplayContentModeCoordinator dealloc];
-[SBDisplayContentModeCoordinator setActiveWindowScene:];
-[SBDisplayContentModeCoordinator poseProvider:didUpdateFromPose:toPose:];
-[SBDisplayContentModeCoordinator windowSceneDidConnect:];
-[SBDisplayContentModeCoordinator acquireForceCoverDisplayOnlyEnabledAssertionWithReason:];
-[SBDisplayContentModeCoordinator acquireForcePrimaryContentAssertionForWindowScene:reason:invalidationHandler:];
-[SBDisplayContentModeCoordinator acquireYoinkActivationAssertionForWindowScene:reason:invalidationHandler:];
-[SBDisplayContentModeCoordinator currentTransitionContext];
-[SBDisplayContentModeCoordinator initWithDevicePoseProvider:];
-[SBDisplayContentModeCoordinator isAppliedDisplayContentModeUserInitiatedForWindowScene:];
-[SBDisplayContentModeCoordinator performDisplayContentModeTransitionWithCoordinator:];
-[SBDisplayContentModeCoordinator poseProvider:transitionIsLikelyFromHingeState:mechanicalAngleDegrees:velocityDegreesPerSecond:];
-[SBDisplayContentModeCoordinator preferredTransitionStyleForDisplayContentModeResolver:];
-[SBDisplayContentModeCoordinator _proxyForObserver:createIfMissing:];
-[SBDisplayContentModeCoordinator _turnOnDisplayForWindowScene:];
-[SBDisplayContentModeCoordinator addContinuousSnapshotProvider:];
-[SBDisplayContentModeCoordinator addTransitionObserver:forWindowScene:];
-[SBDisplayContentModeCoordinator attemptToYoinkToAuxiliaryContentDisplayWithReason:];
-[SBDisplayContentModeCoordinator displayContentModeContextForWindowScene:];
-[SBDisplayContentModeCoordinator displayContentModeForWindowScene:];
-[SBDisplayContentModeCoordinator isContinuousFoldCloakInstalledForWindowScene:];
-[SBDisplayContentModeCoordinator removeContinuousSnapshotProvider:];
-[SBDisplayContentModeCoordinator removeTransitionObserver:forWindowScene:];
-[SBDisplayContentModeCoordinator updateLinkProvider];
-[SBDisplayContentModeCoordinator windowScenesWithDisplayContentMode:];
```
