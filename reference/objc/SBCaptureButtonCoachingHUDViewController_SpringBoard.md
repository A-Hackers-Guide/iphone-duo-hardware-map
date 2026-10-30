# `SBCaptureButtonCoachingHUDViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBOrientationTransformWrapperViewController`
- Protocols: `UIViewControllerTransitioningDelegate`, `SBHUDViewControlling`
- 22 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<SBHUDAttachmentDelegate>" _attachmentDelegate;
{CGPoint="x"d"y"d} _positionOffset;
B _rotating;
B _coachingLabelTextNeedsUpdate;
B _isAttached;
@"<SBCaptureButtonCoachingHUDViewControllerDelegate>" _delegate;
q _state;
@"SBSystemActionCoachingSettings" _settings;
@"BLSAssertion" _liveRenderingAssertion;
Q _stateTransitionAnimationCount;
@"NSString" _coachingText;
@"NSString" _glyphPackageName;
@"NSString" _glyphLandscapeState;
q _coachingLabelOrientation;
@"UIView" _contentView;
@"UIView" _dimmingView;
@"UIView" _coachingContentView;
@"SBCaptureButtonCoachingHUDGlyphView" _glyphView;
@"SBCaptureButtonCoachingHUDButtonHighlight" _coachingButtonHighlightView;
@"SBCaptureButtonCoachingHUDLabelWrapperView" _coachingLabelWrapperView;
@"SBCaptureButtonCoachingHUDLabel" _coachingLabel;
@"_SBCaptureButtonCoachingBackdropLayer_Temp_134941860" _tempBackdropLayer;
```

## Properties

```
@property (T@"<SBCaptureButtonCoachingHUDViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHUDAttachmentDelegate>",W,N,V_attachmentDelegate) attachmentDelegate;
@property (T@"NSArray",R,C,N) physicalButtonSceneTargets;
```

## Instance methods

```
-[SBCaptureButtonCoachingHUDViewController animationControllerForDismissedController:];
-[SBCaptureButtonCoachingHUDViewController animationControllerForPresentedController:presentingController:sourceController:];
-[SBCaptureButtonCoachingHUDViewController physicalButtonSceneTargets];
-[SBCaptureButtonCoachingHUDViewController triggerButton];
-[SBCaptureButtonCoachingHUDViewController transitionToState:animated:completion:];
-[SBCaptureButtonCoachingHUDViewController viewIsAppearing:];
-[SBCaptureButtonCoachingHUDViewController viewDidLoad];
-[SBCaptureButtonCoachingHUDViewController setPositionOffset:];
-[SBCaptureButtonCoachingHUDViewController viewDidLayoutSubviews];
-[SBCaptureButtonCoachingHUDViewController initWithNibName:bundle:];
-[SBCaptureButtonCoachingHUDViewController _canShowWhileLocked];
-[SBCaptureButtonCoachingHUDViewController definesAnimatedDismissal];
-[SBCaptureButtonCoachingHUDViewController setDelegate:];
-[SBCaptureButtonCoachingHUDViewController dismissAnimatedWithCompletion:];
-[SBCaptureButtonCoachingHUDViewController isHUDAttached];
-[SBCaptureButtonCoachingHUDViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBCaptureButtonCoachingHUDViewController delegate];
-[SBCaptureButtonCoachingHUDViewController attachmentIgnoredOrientations];
-[SBCaptureButtonCoachingHUDViewController setAttachmentDelegate:];
-[SBCaptureButtonCoachingHUDViewController viewDidDisappear:];
-[SBCaptureButtonCoachingHUDViewController setCoachingText:glyphPackageName:glyphLandscapeState:];
-[SBCaptureButtonCoachingHUDViewController attachmentDelegate];
-[SBCaptureButtonCoachingHUDViewController state];
```
