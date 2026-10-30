# `AVCaptureDeferredPhotoSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"FigCaptureStillImageSettings" _captureSettings;
@"NSData" _serializedProcessingSettings;
```

## Properties

```
@property (T@"FigCaptureStillImageSettings",R,N,V_captureSettings) captureSettings;
@property (T@"NSData",R,C,N,V_serializedProcessingSettings) serializedProcessingSettings;
```

## Class methods

```
+[AVCaptureDeferredPhotoSettings supportsSecureCoding];
```

## Instance methods

```
-[AVCaptureDeferredPhotoSettings serializedProcessingSettings];
-[AVCaptureDeferredPhotoSettings dealloc];
-[AVCaptureDeferredPhotoSettings encodeWithCoder:];
-[AVCaptureDeferredPhotoSettings initWithCoder:];
-[AVCaptureDeferredPhotoSettings captureSettings];
-[AVCaptureDeferredPhotoSettings _initWithCaptureSettings:serializedProcessingSettings:];
```
