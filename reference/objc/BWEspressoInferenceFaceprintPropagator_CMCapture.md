# `BWEspressoInferenceFaceprintPropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 5 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceMetadataRequirement" _faceprintRequirement;
@"BWInferenceMetadataRequirement" _confidenceRequirement;
Q _faceprintSizeBytes;
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
-[BWEspressoInferenceFaceprintPropagator allowsAsyncPropagation];
-[BWEspressoInferenceFaceprintPropagator dealloc];
-[BWEspressoInferenceFaceprintPropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWEspressoInferenceFaceprintPropagator initWithFaceprintRequirement:faceprintSizeBytes:confidenceRequirement:maxFaces:faceIndex:];
```
