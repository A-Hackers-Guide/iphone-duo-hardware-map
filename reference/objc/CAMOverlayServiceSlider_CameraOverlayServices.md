# `CAMOverlayServiceSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAbstractOverlayServiceControl`
- 11 instance variables, 8 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"<CAMOverlayValueRange>" _displayValueRange;
@"NSArray" _displayValues;
@"NSArray" _values;
q _sliderType;
@"<CAMOverlayFloatValueRange>" _valueRange;
@"NSDictionary" _displayValuesByValue;
@"NSString" _captureDeviceUniqueID;
@"NSString" _captureSessionUniqueID;
@"CAMOverlayDiscreteFloatRange" _primaryValues;
q _rangeScale;
@"NSString" _valueFormat;
```

## Properties

```
@property (Tq,R,N,V_sliderType) sliderType;
@property (T@"<CAMOverlayFloatValueRange>",R,N,V_valueRange) valueRange;
@property (T@"NSDictionary",&,N,V_displayValuesByValue) displayValuesByValue;
@property (T@"NSString",R,N,V_captureDeviceUniqueID) captureDeviceUniqueID;
@property (T@"NSString",R,N,V_captureSessionUniqueID) captureSessionUniqueID;
@property (T@"CAMOverlayDiscreteFloatRange",R,N,V_primaryValues) primaryValues;
@property (Tq,R,N,V_rangeScale) rangeScale;
@property (T@"NSString",C,N,V_valueFormat) valueFormat;
```

## Class methods

```
+[CAMOverlayServiceSlider supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayServiceSlider captureSessionUniqueID];
-[CAMOverlayServiceSlider valueFormat];
-[CAMOverlayServiceSlider captureDeviceUniqueID];
-[CAMOverlayServiceSlider values];
-[CAMOverlayServiceSlider _initWithIdentifier:sliderType:captureUniqueID:zoomRange:];
-[CAMOverlayServiceSlider isContentEqual:];
-[CAMOverlayServiceSlider rangeScale];
-[CAMOverlayServiceSlider isEnabled];
-[CAMOverlayServiceSlider displayValues];
-[CAMOverlayServiceSlider initPhotoZoomSliderWithIdentifier:maximumZoomFactor:captureDeviceUniqueID:];
-[CAMOverlayServiceSlider valueRange];
-[CAMOverlayServiceSlider initWithIdentifier:sliderType:captureUniqueID:];
-[CAMOverlayServiceSlider sliderType];
-[CAMOverlayServiceSlider controlType];
-[CAMOverlayServiceSlider encodeWithCoder:];
-[CAMOverlayServiceSlider initVideoZoomSliderWithIdentifier:maximumZoomFactor:captureDeviceUniqueID:];
-[CAMOverlayServiceSlider updateWithRecording:];
-[CAMOverlayServiceSlider initWithCoder:];
-[CAMOverlayServiceSlider sliderWithPrimaryValues:];
-[CAMOverlayServiceSlider displayValuesByValue];
-[CAMOverlayServiceSlider copyWithZone:];
-[CAMOverlayServiceSlider updateWithFloatValue:];
-[CAMOverlayServiceSlider primaryValues];
-[CAMOverlayServiceSlider sliderUnpackingDisplayValuesIfNeeded];
-[CAMOverlayServiceSlider setDisplayValuesByValue:];
-[CAMOverlayServiceSlider setValueFormat:];
-[CAMOverlayServiceSlider initWithIdentifier:title:imageName:rangeScale:valueRange:primaryValues:];
-[CAMOverlayServiceSlider displayValueRange];
-[CAMOverlayServiceSlider updateWithStyleDictionary:];
```
