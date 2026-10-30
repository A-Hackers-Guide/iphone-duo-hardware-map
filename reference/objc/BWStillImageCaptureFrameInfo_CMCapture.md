# `BWStillImageCaptureFrameInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _mainFlags;
Q _sifrFlags;
```

## Properties

```
@property (TQ,R,N,V_mainFlags) mainFlags;
@property (TQ,R,N,V_sifrFlags) sifrFlags;
```

## Class methods

```
+[BWStillImageCaptureFrameInfo supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageCaptureFrameInfo encodeWithCoder:];
-[BWStillImageCaptureFrameInfo hash];
-[BWStillImageCaptureFrameInfo initWithCoder:];
-[BWStillImageCaptureFrameInfo isEqual:];
-[BWStillImageCaptureFrameInfo initWithMainFlags:sifrFlags:];
-[BWStillImageCaptureFrameInfo mainFlags];
-[BWStillImageCaptureFrameInfo sifrFlags];
```
