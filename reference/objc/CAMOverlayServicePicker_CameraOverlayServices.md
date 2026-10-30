# `CAMOverlayServicePicker`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAbstractOverlayServiceControl`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _pickerType;
@"NSString" _captureSessionUniqueID;
@"NSArray" _valueTitles;
```

## Properties

```
@property (Tq,R,N,V_pickerType) pickerType;
@property (T@"NSString",R,N,V_captureSessionUniqueID) captureSessionUniqueID;
@property (T@"NSArray",R,N,V_valueTitles) valueTitles;
```

## Class methods

```
+[CAMOverlayServicePicker supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayServicePicker captureSessionUniqueID];
-[CAMOverlayServicePicker pickerType];
-[CAMOverlayServicePicker valueTitles];
-[CAMOverlayServicePicker isContentEqual:];
-[CAMOverlayServicePicker isEnabled];
-[CAMOverlayServicePicker initWithIdentifier:pickerType:captureUniqueID:];
-[CAMOverlayServicePicker controlType];
-[CAMOverlayServicePicker encodeWithCoder:];
-[CAMOverlayServicePicker updateWithIndexValue:];
-[CAMOverlayServicePicker initWithCoder:];
-[CAMOverlayServicePicker initWithIdentifier:title:imageName:valueTitles:];
-[CAMOverlayServicePicker copyWithZone:];
-[CAMOverlayServicePicker updateWithStyleDictionary:];
```
