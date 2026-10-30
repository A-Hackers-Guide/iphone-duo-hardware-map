# `LACAgentProxyWithErrorHandler`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAgentProxyXPC`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<LACAgentProxyXPC>" _agentProxy;
@? _errorHandler;
```

## Instance methods

```
-[LACAgentProxyWithErrorHandler dumpStatusWithCompletion:];
-[LACAgentProxyWithErrorHandler initWithAgentProxy:errorHandler:];
-[LACAgentProxyWithErrorHandler queryUuid:completionHandler:];
-[LACAgentProxyWithErrorHandler registerAcmExternalizedFormHash:uuid:completionHandler:];
-[LACAgentProxyWithErrorHandler registerContextWithUuid:ownership:description:originalUuid:originalAcmHash:completionHandler:];
-[LACAgentProxyWithErrorHandler remoteAuthenticationInProgressWithPriority:reply:];
-[LACAgentProxyWithErrorHandler setFUSDisabled:completionHandler:];
```
