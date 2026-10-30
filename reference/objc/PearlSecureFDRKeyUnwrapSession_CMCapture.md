# `PearlSecureFDRKeyUnwrapSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PearlSecureSession`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSData" _hostEphemeralKey;
@"PearlUnwrapData" _hostUnwrapData;
```

## Properties

```
@property (T@"NSData",R,V_hostEphemeralKey) hostEphemeralKey;
@property (T@"PearlUnwrapData",R,V_hostUnwrapData) hostUnwrapData;
```

## Class methods

```
+[PearlSecureFDRKeyUnwrapSession session];
```

## Instance methods

```
-[PearlSecureFDRKeyUnwrapSession clearSession];
-[PearlSecureFDRKeyUnwrapSession establishSharedSecretWithSensorEphemeralKey:];
-[PearlSecureFDRKeyUnwrapSession generateHostEphemeralKeyWithBootNonce:];
-[PearlSecureFDRKeyUnwrapSession hostEphemeralKey];
-[PearlSecureFDRKeyUnwrapSession hostUnwrapData];
-[PearlSecureFDRKeyUnwrapSession setSensorUnwrapData:];
```
