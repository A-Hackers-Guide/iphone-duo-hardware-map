# `BWInferenceHumanPosePropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`, `BWEspressoInferenceTensorMemoryProvider`
- 4 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceMetadataRequirement" _outputRequirement;
B _rotateOutput;
@"NSMutableData" _heatmapData;
^{__IOSurface=} _tensorBackingSurface;
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
-[BWInferenceHumanPosePropagator allowsAsyncPropagation];
-[BWInferenceHumanPosePropagator dealloc];
-[BWInferenceHumanPosePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceHumanPosePropagator backingMemoryForMetadataRequirement:bindingName:surfaceProperties:];
-[BWInferenceHumanPosePropagator initWithOutputRequirement:rotateOutput:];
```
