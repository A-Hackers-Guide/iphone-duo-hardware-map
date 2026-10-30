# `_UIPrototypingMenuNumberCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIPrototypingMenuCell`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
d _min;
d _max;
d _current;
@"UIStackView" _floatValueStackView;
@"UILabel" _minLabel;
@"UILabel" _maxLabel;
@"_UIPrototypingMenuSlider" _slider;
@"UITapGestureRecognizer" _tapRecognizer;
```

## Properties

```
@property (T@"UIStackView",&,N,V_floatValueStackView) floatValueStackView;
@property (T@"UILabel",&,N,V_minLabel) minLabel;
@property (T@"UILabel",&,N,V_maxLabel) maxLabel;
@property (T@"_UIPrototypingMenuSlider",&,N,V_slider) slider;
@property (T@"UITapGestureRecognizer",&,N,V_tapRecognizer) tapRecognizer;
@property (Td,N,V_min) min;
@property (Td,N,V_max) max;
@property (Td,N,V_current) current;
```

## Instance methods

```
-[_UIPrototypingMenuNumberCell tapRecognizer];
-[_UIPrototypingMenuNumberCell min];
-[_UIPrototypingMenuNumberCell setSlider:];
-[_UIPrototypingMenuNumberCell max];
-[_UIPrototypingMenuNumberCell current];
-[_UIPrototypingMenuNumberCell slider];
-[_UIPrototypingMenuNumberCell initWithStyle:reuseIdentifier:];
-[_UIPrototypingMenuNumberCell setMax:];
-[_UIPrototypingMenuNumberCell setTapRecognizer:];
-[_UIPrototypingMenuNumberCell setMin:];
-[_UIPrototypingMenuNumberCell _prototypingSettingDidChange];
-[_UIPrototypingMenuNumberCell _sliderDidChangeValue:];
-[_UIPrototypingMenuNumberCell _tapRecognizerDidRecognizer:];
-[_UIPrototypingMenuNumberCell floatValueStackView];
-[_UIPrototypingMenuNumberCell maxLabel];
-[_UIPrototypingMenuNumberCell minLabel];
-[_UIPrototypingMenuNumberCell setCurrent:];
-[_UIPrototypingMenuNumberCell setFloatValueStackView:];
-[_UIPrototypingMenuNumberCell setMaxLabel:];
-[_UIPrototypingMenuNumberCell setMinLabel:];
```
