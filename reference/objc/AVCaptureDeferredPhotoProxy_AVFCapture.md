# `AVCaptureDeferredPhotoProxy`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCapturePhoto`
- 4 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSString" _applicationIdentifier;
@"NSString" _captureRequestIdentifier;
@"NSString" _photoIdentifier;
@"NSArray" _photoLibraryThumbnailDimensions;
```

## Properties

```
@property (T@"NSString",C,N,V_applicationIdentifier) applicationIdentifier;
@property (T@"NSString",R,C,V_photoIdentifier) persistentStorageUUID;
@property (T@"NSString",R) deferredPhotoIdentifier;
@property (T@"NSArray",R,V_photoLibraryThumbnailDimensions) photoLibraryThumbnailDimensions;
```

## Instance methods

```
-[AVCaptureDeferredPhotoProxy dimensions];
-[AVCaptureDeferredPhotoProxy debugDescription];
-[AVCaptureDeferredPhotoProxy init];
-[AVCaptureDeferredPhotoProxy initWithDeferredPhotoIdentifier:];
-[AVCaptureDeferredPhotoProxy persistentStorageUUID];
-[AVCaptureDeferredPhotoProxy deferredPhotoIdentifier];
-[AVCaptureDeferredPhotoProxy dealloc];
-[AVCaptureDeferredPhotoProxy applicationIdentifier];
-[AVCaptureDeferredPhotoProxy captureRequestIdentifier];
-[AVCaptureDeferredPhotoProxy photoLibraryThumbnailDimensions];
-[AVCaptureDeferredPhotoProxy setApplicationIdentifier:];
-[AVCaptureDeferredPhotoProxy description];
-[AVCaptureDeferredPhotoProxy initWithTimestamp:proxySurface:proxySurfaceSize:proxyFileType:previewPhotoSurface:secureSignedRawSurface:secureSignedRawSurfaceSize:metadata:captureRequest:sequenceCount:photoCount:applicationIdentifier:captureRequestIdentifier:photoIdentifier:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:];
-[AVCaptureDeferredPhotoProxy initWithDeferredPhotoIdentifier:applicationIdentifier:];
-[AVCaptureDeferredPhotoProxy initWithDeferredPhotoIdentifier:applicationIdentifier:photoLibraryThumbnailDimensions:];
-[AVCaptureDeferredPhotoProxy isEqual:];
-[AVCaptureDeferredPhotoProxy initWithApplicationIdentifier:captureRequestIdentifier:photoIdentifier:timestamp:expectedPhotoProcessingFlags:];
```
