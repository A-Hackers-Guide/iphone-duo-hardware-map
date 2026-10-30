# `BWAdaptiveCorrectionPreviewRegistrationProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPreviewRegistrationProvider`
- 1 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BWAdaptiveCorrectionPreviewRegistration" _registration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWAdaptiveCorrectionPreviewRegistrationProvider initialize];
```

## Instance methods

```
-[BWAdaptiveCorrectionPreviewRegistrationProvider dealloc];
-[BWAdaptiveCorrectionPreviewRegistrationProvider cleanupResources];
-[BWAdaptiveCorrectionPreviewRegistrationProvider allocateResourcesWithVideoFormat:metalContext:];
-[BWAdaptiveCorrectionPreviewRegistrationProvider computeApproximateCorrectionForWiderCamera:narrowerCameraPortType:narrowerPixelBufferDimensions:widerToNarrowerCameraScale:];
-[BWAdaptiveCorrectionPreviewRegistrationProvider computeCameraShiftForWiderCamera:narrowerCamera:widerToNarrowerCameraScale:];
-[BWAdaptiveCorrectionPreviewRegistrationProvider initWithCameraInfoByPortType:excludeStaticComponentFromAlignmentShifts:];
-[BWAdaptiveCorrectionPreviewRegistrationProvider registerWiderCamera:narrowerCamera:widerToNarrowerCameraScale:isMacroScene:macroTransitionType:registerHorizontalEdges:];
```
