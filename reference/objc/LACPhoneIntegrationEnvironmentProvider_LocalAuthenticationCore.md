# `LACPhoneIntegrationEnvironmentProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCompanionAuthenticationEnvironmentProviding`
- 5 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<LACEligibilityHelping>" eligibilityHelper;
@"<LACSharingManaging>" sharingManager;
@"OS_dispatch_queue" workQueue;
B hasPairedDevices;
^v subscription;
```

## Properties

```
@property (T@"<LACEligibilityHelping>",N,R,VeligibilityHelper) eligibilityHelper;
@property (T@"<LACSharingManaging>",N,R,VsharingManager) sharingManager;
@property (T@"OS_dispatch_queue",N,R,VworkQueue) workQueue;
@property (TB,N,VhasPairedDevices) hasPairedDevices;
@property (T^v,N,Vsubscription) subscription;
@property (TB,N,R) isFeatureAvailable;
@property (T@"LACCompanionAuthenticationEnvironment",N,R) environment;
```

## Instance methods

```
-[LACPhoneIntegrationEnvironmentProvider subscription];
-[LACPhoneIntegrationEnvironmentProvider init];
-[LACPhoneIntegrationEnvironmentProvider workQueue];
-[LACPhoneIntegrationEnvironmentProvider dealloc];
-[LACPhoneIntegrationEnvironmentProvider setSubscription:];
-[LACPhoneIntegrationEnvironmentProvider environment];
-[LACPhoneIntegrationEnvironmentProvider isFeatureAvailable];
-[LACPhoneIntegrationEnvironmentProvider hasPairedDevices];
-[LACPhoneIntegrationEnvironmentProvider eligibilityHelper];
-[LACPhoneIntegrationEnvironmentProvider initWithEligibilityHelper:sharingManager:workQueue:];
-[LACPhoneIntegrationEnvironmentProvider setHasPairedDevices:];
-[LACPhoneIntegrationEnvironmentProvider sharingManager];
```
