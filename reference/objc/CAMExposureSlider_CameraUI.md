# `CAMExposureSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CEKDiscreteSlider`
- 2 instance variables, 3 properties, 14 instance methods, 4 class methods

## Instance variables

```
B __valueLabelDisabled;
d __previousHorizontalLabelOffset;
```

## Properties

```
@property (Td,N,V__previousHorizontalLabelOffset) _previousHorizontalLabelOffset;
@property (TB,N,V__valueLabelDisabled) _valueLabelDisabled;
@property (Td,R,N) exposureValue;
```

## Class methods

```
+[CAMExposureSlider minimumValue];
+[CAMExposureSlider maximumValue];
+[CAMExposureSlider exposureValues];
+[CAMExposureSlider decimalFormatter];
```

## Instance methods

```
-[CAMExposureSlider accessibilityIdentifier];
-[CAMExposureSlider initWithTickMarkStyle:];
-[CAMExposureSlider _indexOfClosestValidValueForExposureValue:];
-[CAMExposureSlider _previousHorizontalLabelOffset];
-[CAMExposureSlider _valueLabelDisabled];
-[CAMExposureSlider exposureValue];
-[CAMExposureSlider horizontalValueLabelOffset];
-[CAMExposureSlider initWithTickMarkStyle:valueLabelDisabled:];
-[CAMExposureSlider setExposureValueClosestTo:];
-[CAMExposureSlider setExposureValueClosestTo:animated:];
-[CAMExposureSlider set_previousHorizontalLabelOffset:];
-[CAMExposureSlider set_valueLabelDisabled:];
-[CAMExposureSlider updateValueLabel];
-[CAMExposureSlider valueText];
```
