# `WFLockdownModeContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFLockdownModeProviderContext`, `WFContextPresenting`
- 5 instance variables, 10 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _needsDismissal;
@"UIViewController<WFNetworkView>" _provider;
@? _completionHandler;
@"<WFNetworkListRecord>" _network;
Q _securityType;
```

## Properties

```
@property (T@"<WFNetworkListRecord>",&,N,V_network) network;
@property (TQ,N,V_securityType) securityType;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (Tq,R,N) requestedFields;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController<WFNetworkView>",W,N,V_provider) provider;
@property (TB,R,N,V_needsDismissal) needsDismissal;
```

## Instance methods

```
-[WFLockdownModeContext securityType];
-[WFLockdownModeContext setCompletionHandler:];
-[WFLockdownModeContext completionHandler];
-[WFLockdownModeContext network];
-[WFLockdownModeContext provider];
-[WFLockdownModeContext requestedFields];
-[WFLockdownModeContext cancel];
-[WFLockdownModeContext setProvider:];
-[WFLockdownModeContext setSecurityType:];
-[WFLockdownModeContext setNetwork:];
-[WFLockdownModeContext join];
-[WFLockdownModeContext initWithNetwork:securityType:];
-[WFLockdownModeContext needsDismissal];
```
