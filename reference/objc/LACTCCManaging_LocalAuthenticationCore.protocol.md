# `LACTCCManaging` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 3 instance methods, 1 class methods

## Properties

```
@property (class, T@"NSString",R,N) faceIDServiceName;
```

## Class methods

```
+[LACTCCManaging faceIDServiceName];
```

## Instance methods

```
-[LACTCCManaging requestAuthorizationForService:completion:];
-[LACTCCManaging authorizationStatusForService:auditToken:promptUser:];
-[LACTCCManaging authorizationStatusOfFaceIDServiceForAuditToken:];
```
