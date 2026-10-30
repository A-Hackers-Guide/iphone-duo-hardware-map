# `UIStatusBarSignalStrengthItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- 6 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
i _signalStrengthRaw;
i _signalStrengthBars;
B _enableRSSI;
B _showRSSI;
B _showFailure;
B _useSmallBars;
```

## Instance methods

```
-[UIStatusBarSignalStrengthItemView touchesEnded:withEvent:];
-[UIStatusBarSignalStrengthItemView accessibilityHUDRepresentation];
-[UIStatusBarSignalStrengthItemView contentsImage];
-[UIStatusBarSignalStrengthItemView _signalStrengthBarsImageName];
-[UIStatusBarSignalStrengthItemView _stringForRSSI];
-[UIStatusBarSignalStrengthItemView _updateWithRaw:bars:enableRSSI:showFailure:useSmallBars:];
-[UIStatusBarSignalStrengthItemView extraLeftPadding];
-[UIStatusBarSignalStrengthItemView extraRightPadding];
-[UIStatusBarSignalStrengthItemView updateForNewData:actions:];
```
