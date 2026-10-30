# `WiFiTelephonyClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientRegistrationDelegate`, `CoreTelephonyClientDataDelegate`, `CoreTelephonyClientCellularUsagePolicyDelegate`, `CoreTelephonyClientCarrierBundleDelegate`
- 17 instance variables, 28 properties, 48 instance methods, 1 class methods

## Instance variables

```
B _isCellularFallbackEnabled;
B _isIMSRegistrationActiveAndOnWiFi;
B _isCellular5GSupported;
B _cellular5GSupported;
B _cellularFallbackEnabled;
B _imsRegistrationActiveAndOnWiFi;
@? _cellularFallbackStatusChangedHandler;
@? _imsRegistrationStatusChangedHandler;
@? _cellularDataStatusChangedHandler;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"CoreTelephonyClient" _coreTelephonyClient;
@"CTMobileEquipmentInfo" _mobileEquipmentInfo;
@"CTDataStatus" _dataStatus;
@"CTDataConnectionStatus" _connectionStatus;
@"NSString" _radioAccessTechnology;
@"NSString" _registrationStatus;
@"NSString" _carrierName;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
@property (T@"CoreTelephonyClient",&,V_coreTelephonyClient) coreTelephonyClient;
@property (T@"CTMobileEquipmentInfo",&,V_mobileEquipmentInfo) mobileEquipmentInfo;
@property (T@"CTDataStatus",&,V_dataStatus) dataStatus;
@property (T@"CTDataConnectionStatus",&,V_connectionStatus) connectionStatus;
@property (T@"NSString",&,V_radioAccessTechnology) radioAccessTechnology;
@property (T@"NSString",&,V_registrationStatus) registrationStatus;
@property (T@"NSString",&,V_carrierName) carrierName;
@property (TB,GisCellular5GSupported,V_cellular5GSupported) cellular5GSupported;
@property (TB,GisCellularFallbackEnabled,V_cellularFallbackEnabled) cellularFallbackEnabled;
@property (TB,GisIMSRegistrationActiveAndOnWiFi,V_imsRegistrationActiveAndOnWiFi) imsRegistrationActiveAndOnWiFi;
@property (T@?,C,V_cellularFallbackStatusChangedHandler) cellularFallbackStatusChangedHandler;
@property (T@?,C,V_imsRegistrationStatusChangedHandler) imsRegistrationStatusChangedHandler;
@property (T@?,C,V_cellularDataStatusChangedHandler) cellularDataStatusChangedHandler;
@property (TB,R,V_isCellularFallbackEnabled) isCellularFallbackEnabled;
@property (TB,R,V_isIMSRegistrationActiveAndOnWiFi) isIMSRegistrationActiveAndOnWiFi;
@property (TB,R,V_isCellular5GSupported) isCellular5GSupported;
@property (TB,R) isCellular5GActive;
@property (TB,R) isCellularLTEActive;
@property (TB,R) isCellularDataInRoaming;
@property (T@"NSString",R,C) cellularICCID;
@property (T@"NSString",R,C) cellularInterfaceName;
@property (T@"NSString",R,C) cellularCarrierName;
@property (T@"NSString",R,C) cellularDataIndicator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WiFiTelephonyClient sharedInstance];
```

## Instance methods

```
-[WiFiTelephonyClient carrierBundleChange:];
-[WiFiTelephonyClient carrierName];
-[WiFiTelephonyClient mobileEquipmentInfo];
-[WiFiTelephonyClient setCarrierName:];
-[WiFiTelephonyClient setCoreTelephonyClient:];
-[WiFiTelephonyClient setCellularFallbackEnabled:];
-[WiFiTelephonyClient coreTelephonyClient];
-[WiFiTelephonyClient setConnectionStatus:];
-[WiFiTelephonyClient init];
-[WiFiTelephonyClient setMobileEquipmentInfo:];
-[WiFiTelephonyClient setRegistrationStatus:];
-[WiFiTelephonyClient connectionStateChanged:connection:dataConnectionStatusInfo:];
-[WiFiTelephonyClient registrationStatus];
-[WiFiTelephonyClient radioAccessTechnology];
-[WiFiTelephonyClient description];
-[WiFiTelephonyClient dataStatus];
-[WiFiTelephonyClient setInternalQueue:];
-[WiFiTelephonyClient setRadioAccessTechnology:];
-[WiFiTelephonyClient connectionStatus];
-[WiFiTelephonyClient internalQueue];
-[WiFiTelephonyClient displayStatusChanged:status:];
-[WiFiTelephonyClient imsRegistrationChanged:info:];
-[WiFiTelephonyClient reliableNetworkFallbackChanged:userEnabled:];
-[WiFiTelephonyClient _updateCellularMEIAndDataStatus];
-[WiFiTelephonyClient _dataIndicatorToString:];
-[WiFiTelephonyClient _getCurrentDataServiceContext];
-[WiFiTelephonyClient cellularCarrierName];
-[WiFiTelephonyClient cellularDataIndicator];
-[WiFiTelephonyClient cellularDataStatusChangedHandler];
-[WiFiTelephonyClient cellularFallbackStatusChangedHandler];
-[WiFiTelephonyClient cellularICCID];
-[WiFiTelephonyClient cellularInterfaceName];
-[WiFiTelephonyClient imsRegistrationStatusChangedHandler];
-[WiFiTelephonyClient isCellular5GActive];
-[WiFiTelephonyClient isCellular5GSupported];
-[WiFiTelephonyClient isCellular5GSupported];
-[WiFiTelephonyClient isCellularDataInRoaming];
-[WiFiTelephonyClient isCellularFallbackEnabled];
-[WiFiTelephonyClient isCellularFallbackEnabled];
-[WiFiTelephonyClient isCellularLTEActive];
-[WiFiTelephonyClient isIMSRegistrationActiveAndOnWiFi];
-[WiFiTelephonyClient isIMSRegistrationActiveAndOnWiFi];
-[WiFiTelephonyClient setCellular5GSupported:];
-[WiFiTelephonyClient setCellularDataStatusChangedHandler:];
-[WiFiTelephonyClient setCellularFallbackStatusChangedHandler:];
-[WiFiTelephonyClient setDataStatus:];
-[WiFiTelephonyClient setImsRegistrationActiveAndOnWiFi:];
-[WiFiTelephonyClient setImsRegistrationStatusChangedHandler:];
```
