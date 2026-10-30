# `BKUIPearlJindoEnrollViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKUIPearlEnrollViewController`
- Protocols: `BNPresentableObserving`, `BKUIPearlEnrollViewStateTransitionDelegate`, `BKUIAlertControllerListener`, `BKJindoPresentableObserving`
- 6 instance variables, 10 properties, 47 instance methods, 0 class methods

## Instance variables

```
B _jindoNeedsResignActiveRevoke;
@"BKUIJindoPresentableBase" _presentable;
@"NSLayoutConstraint" _bottomContainerTopConstraint;
@"UIView" _hostedTutorialMicaView;
@"NSLayoutConstraint" _hostedTutorialMicaViewCenterConstraint;
@"<UITraitChangeRegistration>" _jindoTraitChangeRegistration;
```

## Properties

```
@property (T@"BKUIJindoPresentableBase",&,N,V_presentable) presentable;
@property (T@"NSLayoutConstraint",&,N,V_bottomContainerTopConstraint) bottomContainerTopConstraint;
@property (T@"UIView",&,N,V_hostedTutorialMicaView) hostedTutorialMicaView;
@property (T@"NSLayoutConstraint",&,N,V_hostedTutorialMicaViewCenterConstraint) hostedTutorialMicaViewCenterConstraint;
@property (TB,N,V_jindoNeedsResignActiveRevoke) jindoNeedsResignActiveRevoke;
@property (T@"<UITraitChangeRegistration>",&,N,V_jindoTraitChangeRegistration) jindoTraitChangeRegistration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKUIPearlJindoEnrollViewController setPresentable:];
-[BKUIPearlJindoEnrollViewController presentViewController:animated:completion:];
-[BKUIPearlJindoEnrollViewController presentableDidAppearAsBanner:];
-[BKUIPearlJindoEnrollViewController viewWillDisappear:];
-[BKUIPearlJindoEnrollViewController didBecomeActive:];
-[BKUIPearlJindoEnrollViewController _sceneDidActivate:];
-[BKUIPearlJindoEnrollViewController viewDidLoad];
-[BKUIPearlJindoEnrollViewController willResignActive:];
-[BKUIPearlJindoEnrollViewController _sceneWillDeactivate:];
-[BKUIPearlJindoEnrollViewController presentable];
-[BKUIPearlJindoEnrollViewController viewDidDisappear:];
-[BKUIPearlJindoEnrollViewController buttonTray];
-[BKUIPearlJindoEnrollViewController _setupUI];
-[BKUIPearlJindoEnrollViewController _isDarkMode];
-[BKUIPearlJindoEnrollViewController nextStateButton];
-[BKUIPearlJindoEnrollViewController _fullEnrollViewSize];
-[BKUIPearlJindoEnrollViewController _handleEnrollStateOnAppear];
-[BKUIPearlJindoEnrollViewController _jindoBottomContainer];
-[BKUIPearlJindoEnrollViewController _postBannerToDestinationWithInitialStateCollapsed:];
-[BKUIPearlJindoEnrollViewController _postBannerToDestinationWithInitialStateCollapsed:enrollViewStateConfiguration:];
-[BKUIPearlJindoEnrollViewController _prepEnrollViewAndEnrollTutorialMica];
-[BKUIPearlJindoEnrollViewController _startOverTitleForState:];
-[BKUIPearlJindoEnrollViewController alertActionTappedFromAlert];
-[BKUIPearlJindoEnrollViewController animateToSuccessCompletionLayout:];
-[BKUIPearlJindoEnrollViewController bottomContainerTopConstraint];
-[BKUIPearlJindoEnrollViewController didChangeActiveLayoutMode:];
-[BKUIPearlJindoEnrollViewController endEnrollFlowWithError:];
-[BKUIPearlJindoEnrollViewController escapeHatchButton];
-[BKUIPearlJindoEnrollViewController escapeHatchButton:state:];
-[BKUIPearlJindoEnrollViewController hostedTutorialMicaView];
-[BKUIPearlJindoEnrollViewController hostedTutorialMicaViewCenterConstraint];
-[BKUIPearlJindoEnrollViewController jindoNeedsResignActiveRevoke];
-[BKUIPearlJindoEnrollViewController jindoTraitChangeRegistration];
-[BKUIPearlJindoEnrollViewController navigateToMidFlowPeriocularSplashScreenWithPrepareAction:completionAction:];
-[BKUIPearlJindoEnrollViewController nextStateButtonContainer];
-[BKUIPearlJindoEnrollViewController nextStateButtonPressed:];
-[BKUIPearlJindoEnrollViewController prepareBottomContainerForAnimationToState:fromState:subState:advancing:];
-[BKUIPearlJindoEnrollViewController prepareForAnimationToState:fromState:subState:advancing:];
-[BKUIPearlJindoEnrollViewController retryMatchOperationButton];
-[BKUIPearlJindoEnrollViewController setBottomContainerTopConstraint:];
-[BKUIPearlJindoEnrollViewController setHostedTutorialMicaView:];
-[BKUIPearlJindoEnrollViewController setHostedTutorialMicaViewCenterConstraint:];
-[BKUIPearlJindoEnrollViewController setJindoNeedsResignActiveRevoke:];
-[BKUIPearlJindoEnrollViewController setJindoTraitChangeRegistration:];
-[BKUIPearlJindoEnrollViewController startOverButtonForState:];
-[BKUIPearlJindoEnrollViewController stateTransitionDidComplete];
-[BKUIPearlJindoEnrollViewController transitionToSuccessFromPeriocularSplash];
```
