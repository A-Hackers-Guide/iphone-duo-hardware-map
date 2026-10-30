# `BWPersonSemanticsConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _enabledSemantics;
B _appliesFinalCropRect;
B _portraitOrientationSupportEnabled;
@"NSString" _inferenceInputAttachedMediaKey;
```

## Properties

```
@property (TB,N,V_portraitOrientationSupportEnabled) portraitOrientationSupportEnabled;
@property (TI,N,V_enabledSemantics) enabledSemantics;
@property (TB,N,V_appliesFinalCropRect) appliesFinalCropRect;
@property (T@"NSString",&,N,V_inferenceInputAttachedMediaKey) inferenceInputAttachedMediaKey;
```

## Class methods

```
+[BWPersonSemanticsConfiguration personSemanticForAttachedMediaKey:];
```

## Instance methods

```
-[BWPersonSemanticsConfiguration setInferenceInputAttachedMediaKey:];
-[BWPersonSemanticsConfiguration initWithInferenceType:];
-[BWPersonSemanticsConfiguration inferenceInputAttachedMediaKey];
-[BWPersonSemanticsConfiguration appliesFinalCropRect];
-[BWPersonSemanticsConfiguration portraitOrientationSupportEnabled];
-[BWPersonSemanticsConfiguration dealloc];
-[BWPersonSemanticsConfiguration setAppliesFinalCropRect:];
-[BWPersonSemanticsConfiguration enabledSemantics];
-[BWPersonSemanticsConfiguration description];
-[BWPersonSemanticsConfiguration setPortraitOrientationSupportEnabled:];
-[BWPersonSemanticsConfiguration setEnabledSemantics:];
```
