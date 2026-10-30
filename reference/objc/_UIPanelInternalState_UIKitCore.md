# `_UIPanelInternalState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 15 instance variables, 15 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _mainViewController;
@"UIViewController" _leadingViewController;
@"UIViewController" _supplementaryViewController;
@"UIViewController" _trailingViewController;
@"UIViewController" _collapsedViewController;
@"UIViewController" _preservedDetailController;
@"<UIPanelControllerDelegate>" _delegate;
@"UISlidingBarConfiguration" _configuration;
@"UISlidingBarStateRequest" _stateRequest;
@"UISlidingBarStateRequest" _externallyAnimatingStateRequest;
q _externallyAnimatingAffectedSides;
@"_UIPanelAnimationState" _animationState;
@"UISlidingBarStateRequest" _interactiveStateRequest;
q _collapsedState;
d _keyboardAdjustment;
```

## Properties

```
@property (T@"UIViewController",&,N,V_mainViewController) mainViewController;
@property (T@"UIViewController",&,N,V_leadingViewController) leadingViewController;
@property (T@"UIViewController",&,N,V_supplementaryViewController) supplementaryViewController;
@property (T@"UIViewController",&,N,V_trailingViewController) trailingViewController;
@property (T@"UIViewController",&,N,V_collapsedViewController) collapsedViewController;
@property (T@"UIViewController",&,N,V_preservedDetailController) preservedDetailController;
@property (T@"<UIPanelControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UISlidingBarConfiguration",C,N,V_configuration) configuration;
@property (T@"UISlidingBarStateRequest",C,N,V_stateRequest) stateRequest;
@property (T@"UISlidingBarStateRequest",C,N,V_externallyAnimatingStateRequest) externallyAnimatingStateRequest;
@property (Tq,N,V_externallyAnimatingAffectedSides) externallyAnimatingAffectedSides;
@property (T@"_UIPanelAnimationState",&,N,V_animationState) animationState;
@property (T@"UISlidingBarStateRequest",C,N,V_interactiveStateRequest) interactiveStateRequest;
@property (Tq,N,V_collapsedState) collapsedState;
@property (Td,N,V_keyboardAdjustment) keyboardAdjustment;
```

## Instance methods

```
-[_UIPanelInternalState animationState];
-[_UIPanelInternalState setConfiguration:];
-[_UIPanelInternalState mainViewController];
-[_UIPanelInternalState setDelegate:];
-[_UIPanelInternalState configuration];
-[_UIPanelInternalState delegate];
-[_UIPanelInternalState description];
-[_UIPanelInternalState keyboardAdjustment];
-[_UIPanelInternalState setAnimationState:];
-[_UIPanelInternalState copyWithZone:];
-[_UIPanelInternalState setKeyboardAdjustment:];
-[_UIPanelInternalState setMainViewController:];
-[_UIPanelInternalState _stateForInteractiveRequest:withAffectedSides:inPossibleStates:];
-[_UIPanelInternalState externallyAnimatingStateRequest];
-[_UIPanelInternalState setSupplementaryViewController:];
-[_UIPanelInternalState _allowedLeadingWidthsForParentWidth:];
-[_UIPanelInternalState _allowedSupplementaryWidthsForParentWidth:];
-[_UIPanelInternalState _allowedTrailingWidthsForParentWidth:];
-[_UIPanelInternalState _allowedWidthsForViewController:parentWidth:];
-[_UIPanelInternalState _defaultWidthForViewController:parentWidth:];
-[_UIPanelInternalState collapsedState];
-[_UIPanelInternalState collapsedViewController];
-[_UIPanelInternalState computePossibleStatesGivenParentView:withSize:];
-[_UIPanelInternalState computePossibleStatesGivenParentView:withSize:forceOverlay:];
-[_UIPanelInternalState externallyAnimatingAffectedSides];
-[_UIPanelInternalState interactiveStateRequest];
-[_UIPanelInternalState leadingViewController];
-[_UIPanelInternalState preservedDetailController];
-[_UIPanelInternalState setCollapsedState:];
-[_UIPanelInternalState setCollapsedViewController:];
-[_UIPanelInternalState setExternallyAnimatingAffectedSides:];
-[_UIPanelInternalState setExternallyAnimatingStateRequest:];
-[_UIPanelInternalState setInteractiveStateRequest:];
-[_UIPanelInternalState setLeadingViewController:];
-[_UIPanelInternalState setPreservedDetailController:];
-[_UIPanelInternalState setStateRequest:];
-[_UIPanelInternalState setTrailingViewController:];
-[_UIPanelInternalState stateRequest];
-[_UIPanelInternalState supplementaryViewController];
-[_UIPanelInternalState trailingViewController];
```
