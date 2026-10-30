# `LACCompanionAuthenticationRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCompanionAuthenticationRequestType`
- 5 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
? acmContextData;
@"LACClientInfo" clientInfo;
q companionType;
@"<LACEvaluationRequest>" evaluationRequest;
B isFallbackAvailable;
```

## Properties

```
@property (T@"NSData",N,R) acmContextData;
@property (T@"LACClientInfo",N,R,VclientInfo) clientInfo;
@property (Tq,N,R,VcompanionType) companionType;
@property (T@"<LACEvaluationRequest>",N,R,VevaluationRequest) evaluationRequest;
@property (TB,N,VisFallbackAvailable) isFallbackAvailable;
@property (TI,N,R) identifier;
```

## Instance methods

```
-[LACCompanionAuthenticationRequest clientInfo];
-[LACCompanionAuthenticationRequest identifier];
-[LACCompanionAuthenticationRequest init];
-[LACCompanionAuthenticationRequest companionType];
-[LACCompanionAuthenticationRequest acmContextData];
-[LACCompanionAuthenticationRequest evaluationRequest];
-[LACCompanionAuthenticationRequest initWithEvaluationRequest:clientInfo:companionType:];
-[LACCompanionAuthenticationRequest isFallbackAvailable];
-[LACCompanionAuthenticationRequest setIsFallbackAvailable:];
```
