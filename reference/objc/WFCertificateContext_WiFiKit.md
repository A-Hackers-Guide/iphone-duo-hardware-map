# `WFCertificateContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFCertificateProviderContext`, `WFContextPresenting`
- 7 instance variables, 12 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _requestedFields;
@"NSArray" _certificateChain;
^{__SecTrust=} _certificateTrust;
@"UIViewController<WFNetworkView>" _provider;
@? _completionHandler;
@"WFNetworkProfile" _profile;
@"WFNetworkScanRecord" _network;
```

## Properties

```
@property (T@"NSArray",&,N,V_certificateChain) certificateChain;
@property (T^{__SecTrust=},N,V_certificateTrust) certificateTrust;
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (Tq,N,V_requestedFields) requestedFields;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController<WFNetworkView>",W,N,V_provider) provider;
@property (TB,R,N) needsDismissal;
```

## Instance methods

```
-[WFCertificateContext setCompletionHandler:];
-[WFCertificateContext completionHandler];
-[WFCertificateContext network];
-[WFCertificateContext dealloc];
-[WFCertificateContext setProfile:];
-[WFCertificateContext provider];
-[WFCertificateContext requestedFields];
-[WFCertificateContext profile];
-[WFCertificateContext cancel];
-[WFCertificateContext setProvider:];
-[WFCertificateContext setRequestedFields:];
-[WFCertificateContext accept];
-[WFCertificateContext setNetwork:];
-[WFCertificateContext certificateChain];
-[WFCertificateContext setCertificateChain:];
-[WFCertificateContext launchSettings];
-[WFCertificateContext certificateTrust];
-[WFCertificateContext setCertificateTrust:];
-[WFCertificateContext initWithNetwork:profile:certificateChain:];
-[WFCertificateContext needsDismissal];
```
