# `BWPreviewRegistration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _registrationQueue;
@"<BWPreviewRegistrationProvider>" _registrationProvider;
i _previewRegistrationType;
@"<MTLCommandQueue>" _metalCommandQueue;
B _excludeStaticComponentFromAlignmentShifts;
```

## Properties

```
@property (Ti,R,V_previewRegistrationType) previewRegistrationType;
```

## Class methods

```
+[BWPreviewRegistration initialize];
```

## Instance methods

```
-[BWPreviewRegistration dealloc];
-[BWPreviewRegistration previewRegistrationType];
-[BWPreviewRegistration cleanupResources];
-[BWPreviewRegistration allocateResourcesAsynchronouslyWithVideoFormat:];
-[BWPreviewRegistration computeApproximateCorrectionForWiderCamera:narrowerCameraPortType:narrowerPixelBufferDimensions:widerToNarrowerCameraScale:];
-[BWPreviewRegistration computeCameraShiftForWiderCamera:narrowerCamera:widerToNarrowerCameraScale:];
-[BWPreviewRegistration initWithCameraInfoByPortType:sensorBinningFactor:registrationType:metalCommandQueue:excludeStaticComponentFromAlignmentShifts:];
-[BWPreviewRegistration registerWiderCamera:narrowerCamera:widerToNarrowerCameraScale:isMacroScene:macroTransitionType:registerHorizontalEdges:completionHandler:];
-[BWPreviewRegistration waitForRegistrationToComplete];
```
