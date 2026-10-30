# `BWInferenceFaceQualityCropDescriptor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceCropDescriptor`
- 3 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
Q _faceIndex;
f _boundingBoxScalingFactor;
B _deviceOriented;
```

## Properties

```
@property (Tc,R,N) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceFaceQualityCropDescriptor initialize];
```

## Instance methods

```
-[BWInferenceFaceQualityCropDescriptor identifier];
-[BWInferenceFaceQualityCropDescriptor copyWithZone:];
-[BWInferenceFaceQualityCropDescriptor applicableToSampleBuffer:forMediaKey:];
-[BWInferenceFaceQualityCropDescriptor initWithFaceIndex:boundingBoxScalingFactor:isDeviceOriented:];
-[BWInferenceFaceQualityCropDescriptor maxCropForDimensions:];
-[BWInferenceFaceQualityCropDescriptor rectForSampleBuffer:];
```
