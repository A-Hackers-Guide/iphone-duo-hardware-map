# `PKVariableSliderView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"UISlider" _slider;
@"UILabel" _label;
@"UIVisualEffectView" _blurView;
d _lastSentTimestamp;
d _valueToSend;
@"<PKVariableSliderViewDelegate>" _delegate;
d _currentValue;
q _fractionalDigits;
d _initialValue;
```

## Instance methods

```
-[PKVariableSliderView intrinsicContentSize];
-[PKVariableSliderView layoutSubviews];
-[PKVariableSliderView sendValueChanged];
-[PKVariableSliderView sliderValueChanged];
```
