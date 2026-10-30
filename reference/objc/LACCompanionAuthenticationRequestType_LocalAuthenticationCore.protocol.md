# `LACCompanionAuthenticationRequestType` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) identifier;
@property (T@"NSData",R,N) acmContextData;
@property (T@"LACClientInfo",R,N) clientInfo;
@property (Tq,R,N) companionType;
@property (TB,R,N) isFallbackAvailable;
```

## Instance methods

```
-[LACCompanionAuthenticationRequestType clientInfo];
-[LACCompanionAuthenticationRequestType identifier];
-[LACCompanionAuthenticationRequestType companionType];
-[LACCompanionAuthenticationRequestType acmContextData];
-[LACCompanionAuthenticationRequestType isFallbackAvailable];
```
