# `AVCaptureFaceIDUnwrapResult`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
q _unwrapStatus;
i _pearlSecureSessionUnwrapError;
i _cameraStreamError;
```

## Properties

```
@property (Tq,R,N,V_unwrapStatus) unwrapStatus;
@property (Ti,R,N,V_pearlSecureSessionUnwrapError) pearlSecureSessionUnwrapError;
@property (Ti,R,N,V_cameraStreamError) cameraStreamError;
```

## Instance methods

```
-[AVCaptureFaceIDUnwrapResult isEqual:];
-[AVCaptureFaceIDUnwrapResult cameraStreamError];
-[AVCaptureFaceIDUnwrapResult initWithUnwrapStatus:pearlSecureSessionError:streamError:];
-[AVCaptureFaceIDUnwrapResult pearlSecureSessionUnwrapError];
-[AVCaptureFaceIDUnwrapResult unwrapStatus];
```
