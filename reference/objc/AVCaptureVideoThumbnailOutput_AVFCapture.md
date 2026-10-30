# `AVCaptureVideoThumbnailOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- 1 instance variables, 4 properties, 17 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureVideoThumbnailOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureVideoThumbnailContentsDelegate>",N) thumbnailContentsDelegate;
@property (T@"NSArray",C,N) filters;
@property (T@"NSArray",C,N) smartStyles;
@property (T{CGSize=dd},N) thumbnailSize;
```

## Class methods

```
+[AVCaptureVideoThumbnailOutput initialize];
+[AVCaptureVideoThumbnailOutput contentsRectForFilterAtIndex:thumbnailSize:filterCount:];
```

## Instance methods

```
-[AVCaptureVideoThumbnailOutput setThumbnailSize:];
-[AVCaptureVideoThumbnailOutput canAddConnection:failureReason:];
-[AVCaptureVideoThumbnailOutput _handleNotification:payload:];
-[AVCaptureVideoThumbnailOutput thumbnailSize];
-[AVCaptureVideoThumbnailOutput init];
-[AVCaptureVideoThumbnailOutput safelyHandleServerConnectionDeathForFigCaptureSession:];
-[AVCaptureVideoThumbnailOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureVideoThumbnailOutput dealloc];
-[AVCaptureVideoThumbnailOutput setFilters:];
-[AVCaptureVideoThumbnailOutput filters];
-[AVCaptureVideoThumbnailOutput connectionMediaTypes];
-[AVCaptureVideoThumbnailOutput attachSafelyToFigCaptureSession:];
-[AVCaptureVideoThumbnailOutput setSmartStyles:];
-[AVCaptureVideoThumbnailOutput _signalInvalidationOfPropagatedContentsIfNecessary];
-[AVCaptureVideoThumbnailOutput setThumbnailContentsDelegate:];
-[AVCaptureVideoThumbnailOutput smartStyles];
-[AVCaptureVideoThumbnailOutput thumbnailContentsDelegate];
```
