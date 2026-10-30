# `BWInferencePostProcessor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",R,C,N) requiredInferenceTypes;
@property (TI,R,N) postProcessorType;
@property (TB,R,N) needsReprepareForLiveReconfiguration;
```

## Instance methods

```
-[BWInferencePostProcessor needsReprepareForLiveReconfiguration];
-[BWInferencePostProcessor postProcessInferenceResults:attachingSampleBuffer:];
-[BWInferencePostProcessor postProcessorType];
-[BWInferencePostProcessor preparePostProcessor];
-[BWInferencePostProcessor requiredInferenceTypes];
```
