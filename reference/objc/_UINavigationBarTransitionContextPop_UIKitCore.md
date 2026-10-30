# `_UINavigationBarTransitionContextPop`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarTransitionContext`
- 6 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endingNewTitleViewFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endingNewBackButtonFrame;
{CGSize="width"d"height"d} _titleTransitionDistance;
{CGSize="width"d"height"d} _titleTransitionDistanceExcludingLargeTitleOffset;
d _titleTransitionAdjustment;
B _unfreezeTitleControlOnFinish;
```

## Instance methods

```
-[_UINavigationBarTransitionContextPop transition];
-[_UINavigationBarTransitionContextPop complete];
-[_UINavigationBarTransitionContextPop prepare];
-[_UINavigationBarTransitionContextPop animate];
-[_UINavigationBarTransitionContextPop cancel];
-[_UINavigationBarTransitionContextPop _animateBackgroundView];
-[_UINavigationBarTransitionContextPop _animateContentView];
-[_UINavigationBarTransitionContextPop _animateFromPalette:fromPaletteFrame:toPalette:toPaletteFrame:];
-[_UINavigationBarTransitionContextPop _animateLargeTitleView];
-[_UINavigationBarTransitionContextPop _animateScaleTransition];
-[_UINavigationBarTransitionContextPop _animateSearchBar];
-[_UINavigationBarTransitionContextPop _finishWithFinalLayout:invalidLayout:];
-[_UINavigationBarTransitionContextPop _prepareBackgroundView];
-[_UINavigationBarTransitionContextPop _prepareContentView];
-[_UINavigationBarTransitionContextPop _prepareLargeTitleView];
-[_UINavigationBarTransitionContextPop _prepareScaleTransition];
-[_UINavigationBarTransitionContextPop _prepareSearchBar];
-[_UINavigationBarTransitionContextPop _prepareTransitionFromPalette:toPalette:toPaletteFrame:];
-[_UINavigationBarTransitionContextPop viewUsingEaseInCurve];
```
