# `CEKApertureSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CEKDiscreteSlider`
- Protocols: `UIScrollViewDelegate`
- 6 instance variables, 15 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _includesOffState;
B __valueLabelDisabled;
Q __minimumApertureIndex;
Q __maximumApertureIndex;
@"NSNumberFormatter" __decimalFormatter;
@"NSNumberFormatter" __wholeNumberFormatter;
```

## Properties

```
@property (TQ,N,S_setMinimumApertureIndex:,V__minimumApertureIndex) _minimumApertureIndex;
@property (TQ,N,S_setMaximumApertureIndex:,V__maximumApertureIndex) _maximumApertureIndex;
@property (T@"NSNumberFormatter",R,N,V__decimalFormatter) _decimalFormatter;
@property (T@"NSNumberFormatter",R,N,V__wholeNumberFormatter) _wholeNumberFormatter;
@property (TB,N,V__valueLabelDisabled) _valueLabelDisabled;
@property (Td,R,N) apertureValue;
@property (Td,R,N) minimumApertureValue;
@property (Td,R,N) maximumApertureValue;
@property (Td,R,N) markedApertureValue;
@property (TB,N,V_includesOffState) includesOffState;
@property (TB,N,GisSliderOn) sliderOn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CEKApertureSlider accessibilityIdentifier];
-[CEKApertureSlider setMinimumApertureValueClosestTo:maximumApertureValueClosestTo:];
-[CEKApertureSlider apertureValue];
-[CEKApertureSlider includesOffState];
-[CEKApertureSlider initWithTickMarkStyle:];
-[CEKApertureSlider isSliderOn];
-[CEKApertureSlider markedApertureValue];
-[CEKApertureSlider maximumApertureValue];
-[CEKApertureSlider minimumApertureValue];
-[CEKApertureSlider setApertureValueClosestTo:];
-[CEKApertureSlider setIncludesOffState:];
-[CEKApertureSlider setMarkedApertureValueClosestTo:];
-[CEKApertureSlider setSliderOn:];
-[CEKApertureSlider _valueLabelDisabled];
-[CEKApertureSlider horizontalValueLabelOffset];
-[CEKApertureSlider initWithTickMarkStyle:valueLabelDisabled:];
-[CEKApertureSlider setApertureValueClosestTo:animated:];
-[CEKApertureSlider set_valueLabelDisabled:];
-[CEKApertureSlider valueText];
-[CEKApertureSlider _decimalFormatter];
-[CEKApertureSlider _discreteIndexForValidApertureIndex:];
-[CEKApertureSlider _maximumApertureIndex];
-[CEKApertureSlider _minimumApertureIndex];
-[CEKApertureSlider _setMaximumApertureIndex:];
-[CEKApertureSlider _setMinimumApertureIndex:];
-[CEKApertureSlider _updateIndexCount];
-[CEKApertureSlider _updateMainTickMarkOffset];
-[CEKApertureSlider _validApertureIndexForDiscreteIndex:];
-[CEKApertureSlider _wholeNumberFormatter];
-[CEKApertureSlider setMarkedApertureValueToNone];
```
