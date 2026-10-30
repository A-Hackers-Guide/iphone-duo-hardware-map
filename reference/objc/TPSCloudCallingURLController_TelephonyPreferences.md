# `TPSCloudCallingURLController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _capabilityEnabled;
B _capabilityProvisioningURLInvalid;
i _capabilityProvisioningStatus;
@"<TPSCloudCallingURLControllerDelegate>" _delegate;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
@"NSURL" _capabilityProvisioningURL;
@"NSData" _capabilityProvisioningPostData;
@"TPSCarrierBundleController" _carrierBundleController;
@"TPSCloudCallingWebViewController" _webViewController;
```

## Properties

```
@property (T@"TPSCarrierBundleController",&,N,V_carrierBundleController) carrierBundleController;
@property (T@"TPSCloudCallingWebViewController",W,N,V_webViewController) webViewController;
@property (T@"<TPSCloudCallingURLControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"TUSenderIdentityCapabilities",R,N) subscriptionCapabilities;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (TB,R,N) shouldEnableCapability;
@property (TB,R,N,GisCapabilityEnabled,V_capabilityEnabled) capabilityEnabled;
@property (Ti,R,N,V_capabilityProvisioningStatus) capabilityProvisioningStatus;
@property (T@"NSURL",R,C,N,V_capabilityProvisioningURL) capabilityProvisioningURL;
@property (TB,R,N,GisCapabilityProvisioningURLInvalid,V_capabilityProvisioningURLInvalid) capabilityProvisioningURLInvalid;
@property (T@"NSData",R,C,N,V_capabilityProvisioningPostData) capabilityProvisioningPostData;
```

## Instance methods

```
-[TPSCloudCallingURLController init];
-[TPSCloudCallingURLController setDelegate:];
-[TPSCloudCallingURLController delegate];
-[TPSCloudCallingURLController initWithSubscriptionContext:];
-[TPSCloudCallingURLController carrierBundleController];
-[TPSCloudCallingURLController setWebViewController:];
-[TPSCloudCallingURLController webViewController];
-[TPSCloudCallingURLController subscriptionContext];
-[TPSCloudCallingURLController subscriptionCapabilities];
-[TPSCloudCallingURLController _webViewControllerWithType:];
-[TPSCloudCallingURLController capabilityProvisioningPostData];
-[TPSCloudCallingURLController capabilityProvisioningStatus];
-[TPSCloudCallingURLController capabilityProvisioningURL];
-[TPSCloudCallingURLController enableCapability];
-[TPSCloudCallingURLController genericErrorAlertController];
-[TPSCloudCallingURLController isCapabilityEnabled];
-[TPSCloudCallingURLController isCapabilityProvisioningURLInvalid];
-[TPSCloudCallingURLController loadWebViewController];
-[TPSCloudCallingURLController provisionCapabilityController];
-[TPSCloudCallingURLController reloadWebViewController];
-[TPSCloudCallingURLController setCarrierBundleController:];
-[TPSCloudCallingURLController shouldEnableCapability];
-[TPSCloudCallingURLController subscriptionCapabilitiesForSubscriptionContextUUID:];
-[TPSCloudCallingURLController updateEmergencyAddressController];
-[TPSCloudCallingURLController webSheetCompletion];
```
