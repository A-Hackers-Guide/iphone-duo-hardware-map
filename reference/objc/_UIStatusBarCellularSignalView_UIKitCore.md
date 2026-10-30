# `_UIStatusBarCellularSignalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarSignalView`
- 3 instance variables, 3 properties, 21 instance methods, 5 class methods

## Instance variables

```
B _needsLargerScale;
B _needsCycleAnimationUpdate;
@"_UIStatusBarCycleAnimation" _cycleAnimation;
```

## Properties

```
@property (TB,N,V_needsLargerScale) needsLargerScale;
@property (TB,N,V_needsCycleAnimationUpdate) needsCycleAnimationUpdate;
@property (T@"_UIStatusBarCycleAnimation",&,N,V_cycleAnimation) cycleAnimation;
```

## Class methods

```
+[_UIStatusBarCellularSignalView _heightForNormalBarAtIndex:iconSize:];
+[_UIStatusBarCellularSignalView _barCornerRadiusForIconSize:];
+[_UIStatusBarCellularSignalView _intrinsicContentSizeForNumberOfBars:iconSize:];
+[_UIStatusBarCellularSignalView _interspaceForIconSize:];
+[_UIStatusBarCellularSignalView _barWidthForIconSize:];
```

## Instance methods

```
-[_UIStatusBarCellularSignalView _iconSizeDidChange];
-[_UIStatusBarCellularSignalView accessibilityHUDRepresentation];
-[_UIStatusBarCellularSignalView didMoveToWindow];
-[_UIStatusBarCellularSignalView _setNeedsUpdateCycleAnimation];
-[_UIStatusBarCellularSignalView applyStyleAttributes:];
-[_UIStatusBarCellularSignalView intrinsicContentSize];
-[_UIStatusBarCellularSignalView _updateActiveBars];
-[_UIStatusBarCellularSignalView _updateCycleAnimationIfNeeded];
-[_UIStatusBarCellularSignalView cycleAnimation];
-[_UIStatusBarCellularSignalView layoutSubviews];
-[_UIStatusBarCellularSignalView _heightForBarAtIndex:];
-[_UIStatusBarCellularSignalView needsLargerScale];
-[_UIStatusBarCellularSignalView _heightForBarAtIndex:mode:];
-[_UIStatusBarCellularSignalView _colorsDidChange];
-[_UIStatusBarCellularSignalView setNeedsLargerScale:];
-[_UIStatusBarCellularSignalView _updateBars];
-[_UIStatusBarCellularSignalView setCycleAnimation:];
-[_UIStatusBarCellularSignalView _updateCycleAnimationNow];
-[_UIStatusBarCellularSignalView needsCycleAnimationUpdate];
-[_UIStatusBarCellularSignalView _updateFromMode:];
-[_UIStatusBarCellularSignalView setNeedsCycleAnimationUpdate:];
```
