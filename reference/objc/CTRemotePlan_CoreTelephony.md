# `CTRemotePlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTPlan`
- 12 instance variables, 12 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"CTRemotePlanIdentifier" _planID;
@"CTPlanTransferAttributes" _transferAttributes;
@"CTPlanSignUpDetails" _signUpDetails;
Q _addOnCarrierFlowType;
@"NSNumber" _primaryAccount;
@"CTDeviceIdentifier" _deviceID;
@"NSNumber" _isDataActive;
@"NSNumber" _needHideForCloudFlow;
@"NSNumber" _needVisitStoreForTransfer;
Q _qsLifecycleState;
Q _qsRole;
Q _addOnPurchaseType;
```

## Properties

```
@property (T@"CTRemotePlanIdentifier",&,N,V_planID) planID;
@property (T@"CTPlanTransferAttributes",&,N,V_transferAttributes) transferAttributes;
@property (T@"CTPlanSignUpDetails",&,N,V_signUpDetails) signUpDetails;
@property (TQ,N,V_addOnPurchaseType) addOnPurchaseType;
@property (TQ,N,V_addOnCarrierFlowType) addOnCarrierFlowType;
@property (T@"NSNumber",&,N,V_primaryAccount) primaryAccount;
@property (T@"CTDeviceIdentifier",&,N,V_deviceID) deviceID;
@property (T@"NSNumber",&,N,V_isDataActive) isDataActive;
@property (T@"NSNumber",&,N,V_needHideForCloudFlow) needHideForCloudFlow;
@property (T@"NSNumber",&,N,V_needVisitStoreForTransfer) needVisitStoreForTransfer;
@property (TQ,N,V_qsLifecycleState) qsLifecycleState;
@property (TQ,N,V_qsRole) qsRole;
```

## Class methods

```
+[CTRemotePlan supportsSecureCoding];
```

## Instance methods

```
-[CTRemotePlan phoneNumber];
-[CTRemotePlan carrierName];
-[CTRemotePlan init];
-[CTRemotePlan deviceID];
-[CTRemotePlan label];
-[CTRemotePlan iccid];
-[CTRemotePlan setDeviceID:];
-[CTRemotePlan countryCode];
-[CTRemotePlan encodeWithCoder:];
-[CTRemotePlan description];
-[CTRemotePlan initWithCoder:];
-[CTRemotePlan isEqual:];
-[CTRemotePlan addOnCarrierFlowType];
-[CTRemotePlan addOnPurchaseType];
-[CTRemotePlan isDataActive];
-[CTRemotePlan needHideForCloudFlow];
-[CTRemotePlan needVisitStoreForTransfer];
-[CTRemotePlan planID];
-[CTRemotePlan primaryAccount];
-[CTRemotePlan qsLifecycleState];
-[CTRemotePlan qsRole];
-[CTRemotePlan setAddOnCarrierFlowType:];
-[CTRemotePlan setAddOnPurchaseType:];
-[CTRemotePlan setIsDataActive:];
-[CTRemotePlan setNeedHideForCloudFlow:];
-[CTRemotePlan setNeedVisitStoreForTransfer:];
-[CTRemotePlan setPlanID:];
-[CTRemotePlan setPrimaryAccount:];
-[CTRemotePlan setQsLifecycleState:];
-[CTRemotePlan setQsRole:];
-[CTRemotePlan setSignUpDetails:];
-[CTRemotePlan setTransferAttributes:];
-[CTRemotePlan signUpDetails];
-[CTRemotePlan transferAttributes];
```
