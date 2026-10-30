# `BWInferenceVideoFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 19 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"BWVideoFormat" _underlyingVideoFormat;
B _deviceOriented;
B _landscapeOriented;
B _applyHorizontalFlip;
q _videoContentMode;
B _includesInvalidContent;
@"<BWInferenceCropDescriptor>" _cropDescriptor;
@? _histogramRequest;
i _rotationDegrees;
i _singleStepRotationDegrees;
```

## Properties

```
@property (Ti,N) singleStepRotationDegrees;
@property (TQ,R,N) width;
@property (TQ,R,N) height;
@property (T{?=ii},R,N) dimensions;
@property (TI,R,N) pixelFormat;
@property (TQ,R,N) extendedWidth;
@property (TQ,R,N) extendedHeight;
@property (Ti,R,N) colorSpaceProperties;
@property (TB,R,N) deviceOriented;
@property (TB,R,N) applyHorizontalFlip;
@property (TB,R,N) landscapeOriented;
@property (Ti,R,N) rotationDegrees;
@property (T@"NSDictionary",R,N) pixelBufferAttributes;
@property (T^{opaqueCMFormatDescription=},R) formatDescription;
@property (T@"BWVideoFormat",R,N) underlyingVideoFormat;
@property (Tq,R,N) videoContentMode;
@property (TB,R,N) includesInvalidContent;
@property (T@"<BWInferenceCropDescriptor>",R,N) cropDescriptor;
@property (T@?,R,C,N,V_histogramRequest) histogramRequest;
```

## Class methods

```
+[BWInferenceVideoFormat formatByResolvingRequirements:];
```

## Instance methods

```
-[BWInferenceVideoFormat formatDescription];
-[BWInferenceVideoFormat landscapeOriented];
-[BWInferenceVideoFormat histogramRequest];
-[BWInferenceVideoFormat includesInvalidContent];
-[BWInferenceVideoFormat extendedWidth];
-[BWInferenceVideoFormat applyHorizontalFlip];
-[BWInferenceVideoFormat extendedHeight];
-[BWInferenceVideoFormat videoContentMode];
-[BWInferenceVideoFormat dimensions];
-[BWInferenceVideoFormat singleStepRotationDegrees];
-[BWInferenceVideoFormat setSingleStepRotationDegrees:];
-[BWInferenceVideoFormat pixelBufferAttributes];
-[BWInferenceVideoFormat rotationDegrees];
-[BWInferenceVideoFormat dealloc];
-[BWInferenceVideoFormat deviceOriented];
-[BWInferenceVideoFormat uncompressedEquivalent];
-[BWInferenceVideoFormat initWithUnderlyingFormat:isDeviceOriented:videoContentMode:includesInvalidContent:cropDescriptor:histogramRequest:rotationDegrees:applyHorizontalFlip:isLandscapeOriented:];
-[BWInferenceVideoFormat representsCompressedEquivalent];
-[BWInferenceVideoFormat underlyingVideoFormat];
-[BWInferenceVideoFormat hash];
-[BWInferenceVideoFormat description];
-[BWInferenceVideoFormat cropDescriptor];
-[BWInferenceVideoFormat pixelFormat];
-[BWInferenceVideoFormat width];
-[BWInferenceVideoFormat copyWithZone:];
-[BWInferenceVideoFormat colorSpaceProperties];
-[BWInferenceVideoFormat isEqual:];
-[BWInferenceVideoFormat height];
```
