# `AVCapturePhotoRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 15 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"AVWeakReferencingDelegateStorage" _delegateStorage;
I _photoCallbackFlavor;
@"AVCapturePhotoSettings" _unresolvedSettings;
@"FigCaptureStillImageSettings" _figSettings;
@"AVCaptureResolvedPhotoSettings" _resolvedSettings;
@"NSArray" _expectedPhotoManifest;
I _firedCallbackFlags;
Q _firedPhotoCallbacksCount;
^{__IOSurface=} _previewSurface;
^{opaqueCMSampleBuffer=} _previewSampleBuffer;
^{__IOSurface=} _thumbnailSurface;
B _delegateSupportsDebugMetadataSidecarFile;
B _delegateSupportsMetadataIdentifiersCallback;
B _lensStabilizationSupported;
```

## Properties

```
@property (TI,R,V_photoCallbackFlavor) photoCallbackFlavor;
@property (T@"AVWeakReferencingDelegateStorage",R,V_delegateStorage) delegateStorage;
@property (T@"AVCapturePhotoSettings",R,V_unresolvedSettings) unresolvedSettings;
@property (T@"FigCaptureStillImageSettings",R,V_figSettings) figSettings;
@property (T@"AVCaptureResolvedPhotoSettings",&,N) resolvedSettings;
@property (T@"NSArray",R,N,V_expectedPhotoManifest) expectedPhotoManifest;
@property (TQ,R,N) expectedPhotoCount;
@property (TI,N,V_firedCallbackFlags) firedCallbackFlags;
@property (TQ,N,V_firedPhotoCallbacksCount) firedPhotoCallbacksCount;
@property (TB,R,V_delegateSupportsDebugMetadataSidecarFile) delegateSupportsDebugMetadataSidecarFile;
@property (TB,R,V_delegateSupportsMetadataIdentifiersCallback) delegateSupportsMetadataIdentifiersCallback;
@property (TB,R,V_lensStabilizationSupported) lensStabilizationSupported;
@property (T^{__IOSurface=},&,N,V_previewSurface) previewSurface;
@property (T^{opaqueCMSampleBuffer=},&,N,V_previewSampleBuffer) previewSampleBuffer;
@property (T^{__IOSurface=},&,N,V_thumbnailSurface) thumbnailSurface;
```

## Class methods

```
+[AVCapturePhotoRequest initialize];
+[AVCapturePhotoRequest requestWithDelegate:settings:figSettings:lensStabilizationSupported:];
```

## Instance methods

```
-[AVCapturePhotoRequest lensStabilizationSupported];
-[AVCapturePhotoRequest setPreviewSampleBuffer:];
-[AVCapturePhotoRequest setFiredCallbackFlags:];
-[AVCapturePhotoRequest setPreviewSurface:];
-[AVCapturePhotoRequest _resolveExpectedPhotoManifest];
-[AVCapturePhotoRequest photoCallbackFlavor];
-[AVCapturePhotoRequest delegateSupportsMetadataIdentifiersCallback];
-[AVCapturePhotoRequest dealloc];
-[AVCapturePhotoRequest delegateSupportsDebugMetadataSidecarFile];
-[AVCapturePhotoRequest delegateStorage];
-[AVCapturePhotoRequest previewSurface];
-[AVCapturePhotoRequest unresolvedSettings];
-[AVCapturePhotoRequest resolvedSettings];
-[AVCapturePhotoRequest previewSampleBuffer];
-[AVCapturePhotoRequest setResolvedSettings:];
-[AVCapturePhotoRequest expectedPhotoCount];
-[AVCapturePhotoRequest figSettings];
-[AVCapturePhotoRequest setThumbnailSurface:];
-[AVCapturePhotoRequest firedCallbackFlags];
-[AVCapturePhotoRequest setFiredPhotoCallbacksCount:];
-[AVCapturePhotoRequest thumbnailSurface];
-[AVCapturePhotoRequest expectedPhotoManifest];
-[AVCapturePhotoRequest firedPhotoCallbacksCount];
-[AVCapturePhotoRequest initWithDelegate:settings:figSettings:lensStabilizationSupported:];
```
