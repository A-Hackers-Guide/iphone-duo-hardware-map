# `TPSWiFiCallingController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallCapabilitiesDelegatePrivate`
- 7 instance variables, 20 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"TUSenderIdentityCapabilities" _subscriptionCapabilities;
@"TPSCloudCallingEmergencyAddressURLController" _emergencyAddressURLController;
@"TPSCloudCallingThumperProvisioningURLController" _thumperProvisioningURLController;
@"TPSCarrierBundleController" _carrierBundleController;
@"TPSEncryptedIdentityClient" _encryptedIdentityClient;
@"NSDictionary" _encryptedIdentityInfo;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"TPSCarrierBundleController",&,N,V_carrierBundleController) carrierBundleController;
@property (T@"TPSEncryptedIdentityClient",&,N,V_encryptedIdentityClient) encryptedIdentityClient;
@property (T@"NSDictionary",C,N,V_encryptedIdentityInfo) encryptedIdentityInfo;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (T@"TUSenderIdentityCapabilities",&,N,V_subscriptionCapabilities) subscriptionCapabilities;
@property (TB,R,N) supportsEncryptedIdentity;
@property (TB,N,GisThumperCallingEnabled) thumperCallingEnabled;
@property (TB,N,GisWiFiCallingEnabled) wiFiCallingEnabled;
@property (TB,N,GisWiFiCallingRoamingEnabled) wiFiCallingRoamingEnabled;
@property (TB,R,N) canEnableThumperCalling;
@property (TB,R,N) supportsWiFiCalling;
@property (TB,R,N) supportsWiFiEmergencyCalling;
@property (TB,R,N) isWiFiCallingCertified;
@property (T@"NSString",R,C,N) localizedCarrierName;
@property (T@"TPSCloudCallingEmergencyAddressURLController",&,N,V_emergencyAddressURLController) emergencyAddressURLController;
@property (T@"TPSCloudCallingThumperProvisioningURLController",&,N,V_thumperProvisioningURLController) thumperProvisioningURLController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSWiFiCallingController didChangeThumperCallingCapabilitiesForSenderIdentityWithUUID:];
-[TPSWiFiCallingController init];
-[TPSWiFiCallingController setWiFiCallingEnabled:];
-[TPSWiFiCallingController canEnableThumperCalling];
-[TPSWiFiCallingController isWiFiCallingEnabled];
-[TPSWiFiCallingController supportsWiFiEmergencyCalling];
-[TPSWiFiCallingController setThumperCallingEnabled:];
-[TPSWiFiCallingController isWiFiCallingRoamingEnabled];
-[TPSWiFiCallingController isThumperCallingEnabled];
-[TPSWiFiCallingController supportsWiFiCalling];
-[TPSWiFiCallingController setWiFiCallingRoamingEnabled:];
-[TPSWiFiCallingController initWithSubscriptionContext:];
-[TPSWiFiCallingController carrierBundleController];
-[TPSWiFiCallingController didChangeWiFiCallingCapabilitiesForSenderIdentityWithUUID:];
-[TPSWiFiCallingController subscriptionContext];
-[TPSWiFiCallingController subscriptionCapabilities];
-[TPSWiFiCallingController emergencyAddressURLController];
-[TPSWiFiCallingController encryptedIdentityClient];
-[TPSWiFiCallingController encryptedIdentityInfo];
-[TPSWiFiCallingController isWiFiCallingCertified];
-[TPSWiFiCallingController localizedCarrierName];
-[TPSWiFiCallingController setCarrierBundleController:];
-[TPSWiFiCallingController setEmergencyAddressURLController:];
-[TPSWiFiCallingController setEncryptedIdentityClient:];
-[TPSWiFiCallingController setEncryptedIdentityInfo:];
-[TPSWiFiCallingController setSubscriptionCapabilities:];
-[TPSWiFiCallingController setThumperProvisioningURLController:];
-[TPSWiFiCallingController subscriptionCapabilitiesForSubscriptionContextUUID:];
-[TPSWiFiCallingController supportsEncryptedIdentity];
-[TPSWiFiCallingController thumperProvisioningURLController];
```
