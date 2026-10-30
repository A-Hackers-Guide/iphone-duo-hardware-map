# `CMStrideCalibrationHistory`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _calibrationTracks;
@"NSArray" _rawSpeedToKValueBins;
@"NSArray" _stepCadenceToStrideLengthBins;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",&,N,V_calibrationTracks) calibrationTracks;
@property (T@"NSArray",&,N,V_rawSpeedToKValueBins) rawSpeedToKValueBins;
@property (T@"NSArray",&,N,V_stepCadenceToStrideLengthBins) stepCadenceToStrideLengthBins;
```

## Class methods

```
+[CMStrideCalibrationHistory supportsSecureCoding];
```

## Instance methods

```
-[CMStrideCalibrationHistory dealloc];
-[CMStrideCalibrationHistory encodeWithCoder:];
-[CMStrideCalibrationHistory initWithCoder:];
-[CMStrideCalibrationHistory copyWithZone:];
-[CMStrideCalibrationHistory binarySampleRepresentation];
-[CMStrideCalibrationHistory calibrationTracks];
-[CMStrideCalibrationHistory initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMStrideCalibrationHistory initWithCalibrationTracks:rawSpeedToKValueBins:stepCadenceToStrideLengthBins:];
-[CMStrideCalibrationHistory rawSpeedToKValueBins];
-[CMStrideCalibrationHistory setCalibrationTracks:];
-[CMStrideCalibrationHistory setRawSpeedToKValueBins:];
-[CMStrideCalibrationHistory setStepCadenceToStrideLengthBins:];
-[CMStrideCalibrationHistory stepCadenceToStrideLengthBins];
```
