# `FigScreenCaptureController`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 26 instance methods, 4 class methods

## Instance variables

```
@"<FigScreenCaptureFrameHandlerDelegate>" _delegateWeak;
i _mode;
@"FigScreenCaptureConfiguration" _screenCaptureConfiguration;
@"FigDisplayConfiguration" _displayConfiguration;
^{OpaqueFigVirtualDisplaySession=} _session;
^{OpaqueFigSimpleMutex=} _lock;
^{__CFDictionary=} _options;
```

## Properties

```
@property (T^{OpaqueFigVirtualDisplaySession=},N,V_session) session;
@property (T^{OpaqueFigSimpleMutex=},N,V_lock) lock;
@property (T^{__CFDictionary=},N,V_options) options;
@property (T{CGSize=dd},R,N) size;
@property (T{?=qiIq},R,N) minIntervalBetweenFrames;
@property (T@"FigScreenCaptureConfiguration",R,N,V_screenCaptureConfiguration) screenCaptureConfiguration;
@property (T@"FigDisplayConfiguration",R,N,V_displayConfiguration) displayConfiguration;
@property (T@"<FigScreenCaptureFrameHandlerDelegate>",W,N,V_delegateWeak) delegate;
```

## Class methods

```
+[FigScreenCaptureController screenCaptureControllerWithCaptureConfiguration:];
+[FigScreenCaptureController screenCaptureControllerWithDisplayConfiguration:];
+[FigScreenCaptureController screenCaptureControllerWithFigVirtualDisplayOptions:];
+[FigScreenCaptureController screenCaptureControllerWithSize:minIntervalBetweenFrames:];
```

## Instance methods

```
-[FigScreenCaptureController setLock:];
-[FigScreenCaptureController displayConfiguration];
-[FigScreenCaptureController setOptions:];
-[FigScreenCaptureController stopCapture];
-[FigScreenCaptureController dealloc];
-[FigScreenCaptureController initWithDisplayConfiguration:];
-[FigScreenCaptureController size];
-[FigScreenCaptureController setSession:];
-[FigScreenCaptureController setDelegate:];
-[FigScreenCaptureController delegate];
-[FigScreenCaptureController description];
-[FigScreenCaptureController lock];
-[FigScreenCaptureController options];
-[FigScreenCaptureController session];
-[FigScreenCaptureController startCapture];
-[FigScreenCaptureController getFVDOptions];
-[FigScreenCaptureController initWithFigVirtualDisplayOptions:];
-[FigScreenCaptureController initWithScreenCaptureConfiguration:];
-[FigScreenCaptureController initWithSize:minIntervalBetweenFrames:];
-[FigScreenCaptureController minIntervalBetweenFrames];
-[FigScreenCaptureController resumeCapture];
-[FigScreenCaptureController screenCaptureConfiguration];
-[FigScreenCaptureController setFigVirtualDisplayOption:forKey:];
-[FigScreenCaptureController suspendCapture];
-[FigScreenCaptureController updateProtectionFlags:];
-[FigScreenCaptureController updateProtectionStatus:];
```
