# `FigCaptureSessionProxy`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureSession=} _session;
q _identifier;
{?="val"[8I]} _clientAuditToken;
B _containsVideoSource;
B _containsStillImageSink;
B _containsMovieFileSink;
B _previewTapOpened;
@"<FigCaptureSessionPreviewTapDelegate>" _previewTapDelegate;
```

## Properties

```
@property (Tq,R) identifier;
@property (T{?=[8I]},R) clientAuditToken;
@property (TB,R) containsVideoSource;
@property (TB,R) containsStillImageSink;
@property (TB,R) containsMovieFileSink;
```

## Class methods

```
+[FigCaptureSessionProxy initialize];
```

## Instance methods

```
-[FigCaptureSessionProxy identifier];
-[FigCaptureSessionProxy clientAuditToken];
-[FigCaptureSessionProxy dealloc];
-[FigCaptureSessionProxy closePreviewTap];
-[FigCaptureSessionProxy containsMovieFileSink];
-[FigCaptureSessionProxy containsStillImageSink];
-[FigCaptureSessionProxy containsVideoSource];
-[FigCaptureSessionProxy initWithFigCaptureSession:identifier:clientAuditToken:containsVideoSource:containsStillImageSink:containsMovieFileSink:];
-[FigCaptureSessionProxy openPreviewTapWithDelegate:];
```
