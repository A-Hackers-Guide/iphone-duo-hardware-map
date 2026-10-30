# `_UITextFieldPasscodeCutoutBackground`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextFieldBackgroundView`
- 5 instance variables, 3 properties, 25 instance methods, 3 class methods

## Instance variables

```
B _hasCustomStrokeColor;
B _hasCustomFillColor;
@"CAShapeLayer" _lighteningOutline;
d _outlineAlpha;
d _cornerRadius;
```

## Properties

```
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T@"UIBezierPath",R,N) customPath;
@property (Td,N) outlineAlpha;
```

## Class methods

```
+[_UITextFieldPasscodeCutoutBackground _strokeColor:];
+[_UITextFieldPasscodeCutoutBackground _fillColor:];
+[_UITextFieldPasscodeCutoutBackground layerClass];
```

## Instance methods

```
-[_UITextFieldPasscodeCutoutBackground setEnabled:animated:];
-[_UITextFieldPasscodeCutoutBackground lineWidth];
-[_UITextFieldPasscodeCutoutBackground _strokeColor:];
-[_UITextFieldPasscodeCutoutBackground setLineWidth:];
-[_UITextFieldPasscodeCutoutBackground setFillColor:];
-[_UITextFieldPasscodeCutoutBackground fillColor];
-[_UITextFieldPasscodeCutoutBackground _fillColor:];
-[_UITextFieldPasscodeCutoutBackground setStrokeColor:];
-[_UITextFieldPasscodeCutoutBackground setActive:];
-[_UITextFieldPasscodeCutoutBackground strokeColor];
-[_UITextFieldPasscodeCutoutBackground setCornerRadius:];
-[_UITextFieldPasscodeCutoutBackground setBounds:];
-[_UITextFieldPasscodeCutoutBackground cornerRadius];
-[_UITextFieldPasscodeCutoutBackground initWithFrame:active:];
-[_UITextFieldPasscodeCutoutBackground setFrame:];
-[_UITextFieldPasscodeCutoutBackground _shouldAnimatePropertyWithKey:];
-[_UITextFieldPasscodeCutoutBackground initWithFrame:];
-[_UITextFieldPasscodeCutoutBackground _pathInset];
-[_UITextFieldPasscodeCutoutBackground _shapeLayer];
-[_UITextFieldPasscodeCutoutBackground _updateLightingOutlinePath];
-[_UITextFieldPasscodeCutoutBackground _updatePath];
-[_UITextFieldPasscodeCutoutBackground customPath];
-[_UITextFieldPasscodeCutoutBackground outlineAlpha];
-[_UITextFieldPasscodeCutoutBackground setLineWidth:updatePath:];
-[_UITextFieldPasscodeCutoutBackground setOutlineAlpha:];
```
