# `LACAuthenticationUIManagerComposite`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAuthenticationUIManaging`, `LACEvaluationEventHandling`, `LACAuthenticationUIProxy`, `LACAuthenticationUIEventHandling`
- 9 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<LACEvaluationRequest>" request;
q type;
? uiEventDelegate;
? authenticationHints;
? managers;
$__lazy_storage_$_customUIManagers;
$__lazy_storage_$_defaultUIManagers;
? extendedInternalInfo;
eventQueue;
```

## Properties

```
@property (T@"<LACEvaluationRequest>",N,R,Vrequest) request;
@property (Tq,N,R,Vtype) type;
@property (T@"<LACAuthenticationUIProxy>",N,W,VuiEventDelegate) uiEventDelegate;
@property (T@"NSDictionary",N,C) authenticationHints;
@property (T@"NSArray",N,R) managers;
@property (T@"NSArray",N,C) customUIManagers;
@property (T@"NSArray",N,C) defaultUIManagers;
@property (T@"NSDictionary",N,C) extendedInternalInfo;
@property (T@"<LACBackoffCounter>",N,R) backoffCounter;
```

## Instance methods

```
-[LACAuthenticationUIManagerComposite init];
-[LACAuthenticationUIManagerComposite dealloc];
-[LACAuthenticationUIManagerComposite managers];
-[LACAuthenticationUIManagerComposite request];
-[LACAuthenticationUIManagerComposite type];
-[LACAuthenticationUIManagerComposite externalizedContextWithError:];
-[LACAuthenticationUIManagerComposite extendedInternalInfoForRemoteUI];
-[LACAuthenticationUIManagerComposite uiEventDelegate];
-[LACAuthenticationUIManagerComposite authenticationHints];
-[LACAuthenticationUIManagerComposite backoffCounter];
-[LACAuthenticationUIManagerComposite customUIManagers];
-[LACAuthenticationUIManagerComposite defaultUIManagers];
-[LACAuthenticationUIManagerComposite extendedInternalInfo];
-[LACAuthenticationUIManagerComposite finishRunWithResult:error:];
-[LACAuthenticationUIManagerComposite handleEvaluationEvent:completion:];
-[LACAuthenticationUIManagerComposite initWithRequest:managers:];
-[LACAuthenticationUIManagerComposite internalInfoWithReply:];
-[LACAuthenticationUIManagerComposite setAuthenticationHints:];
-[LACAuthenticationUIManagerComposite setCustomUIManagers:];
-[LACAuthenticationUIManagerComposite setDefaultUIManagers:];
-[LACAuthenticationUIManagerComposite setExtendedInternalInfo:];
-[LACAuthenticationUIManagerComposite setUiEventDelegate:];
-[LACAuthenticationUIManagerComposite shouldFinishRunWithResult:error:];
-[LACAuthenticationUIManagerComposite uiEvent:options:];
```
