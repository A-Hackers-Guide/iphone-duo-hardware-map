# `PLBBTelephonyRegMsg`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 11 instance variables, 11 properties, 39 instance methods, 1 class methods

## Instance variables

```
C _changed;
@"NSNumber" _cellID;
@"NSNumber" _lac;
@"NSNumber" _dataAttached;
@"NSNumber" _dataActive;
@"NSString" _dataIndicator;
@"NSNumber" _homeNetwork;
@"NSString" _registrationStatus;
@"NSString" _operatorName;
@"NSDate" _timeUpdate;
@"NSDictionary" _telRegInfo;
```

## Properties

```
@property (TC,V_changed) changed;
@property (T@"NSNumber",&,V_cellID) cellID;
@property (T@"NSNumber",&,V_lac) lac;
@property (T@"NSNumber",&,V_dataAttached) dataAttached;
@property (T@"NSNumber",&,V_dataActive) dataActive;
@property (T@"NSString",&,V_dataIndicator) dataIndicator;
@property (T@"NSNumber",&,V_homeNetwork) homeNetwork;
@property (T@"NSString",&,V_registrationStatus) registrationStatus;
@property (T@"NSString",&,V_operatorName) operatorName;
@property (T@"NSDate",&,V_timeUpdate) timeUpdate;
@property (T@"NSDictionary",&,V_telRegInfo) telRegInfo;
```

## Class methods

```
+[PLBBTelephonyRegMsg bbEuLogMsgNameTelephonyReg];
```

## Instance methods

```
-[PLBBTelephonyRegMsg lac];
-[PLBBTelephonyRegMsg setAttrLac:];
-[PLBBTelephonyRegMsg setAttrHomeNetwork:];
-[PLBBTelephonyRegMsg setLac:];
-[PLBBTelephonyRegMsg setOperatorName:];
-[PLBBTelephonyRegMsg setTelRegInfo:];
-[PLBBTelephonyRegMsg setHomeNetwork:];
-[PLBBTelephonyRegMsg setAttrRegistrationStatus:];
-[PLBBTelephonyRegMsg init];
-[PLBBTelephonyRegMsg timeUpdate];
-[PLBBTelephonyRegMsg setAttrDataIndicator:];
-[PLBBTelephonyRegMsg processTelReg];
-[PLBBTelephonyRegMsg logEventPointTelephonyRegistrationAtInit];
-[PLBBTelephonyRegMsg operatorName];
-[PLBBTelephonyRegMsg setAttrDataAttached:];
-[PLBBTelephonyRegMsg refreshTelephonyReg];
-[PLBBTelephonyRegMsg setAttrDataActive:];
-[PLBBTelephonyRegMsg cellID];
-[PLBBTelephonyRegMsg setDataIndicator:];
-[PLBBTelephonyRegMsg setDataActive:];
-[PLBBTelephonyRegMsg setRegistrationStatus:];
-[PLBBTelephonyRegMsg setCellID:];
-[PLBBTelephonyRegMsg sendAndLogPLEntry:withName:withType:];
-[PLBBTelephonyRegMsg setTimeUpdate:];
-[PLBBTelephonyRegMsg logEventPointTelephonyRegistration];
-[PLBBTelephonyRegMsg dataAttached];
-[PLBBTelephonyRegMsg registrationStatus];
-[PLBBTelephonyRegMsg dataIndicator];
-[PLBBTelephonyRegMsg changed];
-[PLBBTelephonyRegMsg setDataAttached:];
-[PLBBTelephonyRegMsg telRegInfo];
-[PLBBTelephonyRegMsg setAttrCellID:];
-[PLBBTelephonyRegMsg dataActive];
-[PLBBTelephonyRegMsg homeNetwork];
-[PLBBTelephonyRegMsg humanReadableDataIndicator:];
-[PLBBTelephonyRegMsg setAttrOperatorName:];
-[PLBBTelephonyRegMsg fillPLEntryAndSend:];
-[PLBBTelephonyRegMsg humanReadableRegistrationStatus:];
-[PLBBTelephonyRegMsg setChanged:];
```
