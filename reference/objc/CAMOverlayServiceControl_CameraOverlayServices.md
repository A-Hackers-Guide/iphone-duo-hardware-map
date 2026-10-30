# `CAMOverlayServiceControl`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAbstractOverlayServiceControl`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSString" _captureDeviceUniqueID;
q _captureDeviceProperty;
@"<CAMOverlayValueRange>" _valueRange;
@"NSString" _valueFormat;
@"CAMOverlayDiscreteFloatRange" _primaryValues;
q _rangeScale;
```

## Properties

```
@property (T@"NSString",&,N,V_captureDeviceUniqueID) captureDeviceUniqueID;
@property (Tq,N,V_captureDeviceProperty) captureDeviceProperty;
@property (T@"<CAMOverlayValueRange>",&,N,V_valueRange) valueRange;
@property (T@"NSString",&,N,V_valueFormat) valueFormat;
@property (T@"CAMOverlayDiscreteFloatRange",&,N,V_primaryValues) primaryValues;
@property (T@"NSString",&,D,N) imageName;
@property (T@"NSString",&,D,N) title;
@property (Tq,N,V_rangeScale) rangeScale;
```

## Class methods

```
+[CAMOverlayServiceControl supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayServiceControl valueFormat];
-[CAMOverlayServiceControl captureDeviceUniqueID];
-[CAMOverlayServiceControl init];
-[CAMOverlayServiceControl rangeScale];
-[CAMOverlayServiceControl valueRange];
-[CAMOverlayServiceControl encodeWithCoder:];
-[CAMOverlayServiceControl setImageName:];
-[CAMOverlayServiceControl initWithCoder:];
-[CAMOverlayServiceControl setTitle:];
-[CAMOverlayServiceControl copyWithZone:];
-[CAMOverlayServiceControl primaryValues];
-[CAMOverlayServiceControl initWithIdentifier:];
-[CAMOverlayServiceControl setValueFormat:];
-[CAMOverlayServiceControl setCaptureDeviceUniqueID:];
-[CAMOverlayServiceControl setValueRange:];
-[CAMOverlayServiceControl captureDeviceProperty];
-[CAMOverlayServiceControl setCaptureDeviceProperty:];
-[CAMOverlayServiceControl setPrimaryValues:];
-[CAMOverlayServiceControl setRangeScale:];
```
