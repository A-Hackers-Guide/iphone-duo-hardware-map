# `_UIFullscreenPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UICurrentContextPresentationController`
- 8 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIView" _counterRotatedView;
d _counterRotatedAngle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _counterRotatedOriginalBounds;
q _originalOrientation;
B _presentingViewControllerHandledCounterRotation;
@? _finalRotationBlock;
@"_UIForcedOrientationTransactionToken" _forcedOrientationToken;
B _disableAnimatedReenablingOfAutorotation;
```

## Instance methods

```
-[_UIFullscreenPresentationController _shouldRespectDefinesPresentationContext];
-[_UIFullscreenPresentationController presentationTransitionDidEnd:];
-[_UIFullscreenPresentationController _placeCounterRotationViewWithView:inWindow:fromOrientation:toOrientation:force:];
-[_UIFullscreenPresentationController _adjustOrientationIfNecessaryInWindow:forViewController:preservingViewController:];
-[_UIFullscreenPresentationController dealloc];
-[_UIFullscreenPresentationController presentationStyle];
-[_UIFullscreenPresentationController _invokesDelegatesOnOrientationChange];
-[_UIFullscreenPresentationController _prepareForMixedOrientationTransitionIfNecessaryInWindow:fromViewController:toViewController:];
-[_UIFullscreenPresentationController frameOfPresentedViewInContainerView];
-[_UIFullscreenPresentationController _shouldAnimateReenablingOfAutorotation];
-[_UIFullscreenPresentationController _transitionDidEnd:isDismissal:];
-[_UIFullscreenPresentationController shouldPresentInFullscreen];
-[_UIFullscreenPresentationController _applyCounterRotationToView:fromOrientation:toOrientation:withBounds:];
-[_UIFullscreenPresentationController _removeCounterRotationIfApplied];
-[_UIFullscreenPresentationController _isEffectivelyFullScreen];
-[_UIFullscreenPresentationController dismissalTransitionDidEnd:];
-[_UIFullscreenPresentationController _setPresentedViewController:];
```
