# `PearlSecureSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
q _cameraType;
@"NSUUID" _sessionID;
```

## Properties

```
@property (T@"NSUUID",R,V_sessionID) sessionID;
```

## Class methods

```
+[PearlSecureSession initialize];
+[PearlSecureSession sessionWithCameraType:];
```

## Instance methods

```
-[PearlSecureSession sessionID];
-[PearlSecureSession dealloc];
-[PearlSecureSession invalidate];
-[PearlSecureSession clearSession];
-[PearlSecureSession generateHostEphemeralKey:hostEphemeralKey:];
-[PearlSecureSession initWithCameraType:];
```
