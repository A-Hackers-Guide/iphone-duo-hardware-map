# `PLBBTelephonyActivityMsg`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBBMsgRoot`
- 10 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSString" _activeBand;
@"NSString" _dataStatus;
@"NSString" _currentRat;
@"NSString" _preferredRat;
@"NSString" _campedRat;
@"NSString" _callStatus;
@"NSString" _airplaneMode;
@"NSString" _simStatus;
@"NSNumber" _signalStrength;
@"NSNumber" _signalBars;
```

## Properties

```
@property (T@"NSString",&,V_activeBand) activeBand;
@property (T@"NSString",&,V_dataStatus) dataStatus;
@property (T@"NSString",&,V_currentRat) currentRat;
@property (T@"NSString",&,V_preferredRat) preferredRat;
@property (T@"NSString",&,V_campedRat) campedRat;
@property (T@"NSString",&,V_callStatus) callStatus;
@property (T@"NSString",&,V_airplaneMode) airplaneMode;
@property (T@"NSString",&,V_simStatus) simStatus;
@property (T@"NSNumber",&,V_signalStrength) signalStrength;
@property (T@"NSNumber",&,V_signalBars) signalBars;
```

## Class methods

```
+[PLBBTelephonyActivityMsg entryEventPointDefinitionTelephonyActivity];
```

## Instance methods

```
-[PLBBTelephonyActivityMsg signalStrength];
-[PLBBTelephonyActivityMsg signalBars];
-[PLBBTelephonyActivityMsg callStatus];
-[PLBBTelephonyActivityMsg setCallStatus:];
-[PLBBTelephonyActivityMsg sendAndLogPLEntry:withName:withType:];
-[PLBBTelephonyActivityMsg setSignalBars:];
-[PLBBTelephonyActivityMsg setSimStatus:];
-[PLBBTelephonyActivityMsg airplaneMode];
-[PLBBTelephonyActivityMsg dataStatus];
-[PLBBTelephonyActivityMsg simStatus];
-[PLBBTelephonyActivityMsg setAirplaneMode:];
-[PLBBTelephonyActivityMsg setSignalStrength:];
-[PLBBTelephonyActivityMsg setDataStatus:];
-[PLBBTelephonyActivityMsg currentRat];
-[PLBBTelephonyActivityMsg setCurrentRat:];
-[PLBBTelephonyActivityMsg activeBand];
-[PLBBTelephonyActivityMsg campedRat];
-[PLBBTelephonyActivityMsg logPointIntervalTelephonyActivity];
-[PLBBTelephonyActivityMsg logPointIntervalTelephonyActivityAirplaneModeChange];
-[PLBBTelephonyActivityMsg preferredRat];
-[PLBBTelephonyActivityMsg refreshTelephonyActivity];
-[PLBBTelephonyActivityMsg setActiveBand:];
-[PLBBTelephonyActivityMsg setCampedRat:];
-[PLBBTelephonyActivityMsg setPreferredRat:];
```
