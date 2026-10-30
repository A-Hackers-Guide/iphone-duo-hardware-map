# `BWInferenceLazyVideoRequirement`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceVideoRequirement`
- Protocols: `NSCopying`
- 2 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _preparedByAttachedMediaKey;
@? _videoFormatProvider;
```

## Properties

```
@property (T@"NSString",R,C,N,V_preparedByAttachedMediaKey) preparedByAttachedMediaKey;
```

## Class methods

```
+[BWInferenceLazyVideoRequirement initialize];
```

## Instance methods

```
-[BWInferenceLazyVideoRequirement initWithAttachedMediaKey:count:];
-[BWInferenceLazyVideoRequirement dealloc];
-[BWInferenceLazyVideoRequirement initWithAttachedMediaKey:preparedByAttachedMediaKey:videoFormatProvider:];
-[BWInferenceLazyVideoRequirement initWithAttachedMediaKey:preparedByAttachedMediaKey:count:videoFormatProvider:];
-[BWInferenceLazyVideoRequirement description];
-[BWInferenceLazyVideoRequirement initWithAttachedMediaKey:videoFormat:count:];
-[BWInferenceLazyVideoRequirement preparedByAttachedMediaKey];
-[BWInferenceLazyVideoRequirement copyWithZone:];
-[BWInferenceLazyVideoRequirement initWithLazyVideoRequirement:];
-[BWInferenceLazyVideoRequirement prepareForInputInferenceVideoFormat:];
```
