# `CAMOverlayServiceControlUpdate`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 9 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _booleanValue;
B _recording;
B _enabled;
f _floatValue;
@"NSString" _controlIdentifier;
q _valueType;
q _indexValue;
@"NSDictionary" _styleDictionary;
```

## Properties

```
@property (T@"NSString",R,N,V_controlIdentifier) controlIdentifier;
@property (Tq,R,N,V_valueType) valueType;
@property (Tf,R,N,V_floatValue) floatValue;
@property (Tq,R,N,V_indexValue) indexValue;
@property (T@"NSDictionary",R,N,V_styleDictionary) styleDictionary;
@property (TB,R,N,V_booleanValue) booleanValue;
@property (TB,R,N,GisRecording,V_recording) recording;
@property (TB,R,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N,GisValueUpdate) valueUpdate;
```

## Class methods

```
+[CAMOverlayServiceControlUpdate supportsSecureCoding];
```

## Instance methods

```
-[CAMOverlayServiceControlUpdate floatValue];
-[CAMOverlayServiceControlUpdate _valueString];
-[CAMOverlayServiceControlUpdate isRecording];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:booleanValue:];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:isRecording:];
-[CAMOverlayServiceControlUpdate indexValue];
-[CAMOverlayServiceControlUpdate debugDescription];
-[CAMOverlayServiceControlUpdate _valueTypeString];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:floatValue:];
-[CAMOverlayServiceControlUpdate valueType];
-[CAMOverlayServiceControlUpdate booleanValue];
-[CAMOverlayServiceControlUpdate styleDictionary];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:indexValue:];
-[CAMOverlayServiceControlUpdate isEnabled];
-[CAMOverlayServiceControlUpdate isEqualToUpdate:];
-[CAMOverlayServiceControlUpdate encodeWithCoder:];
-[CAMOverlayServiceControlUpdate description];
-[CAMOverlayServiceControlUpdate initWithCoder:];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:styleDictionary:];
-[CAMOverlayServiceControlUpdate controlIdentifier];
-[CAMOverlayServiceControlUpdate copyWithZone:];
-[CAMOverlayServiceControlUpdate isEqual:];
-[CAMOverlayServiceControlUpdate isValueUpdate];
-[CAMOverlayServiceControlUpdate _initWithControlIdentifier:isEnabled:];
```
