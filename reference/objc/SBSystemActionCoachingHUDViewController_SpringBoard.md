# `SBSystemActionCoachingHUDViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBOrientationTransformWrapperViewController`
- Protocols: `SBControlSystemActionObserver`, `UIViewControllerTransitioningDelegate`, `SBHUDViewControlling`
- 28 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<SBHUDAttachmentDelegate>" _attachmentDelegate;
{CGPoint="x"d"y"d} _positionOffset;
B _rotating;
B _coachingLabelTextNeedsUpdate;
B _coachingLabelOccluded;
B _shouldLayoutForButtonHints;
B _isAttached;
@"<SBSystemActionCoachingHUDViewControllerDelegate>" _delegate;
@"SBSystemAction" _action;
@"NSArray" _systemApertureFrames;
q _state;
@"SBRingerControl" _ringerControl;
@"SBActivityManager" _activityManager;
@"SBApplicationController" _applicationController;
@"SBDoNotDisturbStateMonitor" _doNotDisturbStateMonitor;
@"SBFlashlightActivityManager" _flashlightActivityManager;
@"SBFocusActivityManager" _focusActivityManager;
@"SBSystemActionCoachingSettings" _settings;
@"<BSInvalidatable>" _contentVisibilityAssertion;
@"BLSAssertion" _liveRenderingAssertion;
Q _stateTransitionAnimationCount;
q _coachingLabelOrientation;
@"UIView" _contentView;
@"UIView" _dimmingView;
@"UIView" _coachingContentView;
@"UIView" _coachingButton;
@"UIView" _coachingLabelWrapperView;
@"UILabel" _coachingLabel;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHUDAttachmentDelegate>",W,N,V_attachmentDelegate) attachmentDelegate;
@property (T@"NSArray",R,C,N) physicalButtonSceneTargets;
```

## Instance methods

```
-[SBSystemActionCoachingHUDViewController animationControllerForDismissedController:];
-[SBSystemActionCoachingHUDViewController animationControllerForPresentedController:presentingController:sourceController:];
-[SBSystemActionCoachingHUDViewController physicalButtonSceneTargets];
-[SBSystemActionCoachingHUDViewController triggerButton];
-[SBSystemActionCoachingHUDViewController viewIsAppearing:];
-[SBSystemActionCoachingHUDViewController viewDidLoad];
-[SBSystemActionCoachingHUDViewController setPositionOffset:];
-[SBSystemActionCoachingHUDViewController viewDidLayoutSubviews];
-[SBSystemActionCoachingHUDViewController _canShowWhileLocked];
-[SBSystemActionCoachingHUDViewController definesAnimatedDismissal];
-[SBSystemActionCoachingHUDViewController dismissAnimatedWithCompletion:];
-[SBSystemActionCoachingHUDViewController isHUDAttached];
-[SBSystemActionCoachingHUDViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBSystemActionCoachingHUDViewController attachmentIgnoredOrientations];
-[SBSystemActionCoachingHUDViewController setAttachmentDelegate:];
-[SBSystemActionCoachingHUDViewController viewDidDisappear:];
-[SBSystemActionCoachingHUDViewController attachmentDelegate];
-[SBSystemActionCoachingHUDViewController controlSystemAction:propertiesDidChange:];
```
