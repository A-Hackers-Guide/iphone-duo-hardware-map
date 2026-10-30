# `SecJWSEncoder`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _publicKey;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _privateKey;
```

## Properties

```
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_publicKey) publicKey;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_privateKey) privateKey;
```

## Instance methods

```
-[SecJWSEncoder publicKey];
-[SecJWSEncoder setPublicKey:];
-[SecJWSEncoder init];
-[SecJWSEncoder dealloc];
-[SecJWSEncoder appendPaddedToData:ptr:len:expected:];
-[SecJWSEncoder base64URLEncodedStringRepresentationWithData:];
-[SecJWSEncoder base64URLEncodedStringRepresentationWithDictionary:];
-[SecJWSEncoder compactJSONStringRepresentationWithDictionary:];
-[SecJWSEncoder createKeyPair];
-[SecJWSEncoder encodedJWSWithPayload:kid:nonce:url:error:];
-[SecJWSEncoder initWithPublicKey:privateKey:];
-[SecJWSEncoder jwkPublicKey];
-[SecJWSEncoder privateKey];
-[SecJWSEncoder setPrivateKey:];
-[SecJWSEncoder signatureWithProtectedHeader:payload:];
```
