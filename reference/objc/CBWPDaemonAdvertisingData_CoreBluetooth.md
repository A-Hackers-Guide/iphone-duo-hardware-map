# `CBWPDaemonAdvertisingData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
C _advInstanceType;
B _enableAdvertisingWithPowerAssertion;
B _enableEPAForAdvertisement;
B _enableObjectLocatorResponseOnAdvertisingInstance;
B _stopOnAdvertisingAddressChange;
S _advInterval;
@"NSDictionary" _advDataPerType;
@"NSArray" _listOfClients;
@"NSData" _mfgData;
@ _advertisingMetric;
```

## Properties

```
@property (TC,N,V_advInstanceType) advInstanceType;
@property (TS,N,V_advInterval) advInterval;
@property (T@"NSDictionary",C,N,V_advDataPerType) advDataPerType;
@property (TB,N,V_enableAdvertisingWithPowerAssertion) enableAdvertisingWithPowerAssertion;
@property (TB,N,V_enableEPAForAdvertisement) enableEPAForAdvertisement;
@property (TB,N,V_enableObjectLocatorResponseOnAdvertisingInstance) enableObjectLocatorResponseOnAdvertisingInstance;
@property (T@"NSArray",C,N,V_listOfClients) listOfClients;
@property (T@"NSData",C,N,V_mfgData) mfgData;
@property (TB,N,V_stopOnAdvertisingAddressChange) stopOnAdvertisingAddressChange;
@property (T@,C,N,V_advertisingMetric) advertisingMetric;
```

## Instance methods

```
-[CBWPDaemonAdvertisingData setListOfClients:];
-[CBWPDaemonAdvertisingData setEnableEPAForAdvertisement:];
-[CBWPDaemonAdvertisingData enableEPAForAdvertisement];
-[CBWPDaemonAdvertisingData descriptionWithLevel:];
-[CBWPDaemonAdvertisingData setAdvInterval:];
-[CBWPDaemonAdvertisingData setAdvertisingMetric:];
-[CBWPDaemonAdvertisingData setStopOnAdvertisingAddressChange:];
-[CBWPDaemonAdvertisingData setAdvInstanceType:];
-[CBWPDaemonAdvertisingData advInstanceType];
-[CBWPDaemonAdvertisingData setEnableAdvertisingWithPowerAssertion:];
-[CBWPDaemonAdvertisingData setAdvDataPerType:];
-[CBWPDaemonAdvertisingData advInterval];
-[CBWPDaemonAdvertisingData advertisingMetric];
-[CBWPDaemonAdvertisingData description];
-[CBWPDaemonAdvertisingData stopOnAdvertisingAddressChange];
-[CBWPDaemonAdvertisingData advDataPerType];
-[CBWPDaemonAdvertisingData enableAdvertisingWithPowerAssertion];
-[CBWPDaemonAdvertisingData copyWithZone:];
-[CBWPDaemonAdvertisingData setMfgData:];
-[CBWPDaemonAdvertisingData setEnableObjectLocatorResponseOnAdvertisingInstance:];
-[CBWPDaemonAdvertisingData isEqual:];
-[CBWPDaemonAdvertisingData enableObjectLocatorResponseOnAdvertisingInstance];
-[CBWPDaemonAdvertisingData mfgData];
-[CBWPDaemonAdvertisingData listOfClients];
```
