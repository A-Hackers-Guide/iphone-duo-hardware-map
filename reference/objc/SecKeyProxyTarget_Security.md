# `SecKeyProxyTarget`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SecKeyProxyProtocol`
- 3 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@ _key;
@"NSData" _certificate;
@"SecKeyProxy" _publicKeyProxy;
```

## Properties

```
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N) key;
```

## Instance methods

```
-[SecKeyProxyTarget key];
-[SecKeyProxyTarget getAlgorithmIDWithReply:];
-[SecKeyProxyTarget getAttributesWithReply:];
-[SecKeyProxyTarget getBlockSizeWithReply:];
-[SecKeyProxyTarget getDescriptionWithReply:];
-[SecKeyProxyTarget getExternalRepresentationWithReply:];
-[SecKeyProxyTarget getPublicKey:];
-[SecKeyProxyTarget initWithKey:certificate:];
-[SecKeyProxyTarget initializeWithReply:];
-[SecKeyProxyTarget performOperation:mode:algorithm:parameters:reply:];
```
