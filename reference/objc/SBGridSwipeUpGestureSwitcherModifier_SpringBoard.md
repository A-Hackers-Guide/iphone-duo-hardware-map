# `SBGridSwipeUpGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 4 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _translation;
B _isApplyingContentViewScaleToSwitcherViewBounds;
@"SBDismissSiriSwitcherModifier" _dismissSiriModifier;
B _delayCompletionUntilTransitionBegins;
```

## Properties

```
@property (TB,R,N,V_delayCompletionUntilTransitionBegins) delayCompletionUntilTransitionBegins;
```

## Instance methods

```
-[SBGridSwipeUpGestureSwitcherModifier contentViewScale];
-[SBGridSwipeUpGestureSwitcherModifier handleGestureEvent:];
-[SBGridSwipeUpGestureSwitcherModifier _applyPrototypeSettings];
-[SBGridSwipeUpGestureSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBGridSwipeUpGestureSwitcherModifier isHomeScreenContentRequired];
-[SBGridSwipeUpGestureSwitcherModifier didMoveToParentModifier:];
-[SBGridSwipeUpGestureSwitcherModifier switcherViewBounds];
-[SBGridSwipeUpGestureSwitcherModifier homeScreenBackdropBlurType];
-[SBGridSwipeUpGestureSwitcherModifier isSwitcherWindowVisible];
-[SBGridSwipeUpGestureSwitcherModifier handleTransitionEvent:];
-[SBGridSwipeUpGestureSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBGridSwipeUpGestureSwitcherModifier visibleAppLayouts];
-[SBGridSwipeUpGestureSwitcherModifier wallpaperStyle];
-[SBGridSwipeUpGestureSwitcherModifier scrollViewContentOffset];
-[SBGridSwipeUpGestureSwitcherModifier _performBlockByApplyContentViewScaleToSwitcherViewBounds:];
-[SBGridSwipeUpGestureSwitcherModifier delayCompletionUntilTransitionBegins];
-[SBGridSwipeUpGestureSwitcherModifier finalResponseForGestureEvent:];
-[SBGridSwipeUpGestureSwitcherModifier initWithGestureID:];
-[SBGridSwipeUpGestureSwitcherModifier initWithGestureID:delayCompletionUntilTransitionBegins:];
```
