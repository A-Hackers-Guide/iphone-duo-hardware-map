# `SRPhotoplethysmogramOpticalSample`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 13 instance variables, 13 properties, 23 instance methods, 1 class methods

## Instance variables

```
d _rawNominalWavelength;
d _rawEffectiveWavelength;
d _rawFrequency;
q _emitter;
@"NSIndexSet" _activePhotodiodeIndexes;
q _signalIdentifier;
q _nanosecondsSinceStart;
@"NSNumber" _normalizedReflectance;
@"NSNumber" _whiteNoise;
@"NSNumber" _pinkNoise;
@"NSNumber" _backgroundNoise;
@"NSNumber" _backgroundNoiseOffset;
@"NSArray" _conditions;
```

## Properties

```
@property (Tq,R,N,V_emitter) emitter;
@property (T@"NSIndexSet",R,N,V_activePhotodiodeIndexes) activePhotodiodeIndexes;
@property (Tq,R,N,V_signalIdentifier) signalIdentifier;
@property (T@"NSMeasurement",R,N) nominalWavelength;
@property (T@"NSMeasurement",R,N) effectiveWavelength;
@property (T@"NSMeasurement",R,N) samplingFrequency;
@property (Tq,R,N,V_nanosecondsSinceStart) nanosecondsSinceStart;
@property (T@"NSNumber",R,N,V_normalizedReflectance) normalizedReflectance;
@property (T@"NSNumber",R,N,V_whiteNoise) whiteNoise;
@property (T@"NSNumber",R,N,V_pinkNoise) pinkNoise;
@property (T@"NSNumber",R,N,V_backgroundNoise) backgroundNoise;
@property (T@"NSNumber",R,N,V_backgroundNoiseOffset) backgroundNoiseOffset;
@property (T@"NSArray",R,C,N,V_conditions) conditions;
```

## Class methods

```
+[SRPhotoplethysmogramOpticalSample supportsSecureCoding];
```

## Instance methods

```
-[SRPhotoplethysmogramOpticalSample dealloc];
-[SRPhotoplethysmogramOpticalSample conditions];
-[SRPhotoplethysmogramOpticalSample encodeWithCoder:];
-[SRPhotoplethysmogramOpticalSample hash];
-[SRPhotoplethysmogramOpticalSample description];
-[SRPhotoplethysmogramOpticalSample initWithCoder:];
-[SRPhotoplethysmogramOpticalSample copyWithZone:];
-[SRPhotoplethysmogramOpticalSample isEqual:];
-[SRPhotoplethysmogramOpticalSample samplingFrequency];
-[SRPhotoplethysmogramOpticalSample signalIdentifier];
-[SRPhotoplethysmogramOpticalSample backgroundNoise];
-[SRPhotoplethysmogramOpticalSample emitter];
-[SRPhotoplethysmogramOpticalSample activePhotodiodeIndexes];
-[SRPhotoplethysmogramOpticalSample backgroundNoiseOffset];
-[SRPhotoplethysmogramOpticalSample effectiveWavelength];
-[SRPhotoplethysmogramOpticalSample initWithEmitter:photodiodes:signalIdentifier:nominalWavelength:effectiveWavelength:frequency:timestamp:normalizedReflectance:whiteNoise:pinkNoise:backgroundNoise:backgrounNoiseOffset:conditions:];
-[SRPhotoplethysmogramOpticalSample initWithHAPPGOpticalSample:];
-[SRPhotoplethysmogramOpticalSample isEqualToOpticalSample:];
-[SRPhotoplethysmogramOpticalSample nanosecondsSinceStart];
-[SRPhotoplethysmogramOpticalSample nominalWavelength];
-[SRPhotoplethysmogramOpticalSample normalizedReflectance];
-[SRPhotoplethysmogramOpticalSample pinkNoise];
-[SRPhotoplethysmogramOpticalSample whiteNoise];
```
