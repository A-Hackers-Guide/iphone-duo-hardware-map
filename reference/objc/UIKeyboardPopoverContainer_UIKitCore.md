# `UIKeyboardPopoverContainer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 8 instance methods, 20 class methods

## Instance variables

```
@"_UIKeyboardPopover" _popoverContainerView;
@"UIKBVisualEffectView" _backdrop;
@"_UIPopoverView" _popover;
@"_UIKeyboardPopoverAffordance" _affordance;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetFull;
d _arrowOffset;
Q _direction;
@"NSLayoutConstraint" _keyboardAreaHeight;
```

## Properties

```
@property (T@"UIView",R) affordance;
@property (T@"UIView",R) backdropParent;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) frame;
```

## Class methods

```
+[UIKeyboardPopoverContainer edgeOffset];
+[UIKeyboardPopoverContainer dragAreaHeight];
+[UIKeyboardPopoverContainer displayScale];
+[UIKeyboardPopoverContainer propertiesForTargetRect:withHeight:onScreenSize:];
+[UIKeyboardPopoverContainer pillColor];
+[UIKeyboardPopoverContainer shadowColor];
+[UIKeyboardPopoverContainer borderWidth];
+[UIKeyboardPopoverContainer cornerRadius];
+[UIKeyboardPopoverContainer contentInsets];
+[UIKeyboardPopoverContainer pillCornerRadius];
+[UIKeyboardPopoverContainer shadowOpacity];
+[UIKeyboardPopoverContainer arrowHeight];
+[UIKeyboardPopoverContainer propertiesForSpecificKeyboardFrame:onScreenSize:];
+[UIKeyboardPopoverContainer pillDistanceToEdge];
+[UIKeyboardPopoverContainer frameAtOffset:keyboardSize:screenSize:];
+[UIKeyboardPopoverContainer shadowOffset];
+[UIKeyboardPopoverContainer extraWidth];
+[UIKeyboardPopoverContainer borderColor];
+[UIKeyboardPopoverContainer shadowRadius];
+[UIKeyboardPopoverContainer pillSize];
```

## Instance methods

```
-[UIKeyboardPopoverContainer invalidate];
-[UIKeyboardPopoverContainer frame];
-[UIKeyboardPopoverContainer _updateKeyboardLayoutGuideForPopover:];
-[UIKeyboardPopoverContainer affordance];
-[UIKeyboardPopoverContainer applyProperties:];
-[UIKeyboardPopoverContainer backdropParent];
-[UIKeyboardPopoverContainer initWithView:usingBackdropStyle:];
-[UIKeyboardPopoverContainer updateBackdropStyle:];
```
