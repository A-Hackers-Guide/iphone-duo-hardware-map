# `BWInferenceSampleBufferPropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 4 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _videoRequirements;
@"NSArray" _cloneVideoRequirements;
@"NSArray" _metadataRequirements;
B _updateMetadataWithCropRect;
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
-[BWInferenceSampleBufferPropagator allowsAsyncPropagation];
-[BWInferenceSampleBufferPropagator dealloc];
-[BWInferenceSampleBufferPropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWInferenceSampleBufferPropagator initWithVideoRequirements:cloneRequirements:metadataRequirements:updateMetadataWithCropRect:];
```
