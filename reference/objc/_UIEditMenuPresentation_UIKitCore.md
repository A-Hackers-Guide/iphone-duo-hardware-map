# `_UIEditMenuPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _enforcesMenuControllerLifecycle;
@"UIView" _sourceView;
@"<_UIEditMenuPresentationDelegate>" _delegate;
@"UIMenu" _displayedMenu;
@"UIEditMenuConfiguration" _activeConfiguration;
@"UIEditMenuConfiguration" _dismissingConfiguration;
Q _currentState;
@"_UIEditMenuPresentationAnimator" _presentAnimator;
@"_UIEditMenuPresentationAnimator" _dismissAnimator;
```

## Properties

```
@property (TQ,N,V_currentState) currentState;
@property (T@"_UIEditMenuPresentationAnimator",&,N,V_presentAnimator) presentAnimator;
@property (T@"_UIEditMenuPresentationAnimator",&,N,V_dismissAnimator) dismissAnimator;
@property (T@"UIMenu",&,N,V_displayedMenu) displayedMenu;
@property (T@"UIEditMenuConfiguration",&,N,V_activeConfiguration) activeConfiguration;
@property (T@"UIView",R,W,N,V_sourceView) sourceView;
@property (T@"<_UIEditMenuPresentationDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_enforcesMenuControllerLifecycle) enforcesMenuControllerLifecycle;
@property (T@"UIEditMenuConfiguration",&,N,V_dismissingConfiguration) dismissingConfiguration;
```

## Instance methods

```
-[_UIEditMenuPresentation activeConfiguration];
-[_UIEditMenuPresentation didTransitionFrom:to:];
-[_UIEditMenuPresentation displayedMenu];
-[_UIEditMenuPresentation menuFrameInCoordinateSpace:];
-[_UIEditMenuPresentation setActiveConfiguration:];
-[_UIEditMenuPresentation setCurrentState:];
-[_UIEditMenuPresentation delegate];
-[_UIEditMenuPresentation currentState];
-[_UIEditMenuPresentation sourceView];
-[_UIEditMenuPresentation enforcesMenuControllerLifecycle];
-[_UIEditMenuPresentation presentAnimator];
-[_UIEditMenuPresentation completeHandoff];
-[_UIEditMenuPresentation dismissAnimator];
-[_UIEditMenuPresentation animateFadeWithDelay:animations:completion:];
-[_UIEditMenuPresentation animateReducedMotionTransitionWithDelay:animations:completion:];
-[_UIEditMenuPresentation animateScaleDismissalWithAnimations:completion:];
-[_UIEditMenuPresentation animateScalePresentWithDelay:animations:completion:];
-[_UIEditMenuPresentation completeIntelligentAssistantTransition];
-[_UIEditMenuPresentation dismissingConfiguration];
-[_UIEditMenuPresentation displayMenu:configuration:];
-[_UIEditMenuPresentation forceEndDismissalIfNeeded];
-[_UIEditMenuPresentation forceEndPresentIfNeeded];
-[_UIEditMenuPresentation hideMenuWithReason:];
-[_UIEditMenuPresentation initWithDelegate:sourceView:];
-[_UIEditMenuPresentation replaceVisibleMenuWithMenu:reason:];
-[_UIEditMenuPresentation resolvedUserInterfaceStyle];
-[_UIEditMenuPresentation setDismissAnimator:];
-[_UIEditMenuPresentation setDismissingConfiguration:];
-[_UIEditMenuPresentation setDisplayedMenu:];
-[_UIEditMenuPresentation setEnforcesMenuControllerLifecycle:];
-[_UIEditMenuPresentation setPresentAnimator:];
-[_UIEditMenuPresentation sourceViewDidUpdateFromTraitCollection:];
-[_UIEditMenuPresentation transitionWithEvent:];
-[_UIEditMenuPresentation updateMenuPositionAnimated:];
```
