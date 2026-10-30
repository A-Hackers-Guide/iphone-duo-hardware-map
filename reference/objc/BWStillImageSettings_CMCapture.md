# `BWStillImageSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"FigCaptureStillImageSettings" _requestedSettings;
@"BWStillImageCaptureSettings" _captureSettings;
@"BWStillImageProcessingSettings" _processingSettings;
```

## Properties

```
@property (Tq,R,N) settingsID;
@property (T@"FigCaptureStillImageSettings",R,N,V_requestedSettings) requestedSettings;
@property (T@"BWStillImageCaptureSettings",R,N,V_captureSettings) captureSettings;
@property (T@"BWStillImageProcessingSettings",R,N,V_processingSettings) processingSettings;
```

## Class methods

```
+[BWStillImageSettings supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageSettings dealloc];
-[BWStillImageSettings settingsID];
-[BWStillImageSettings encodeWithCoder:];
-[BWStillImageSettings hash];
-[BWStillImageSettings description];
-[BWStillImageSettings initWithCoder:];
-[BWStillImageSettings isEqual:];
-[BWStillImageSettings captureSettings];
-[BWStillImageSettings initWithRequestedSettings:captureSettings:processingSettings:];
-[BWStillImageSettings processingSettings];
-[BWStillImageSettings requestedSettings];
```
