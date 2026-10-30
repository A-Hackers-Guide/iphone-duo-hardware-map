# `BWEspressoInferenceFaceQualityPropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 4 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceMetadataRequirement" _faceQualityRequirement;
Q _faceQualitySizeBytes;
Q _maxFaces;
Q _faceIndex;
```

## Properties

```
@property (TB,R,N) allowsAsyncPropagation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWEspressoInferenceFaceQualityPropagator allowsAsyncPropagation];
-[BWEspressoInferenceFaceQualityPropagator dealloc];
-[BWEspressoInferenceFaceQualityPropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWEspressoInferenceFaceQualityPropagator initWithFaceQualityRequirement:faceQualitySizeBytes:maxFaces:faceIndex:];
```
