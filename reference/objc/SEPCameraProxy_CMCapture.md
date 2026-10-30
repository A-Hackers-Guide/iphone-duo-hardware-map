# `SEPCameraProxy`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 9 instance methods, 4 class methods

## Instance variables

```
@"NSUUID" _activeSessionID;
q _cameraType;
```

## Properties

```
@property (Tq,R,V_cameraType) cameraType;
```

## Class methods

```
+[SEPCameraProxy initServiceConnection];
+[SEPCameraProxy isValidCameraType:];
+[SEPCameraProxy pearlToSecureSessionError:];
+[SEPCameraProxy sharedInstanceWithCameraType:];
```

## Instance methods

```
-[SEPCameraProxy cameraType];
-[SEPCameraProxy clearSession];
-[SEPCameraProxy generateHostEphemeralKeyWithSession:bootNonce:hostEphemeralKey:];
-[SEPCameraProxy registerWithPearlSecureSession:];
-[SEPCameraProxy deregisterWithPearlSecureSession:];
-[SEPCameraProxy establishSharedSecretWithSession:sensorEphemeralKey:sensorEphemeralKeySignature:];
-[SEPCameraProxy generateHostUnwrapDataWithSession:wrappedHostEncKey:wrappedHostEncKeyHmac:hostIV:hostTag:hostSignature:];
-[SEPCameraProxy initWithCameraType:];
-[SEPCameraProxy setSensorUnwrapDataWithSession:unwrappedSensorEncKey:unwrappedSensorEncKeyHmac:sensorIV:sensorEphemeralKeySignature:];
```
