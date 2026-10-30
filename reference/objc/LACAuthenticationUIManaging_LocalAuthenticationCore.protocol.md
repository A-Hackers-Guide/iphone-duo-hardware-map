# `LACAuthenticationUIManaging` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `LACEvaluationEventHandling`
- 0 instance variables, 4 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) authenticationHints;
@property (T@"<LACAuthenticationUIProxy>",W,N) uiEventDelegate;
@property (T@"<LACEvaluationRequest>",R,N) request;
@property (Tq,R,N) type;
```

## Instance methods

```
-[LACAuthenticationUIManaging request];
-[LACAuthenticationUIManaging type];
-[LACAuthenticationUIManaging uiEventDelegate];
-[LACAuthenticationUIManaging authenticationHints];
-[LACAuthenticationUIManaging setAuthenticationHints:];
-[LACAuthenticationUIManaging setUiEventDelegate:];
```
