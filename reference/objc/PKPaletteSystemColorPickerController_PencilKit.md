# `PKPaletteSystemColorPickerController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteBaseColorPickerController`
- Protocols: `UIColorPickerViewControllerDelegate`
- 3 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _onlyConvertsBlackAndWhiteInDark;
d _colorMaximumLinearExposure;
@"UIColorPickerViewController" _colorPickerViewController;
```

## Properties

```
@property (T@"UIColorPickerViewController",&,N,V_colorPickerViewController) colorPickerViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteSystemColorPickerController init];
-[PKPaletteSystemColorPickerController viewController];
-[PKPaletteSystemColorPickerController colorPickerViewController:didSelectColor:continuously:];
-[PKPaletteSystemColorPickerController selectedColor];
-[PKPaletteSystemColorPickerController setSelectedColor:];
-[PKPaletteSystemColorPickerController setSupportsAlpha:];
-[PKPaletteSystemColorPickerController supportsAlpha];
-[PKPaletteSystemColorPickerController colorAppearance];
-[PKPaletteSystemColorPickerController _shouldConvertColorPickerColorFromDarkToLight];
-[PKPaletteSystemColorPickerController _shouldConvertColorPickerColorFromDarkToLight:];
-[PKPaletteSystemColorPickerController colorMaximumLinearExposure];
-[PKPaletteSystemColorPickerController colorPickerViewController];
-[PKPaletteSystemColorPickerController dismissEyeDropper];
-[PKPaletteSystemColorPickerController setColorAppearance:];
-[PKPaletteSystemColorPickerController setColorMaximumLinearExposure:];
-[PKPaletteSystemColorPickerController setColorPickerViewController:];
```
