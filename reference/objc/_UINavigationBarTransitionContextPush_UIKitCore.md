# `_UINavigationBarTransitionContextPush`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarTransitionContext`
- 6 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endingNewTitleViewFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endingNewBackButtonFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endingBackIndicatorViewFrame;
{CGSize="width"d"height"d} _titleTransitionDistance;
{CGSize="width"d"height"d} _titleTransitionDistanceExcludingLargeTitleOffset;
B _unfreezeTitleControlOnFinish;
```

## Instance methods

```
-[_UINavigationBarTransitionContextPush transition];
-[_UINavigationBarTransitionContextPush complete];
-[_UINavigationBarTransitionContextPush prepare];
-[_UINavigationBarTransitionContextPush animate];
-[_UINavigationBarTransitionContextPush cancel];
-[_UINavigationBarTransitionContextPush _animateBackgroundView];
-[_UINavigationBarTransitionContextPush _animateContentView];
-[_UINavigationBarTransitionContextPush _animateFromPalette:fromPaletteFrame:toPalette:toPaletteFrame:];
-[_UINavigationBarTransitionContextPush _animateLargeTitleView];
-[_UINavigationBarTransitionContextPush _animateScaleTransition];
-[_UINavigationBarTransitionContextPush _animateSearchBar];
-[_UINavigationBarTransitionContextPush _finishWithFinalLayout:invalidLayout:];
-[_UINavigationBarTransitionContextPush _prepareBackgroundView];
-[_UINavigationBarTransitionContextPush _prepareContentView];
-[_UINavigationBarTransitionContextPush _prepareLargeTitleView];
-[_UINavigationBarTransitionContextPush _prepareScaleTransition];
-[_UINavigationBarTransitionContextPush _prepareSearchBar];
-[_UINavigationBarTransitionContextPush _prepareTransitionFromPalette:toPalette:toPaletteFrame:];
```
