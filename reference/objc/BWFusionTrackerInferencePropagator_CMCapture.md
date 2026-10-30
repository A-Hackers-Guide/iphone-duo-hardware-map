# `BWFusionTrackerInferencePropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 3 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceVideoRequirement" _inputVideoRequirement;
@"NSMutableDictionary" _outputTensorRequirements;
q _operation;
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
-[BWFusionTrackerInferencePropagator allowsAsyncPropagation];
-[BWFusionTrackerInferencePropagator dealloc];
-[BWFusionTrackerInferencePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWFusionTrackerInferencePropagator initWithInputVideoRequirement:outputTensorRequirements:operation:];
```
