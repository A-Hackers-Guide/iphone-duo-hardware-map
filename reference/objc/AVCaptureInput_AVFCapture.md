# `AVCaptureInput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureInputInternal" _inputInternal;
```

## Properties

```
@property (T@"NSArray",R,N) ports;
```

## Class methods

```
+[AVCaptureInput initialize];
```

## Instance methods

```
-[AVCaptureInput ports];
-[AVCaptureInput clock];
-[AVCaptureInput videoDevice];
-[AVCaptureInput updateSupportedProperties];
-[AVCaptureInput detachSafelyFromFigCaptureSession:];
-[AVCaptureInput dealloc];
-[AVCaptureInput setSession:];
-[AVCaptureInput handleChangedActiveFormat:forDevice:];
-[AVCaptureInput detachFromFigCaptureSession:];
-[AVCaptureInput attachToFigCaptureSession:];
-[AVCaptureInput performFigCaptureSessionOperationSafelyUsingBlock:];
-[AVCaptureInput session];
-[AVCaptureInput attachSafelyToFigCaptureSession:];
-[AVCaptureInput initSubclass];
```
