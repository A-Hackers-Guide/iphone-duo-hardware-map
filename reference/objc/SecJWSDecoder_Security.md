# `SecJWSDecoder`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _keyID;
@"NSData" _payload;
@"NSData" _signature;
@"NSError" _verificationError;
```

## Properties

```
@property (T@"NSString",R,N,V_keyID) keyID;
@property (T@"NSData",R,N,V_payload) payload;
@property (T@"NSData",R,N,V_signature) signature;
@property (T@"NSError",R,N,V_verificationError) verificationError;
```

## Instance methods

```
-[SecJWSDecoder keyID];
-[SecJWSDecoder payload];
-[SecJWSDecoder signature];
-[SecJWSDecoder dataWithBase64URLEncodedString:];
-[SecJWSDecoder _createASN1SignatureFromJWSSignature:];
-[SecJWSDecoder _validateJWSProtectedHeader:];
-[SecJWSDecoder _validateJWSSignature:ofHeader:andPayload:withPublicKey:];
-[SecJWSDecoder initWithJWSCompactEncodedString:keyID:publicKey:];
-[SecJWSDecoder verificationError];
```
