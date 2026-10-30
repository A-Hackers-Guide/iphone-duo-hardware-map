# `WiFiCoreTelephonyManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _hasFetchedDataSubscriptionContext;
@"CoreTelephonyClient" _telephonyClient;
@"NSObject<OS_dispatch_queue>" _telephonyQueue;
@"CTXPCServiceSubscriptionContext" _cachedDataSubscriptionContext;
^{__CTServerConnection=} _ctServerConnection;
```

## Properties

```
@property (T@"CoreTelephonyClient",&,N,V_telephonyClient) telephonyClient;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_telephonyQueue) telephonyQueue;
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_cachedDataSubscriptionContext) cachedDataSubscriptionContext;
@property (TB,N,V_hasFetchedDataSubscriptionContext) hasFetchedDataSubscriptionContext;
@property (T^{__CTServerConnection=},N,V_ctServerConnection) ctServerConnection;
```

## Class methods

```
+[WiFiCoreTelephonyManager sharedManager];
```

## Instance methods

```
-[WiFiCoreTelephonyManager init];
-[WiFiCoreTelephonyManager activeDataSubscriptionContext];
-[WiFiCoreTelephonyManager dealloc];
-[WiFiCoreTelephonyManager ctServerConnection];
-[WiFiCoreTelephonyManager setTelephonyClient:];
-[WiFiCoreTelephonyManager telephonyClient];
-[WiFiCoreTelephonyManager dataUsageForLastPeriods:completion:];
-[WiFiCoreTelephonyManager setTelephonyQueue:];
-[WiFiCoreTelephonyManager telephonyQueue];
-[WiFiCoreTelephonyManager setCtServerConnection:];
-[WiFiCoreTelephonyManager cachedDataSubscriptionContext];
-[WiFiCoreTelephonyManager copyStartDateOfCellularDataUsageRecordsWithCompletion:];
-[WiFiCoreTelephonyManager getIntelligentConnectivityFeatureAvailable:enabled:error:];
-[WiFiCoreTelephonyManager hasActiveCellularPlan];
-[WiFiCoreTelephonyManager hasFetchedDataSubscriptionContext];
-[WiFiCoreTelephonyManager resetIntelligentConnectivityStatistics:];
-[WiFiCoreTelephonyManager setCachedDataSubscriptionContext:];
-[WiFiCoreTelephonyManager setHasFetchedDataSubscriptionContext:];
-[WiFiCoreTelephonyManager setIntelligentConnectivity:error:];
-[WiFiCoreTelephonyManager shouldShowIntelligentConnectivity];
-[WiFiCoreTelephonyManager shouldShowNoActivePlanState];
```
