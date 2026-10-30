# `LACAgentProxyXPCWrapper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAgentProxyXPC`
- 3 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
@"<LACAgentProxyXPC>" _agentProxy;
@"<LACAgentProxyXPCWrapperDelegate>" _delegate;
```

## Properties

```
@property (T@"<LACAgentProxyXPCWrapperDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[LACAgentProxyXPCWrapper initWithConnection:];
-[LACAgentProxyXPCWrapper setDelegate:];
-[LACAgentProxyXPCWrapper delegate];
-[LACAgentProxyXPCWrapper dumpStatusWithCompletion:];
-[LACAgentProxyXPCWrapper _agentProxy:];
-[LACAgentProxyXPCWrapper queryUuid:completionHandler:];
-[LACAgentProxyXPCWrapper registerAcmExternalizedFormHash:uuid:completionHandler:];
-[LACAgentProxyXPCWrapper registerContextWithUuid:ownership:description:originalUuid:originalAcmHash:completionHandler:];
-[LACAgentProxyXPCWrapper remoteAuthenticationInProgressWithPriority:reply:];
-[LACAgentProxyXPCWrapper setFUSDisabled:completionHandler:];
```
