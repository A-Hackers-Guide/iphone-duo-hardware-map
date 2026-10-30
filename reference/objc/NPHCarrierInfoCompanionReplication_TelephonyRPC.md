# `NPHCarrierInfoCompanionReplication`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSUserDefaults" _mobilePhoneUserDefaults;
@"NSUserDefaults" _nanoPhoneUserDefaults;
@"NPSManager" _npsManager;
```

## Properties

```
@property (T@"NSUserDefaults",R,N,V_mobilePhoneUserDefaults) mobilePhoneUserDefaults;
@property (T@"NSUserDefaults",R,N,V_nanoPhoneUserDefaults) nanoPhoneUserDefaults;
@property (T@"NPSManager",R,N,V_npsManager) npsManager;
```

## Class methods

```
+[NPHCarrierInfoCompanionReplication sharedInstance];
```

## Instance methods

```
-[NPHCarrierInfoCompanionReplication init];
-[NPHCarrierInfoCompanionReplication dealloc];
-[NPHCarrierInfoCompanionReplication npsManager];
-[NPHCarrierInfoCompanionReplication _updateHasCarrierVoicemailAccountsKey];
-[NPHCarrierInfoCompanionReplication _updateIsVisualVoicemailServiceSubscribed];
-[NPHCarrierInfoCompanionReplication _visualVMSubscriptionStateStatusChanged:];
-[NPHCarrierInfoCompanionReplication mobilePhoneUserDefaults];
-[NPHCarrierInfoCompanionReplication nanoPhoneUserDefaults];
```
