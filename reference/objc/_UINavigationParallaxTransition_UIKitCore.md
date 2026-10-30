# `_UINavigationParallaxTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerPreemptableAnimatedTransitioning`, `UIViewControllerAnimatedTransitioning_Internal`, `UIViewControllerAnimatedTransitioningEx`
- 21 instance variables, 30 properties, 54 instance methods, 2 class methods

## Instance variables

```
@"<UIViewImplicitlyAnimating>" _propertyAnimator;
@"NSUUID" _currentRunningAnimationsUUID;
@"NSUUID" _currentTrackingAnimatorsAnimationsUUID;
@"<_UIInvalidatable>" _keyboardLayoutGuideTransitionAssertion;
@"_UIVisualEffectBackdropView" _captureBackdropView;
B _clipUnderlapWhileTransitioning;
B __shouldReverseLayoutDirection;
q _operation;
@"<UIViewControllerContextTransitioning>" _transitionContext;
@"_UINavigationInteractiveTransitionBase" _interactionController;
@"_UIParallaxDimmingView" _borderDimmingView;
@"_UIParallaxDimmingView" _contentDimmingView;
@"UIView" _containerFromView;
@"UIView" _containerToView;
@"UIView" _clipUnderView;
q _transitionStyle;
d _transitionGap;
@"UIColor" _overrideDimmingColor;
@"_UIViewControllerAnimatedTransitionHandoffData" _preemptionHandoffData;
@"UIView" _fromOverlayView;
@"UIView" _toOverlayView;
```

## Properties

```
@property (TB,?,R,N) prefersPreemptionEnabledForPresentations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIViewControllerAnimatedTransitionHandoffData",&,N,V_preemptionHandoffData) preemptionHandoffData;
@property (T@"UIView",&,N,V_fromOverlayView) fromOverlayView;
@property (T@"UIView",&,N,V_toOverlayView) toOverlayView;
@property (Tq,N,V_operation) operation;
@property (T@"<UIViewControllerContextTransitioning>",&,N,V_transitionContext) transitionContext;
@property (T@"_UINavigationInteractiveTransitionBase",W,N,V_interactionController) interactionController;
@property (T@"_UIParallaxDimmingView",&,N,V_borderDimmingView) borderDimmingView;
@property (T@"_UIParallaxDimmingView",&,N,V_contentDimmingView) contentDimmingView;
@property (T@"UIView",&,N,V_containerFromView) containerFromView;
@property (T@"UIView",&,N,V_containerToView) containerToView;
@property (T@"UIView",&,N,V_clipUnderView) clipUnderView;
@property (TB,N,V_clipUnderlapWhileTransitioning) clipUnderlapWhileTransitioning;
@property (Tq,N,V_transitionStyle) transitionStyle;
@property (Td,N,V_transitionGap) transitionGap;
@property (TB,N,S_setShouldReverseLayoutDirection:,V__shouldReverseLayoutDirection) _shouldReverseLayoutDirection;
@property (T@"UIColor",&,N,V_overrideDimmingColor) overrideDimmingColor;
@property (Tq,?,R,N) _navigationBarTransitionVariant;
@property (T@"UIView",?,R,N) _navigationBarTransitionOverlay;
@property (TB,?,R,N) _shouldCrossFadeNavigationBarVisibility;
@property (TB,?,R,N) _shouldCrossFadeBottomBars;
@property (TB,?,R,N) _shouldAnimateBottomBarVisibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationParallaxTransition defaultSlidingTransitionDuration];
+[_UINavigationParallaxTransition setDefaultSlidingTransitionDuration:];
```

## Instance methods

```
-[_UINavigationParallaxTransition setOperation:];
-[_UINavigationParallaxTransition operation];
-[_UINavigationParallaxTransition animateTransition:];
-[_UINavigationParallaxTransition parallaxOffset];
-[_UINavigationParallaxTransition resizedToContainerView];
-[_UINavigationParallaxTransition transitionDuration:];
-[_UINavigationParallaxTransition transitionGap];
-[_UINavigationParallaxTransition transitionContext];
-[_UINavigationParallaxTransition containerFromView];
-[_UINavigationParallaxTransition _shouldReverseLayoutDirection];
-[_UINavigationParallaxTransition borderDimmingView];
-[_UINavigationParallaxTransition shadowContainerForKeyboardTransition:];
-[_UINavigationParallaxTransition setClipUnderView:];
-[_UINavigationParallaxTransition setPreemptionHandoffData:];
-[_UINavigationParallaxTransition resizeShadow:];
-[_UINavigationParallaxTransition setTransitionContext:];
-[_UINavigationParallaxTransition toOverlayView];
-[_UINavigationParallaxTransition prepareToAnimateKeyboard:];
-[_UINavigationParallaxTransition resizedFromContainerView];
-[_UINavigationParallaxTransition animatePreemptionSnapshotsWithContext:];
-[_UINavigationParallaxTransition _animateOrCreatePropertyAnimatorForTransition:];
-[_UINavigationParallaxTransition interruptibleAnimatorForTransition:];
-[_UINavigationParallaxTransition overrideDimmingColor];
-[_UINavigationParallaxTransition gapBetweenViews];
-[_UINavigationParallaxTransition animationEnded:];
-[_UINavigationParallaxTransition animateKeyboard:];
-[_UINavigationParallaxTransition _setShouldReverseLayoutDirection:];
-[_UINavigationParallaxTransition _shouldUseInterruptibleAnimatorWithTraitCollection:];
-[_UINavigationParallaxTransition setFromOverlayView:];
-[_UINavigationParallaxTransition transitionStyle];
-[_UINavigationParallaxTransition setInteractionController:];
-[_UINavigationParallaxTransition interactionController];
-[_UINavigationParallaxTransition setOverrideDimmingColor:];
-[_UINavigationParallaxTransition clipUnderlapWhileTransitioning];
-[_UINavigationParallaxTransition fromOverlayView];
-[_UINavigationParallaxTransition _animationWillEnd:didComplete:];
-[_UINavigationParallaxTransition preemptWithContext:];
-[_UINavigationParallaxTransition setContainerToView:];
-[_UINavigationParallaxTransition contentDimmingView];
-[_UINavigationParallaxTransition setContainerFromView:];
-[_UINavigationParallaxTransition setTransitionGap:];
-[_UINavigationParallaxTransition _stopTransitionImmediately];
-[_UINavigationParallaxTransition setTransitionStyle:];
-[_UINavigationParallaxTransition clipUnderView];
-[_UINavigationParallaxTransition preemptionHandoffData];
-[_UINavigationParallaxTransition willBeginAfterPreemptionWithContext:data:];
-[_UINavigationParallaxTransition setToOverlayView:];
-[_UINavigationParallaxTransition completeKeyboard:];
-[_UINavigationParallaxTransition setBorderDimmingView:];
-[_UINavigationParallaxTransition setContentDimmingView:];
-[_UINavigationParallaxTransition initWithCurrentOperation:];
-[_UINavigationParallaxTransition setClipUnderlapWhileTransitioning:];
-[_UINavigationParallaxTransition containerToView];
-[_UINavigationParallaxTransition shouldPreemptWithContext:];
```
