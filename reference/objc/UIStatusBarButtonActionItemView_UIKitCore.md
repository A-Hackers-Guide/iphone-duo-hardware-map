# `UIStatusBarButtonActionItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- 4 instance variables, 3 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UIButton" _button;
@"UIButton" _externalButton;
B _selected;
@"CALayer" _ringLayer;
```

## Properties

```
@property (TB,N,V_selected) selected;
@property (T@"CALayer",&,N,V_ringLayer) ringLayer;
@property (TB,R,N) extendsHitTestingFrame;
```

## Instance methods

```
-[UIStatusBarButtonActionItemView buttonType];
-[UIStatusBarButtonActionItemView setSelected:];
-[UIStatusBarButtonActionItemView didUpdateFocusInContext:withAnimationCoordinator:];
-[UIStatusBarButtonActionItemView pressesCancelled:withEvent:];
-[UIStatusBarButtonActionItemView pressesEnded:withEvent:];
-[UIStatusBarButtonActionItemView layoutSubviews];
-[UIStatusBarButtonActionItemView canBecomeFocused];
-[UIStatusBarButtonActionItemView pressesBegan:withEvent:];
-[UIStatusBarButtonActionItemView pointInside:withEvent:];
-[UIStatusBarButtonActionItemView selected];
-[UIStatusBarButtonActionItemView allowsUserInteraction];
-[UIStatusBarButtonActionItemView _contentsImageFrame];
-[UIStatusBarButtonActionItemView _createButton];
-[UIStatusBarButtonActionItemView _doubleTapButton:];
-[UIStatusBarButtonActionItemView _pressAndHoldButton:];
-[UIStatusBarButtonActionItemView _pressButton:];
-[UIStatusBarButtonActionItemView _triggerButtonWithAction:];
-[UIStatusBarButtonActionItemView extendsHitTestingFrame];
-[UIStatusBarButtonActionItemView highlightImage];
-[UIStatusBarButtonActionItemView ringLayer];
-[UIStatusBarButtonActionItemView setLayerHighlightImage:];
-[UIStatusBarButtonActionItemView setRingLayer:];
-[UIStatusBarButtonActionItemView showsTouchWhenHighlighted];
-[UIStatusBarButtonActionItemView updateContentsAndWidth];
-[UIStatusBarButtonActionItemView usesAdvancedActions];
```
