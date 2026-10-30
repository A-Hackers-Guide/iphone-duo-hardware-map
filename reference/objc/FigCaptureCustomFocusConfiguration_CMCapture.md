# `FigCaptureCustomFocusConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
i _requestID;
f _lensPosition;
B _clampToHyperfocalLogicalLensPositionEnabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _calculateFocusPositionLock;
@"NSMutableDictionary" _captureStreamFocusPositionsByPortType;
B _commandSubmitted;
```

## Class methods

```
+[FigCaptureCustomFocusConfiguration initialize];
```

## Instance methods

```
-[FigCaptureCustomFocusConfiguration dealloc];
-[FigCaptureCustomFocusConfiguration description];
-[FigCaptureCustomFocusConfiguration _captureStreamFocusPositionForLensPosition:];
-[FigCaptureCustomFocusConfiguration _initWithLensPosition:clampToHyperfocal:requestID:];
```
