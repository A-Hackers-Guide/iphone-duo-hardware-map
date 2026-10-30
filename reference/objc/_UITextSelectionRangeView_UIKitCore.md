# `_UITextSelectionRangeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"UIColor" _selectionColor;
@"UIColor" _selectionBorderColor;
d _selectionBorderWidth;
```

## Properties

```
@property (T@"CAShapeLayer",R,N) pathLayer;
@property (T^{CGPath=},N) path;
@property (T@"UIColor",&,N,V_selectionColor) selectionColor;
@property (T@"UIColor",&,N,V_selectionBorderColor) selectionBorderColor;
@property (Td,N,V_selectionBorderWidth) selectionBorderWidth;
```

## Class methods

```
+[_UITextSelectionRangeView layerClass];
```

## Instance methods

```
-[_UITextSelectionRangeView _dynamicUserInterfaceTraitDidChange];
-[_UITextSelectionRangeView selectionBorderColor];
-[_UITextSelectionRangeView setSelectionBorderColor:];
-[_UITextSelectionRangeView setSelectionBorderWidth:];
-[_UITextSelectionRangeView setPath:];
-[_UITextSelectionRangeView selectionColor];
-[_UITextSelectionRangeView selectionBorderWidth];
-[_UITextSelectionRangeView setSelectionColor:];
-[_UITextSelectionRangeView pathLayer];
-[_UITextSelectionRangeView path];
```
