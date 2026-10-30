# `UIColorWell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIDragInteractionDelegate`, `UIDropInteractionDelegate`, `_UIColorPickerViewControllerDelegate`, `_UIColorWellControl`
- 10 instance variables, 11 properties, 39 instance methods, 1 class methods

## Instance variables

```
@"_UIColorWellVisualStyle" _style;
@"UIColorPickerViewController" _colorPicker;
@"UIDragInteraction" _dragInteraction;
@"UIDropInteraction" _dropInteraction;
B _supportsAlpha;
B _supportsEyedropper;
@"UIColor" _selectedColor;
@"NSString" _title;
d _maximumLinearExposure;
@"<_UIColorWellDelegate>" __delegate;
```

## Properties

```
@property (T@"<_UIColorWellDelegate>",W,N,V__delegate) _delegate;
@property (Td,N) maxGain;
@property (T@"NSString",C,N,V_title) title;
@property (TB,N,V_supportsAlpha) supportsAlpha;
@property (T@"UIColor",&,N,V_selectedColor) selectedColor;
@property (TB,N,V_supportsEyedropper) supportsEyedropper;
@property (Td,N,V_maximumLinearExposure) maximumLinearExposure;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIColorWell styleForColorWell:];
```

## Instance methods

```
-[UIColorWell dragInteraction:previewForLiftingItem:session:];
-[UIColorWell _controlEventsForActionTriggered];
-[UIColorWell _commonInit];
-[UIColorWell dragInteraction:itemsForBeginningSession:];
-[UIColorWell dropInteraction:sessionDidUpdate:];
-[UIColorWell dropInteraction:performDrop:];
-[UIColorWell setMaxGain:];
-[UIColorWell _intrinsicSizeWithinSize:];
-[UIColorWell dropInteraction:canHandleSession:];
-[UIColorWell layoutSubviews];
-[UIColorWell _delegate];
-[UIColorWell sizeThatFits:];
-[UIColorWell _contentHuggingDefault_isUsuallyFixedHeight];
-[UIColorWell title];
-[UIColorWell encodeWithCoder:];
-[UIColorWell set_delegate:];
-[UIColorWell maxGain];
-[UIColorWell initWithCoder:];
-[UIColorWell setTitle:];
-[UIColorWell _populateArchivedSubviews:];
-[UIColorWell initWithFrame:];
-[UIColorWell _contentHuggingDefault_isUsuallyFixedWidth];
-[UIColorWell setPickerTitle:];
-[UIColorWell _colorPickerViewControllerDidDeselectColor:];
-[UIColorWell _colorPickerViewControllerDidHideEyedropper:];
-[UIColorWell _colorPickerViewControllerDidShowEyedropper:];
-[UIColorWell _setSelectedColor:notifyingStyle:notifyingUIPicker:sendingAction:];
-[UIColorWell _setSupportsEyedropper:];
-[UIColorWell colorPickerViewController:didSelectColor:continuously:];
-[UIColorWell maximumLinearExposure];
-[UIColorWell selectedColor];
-[UIColorWell setMaximumLinearExposure:];
-[UIColorWell setSelectedColor:];
-[UIColorWell setSupportsAlpha:];
-[UIColorWell setSupportsEyedropper:];
-[UIColorWell styleDidSelectColor:];
-[UIColorWell styleRequestedColorPickerPresentation];
-[UIColorWell supportsAlpha];
-[UIColorWell supportsEyedropper];
```
