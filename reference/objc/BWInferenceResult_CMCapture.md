# `BWInferenceResult`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
i _inferenceType;
{?="value"q"timescale"i"flags"I"epoch"q} _timestamp;
@"NSDictionary" _inferences;
@"NSString" _preventionReason;
```

## Properties

```
@property (Ti,R,N,V_inferenceType) inferenceType;
@property (T{?=qiIq},R,N,V_timestamp) timestamp;
@property (T@"NSDictionary",R,C,N,V_inferences) inferences;
@property (T@"NSString",R,C,N,V_preventionReason) preventionReason;
@property (TB,R,N,GisValid) valid;
```

## Instance methods

```
-[BWInferenceResult dealloc];
-[BWInferenceResult timestamp];
-[BWInferenceResult isValid];
-[BWInferenceResult description];
-[BWInferenceResult inferenceType];
-[BWInferenceResult inferences];
-[BWInferenceResult initWithInferenceType:inferences:atTimestamp:];
-[BWInferenceResult initWithInferenceType:preventionReason:atTimestamp:];
-[BWInferenceResult initWithResult:replacementInferences:replacementPreventionReason:];
-[BWInferenceResult preventionReason];
```
