# `FigCaptureSessionLoggingPrefix`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="val"[8I]} _clientAuditToken;
i _clientPID;
i _clientPIDUsedForLoggingPrefix;
^{OpaqueFigCaptureSession=} _captureSession;
{_opaque_pthread_rwlock_t="__sig"q"__opaque"[192c]} _stringValueLock;
@"NSString" _stringValue;
@"NSString" _stringValueWithoutAngleBrackets;
```

## Instance methods

```
-[FigCaptureSessionLoggingPrefix dealloc];
-[FigCaptureSessionLoggingPrefix description];
-[FigCaptureSessionLoggingPrefix _updateLoggingPrefix];
```
