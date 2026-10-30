# `TPSCloudCallingThumperProvisioningURLController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSCloudCallingURLController`
- Protocols: `TUCallCapabilitiesDelegatePrivate`
- 0 instance variables, 6 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) shouldShowUpgradeToThumperButton;
@property (TB,R,N,GisThumperProvisioningInProcess) thumperProvisioningInProcess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCloudCallingThumperProvisioningURLController initWithSubscriptionContext:];
-[TPSCloudCallingThumperProvisioningURLController didChangeThumperCallingProvisionalURLForSenderIdentityWithUUID:];
-[TPSCloudCallingThumperProvisioningURLController capabilityProvisioningPostData];
-[TPSCloudCallingThumperProvisioningURLController capabilityProvisioningStatus];
-[TPSCloudCallingThumperProvisioningURLController capabilityProvisioningURL];
-[TPSCloudCallingThumperProvisioningURLController enableCapability];
-[TPSCloudCallingThumperProvisioningURLController isCapabilityEnabled];
-[TPSCloudCallingThumperProvisioningURLController isCapabilityProvisioningURLInvalid];
-[TPSCloudCallingThumperProvisioningURLController isThumperProvisioningInProcess];
-[TPSCloudCallingThumperProvisioningURLController requestTimeoutController];
-[TPSCloudCallingThumperProvisioningURLController shouldShowEmergencyAddress];
-[TPSCloudCallingThumperProvisioningURLController shouldShowUpgradeToThumperButton];
-[TPSCloudCallingThumperProvisioningURLController webSheetCompletion];
```
