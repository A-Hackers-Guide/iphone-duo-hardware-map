# `WFWAPICertificatePromptOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- Protocols: `WFOtherNetworkViewControllerDelegate`
- 8 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _userCancelled;
^{__SecIdentity=} _WAPIRootCertificate;
@"NSData" _WAPIIdentityPEMBlob;
@"UIViewController" _rootViewController;
@"WFNetworkScanRecord" _network;
@"WFOtherNetworkViewController" _promptViewController;
@"UINavigationController" _navigationController;
@"NSArray" _wapiIdentityMapping;
```

## Properties

```
@property (TB,N,V_userCancelled) userCancelled;
@property (T^{__SecIdentity=},N,V_WAPIRootCertificate) WAPIRootCertificate;
@property (T@"NSData",&,N,V_WAPIIdentityPEMBlob) WAPIIdentityPEMBlob;
@property (T@"UIViewController",&,N,V_rootViewController) rootViewController;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (T@"WFOtherNetworkViewController",&,N,V_promptViewController) promptViewController;
@property (T@"UINavigationController",&,N,V_navigationController) navigationController;
@property (T@"NSArray",&,N,V_wapiIdentityMapping) wapiIdentityMapping;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFWAPICertificatePromptOperation rootViewController];
-[WFWAPICertificatePromptOperation setRootViewController:];
-[WFWAPICertificatePromptOperation network];
-[WFWAPICertificatePromptOperation finish];
-[WFWAPICertificatePromptOperation start];
-[WFWAPICertificatePromptOperation setNavigationController:];
-[WFWAPICertificatePromptOperation navigationController];
-[WFWAPICertificatePromptOperation setNetwork:];
-[WFWAPICertificatePromptOperation setUserCancelled:];
-[WFWAPICertificatePromptOperation userCancelled];
-[WFWAPICertificatePromptOperation WAPIIdentityPEMBlob];
-[WFWAPICertificatePromptOperation WAPIRootCertificate];
-[WFWAPICertificatePromptOperation initWithRootViewController:network:];
-[WFWAPICertificatePromptOperation otherNetworkViewController:isValidPassword:];
-[WFWAPICertificatePromptOperation otherNetworkViewControllerUserDidTapCancel:];
-[WFWAPICertificatePromptOperation otherNetworkViewControllerUserDidTapJoin:];
-[WFWAPICertificatePromptOperation promptViewController];
-[WFWAPICertificatePromptOperation setPromptViewController:];
-[WFWAPICertificatePromptOperation setWAPIIdentityPEMBlob:];
-[WFWAPICertificatePromptOperation setWAPIRootCertificate:];
-[WFWAPICertificatePromptOperation setWapiIdentityMapping:];
-[WFWAPICertificatePromptOperation wapiIdentityMapping];
```
