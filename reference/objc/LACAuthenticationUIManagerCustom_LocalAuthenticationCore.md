# `LACAuthenticationUIManagerCustom`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAuthenticationUIManaging`, `LACEvaluationEventHandling`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<LACEvaluationRequest>" request;
q type;
? authenticationHints;
? uiEventDelegate;
? uiDelegate;
```

## Properties

```
@property (T@"<LACEvaluationRequest>",N,R,Vrequest) request;
@property (Tq,N,R,Vtype) type;
@property (T@"NSDictionary",N,C) authenticationHints;
@property (T@"<LACAuthenticationUIProxy>",N,W,VuiEventDelegate) uiEventDelegate;
@property (T@"<LACContextUIDelegate>",N,W,VuiDelegate) uiDelegate;
```

## Instance methods

```
-[LACAuthenticationUIManagerCustom init];
-[LACAuthenticationUIManagerCustom setUiDelegate:];
-[LACAuthenticationUIManagerCustom request];
-[LACAuthenticationUIManagerCustom type];
-[LACAuthenticationUIManagerCustom uiDelegate];
-[LACAuthenticationUIManagerCustom uiEventDelegate];
-[LACAuthenticationUIManagerCustom authenticationHints];
-[LACAuthenticationUIManagerCustom handleEvaluationEvent:completion:];
-[LACAuthenticationUIManagerCustom initWithRequest:uiDelegate:];
-[LACAuthenticationUIManagerCustom setAuthenticationHints:];
-[LACAuthenticationUIManagerCustom setUiEventDelegate:];
```
