# `SBIsolatedSceneOrientationFollowingWrapperViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBTraitsParticipantDelegate`, `SBDeviceApplicationCounterRotatableSceneOverlayViewDelegate`, `SBDeviceApplicationSceneOverlayViewControllerPrivate`
- 16 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"UIViewController" _contentViewController;
B _contentViewControllerBeingRemoved;
@"SBWindowScene" _windowScene;
@"SBWindow" _appOverlayWindow;
@"SBAccessoryWindowScene" _isolatedWindowScene;
@"<UIScenePresenter>" _scenePresenter;
@"TRAParticipant" _traitsParticipant;
@"TRAParticipant" _followedParticipant;
@"<BSInvalidatable>" _traitsResolutionPolicySpecifier;
@"TRAOrientationResolutionPolicyInfo" _traitsOrientationResolutionPolicy;
B _initialOrientationHasBeenApplied;
@"UIView" _hostedOverlayView;
@"SBIsolatedSceneOrientationFollowingView" _containerView;
B _rendersWhileLocked;
@"<SBIsolatedSceneOrientationFollowingWrapperOrientationDelegate>" _orientationDelegate;
```

## Properties

```
@property (T@"<SBIsolatedSceneOrientationFollowingWrapperOrientationDelegate>",W,N,V_orientationDelegate) orientationDelegate;
@property (Tq,R,N) currentInterfaceOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) containerOrientation;
@property (T@"UIView<SBDeviceApplicationSceneOverlayView>",R,N) overlayView;
```

## Instance methods

```
-[SBIsolatedSceneOrientationFollowingWrapperViewController containerOrientation];
-[SBIsolatedSceneOrientationFollowingWrapperViewController viewWillDisappear:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController participantAssociatedWindows:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController didChangeSettingsForParticipant:context:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController updatePreferencesForParticipant:updater:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController overlayView];
-[SBIsolatedSceneOrientationFollowingWrapperViewController currentInterfaceOrientation];
-[SBIsolatedSceneOrientationFollowingWrapperViewController viewWillAppear:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _canShowWhileLocked];
-[SBIsolatedSceneOrientationFollowingWrapperViewController viewDidAppear:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController loadView];
-[SBIsolatedSceneOrientationFollowingWrapperViewController viewWillLayoutSubviews];
-[SBIsolatedSceneOrientationFollowingWrapperViewController viewDidDisappear:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController appendDescriptionForParticipant:withBuilder:multilinePrefix:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController containerDidUpdateTraitsParticipant:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController setOrientationDelegate:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _boundsForOverlayRootView];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _containerViewWillRotateFromInterfaceOrientation:toInterfaceOrientation:withAnimationSettings:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _hostOrientation];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _isSceneStatusBarHidden];
-[SBIsolatedSceneOrientationFollowingWrapperViewController _updateOrientationResolutionPolicyWithContainerTraitsParticipant:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController initWithContentViewController:sceneHandle:windowScene:orientationDelegate:rendersWhileLocked:];
-[SBIsolatedSceneOrientationFollowingWrapperViewController orientationDelegate];
```
