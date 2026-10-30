# `SBAssistantRootViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughViewController`
- Protocols: `SBFluidGestureDismissable`
- 12 instance variables, 12 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"SiriPresentationSpringBoardMainScreenViewController" _siriPresentationViewController;
@"SBFTouchPassThroughView" _contentView;
@"SBFTouchPassThroughView" _clippingView;
@"UIView" _dimmingView;
@"SBFluidDismissalState" _fluidDismissalState;
@"SBHomeGrabberView" _homeAffordanceView;
@"SBKeyboardHomeAffordanceAssertion" _keyboardHomeAffordanceAssertion;
@"SBFHomeGrabberSettings" _grabberSettings;
B _keyboardPresented;
B _keyboardStashed;
B _ownsHomeGesture;
B _showsHomeAffordance;
```

## Properties

```
@property (T@"SBFluidDismissalState",&,N) fluidDismissalState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,N,V_clippingView) clippingView;
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"SiriPresentationSpringBoardMainScreenViewController",&,N,V_siriPresentationViewController) siriPresentationViewController;
@property (TB,N,V_ownsHomeGesture) ownsHomeGesture;
@property (TB,N,V_showsHomeAffordance) showsHomeAffordance;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N) homeGrabberPointerClickDelegate;
@property (TB,N) dimsContentBelow;
```

## Instance methods

```
-[SBAssistantRootViewController childViewControllerForHomeIndicatorAutoHidden];
-[SBAssistantRootViewController ownsHomeGesture];
-[SBAssistantRootViewController init];
-[SBAssistantRootViewController supportedInterfaceOrientations];
-[SBAssistantRootViewController getRotationContentSettings:forWindow:];
-[SBAssistantRootViewController shouldAutorotate];
-[SBAssistantRootViewController _canShowWhileLocked];
-[SBAssistantRootViewController childViewControllerForScreenEdgesDeferringSystemGestures];
-[SBAssistantRootViewController clippingView];
-[SBAssistantRootViewController loadView];
-[SBAssistantRootViewController setOwnsHomeGesture:];
-[SBAssistantRootViewController contentView];
-[SBAssistantRootViewController viewWillLayoutSubviews];
-[SBAssistantRootViewController shouldAutomaticallyForwardRotationMethods];
-[SBAssistantRootViewController _edgeInsetsForChildViewController:insetsAreAbsolute:];
-[SBAssistantRootViewController setFluidDismissalState:];
-[SBAssistantRootViewController fluidDismissalState];
-[SBAssistantRootViewController shouldAutomaticallyForwardAppearanceMethods];
-[SBAssistantRootViewController setNeedsUpdateOfHomeIndicatorAutoHidden];
-[SBAssistantRootViewController setNeedsUpdateOfScreenEdgesDeferringSystemGestures];
-[SBAssistantRootViewController wantsFullScreenLayout];
-[SBAssistantRootViewController _keyboardWillShowNotification:];
-[SBAssistantRootViewController _updateHomeAffordance];
-[SBAssistantRootViewController homeGrabberPointerClickDelegate];
-[SBAssistantRootViewController _keyboardWillHideNotification:];
-[SBAssistantRootViewController _setStatusBarHidden:animated:];
-[SBAssistantRootViewController _updateKeyboardForHomeGesture];
-[SBAssistantRootViewController dimsContentBelow];
-[SBAssistantRootViewController setDimsContentBelow:];
-[SBAssistantRootViewController setHomeGrabberPointerClickDelegate:];
-[SBAssistantRootViewController setShowsHomeAffordance:];
-[SBAssistantRootViewController setSiriPresentationViewController:];
-[SBAssistantRootViewController showsHomeAffordance];
-[SBAssistantRootViewController siriPresentationViewController];
```
