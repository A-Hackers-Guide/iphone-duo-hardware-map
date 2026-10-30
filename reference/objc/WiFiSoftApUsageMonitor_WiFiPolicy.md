# `WiFiSoftApUsageMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 39 instance methods, 1 class methods

## Instance variables

```
B _compatibilityEnabled;
B _compatibilityToggled;
B _statsValid;
@"NSDate" _softApOldestActiveTime;
Q _softApUpCount;
Q _noClientConnectedSessionCount;
Q _onlyAppleClientConnectedSessionCount;
Q _onlyOtherClientConnectedSessionCount;
Q _mixClientConnectedSessionCount;
Q _appleClientConnectCount;
Q _otherClientConnectCount;
Q _twoFourGHzSessionCount;
Q _fiveGHzSessionCount;
@"NSObject<OS_dispatch_queue>" _internalQueue;
```

## Properties

```
@property (T@"NSDate",&,N,V_softApOldestActiveTime) softApOldestActiveTime;
@property (TQ,N,V_softApUpCount) softApUpCount;
@property (TQ,N,V_noClientConnectedSessionCount) noClientConnectedSessionCount;
@property (TQ,N,V_onlyAppleClientConnectedSessionCount) onlyAppleClientConnectedSessionCount;
@property (TQ,N,V_onlyOtherClientConnectedSessionCount) onlyOtherClientConnectedSessionCount;
@property (TQ,N,V_mixClientConnectedSessionCount) mixClientConnectedSessionCount;
@property (TQ,N,V_appleClientConnectCount) appleClientConnectCount;
@property (TQ,N,V_otherClientConnectCount) otherClientConnectCount;
@property (TQ,N,V_twoFourGHzSessionCount) twoFourGHzSessionCount;
@property (TQ,N,V_fiveGHzSessionCount) fiveGHzSessionCount;
@property (TB,N,V_compatibilityEnabled) compatibilityEnabled;
@property (TB,N,V_compatibilityToggled) compatibilityToggled;
@property (TB,N,V_statsValid) statsValid;
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
```

## Class methods

```
+[WiFiSoftApUsageMonitor sharedInstance];
```

## Instance methods

```
-[WiFiSoftApUsageMonitor init];
-[WiFiSoftApUsageMonitor setOtherClientConnectCount:];
-[WiFiSoftApUsageMonitor appleClientConnectCount];
-[WiFiSoftApUsageMonitor description];
-[WiFiSoftApUsageMonitor compatibilityEnabled];
-[WiFiSoftApUsageMonitor setAppleClientConnectCount:];
-[WiFiSoftApUsageMonitor setCompatibilityEnabled:];
-[WiFiSoftApUsageMonitor setInternalQueue:];
-[WiFiSoftApUsageMonitor otherClientConnectCount];
-[WiFiSoftApUsageMonitor internalQueue];
-[WiFiSoftApUsageMonitor resetStats];
-[WiFiSoftApUsageMonitor statsDictionary];
-[WiFiSoftApUsageMonitor compatibilityToggled];
-[WiFiSoftApUsageMonitor fiveGHzSessionCount];
-[WiFiSoftApUsageMonitor initStats];
-[WiFiSoftApUsageMonitor initStats:];
-[WiFiSoftApUsageMonitor mixClientConnectedSessionCount];
-[WiFiSoftApUsageMonitor noClientConnectedSessionCount];
-[WiFiSoftApUsageMonitor onlyAppleClientConnectedSessionCount];
-[WiFiSoftApUsageMonitor onlyOtherClientConnectedSessionCount];
-[WiFiSoftApUsageMonitor persistStats];
-[WiFiSoftApUsageMonitor resetStatsInternal];
-[WiFiSoftApUsageMonitor setCompatibilityToggled:];
-[WiFiSoftApUsageMonitor setFiveGHzSessionCount:];
-[WiFiSoftApUsageMonitor setMixClientConnectedSessionCount:];
-[WiFiSoftApUsageMonitor setNoClientConnectedSessionCount:];
-[WiFiSoftApUsageMonitor setOnlyAppleClientConnectedSessionCount:];
-[WiFiSoftApUsageMonitor setOnlyOtherClientConnectedSessionCount:];
-[WiFiSoftApUsageMonitor setSoftApOldestActiveTime:];
-[WiFiSoftApUsageMonitor setSoftApUpCount:];
-[WiFiSoftApUsageMonitor setStatsValid:];
-[WiFiSoftApUsageMonitor setTwoFourGHzSessionCount:];
-[WiFiSoftApUsageMonitor softApOldestActiveTime];
-[WiFiSoftApUsageMonitor softApUpCount];
-[WiFiSoftApUsageMonitor statsDictionaryInternal:];
-[WiFiSoftApUsageMonitor statsValid];
-[WiFiSoftApUsageMonitor twoFourGHzSessionCount];
-[WiFiSoftApUsageMonitor updateStats:];
-[WiFiSoftApUsageMonitor updateStatsInternal:];
```
