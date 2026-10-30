# `UIMutableApplicationSceneSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSMutableSceneSettings`
- Protocols: `UIApplicationSceneSettings`
- 0 instance variables, 42 properties, 82 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",&,N) persistenceIdentifier;
@property (TB,N) underLock;
@property (TQ,N) statusBarStyleOverridesToSuppress;
@property (TQ,N) deactivationReasons;
@property (Tq,N) userInterfaceStyle;
@property (T@"NSNumber",&,N) forcedStatusBarStyle;
@property (TB,N) forcedStatusBarForegroundTransparent;
@property (TB,N) deviceOrientationEventsEnabled;
@property (TB,N) canShowAlerts;
@property (TB,N) idleModeEnabled;
@property (TB,N) statusBarDisabled;
@property (T{UIEdgeInsets=dddd},N) peripheryInsets;
@property (Tq,N) statusBarParts;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) statusBarAvoidanceFrame;
@property (Td,N) statusBarHeight;
@property (Td,N) systemMinimumMargin;
@property (T{UIEdgeInsets=dddd},N) safeAreaInsetsPortrait;
@property (Td,N) homeAffordanceOverlayAllowance;
@property (T{UIEdgeInsets=dddd},N) safeAreaInsetsLandscapeLeft;
@property (T{UIEdgeInsets=dddd},N) safeAreaInsetsPortraitUpsideDown;
@property (T{UIEdgeInsets=dddd},N) safeAreaInsetsLandscapeRight;
@property (Tq,N) deviceOrientation;
@property (TQ,N) artworkSubtype;
@property (T@"BSCornerRadiusConfiguration",&,N) cornerRadiusConfiguration;
@property (TI,N) hostContextIdentifierForSnapshotting;
@property (TQ,N) scenePresenterRenderIdentifierForSnapshotting;
@property (Tq,N) accessibilityContrast;
@property (Tq,N) pointerLockStatus;
@property (Tq,N) interfaceOrientationMode;
@property (T@"<BSInterfaceOrientationMapResolving><BSXPCSecureCoding>",&,N) interfaceOrientationMapResolver;
@property (TB,N) screenBoundsIgnoresSceneOrientation;
@property (Tq,N) screenReferenceDisplayModeStatus;
@property (TB,N) enhancedWindowingEnabled;
@property (TQ,N) hostReferenceAngleMode;
@property (Td,N) angleFromHostReferenceUprightDirection;
@property (T@"NSSet",&,N) targetOfEventDeferringEnvironments;
@property (TB,N) inLiveResize;
@property (TB,N) isCapturingContentForAdditionalRenderingDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMutableApplicationSceneSettings statusBarHeight];
-[UIMutableApplicationSceneSettings setDeviceOrientation:];
-[UIMutableApplicationSceneSettings peripheryInsets];
-[UIMutableApplicationSceneSettings deviceOrientation];
-[UIMutableApplicationSceneSettings statusBarAvoidanceFrame];
-[UIMutableApplicationSceneSettings setStatusBarAvoidanceFrame:];
-[UIMutableApplicationSceneSettings cornerRadiusConfiguration];
-[UIMutableApplicationSceneSettings hostReferenceAngleMode];
-[UIMutableApplicationSceneSettings accessibilityContrast];
-[UIMutableApplicationSceneSettings inLiveResize];
-[UIMutableApplicationSceneSettings setStatusBarHeight:];
-[UIMutableApplicationSceneSettings setCornerRadiusConfiguration:];
-[UIMutableApplicationSceneSettings valueDescriptionForFlag:object:ofSetting:];
-[UIMutableApplicationSceneSettings setAccessibilityContrast:];
-[UIMutableApplicationSceneSettings keyDescriptionForSetting:];
-[UIMutableApplicationSceneSettings setIsCapturingContentForAdditionalRenderingDestination:];
-[UIMutableApplicationSceneSettings userInterfaceStyle];
-[UIMutableApplicationSceneSettings setUserInterfaceStyle:];
-[UIMutableApplicationSceneSettings setPersistenceIdentifier:];
-[UIMutableApplicationSceneSettings defaultStatusBarHeightForOrientation:];
-[UIMutableApplicationSceneSettings setInLiveResize:];
-[UIMutableApplicationSceneSettings statusBarParts];
-[UIMutableApplicationSceneSettings setDeactivationReasons:];
-[UIMutableApplicationSceneSettings setStatusBarParts:];
-[UIMutableApplicationSceneSettings persistenceIdentifier];
-[UIMutableApplicationSceneSettings copyWithZone:];
-[UIMutableApplicationSceneSettings isCapturingContentForAdditionalRenderingDestination];
-[UIMutableApplicationSceneSettings deactivationReasons];
-[UIMutableApplicationSceneSettings idleModeEnabled];
-[UIMutableApplicationSceneSettings interfaceOrientationMapResolver];
-[UIMutableApplicationSceneSettings setSafeAreaInsetsLandscapeLeft:];
-[UIMutableApplicationSceneSettings angleFromHostReferenceUprightDirection];
-[UIMutableApplicationSceneSettings artworkSubtype];
-[UIMutableApplicationSceneSettings canShowAlerts];
-[UIMutableApplicationSceneSettings deviceOrientationEventsEnabled];
-[UIMutableApplicationSceneSettings enhancedWindowingEnabled];
-[UIMutableApplicationSceneSettings forcedStatusBarForegroundTransparent];
-[UIMutableApplicationSceneSettings forcedStatusBarStyle];
-[UIMutableApplicationSceneSettings homeAffordanceOverlayAllowance];
-[UIMutableApplicationSceneSettings hostContextIdentifierForSnapshotting];
-[UIMutableApplicationSceneSettings interfaceOrientationMode];
-[UIMutableApplicationSceneSettings isUISubclass];
-[UIMutableApplicationSceneSettings pointerLockStatus];
-[UIMutableApplicationSceneSettings safeAreaInsetsLandscapeLeft];
-[UIMutableApplicationSceneSettings safeAreaInsetsLandscapeRight];
-[UIMutableApplicationSceneSettings safeAreaInsetsPortrait];
-[UIMutableApplicationSceneSettings safeAreaInsetsPortraitUpsideDown];
-[UIMutableApplicationSceneSettings scenePresenterRenderIdentifierForSnapshotting];
-[UIMutableApplicationSceneSettings screenBoundsIgnoresSceneOrientation];
-[UIMutableApplicationSceneSettings screenReferenceDisplayModeStatus];
-[UIMutableApplicationSceneSettings setAngleFromHostReferenceUprightDirection:];
-[UIMutableApplicationSceneSettings setArtworkSubtype:];
-[UIMutableApplicationSceneSettings setCanShowAlerts:];
-[UIMutableApplicationSceneSettings setDefaultStatusBarHeight:forOrientation:];
-[UIMutableApplicationSceneSettings setDeviceOrientationEventsEnabled:];
-[UIMutableApplicationSceneSettings setEnhancedWindowingEnabled:];
-[UIMutableApplicationSceneSettings setForcedStatusBarForegroundTransparent:];
-[UIMutableApplicationSceneSettings setForcedStatusBarStyle:];
-[UIMutableApplicationSceneSettings setHomeAffordanceOverlayAllowance:];
-[UIMutableApplicationSceneSettings setHostContextIdentifierForSnapshotting:];
-[UIMutableApplicationSceneSettings setHostReferenceAngleMode:];
-[UIMutableApplicationSceneSettings setIdleModeEnabled:];
-[UIMutableApplicationSceneSettings setInterfaceOrientationMapResolver:];
-[UIMutableApplicationSceneSettings setInterfaceOrientationMode:];
-[UIMutableApplicationSceneSettings setPeripheryInsets:];
-[UIMutableApplicationSceneSettings setPointerLockStatus:];
-[UIMutableApplicationSceneSettings setSafeAreaInsetsLandscapeRight:];
-[UIMutableApplicationSceneSettings setSafeAreaInsetsPortrait:];
-[UIMutableApplicationSceneSettings setSafeAreaInsetsPortraitUpsideDown:];
-[UIMutableApplicationSceneSettings setScenePresenterRenderIdentifierForSnapshotting:];
-[UIMutableApplicationSceneSettings setScreenBoundsIgnoresSceneOrientation:];
-[UIMutableApplicationSceneSettings setScreenReferenceDisplayModeStatus:];
-[UIMutableApplicationSceneSettings setStatusBarDisabled:];
-[UIMutableApplicationSceneSettings setStatusBarStyleOverridesToSuppress:];
-[UIMutableApplicationSceneSettings setSystemMinimumMargin:];
-[UIMutableApplicationSceneSettings setTargetOfEventDeferringEnvironments:];
-[UIMutableApplicationSceneSettings setUnderLock:];
-[UIMutableApplicationSceneSettings statusBarDisabled];
-[UIMutableApplicationSceneSettings statusBarStyleOverridesToSuppress];
-[UIMutableApplicationSceneSettings systemMinimumMargin];
-[UIMutableApplicationSceneSettings targetOfEventDeferringEnvironments];
-[UIMutableApplicationSceneSettings underLock];
```
