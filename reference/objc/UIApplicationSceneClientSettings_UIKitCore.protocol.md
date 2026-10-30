# `UIApplicationSceneClientSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 51 properties, 51 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) statusBarStyle;
@property (Tq,R,N) statusBarModernStyle;
@property (T@"NSDictionary",R,C,N) statusBarPartStyles;
@property (TB,R,N) statusBarHidden;
@property (TB,R,N) prefersStatusBarHidden;
@property (Tq,R,N) statusBarAxis;
@property (Td,R,N) statusBarAlpha;
@property (TB,R,N,GisStatusBarForegroundTransparent) statusBarForegroundTransparent;
@property (TI,R,N) statusBarContextID;
@property (Tq,R,N) defaultStatusBarStyle;
@property (TB,R,N) defaultStatusBarHidden;
@property (Tq,R,N) userInterfaceStyle;
@property (T@"NSString",R,C,N) defaultPNGName;
@property (Td,R,N) defaultPNGExpirationTime;
@property (Tq,R,N) compatibilityMode;
@property (TB,R,N) deviceOrientationEventsEnabled;
@property (TB,R,N) interfaceOrientationChangesDisabled;
@property (Tq,R,N) interfaceOrientation;
@property (TQ,R,N) supportedInterfaceOrientations;
@property (TB,R,N) idleTimerDisabled;
@property (TQ,R,N) proximityDetectionModes;
@property (Td,R,N) controlCenterAmbiguousActivationMargin;
@property (Tq,R,N) controlCenterRevealMode;
@property (Tq,R,N) notificationCenterRevealMode;
@property (Tq,R,N) editingInteractionConfiguration;
@property (T{UIEdgeInsets=dddd},R,N) primaryWindowOverlayInsets;
@property (Tq,R,N) backgroundStyle;
@property (TB,R,N) idleModeVisualEffectsEnabled;
@property (Tq,R,N) whitePointAdaptivityStyle;
@property (T@"FBSDisplayMode",R,C,N) requestedDisplayMode;
@property (T@"FBSDisplayConfigurationRequest",R,C,N) displayConfigurationRequest;
@property (TB,R,N,GisReachabilitySupported) reachabilitySupported;
@property (TQ,R,N) screenEdgesDeferringSystemGestures;
@property (TB,R,N) homeIndicatorAutoHidden;
@property (TB,R,N) wantsExclusiveForeground;
@property (TQ,R,N) visibleMiniAlertCount;
@property (T@"NSArray",R,N) audioCategoriesDisablingVolumeHUD;
@property (Td,R,N) brightnessLevel;
@property (TB,R,N) disablesMirroring;
@property (T@"NSString",R,C,N) sceneTitle;
@property (T@"NSString",R,C,N) canvasTitle;
@property (T@"NSData",R,N) activationConditionsData;
@property (Tq,R,N) sceneActivationBias;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) screenFocusedFrame;
@property (Tq,R,N) preferredPointerLockStatus;
@property (T@"_UIPhysicalButtonConfigurationSet",R,C,N) physicalButtonConfigurations;
@property (T@"NSArray",R,N) multitaskingDragExclusionRects;
@property (Tq,R,N) playbackControlsState;
@property (TB,R,N) containsSearchView;
@property (TB,R,N) discardSessionOnUserDisconnect;
@property (TB,R,N) systemInputActive;
```

## Instance methods

```
-[UIApplicationSceneClientSettings statusBarAlpha];
-[UIApplicationSceneClientSettings interfaceOrientation];
-[UIApplicationSceneClientSettings wantsExclusiveForeground];
-[UIApplicationSceneClientSettings statusBarHidden];
-[UIApplicationSceneClientSettings supportedInterfaceOrientations];
-[UIApplicationSceneClientSettings homeIndicatorAutoHidden];
-[UIApplicationSceneClientSettings multitaskingDragExclusionRects];
-[UIApplicationSceneClientSettings activationConditionsData];
-[UIApplicationSceneClientSettings audioCategoriesDisablingVolumeHUD];
-[UIApplicationSceneClientSettings sceneTitle];
-[UIApplicationSceneClientSettings compatibilityMode];
-[UIApplicationSceneClientSettings idleTimerDisabled];
-[UIApplicationSceneClientSettings userInterfaceStyle];
-[UIApplicationSceneClientSettings backgroundStyle];
-[UIApplicationSceneClientSettings preferredPointerLockStatus];
-[UIApplicationSceneClientSettings screenEdgesDeferringSystemGestures];
-[UIApplicationSceneClientSettings prefersStatusBarHidden];
-[UIApplicationSceneClientSettings statusBarAxis];
-[UIApplicationSceneClientSettings whitePointAdaptivityStyle];
-[UIApplicationSceneClientSettings statusBarStyle];
-[UIApplicationSceneClientSettings defaultStatusBarStyle];
-[UIApplicationSceneClientSettings brightnessLevel];
-[UIApplicationSceneClientSettings editingInteractionConfiguration];
-[UIApplicationSceneClientSettings canvasTitle];
-[UIApplicationSceneClientSettings containsSearchView];
-[UIApplicationSceneClientSettings controlCenterAmbiguousActivationMargin];
-[UIApplicationSceneClientSettings controlCenterRevealMode];
-[UIApplicationSceneClientSettings defaultPNGExpirationTime];
-[UIApplicationSceneClientSettings defaultPNGName];
-[UIApplicationSceneClientSettings defaultStatusBarHidden];
-[UIApplicationSceneClientSettings deviceOrientationEventsEnabled];
-[UIApplicationSceneClientSettings disablesMirroring];
-[UIApplicationSceneClientSettings discardSessionOnUserDisconnect];
-[UIApplicationSceneClientSettings displayConfigurationRequest];
-[UIApplicationSceneClientSettings idleModeVisualEffectsEnabled];
-[UIApplicationSceneClientSettings interfaceOrientationChangesDisabled];
-[UIApplicationSceneClientSettings isReachabilitySupported];
-[UIApplicationSceneClientSettings isStatusBarForegroundTransparent];
-[UIApplicationSceneClientSettings notificationCenterRevealMode];
-[UIApplicationSceneClientSettings physicalButtonConfigurations];
-[UIApplicationSceneClientSettings playbackControlsState];
-[UIApplicationSceneClientSettings primaryWindowOverlayInsets];
-[UIApplicationSceneClientSettings proximityDetectionModes];
-[UIApplicationSceneClientSettings requestedDisplayMode];
-[UIApplicationSceneClientSettings sceneActivationBias];
-[UIApplicationSceneClientSettings screenFocusedFrame];
-[UIApplicationSceneClientSettings statusBarContextID];
-[UIApplicationSceneClientSettings statusBarModernStyle];
-[UIApplicationSceneClientSettings statusBarPartStyles];
-[UIApplicationSceneClientSettings systemInputActive];
-[UIApplicationSceneClientSettings visibleMiniAlertCount];
```
