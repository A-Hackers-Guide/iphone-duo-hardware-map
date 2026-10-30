# `UITextSelectionRectView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"UIColor" _selectionColor;
@"UIColor" _selectionBorderColor;
d _selectionBorderWidth;
d _selectionCornerRadius;
```

## Properties

```
@property (TB,R,N) hasPath;
@property (T@"CAShapeLayer",R,N) pathLayer;
@property (T@"UIColor",&,N,V_selectionColor) selectionColor;
@property (T@"UIColor",&,N,V_selectionBorderColor) selectionBorderColor;
@property (Td,N,V_selectionBorderWidth) selectionBorderWidth;
@property (Td,N,V_selectionCornerRadius) selectionCornerRadius;
```

## Class methods

```
+[UITextSelectionRectView layerClass];
```

## Instance methods

```
-[UITextSelectionRectView _dynamicUserInterfaceTraitDidChange];
-[UITextSelectionRectView selectionBorderColor];
-[UITextSelectionRectView selectionCornerRadius];
-[UITextSelectionRectView setSelectionBorderColor:];
-[UITextSelectionRectView setSelectionCornerRadius:];
-[UITextSelectionRectView setSelectionBorderWidth:];
-[UITextSelectionRectView setPath:];
-[UITextSelectionRectView selectionColor];
-[UITextSelectionRectView selectionBorderWidth];
-[UITextSelectionRectView setSelectionColor:];
-[UITextSelectionRectView pathLayer];
-[UITextSelectionRectView path];
-[UITextSelectionRectView hasPath];
```
