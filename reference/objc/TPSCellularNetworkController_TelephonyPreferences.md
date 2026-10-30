# `TPSCellularNetworkController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TPSRegistrationTelephonyControllerDelegate`
- 7 instance variables, 12 properties, 23 instance methods, 0 class methods

## Instance variables

```
q _networkSelectionMode;
@"TPSCellularNetworkItem" _selectedNetworkItem;
@"NSArray" _networkItems;
@"TPSRegistrationTelephonyController" _registrationController;
@"NSArray" _networks;
@"CTNetworkSelectionInfo" _networkSelectionInfo;
@"CTXPCServiceSubscriptionContext" _subscriptionContext;
```

## Properties

```
@property (T@"NSArray",C,N,V_networkItems) networkItems;
@property (Tq,N,V_networkSelectionMode) networkSelectionMode;
@property (T@"TPSCellularNetworkItem",&,N,V_selectedNetworkItem) selectedNetworkItem;
@property (T@"TPSRegistrationTelephonyController",R,N,V_registrationController) registrationController;
@property (T@"NSArray",C,N,V_networks) networks;
@property (T@"CTNetworkSelectionInfo",&,N,V_networkSelectionInfo) networkSelectionInfo;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_subscriptionContext) subscriptionContext;
@property (TB,R,N,GisNetworkSelectionEnabled) networkSelectionEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPSCellularNetworkController setNetworks:];
-[TPSCellularNetworkController init];
-[TPSCellularNetworkController networks];
-[TPSCellularNetworkController initWithSubscriptionContext:];
-[TPSCellularNetworkController subscriptionContext];
-[TPSCellularNetworkController networkSelectionMode];
-[TPSCellularNetworkController setNetworkSelectionMode:];
-[TPSCellularNetworkController isNetworkSelectionEnabled];
-[TPSCellularNetworkController networkItemAtIndex:];
-[TPSCellularNetworkController networkItemForNetwork:];
-[TPSCellularNetworkController networkItems];
-[TPSCellularNetworkController networkSelectionInfo];
-[TPSCellularNetworkController networkSelectionInfoChangedForRegistrationController:];
-[TPSCellularNetworkController networksChangedForRegistrationController:];
-[TPSCellularNetworkController registrationController];
-[TPSCellularNetworkController selectNetworkItemAtIndex:];
-[TPSCellularNetworkController selectNetworkSelectionMode:];
-[TPSCellularNetworkController selectedNetworkItem];
-[TPSCellularNetworkController setNetworkItems:];
-[TPSCellularNetworkController setNetworkSelectionInfo:];
-[TPSCellularNetworkController setSelectedNetworkItem:];
-[TPSCellularNetworkController updateNetworkSelectionModeForNetworkSelectionInfo:];
-[TPSCellularNetworkController updateSelectedNetworkForNetworkSelectionInfo:];
```
