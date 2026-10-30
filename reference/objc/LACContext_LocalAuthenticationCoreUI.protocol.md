# `LACContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"NSUUID",R,N) uuid;
@property (T@"NSData",R) externalizedContext;
@property (T@"<LACContextUIDelegate>",W,N) uiDelegate;
```

## Instance methods

```
-[LACContext uuid];
-[LACContext bootstrapServiceType:completionHandler:];
-[LACContext setUiDelegate:];
-[LACContext externalizedContext];
-[LACContext pauseProcessedEvent:pause:reply:];
-[LACContext invalidate];
-[LACContext failProcessedEvent:failureError:reply:];
-[LACContext resetWithReply:];
-[LACContext uiDelegate];
-[LACContext addContextObserver:];
-[LACContext removeContextObserver:];
-[LACContext setOption:value:];
-[LACContext canEvaluateCorePolicy:error:];
-[LACContext coreCredentialOfType:error:];
-[LACContext coreCredentialOfType:reply:];
-[LACContext evaluateCorePolicy:options:error:];
-[LACContext evaluateCorePolicy:options:reply:];
-[LACContext setCoreCredential:type:error:];
-[LACContext setCoreCredential:type:options:error:];
-[LACContext setCoreCredential:type:options:reply:];
-[LACContext setCoreCredential:type:reply:];
```
