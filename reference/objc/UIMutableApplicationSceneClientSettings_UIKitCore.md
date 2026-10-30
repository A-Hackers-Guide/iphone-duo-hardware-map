# `UIMutableApplicationSceneClientSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSMutableSceneClientSettings`
- Protocols: `UIApplicationSceneClientSettings`
- 3 instance variables, 55 properties, 107 instance methods, 0 class methods

## Instance variables

```
B _statusBarForegroundTransparent;
B _discardSessionOnUserDisconnect;
q _sceneActivationBias;
```

## Properties

```
@property (Tq,N) statusBarStyle;
@property (Tq,N) statusBarModernStyle;
@property (T@"NSDictionary",C,N) statusBarPartStyles;
@property (TB,N) statusBarHidden;
@property (TB,N) prefersStatusBarHidden;
@property (Tq,N) statusBarAxis;
@property (Td,N) statusBarAlpha;
@property (TB,N,GisStatusBarForegroundTransparent,V_statusBarForegroundTransparent) statusBarForegroundTransparent;
@property (TI,N) statusBarContextID;
@property (Tq,N) defaultStatusBarStyle;
@property (TB,N) defaultStatusBarHidden;
@property (Tq,N) userInterfaceStyle;
@property (T@"NSString",C,N) defaultPNGName;
@property (Td,N) defaultPNGExpirationTime;
@property (Tq,N) compatibilityMode;
@property (TB,N) deviceOrientationEventsEnabled;
@property (TB,N) interfaceOrientationChangesDisabled;
@property (Tq,N) interfaceOrientation;
@property (TQ,N) supportedInterfaceOrientations;
@property (TB,N) idleTimerDisabled;
@property (TQ,N) proximityDetectionModes;
@property (Td,N) controlCenterAmbiguousActivationMargin;
@property (Tq,N) controlCenterRevealMode;
@property (Tq,N) notificationCenterRevealMode;
@property (Tq,N) editingInteractionConfiguration;
@property (T{UIEdgeInsets=dddd},N) primaryWindowOverlayInsets;
@property (Tq,N) backgroundStyle;
@property (TB,N) idleModeVisualEffectsEnabled;
@property (Tq,N) whitePointAdaptivityStyle;
@property (T@"FBSDisplayMode",C,N) requestedDisplayMode;
@property (T@"FBSDisplayConfigurationRequest",C,N) displayConfigurationRequest;
@property (TB,N,GisReachabilitySupported) reachabilitySupported;
@property (TQ,N) screenEdgesDeferringSystemGestures;
@property (TB,N) homeIndicatorAutoHidden;
@property (TB,N) wantsExclusiveForeground;
@property (TQ,N) visibleMiniAlertCount;
@property (T@"NSArray",&,N) audioCategoriesDisablingVolumeHUD;
@property (Td,N) brightnessLevel;
@property (TB,N) disablesMirroring;
@property (T@"NSString",C,N) sceneTitle;
@property (T@"NSString",C,N) canvasTitle;
@property (T@"NSData",&,N) activationConditionsData;
@property (Tq,N,V_sceneActivationBias) sceneActivationBias;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) screenFocusedFrame;
@property (Tq,N) preferredPointerLockStatus;
@property (T@"_UIPhysicalButtonConfigurationSet",C,N) physicalButtonConfigurations;
@property (T@"NSArray",&,N) multitaskingDragExclusionRects;
@property (Tq,N) playbackControlsState;
@property (TB,N) containsSearchView;
@property (TB,N,V_discardSessionOnUserDisconnect) discardSessionOnUserDisconnect;
@property (TB,N) systemInputActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMutableApplicationSceneClientSettings statusBarAlpha];
-[UIMutableApplicationSceneClientSettings interfaceOrientation];
-[UIMutableApplicationSceneClientSettings setStatusBarAxis:];
-[UIMutableApplicationSceneClientSettings wantsExclusiveForeground];
-[UIMutableApplicationSceneClientSettings setCompatibilityMode:];
-[UIMutableApplicationSceneClientSettings statusBarHidden];
-[UIMutableApplicationSceneClientSettings setInterfaceOrientation:];
-[UIMutableApplicationSceneClientSettings supportedInterfaceOrientations];
-[UIMutableApplicationSceneClientSettings homeIndicatorAutoHidden];
-[UIMutableApplicationSceneClientSettings multitaskingDragExclusionRects];
-[UIMutableApplicationSceneClientSettings activationConditionsData];
-[UIMutableApplicationSceneClientSettings audioCategoriesDisablingVolumeHUD];
-[UIMutableApplicationSceneClientSettings valueDescriptionForFlag:object:ofSetting:];
-[UIMutableApplicationSceneClientSettings setAudioCategoriesDisablingVolumeHUD:];
-[UIMutableApplicationSceneClientSettings sceneTitle];
-[UIMutableApplicationSceneClientSettings compatibilityMode];
-[UIMutableApplicationSceneClientSettings keyDescriptionForSetting:];
-[UIMutableApplicationSceneClientSettings idleTimerDisabled];
-[UIMutableApplicationSceneClientSettings userInterfaceStyle];
-[UIMutableApplicationSceneClientSettings setUserInterfaceStyle:];
-[UIMutableApplicationSceneClientSettings backgroundStyle];
-[UIMutableApplicationSceneClientSettings setStatusBarAlpha:];
-[UIMutableApplicationSceneClientSettings preferredPointerLockStatus];
-[UIMutableApplicationSceneClientSettings screenEdgesDeferringSystemGestures];
-[UIMutableApplicationSceneClientSettings prefersStatusBarHidden];
-[UIMutableApplicationSceneClientSettings copyWithZone:];
-[UIMutableApplicationSceneClientSettings setWhitePointAdaptivityStyle:];
-[UIMutableApplicationSceneClientSettings statusBarAxis];
-[UIMutableApplicationSceneClientSettings whitePointAdaptivityStyle];
-[UIMutableApplicationSceneClientSettings statusBarStyle];
-[UIMutableApplicationSceneClientSettings setStatusBarStyle:];
-[UIMutableApplicationSceneClientSettings setBackgroundStyle:];
-[UIMutableApplicationSceneClientSettings defaultStatusBarStyle];
-[UIMutableApplicationSceneClientSettings brightnessLevel];
-[UIMutableApplicationSceneClientSettings editingInteractionConfiguration];
-[UIMutableApplicationSceneClientSettings setCanvasTitle:];
-[UIMutableApplicationSceneClientSettings setDisplayConfigurationRequest:];
-[UIMutableApplicationSceneClientSettings canvasTitle];
-[UIMutableApplicationSceneClientSettings containsSearchView];
-[UIMutableApplicationSceneClientSettings controlCenterAmbiguousActivationMargin];
-[UIMutableApplicationSceneClientSettings controlCenterRevealMode];
-[UIMutableApplicationSceneClientSettings defaultPNGExpirationTime];
-[UIMutableApplicationSceneClientSettings defaultPNGName];
-[UIMutableApplicationSceneClientSettings defaultStatusBarHidden];
-[UIMutableApplicationSceneClientSettings deviceOrientationEventsEnabled];
-[UIMutableApplicationSceneClientSettings disablesMirroring];
-[UIMutableApplicationSceneClientSettings discardSessionOnUserDisconnect];
-[UIMutableApplicationSceneClientSettings displayConfigurationRequest];
-[UIMutableApplicationSceneClientSettings idleModeVisualEffectsEnabled];
-[UIMutableApplicationSceneClientSettings interfaceOrientationChangesDisabled];
-[UIMutableApplicationSceneClientSettings isReachabilitySupported];
-[UIMutableApplicationSceneClientSettings isStatusBarForegroundTransparent];
-[UIMutableApplicationSceneClientSettings isUISubclass];
-[UIMutableApplicationSceneClientSettings notificationCenterRevealMode];
-[UIMutableApplicationSceneClientSettings physicalButtonConfigurations];
-[UIMutableApplicationSceneClientSettings playbackControlsState];
-[UIMutableApplicationSceneClientSettings primaryWindowOverlayInsets];
-[UIMutableApplicationSceneClientSettings proximityDetectionModes];
-[UIMutableApplicationSceneClientSettings requestedDisplayMode];
-[UIMutableApplicationSceneClientSettings sceneActivationBias];
-[UIMutableApplicationSceneClientSettings screenFocusedFrame];
-[UIMutableApplicationSceneClientSettings setActivationConditionsData:];
-[UIMutableApplicationSceneClientSettings setBrightnessLevel:];
-[UIMutableApplicationSceneClientSettings setContainsSearchView:];
-[UIMutableApplicationSceneClientSettings setControlCenterAmbiguousActivationMargin:];
-[UIMutableApplicationSceneClientSettings setControlCenterRevealMode:];
-[UIMutableApplicationSceneClientSettings setDefaultPNGExpirationTime:];
-[UIMutableApplicationSceneClientSettings setDefaultPNGName:];
-[UIMutableApplicationSceneClientSettings setDefaultStatusBarHidden:];
-[UIMutableApplicationSceneClientSettings setDefaultStatusBarStyle:];
-[UIMutableApplicationSceneClientSettings setDeviceOrientationEventsEnabled:];
-[UIMutableApplicationSceneClientSettings setDisablesMirroring:];
-[UIMutableApplicationSceneClientSettings setDiscardSessionOnUserDisconnect:];
-[UIMutableApplicationSceneClientSettings setEditingInteractionConfiguration:];
-[UIMutableApplicationSceneClientSettings setHomeIndicatorAutoHidden:];
-[UIMutableApplicationSceneClientSettings setIdleModeVisualEffectsEnabled:];
-[UIMutableApplicationSceneClientSettings setIdleTimerDisabled:];
-[UIMutableApplicationSceneClientSettings setInterfaceOrientationChangesDisabled:];
-[UIMutableApplicationSceneClientSettings setMultitaskingDragExclusionRects:];
-[UIMutableApplicationSceneClientSettings setNotificationCenterRevealMode:];
-[UIMutableApplicationSceneClientSettings setPhysicalButtonConfigurations:];
-[UIMutableApplicationSceneClientSettings setPlaybackControlsState:];
-[UIMutableApplicationSceneClientSettings setPreferredPointerLockStatus:];
-[UIMutableApplicationSceneClientSettings setPrefersStatusBarHidden:];
-[UIMutableApplicationSceneClientSettings setPrimaryWindowOverlayInsets:];
-[UIMutableApplicationSceneClientSettings setProximityDetectionModes:];
-[UIMutableApplicationSceneClientSettings setReachabilitySupported:];
-[UIMutableApplicationSceneClientSettings setRequestedDisplayMode:];
-[UIMutableApplicationSceneClientSettings setSceneActivationBias:];
-[UIMutableApplicationSceneClientSettings setSceneTitle:];
-[UIMutableApplicationSceneClientSettings setScreenEdgesDeferringSystemGestures:];
-[UIMutableApplicationSceneClientSettings setScreenFocusedFrame:];
-[UIMutableApplicationSceneClientSettings setStatusBarContextID:];
-[UIMutableApplicationSceneClientSettings setStatusBarForegroundTransparent:];
-[UIMutableApplicationSceneClientSettings setStatusBarHidden:];
-[UIMutableApplicationSceneClientSettings setStatusBarModernStyle:];
-[UIMutableApplicationSceneClientSettings setStatusBarPartStyles:];
-[UIMutableApplicationSceneClientSettings setSupportedInterfaceOrientations:];
-[UIMutableApplicationSceneClientSettings setSystemInputActive:];
-[UIMutableApplicationSceneClientSettings setVisibleMiniAlertCount:];
-[UIMutableApplicationSceneClientSettings setWantsExclusiveForeground:];
-[UIMutableApplicationSceneClientSettings settings:appendDescriptionToBuilder:forFlag:object:ofSetting:];
-[UIMutableApplicationSceneClientSettings statusBarContextID];
-[UIMutableApplicationSceneClientSettings statusBarModernStyle];
-[UIMutableApplicationSceneClientSettings statusBarPartStyles];
-[UIMutableApplicationSceneClientSettings systemInputActive];
-[UIMutableApplicationSceneClientSettings visibleMiniAlertCount];
```
