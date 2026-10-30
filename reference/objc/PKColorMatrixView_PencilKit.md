# `PKColorMatrixView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKColorPickerCrosshairViewDelegate`, `_PKColorPickerImplementation`
- 6 instance variables, 10 properties, 28 instance methods, 4 class methods

## Instance variables

```
@"UIColor" selectedColor;
@"<_PKColorPickerImplementationDelegate>" _colorPickerDelegate;
q _colorAppearance;
@"NSArray" _colorMatrix;
@"NSArray" _darkColorMatrix;
@"NSArray" _colorButtons;
```

## Properties

```
@property (T@"NSArray",&,N,V_colorMatrix) colorMatrix;
@property (T@"NSArray",&,N,V_darkColorMatrix) darkColorMatrix;
@property (T@"NSArray",&,N,V_colorButtons) colorButtons;
@property (T@"UIColor",&,N,VselectedColor) selectedColor;
@property (T@"<_PKColorPickerImplementationDelegate>",W,N,V_colorPickerDelegate) colorPickerDelegate;
@property (Tq,N,V_colorAppearance) colorAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKColorMatrixView _representableColorForColor:];
+[PKColorMatrixView _rgbDistanceFromColor:toColor:];
+[PKColorMatrixView defaultColorMatrix];
+[PKColorMatrixView flippedColorMatrix:];
```

## Instance methods

```
-[PKColorMatrixView setColorMatrix:];
-[PKColorMatrixView layoutSubviews];
-[PKColorMatrixView colorMatrix];
-[PKColorMatrixView initWithFrame:];
-[PKColorMatrixView selectedColor];
-[PKColorMatrixView setSelectedColor:];
-[PKColorMatrixView didTapColorButton:];
-[PKColorMatrixView colorButtons];
-[PKColorMatrixView setColorButtons:];
-[PKColorMatrixView _colorForPoint:];
-[PKColorMatrixView _pointForColor:];
-[PKColorMatrixView colorAppearance];
-[PKColorMatrixView darkColorMatrix];
-[PKColorMatrixView _boundedPointForPoint:];
-[PKColorMatrixView _frameForViewWithPoint:];
-[PKColorMatrixView _pointForCGPoint:];
-[PKColorMatrixView _pointFromButton:];
-[PKColorMatrixView colorForColorPickerCrosshairView:frame:];
-[PKColorMatrixView colorPickerCrosshairViewShouldUpdateColor:point:];
-[PKColorMatrixView colorPickerCrosshairViewShouldUpdateWithColor:];
-[PKColorMatrixView colorPickerDelegate];
-[PKColorMatrixView cornerPositionForColorPickerCrosshairView:];
-[PKColorMatrixView frameForColorPickerCrosshairView:];
-[PKColorMatrixView representableColorForColor:];
-[PKColorMatrixView setColorAppearance:];
-[PKColorMatrixView setColorPickerDelegate:];
-[PKColorMatrixView setDarkColorMatrix:];
-[PKColorMatrixView uiColorMatrix];
```
