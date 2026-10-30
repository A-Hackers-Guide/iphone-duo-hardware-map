# `LACUIMechanism` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) instanceId;
@property (TB,R,N) isRunning;
@property (T@"<LACEvaluationRequest>",R,N) request;
```

## Instance methods

```
-[LACUIMechanism isRunning];
-[LACUIMechanism request];
-[LACUIMechanism instanceId];
-[LACUIMechanism failAuthenticationWithError:];
-[LACUIMechanism internalInfoWithReply:];
-[LACUIMechanism uiEvent:options:];
-[LACUIMechanism uiFailureWithError:];
-[LACUIMechanism uiSuccessWithResult:];
```
