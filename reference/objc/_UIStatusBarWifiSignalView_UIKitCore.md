# `_UIStatusBarWifiSignalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarSignalView`
- 2 instance variables, 2 properties, 17 instance methods, 6 class methods

## Instance variables

```
B _needsCycleAnimationUpdate;
@"_UIStatusBarCycleAnimation" _cycleAnimation;
```

## Properties

```
@property (TB,N,V_needsCycleAnimationUpdate) needsCycleAnimationUpdate;
@property (T@"_UIStatusBarCycleAnimation",&,N,V_cycleAnimation) cycleAnimation;
```

## Class methods

```
+[_UIStatusBarWifiSignalView widthForIconSize:];
+[_UIStatusBarWifiSignalView _intrinsicContentSizeForNumberOfBars:iconSize:];
+[_UIStatusBarWifiSignalView _interspaceForIconSize:];
+[_UIStatusBarWifiSignalView _barImageWithSize:forScale:distance:angle:centerPoint:cornerRadius:thickness:rounded:];
+[_UIStatusBarWifiSignalView _barThicknessAtIndex:iconSize:];
+[_UIStatusBarWifiSignalView _totalWidthForIconSize:];
```

## Instance methods

```
-[_UIStatusBarWifiSignalView _iconSizeDidChange];
-[_UIStatusBarWifiSignalView accessibilityHUDRepresentation];
-[_UIStatusBarWifiSignalView didMoveToWindow];
-[_UIStatusBarWifiSignalView _setNeedsUpdateCycleAnimation];
-[_UIStatusBarWifiSignalView intrinsicContentSize];
-[_UIStatusBarWifiSignalView _updateActiveBars];
-[_UIStatusBarWifiSignalView _updateCycleAnimationIfNeeded];
-[_UIStatusBarWifiSignalView cycleAnimation];
-[_UIStatusBarWifiSignalView layoutSubviews];
-[_UIStatusBarWifiSignalView _colorsDidChange];
-[_UIStatusBarWifiSignalView _updateBars];
-[_UIStatusBarWifiSignalView setCycleAnimation:];
-[_UIStatusBarWifiSignalView _updateCycleAnimationNow];
-[_UIStatusBarWifiSignalView needsCycleAnimationUpdate];
-[_UIStatusBarWifiSignalView _updateFromMode:];
-[_UIStatusBarWifiSignalView setNeedsCycleAnimationUpdate:];
-[_UIStatusBarWifiSignalView _barCornerRadius];
```
