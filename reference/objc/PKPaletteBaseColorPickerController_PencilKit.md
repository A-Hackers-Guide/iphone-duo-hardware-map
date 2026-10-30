# `PKPaletteBaseColorPickerController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKPaletteColorPickerController`, `PKPaletteColorPicker`
- 6 instance variables, 11 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _supportsAlpha;
@"<PKPaletteColorPicker>" _colorPicker;
@"UIViewController" _viewController;
@"<PKPaletteColorPickerControllerDelegate>" _delegate;
@"UIColor" _selectedColor;
q _colorAppearance;
```

## Properties

```
@property (T@"<PKPaletteColorPicker>",R,N,V_colorPicker) colorPicker;
@property (T@"UIViewController",R,N,V_viewController) viewController;
@property (Td,N) colorMaximumLinearExposure;
@property (T@"<PKPaletteColorPickerControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIColor",C,N,V_selectedColor) selectedColor;
@property (TB,N,V_supportsAlpha) supportsAlpha;
@property (Tq,N,V_colorAppearance) colorAppearance;
```

## Instance methods

```
-[PKPaletteBaseColorPickerController viewController];
-[PKPaletteBaseColorPickerController setDelegate:];
-[PKPaletteBaseColorPickerController delegate];
-[PKPaletteBaseColorPickerController selectedColor];
-[PKPaletteBaseColorPickerController setSelectedColor:];
-[PKPaletteBaseColorPickerController setSupportsAlpha:];
-[PKPaletteBaseColorPickerController supportsAlpha];
-[PKPaletteBaseColorPickerController colorPicker];
-[PKPaletteBaseColorPickerController colorAppearance];
-[PKPaletteBaseColorPickerController colorMaximumLinearExposure];
-[PKPaletteBaseColorPickerController dismissEyeDropper];
-[PKPaletteBaseColorPickerController setColorAppearance:];
-[PKPaletteBaseColorPickerController setColorMaximumLinearExposure:];
-[PKPaletteBaseColorPickerController setSelectedColorForPoint:];
```
