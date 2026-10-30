# `WFTrustCertificateViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TrustCertificateViewController`
- Protocols: `TrustCertificateViewControllerDelegate`, `WFNetworkView`
- 2 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _wantsModalPresentation;
@"<WFCertificateProviderContext>" _credentialsContext;
```

## Properties

```
@property (T@"<WFCertificateProviderContext>",&,N,V_credentialsContext) credentialsContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N,V_wantsModalPresentation) wantsModalPresentation;
```

## Instance methods

```
-[WFTrustCertificateViewController wantsModalPresentation];
-[WFTrustCertificateViewController trustCertificateViewController:finishedWithReturnCode:];
-[WFTrustCertificateViewController credentialsContext];
-[WFTrustCertificateViewController initWithCertificateProviderContext:];
-[WFTrustCertificateViewController setCredentialsContext:];
```
