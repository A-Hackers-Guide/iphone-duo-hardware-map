# `PearlSecureStreamingSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PearlSecureSession`
- 1 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSData" _hostEphemeralKey;
```

## Properties

```
@property (T@"NSData",R,V_hostEphemeralKey) hostEphemeralKey;
```

## Class methods

```
+[PearlSecureStreamingSession sessionWithCameraType:];
```

## Instance methods

```
-[PearlSecureStreamingSession clearSession];
-[PearlSecureStreamingSession establishSharedSecretWithSensorEphemeralKey:sensorEphemeralKeySignature:];
-[PearlSecureStreamingSession generateHostEphemeralKey];
-[PearlSecureStreamingSession hostEphemeralKey];
```
