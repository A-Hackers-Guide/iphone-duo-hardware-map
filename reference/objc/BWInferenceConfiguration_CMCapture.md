# `BWInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _inferenceType;
I _priority;
f _maximumFramesPerSecond;
B _propagatesFrameRatePrevention;
@"NSDictionary" _tuningParameters;
@"NSString" _contextName;
```

## Properties

```
@property (Ti,R,N,V_inferenceType) inferenceType;
@property (TI,N,V_priority) priority;
@property (Tf,N,V_maximumFramesPerSecond) maximumFramesPerSecond;
@property (TB,N,V_propagatesFrameRatePrevention) propagatesFrameRatePrevention;
@property (T@"NSDictionary",C,N,V_tuningParameters) tuningParameters;
@property (T@"NSString",C,N,V_contextName) contextName;
```

## Instance methods

```
-[BWInferenceConfiguration tuningParameters];
-[BWInferenceConfiguration priority];
-[BWInferenceConfiguration initWithInferenceType:];
-[BWInferenceConfiguration setTuningParameters:];
-[BWInferenceConfiguration setPriority:];
-[BWInferenceConfiguration dealloc];
-[BWInferenceConfiguration maximumFramesPerSecond];
-[BWInferenceConfiguration contextName];
-[BWInferenceConfiguration description];
-[BWInferenceConfiguration inferenceType];
-[BWInferenceConfiguration setContextName:];
-[BWInferenceConfiguration propagatesFrameRatePrevention];
-[BWInferenceConfiguration setMaximumFramesPerSecond:];
-[BWInferenceConfiguration setPropagatesFrameRatePrevention:];
```
