# `BWEspressoE5InferenceCamGazePropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 5 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceMetadataRequirement" _camGazeRequirement;
Q _camGazeSizeBytes;
Q _camGazeOutputElementCount;
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
-[BWEspressoE5InferenceCamGazePropagator allowsAsyncPropagation];
-[BWEspressoE5InferenceCamGazePropagator dealloc];
-[BWEspressoE5InferenceCamGazePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWEspressoE5InferenceCamGazePropagator initWithCamGazeRequirement:camGazeSizeBytes:maxFaces:faceIndex:];
```
