# `UIApplicationSceneSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 38 properties, 39 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) persistenceIdentifier;
@property (TB,R,N) underLock;
@property (TQ,R,N) statusBarStyleOverridesToSuppress;
@property (TQ,R,N) deactivationReasons;
@property (Tq,R,N) userInterfaceStyle;
@property (T@"NSNumber",R,N) forcedStatusBarStyle;
@property (TB,R,N) forcedStatusBarForegroundTransparent;
@property (TB,R,N) deviceOrientationEventsEnabled;
@property (TB,R,N) canShowAlerts;
@property (TB,R,N) idleModeEnabled;
@property (TB,R,N) statusBarDisabled;
@property (T{UIEdgeInsets=dddd},R,N) peripheryInsets;
@property (Tq,R,N) statusBarParts;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) statusBarAvoidanceFrame;
@property (Td,R,N) statusBarHeight;
@property (Td,R,N) systemMinimumMargin;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsPortrait;
@property (Td,R,N) homeAffordanceOverlayAllowance;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsLandscapeLeft;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsPortraitUpsideDown;
@property (T{UIEdgeInsets=dddd},R,N) safeAreaInsetsLandscapeRight;
@property (Tq,R,N) deviceOrientation;
@property (TQ,R,N) artworkSubtype;
@property (T@"BSCornerRadiusConfiguration",R,N) cornerRadiusConfiguration;
@property (TI,R,N) hostContextIdentifierForSnapshotting;
@property (TQ,R,N) scenePresenterRenderIdentifierForSnapshotting;
@property (Tq,R,N) accessibilityContrast;
@property (Tq,R,N) pointerLockStatus;
@property (Tq,R,N) interfaceOrientationMode;
@property (T@"<BSInterfaceOrientationMapResolving><BSXPCSecureCoding>",R,N) interfaceOrientationMapResolver;
@property (TB,R,N) screenBoundsIgnoresSceneOrientation;
@property (Tq,R,N) screenReferenceDisplayModeStatus;
@property (TB,R,N) enhancedWindowingEnabled;
@property (TQ,R,N) hostReferenceAngleMode;
@property (Td,R,N) angleFromHostReferenceUprightDirection;
@property (T@"NSSet",R,N) targetOfEventDeferringEnvironments;
@property (TB,R,N) inLiveResize;
@property (TB,R,N) isCapturingContentForAdditionalRenderingDestination;
```

## Instance methods

```
-[UIApplicationSceneSettings statusBarHeight];
-[UIApplicationSceneSettings peripheryInsets];
-[UIApplicationSceneSettings deviceOrientation];
-[UIApplicationSceneSettings statusBarAvoidanceFrame];
-[UIApplicationSceneSettings cornerRadiusConfiguration];
-[UIApplicationSceneSettings hostReferenceAngleMode];
-[UIApplicationSceneSettings accessibilityContrast];
-[UIApplicationSceneSettings inLiveResize];
-[UIApplicationSceneSettings userInterfaceStyle];
-[UIApplicationSceneSettings defaultStatusBarHeightForOrientation:];
-[UIApplicationSceneSettings statusBarParts];
-[UIApplicationSceneSettings persistenceIdentifier];
-[UIApplicationSceneSettings isCapturingContentForAdditionalRenderingDestination];
-[UIApplicationSceneSettings deactivationReasons];
-[UIApplicationSceneSettings idleModeEnabled];
-[UIApplicationSceneSettings interfaceOrientationMapResolver];
-[UIApplicationSceneSettings angleFromHostReferenceUprightDirection];
-[UIApplicationSceneSettings artworkSubtype];
-[UIApplicationSceneSettings canShowAlerts];
-[UIApplicationSceneSettings deviceOrientationEventsEnabled];
-[UIApplicationSceneSettings enhancedWindowingEnabled];
-[UIApplicationSceneSettings forcedStatusBarForegroundTransparent];
-[UIApplicationSceneSettings forcedStatusBarStyle];
-[UIApplicationSceneSettings homeAffordanceOverlayAllowance];
-[UIApplicationSceneSettings hostContextIdentifierForSnapshotting];
-[UIApplicationSceneSettings interfaceOrientationMode];
-[UIApplicationSceneSettings pointerLockStatus];
-[UIApplicationSceneSettings safeAreaInsetsLandscapeLeft];
-[UIApplicationSceneSettings safeAreaInsetsLandscapeRight];
-[UIApplicationSceneSettings safeAreaInsetsPortrait];
-[UIApplicationSceneSettings safeAreaInsetsPortraitUpsideDown];
-[UIApplicationSceneSettings scenePresenterRenderIdentifierForSnapshotting];
-[UIApplicationSceneSettings screenBoundsIgnoresSceneOrientation];
-[UIApplicationSceneSettings screenReferenceDisplayModeStatus];
-[UIApplicationSceneSettings statusBarDisabled];
-[UIApplicationSceneSettings statusBarStyleOverridesToSuppress];
-[UIApplicationSceneSettings systemMinimumMargin];
-[UIApplicationSceneSettings targetOfEventDeferringEnvironments];
-[UIApplicationSceneSettings underLock];
```
