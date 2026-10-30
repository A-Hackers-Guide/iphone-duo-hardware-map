# `_PKColorPickerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_PKColorPickerImplementationDelegate`
- 6 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<_PKColorPickerViewDelegate>" _delegate;
@"UIColor" _selectedColor;
@"UIColor" _initialColor;
@"UIPanGestureRecognizer" _crosshairPanGR;
@"PKColorPickerCrosshairView" _crosshairView;
@"PKColorMatrixView" _gridColorPicker;
```

## Properties

```
@property (T@"<_PKColorPickerViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UIColor",&,N,V_selectedColor) selectedColor;
@property (T@"UIColor",&,N,V_initialColor) initialColor;
@property (T@"UIPanGestureRecognizer",&,N,V_crosshairPanGR) crosshairPanGR;
@property (T@"PKColorPickerCrosshairView",&,N,V_crosshairView) crosshairView;
@property (T@"PKColorMatrixView",&,N,V_gridColorPicker) gridColorPicker;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_PKColorPickerView layoutSubviews];
-[_PKColorPickerView sizeThatFits:];
-[_PKColorPickerView setDelegate:];
-[_PKColorPickerView delegate];
-[_PKColorPickerView initWithFrame:];
-[_PKColorPickerView selectedColor];
-[_PKColorPickerView setSelectedColor:];
-[_PKColorPickerView gridColorPicker];
-[_PKColorPickerView _setSelectedColorForPoint:];
-[_PKColorPickerView colorPickerImplementationDidChangeSelectedColor:];
-[_PKColorPickerView colorPickerImplementationUserDidTouchUpInside:];
-[_PKColorPickerView crosshairPanGR];
-[_PKColorPickerView crosshairView];
-[_PKColorPickerView didPanCrosshair:];
-[_PKColorPickerView initialColor];
-[_PKColorPickerView pointIsSignificantlyOutside:];
-[_PKColorPickerView setCrosshairPanGR:];
-[_PKColorPickerView setCrosshairView:];
-[_PKColorPickerView setGridColorPicker:];
-[_PKColorPickerView setInitialColor:];
```
