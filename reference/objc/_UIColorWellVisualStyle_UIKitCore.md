# `_UIColorWellVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _supportsAlpha;
B _supportsEyedropper;
B _wantsSystemDragAndDrop;
B _wantsExtraTouchInsets;
@"<_UIColorWellControl>" _colorWell;
@"UIColor" _selectedColor;
@"NSString" _pickerTitle;
d _maxGain;
@"UIDragPreviewParameters" _dragPreviewParameters;
```

## Properties

```
@property (T@"<_UIColorWellControl>",W,N,V_colorWell) colorWell;
@property (T@"UIColor",&,N,V_selectedColor) selectedColor;
@property (T@"NSString",&,N,V_pickerTitle) pickerTitle;
@property (TB,N,V_supportsAlpha) supportsAlpha;
@property (TB,N,V_supportsEyedropper) supportsEyedropper;
@property (Td,N,V_maxGain) maxGain;
@property (TB,N,V_wantsSystemDragAndDrop) wantsSystemDragAndDrop;
@property (TB,N,V_wantsExtraTouchInsets) wantsExtraTouchInsets;
@property (T@"UIDragPreviewParameters",R,N,V_dragPreviewParameters) dragPreviewParameters;
```

## Instance methods

```
-[_UIColorWellVisualStyle setMaxGain:];
-[_UIColorWellVisualStyle maxGain];
-[_UIColorWellVisualStyle intrinsicSizeWithinSize:];
-[_UIColorWellVisualStyle setPickerTitle:];
-[_UIColorWellVisualStyle colorWell];
-[_UIColorWellVisualStyle dragPreviewParameters];
-[_UIColorWellVisualStyle initWithColorWell:];
-[_UIColorWellVisualStyle pickerTitle];
-[_UIColorWellVisualStyle selectedColor];
-[_UIColorWellVisualStyle setColorWell:];
-[_UIColorWellVisualStyle setSelectedColor:];
-[_UIColorWellVisualStyle setSelectedColor:notifyingPicker:];
-[_UIColorWellVisualStyle setSupportsAlpha:];
-[_UIColorWellVisualStyle setSupportsEyedropper:];
-[_UIColorWellVisualStyle setWantsExtraTouchInsets:];
-[_UIColorWellVisualStyle setWantsSystemDragAndDrop:];
-[_UIColorWellVisualStyle supportsAlpha];
-[_UIColorWellVisualStyle supportsEyedropper];
-[_UIColorWellVisualStyle wantsExtraTouchInsets];
-[_UIColorWellVisualStyle wantsSystemDragAndDrop];
```
