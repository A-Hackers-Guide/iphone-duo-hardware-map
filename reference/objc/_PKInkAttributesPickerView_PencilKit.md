# `_PKInkAttributesPickerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_PKColorAlphaSliderDelegate`
- 13 instance variables, 18 properties, 39 instance methods, 1 class methods

## Instance variables

```
B _showsTopSeparator;
@"<_PKInkAttributesPickerViewDelegate>" _delegate;
@"PKInk" _ink;
Q _displayMode;
d _minimumOpacityValue;
@"_PKInkThicknessPicker" _azimuthPicker;
@"_PKInkThicknessPicker" _thicknessPicker;
@"UIView" _colorAlphaSliderView;
@"<_PKColorAlphaSlider>" _colorAlphaSlider;
@"PKToolConfiguration" _toolConfiguration;
@"UIView" _topSeparatorView;
@"UIView" _middleSeparatorView;
@"UIView" _middleSeparatorViewB;
```

## Properties

```
@property (T@"_PKInkThicknessPicker",&,N,V_azimuthPicker) azimuthPicker;
@property (T@"_PKInkThicknessPicker",&,N,V_thicknessPicker) thicknessPicker;
@property (T@"UIView",&,N,V_colorAlphaSliderView) colorAlphaSliderView;
@property (T@"<_PKColorAlphaSlider>",&,N,V_colorAlphaSlider) colorAlphaSlider;
@property (T@"PKToolConfiguration",&,N,V_toolConfiguration) toolConfiguration;
@property (T@"UIView",&,N,V_topSeparatorView) topSeparatorView;
@property (T@"UIView",&,N,V_middleSeparatorView) middleSeparatorView;
@property (T@"UIView",&,N,V_middleSeparatorViewB) middleSeparatorViewB;
@property (T@"<_PKInkAttributesPickerViewDelegate>",W,N,V_delegate) delegate;
@property (T@"PKInk",&,N,V_ink) ink;
@property (TQ,N,V_displayMode) displayMode;
@property (Tq,N) colorAppearance;
@property (Td,N,V_minimumOpacityValue) minimumOpacityValue;
@property (TB,N,V_showsTopSeparator) showsTopSeparator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_PKInkAttributesPickerView angleWeightsToImages];
```

## Instance methods

```
-[_PKInkAttributesPickerView showsTopSeparator];
-[_PKInkAttributesPickerView setDisplayMode:];
-[_PKInkAttributesPickerView displayMode];
-[_PKInkAttributesPickerView layoutSubviews];
-[_PKInkAttributesPickerView sizeThatFits:];
-[_PKInkAttributesPickerView setShowsTopSeparator:];
-[_PKInkAttributesPickerView setDelegate:];
-[_PKInkAttributesPickerView ink];
-[_PKInkAttributesPickerView delegate];
-[_PKInkAttributesPickerView _updateUI];
-[_PKInkAttributesPickerView setInk:];
-[_PKInkAttributesPickerView topSeparatorView];
-[_PKInkAttributesPickerView setTopSeparatorView:];
-[_PKInkAttributesPickerView thicknessPicker];
-[_PKInkAttributesPickerView colorAppearance];
-[_PKInkAttributesPickerView _azimuthValueChanged:];
-[_PKInkAttributesPickerView _colorAlphaSliderUserDidChangeSlider:];
-[_PKInkAttributesPickerView _colorAlphaSliderUserDidEndDraggingSlider:];
-[_PKInkAttributesPickerView _colorAlphaSliderUserDidStartDraggingSlider:];
-[_PKInkAttributesPickerView _opacityValueChanged:];
-[_PKInkAttributesPickerView _thicknessValueChanged:];
-[_PKInkAttributesPickerView azimuthPicker];
-[_PKInkAttributesPickerView colorAlphaSlider];
-[_PKInkAttributesPickerView colorAlphaSliderView];
-[_PKInkAttributesPickerView initWithInk:toolConfiguration:];
-[_PKInkAttributesPickerView middleSeparatorView];
-[_PKInkAttributesPickerView middleSeparatorViewB];
-[_PKInkAttributesPickerView minimumOpacityValue];
-[_PKInkAttributesPickerView setAzimuthPicker:];
-[_PKInkAttributesPickerView setColorAlphaSlider:];
-[_PKInkAttributesPickerView setColorAlphaSliderView:];
-[_PKInkAttributesPickerView setColorAppearance:];
-[_PKInkAttributesPickerView setInk:animated:];
-[_PKInkAttributesPickerView setMiddleSeparatorView:];
-[_PKInkAttributesPickerView setMiddleSeparatorViewB:];
-[_PKInkAttributesPickerView setMinimumOpacityValue:];
-[_PKInkAttributesPickerView setThicknessPicker:];
-[_PKInkAttributesPickerView setToolConfiguration:];
-[_PKInkAttributesPickerView toolConfiguration];
```
