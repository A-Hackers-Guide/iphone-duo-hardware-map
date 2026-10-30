# `LACTCCManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACTCCManaging`
- 0 instance variables, 4 properties, 4 instance methods, 2 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACTCCManager sharedInstance];
+[LACTCCManager faceIDServiceName];
```

## Instance methods

```
-[LACTCCManager requestAuthorizationForService:completion:];
-[LACTCCManager _authorizationStatusFromRight:];
-[LACTCCManager authorizationStatusForService:auditToken:promptUser:];
-[LACTCCManager authorizationStatusOfFaceIDServiceForAuditToken:];
```
