# `LACDefaultServiceSession`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACServiceSession`
- 4 instance variables, 8 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<LACService>" _service;
@"NSString" _serviceType;
@"NSString" _clientID;
@"NSUUID" _sessionID;
```

## Properties

```
@property (T@"NSUUID",R,N,V_sessionID) sessionID;
@property (T@"NSString",R,N,V_serviceType) serviceType;
@property (T@"<LACService>",R,N,V_service) service;
@property (T@"NSString",R,N,V_clientID) clientID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDefaultServiceSession clientID];
-[LACDefaultServiceSession sessionID];
-[LACDefaultServiceSession dealloc];
-[LACDefaultServiceSession service];
-[LACDefaultServiceSession serviceType];
-[LACDefaultServiceSession initWithService:serviceType:client:];
```
