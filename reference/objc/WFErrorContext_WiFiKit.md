# `WFErrorContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFErrorProviderContext`, `WFContextPresenting`
- 6 instance variables, 11 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _needsDismissal;
@"UIViewController<WFNetworkView>" _provider;
@"<WFDiagnosticsResultItem>" _result;
@? _completionHandler;
@"NSError" _error;
@"<WFNetworkListRecord>" _network;
```

## Properties

```
@property (T@"NSError",&,N,V_error) error;
@property (T@"<WFNetworkListRecord>",&,N,V_network) network;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"<WFDiagnosticsResultItem>",&,N,V_result) result;
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
-[WFErrorContext setError:];
-[WFErrorContext setResult:];
-[WFErrorContext setCompletionHandler:];
-[WFErrorContext completionHandler];
-[WFErrorContext network];
-[WFErrorContext provider];
-[WFErrorContext requestedFields];
-[WFErrorContext error];
-[WFErrorContext result];
-[WFErrorContext description];
-[WFErrorContext cancel];
-[WFErrorContext setProvider:];
-[WFErrorContext setNetwork:];
-[WFErrorContext _userInfoForAssociationError:networkName:];
-[WFErrorContext initWithAssociationError:network:diagnosticsResult:];
-[WFErrorContext needsDismissal];
```
