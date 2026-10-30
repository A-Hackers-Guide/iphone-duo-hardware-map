# `TPSCallForwardingListController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPSListController`
- Protocols: `TPSCallForwardingControllerDelegate`
- 6 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _isAllowSupplementaryServicesOnDevice;
@"TPSCallForwardingController" _callForwardingController;
@"PSSpecifier" _conditionalServiceSwitchSpecifier;
@"PSSpecifier" _mainSwitchSpecifier;
@"TPSCarrierBundleController" _carrierBundleController;
@"CoreTelephonyClient" _telephonyClient;
```

## Properties

```
@property (T@"PSSpecifier",R,N,V_conditionalServiceSwitchSpecifier) conditionalServiceSwitchSpecifier;
@property (T@"PSSpecifier",R,N,V_mainSwitchSpecifier) mainSwitchSpecifier;
@property (TB,N,V_isAllowSupplementaryServicesOnDevice) isAllowSupplementaryServicesOnDevice;
@property (T@"TPSCarrierBundleController",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"CoreTelephonyClient",&,N,V_telephonyClient) telephonyClient;
@property (T@"TPSCallForwardingController",R,N,V_callForwardingController) callForwardingController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCallForwardingListController tableView:cellForRowAtIndexPath:];
-[TPSCallForwardingListController init];
-[TPSCallForwardingListController setTelephonyClient:];
-[TPSCallForwardingListController telephonyClient];
-[TPSCallForwardingListController configureCell:];
-[TPSCallForwardingListController specifiers];
-[TPSCallForwardingListController carrierBundleController];
-[TPSCallForwardingListController callForwardingController];
-[TPSCallForwardingListController callForwardingController:didChangeServiceType:];
-[TPSCallForwardingListController callForwardingController:didChangeValue:error:];
-[TPSCallForwardingListController conditionalServiceBusyPhoneNumber:];
-[TPSCallForwardingListController conditionalServiceSwitchOn:];
-[TPSCallForwardingListController conditionalServiceSwitchSpecifier];
-[TPSCallForwardingListController conditionalServiceTypeSpecifiers];
-[TPSCallForwardingListController conditionalServiceUnansweredPhoneNumber:];
-[TPSCallForwardingListController conditionalServiceUnreachablePhoneNumber:];
-[TPSCallForwardingListController configureCell:forSpecifier:];
-[TPSCallForwardingListController isAllowSupplementaryServicesOnDevice];
-[TPSCallForwardingListController mainSwitchSpecifier];
-[TPSCallForwardingListController setConditionalServiceBusyPhoneNumber:specifier:];
-[TPSCallForwardingListController setConditionalServiceSwitchOn:specifier:];
-[TPSCallForwardingListController setConditionalServiceUnansweredPhoneNumber:specifier:];
-[TPSCallForwardingListController setConditionalServiceUnreachablePhoneNumber:specifier:];
-[TPSCallForwardingListController setIsAllowSupplementaryServicesOnDevice:];
-[TPSCallForwardingListController setMainSwitchOn:];
-[TPSCallForwardingListController setUnconditionalServicePhoneNumber:specifier:];
-[TPSCallForwardingListController unconditionalServicePhoneNumber:];
-[TPSCallForwardingListController unconditionalServiceTypeSpecifiers];
```
