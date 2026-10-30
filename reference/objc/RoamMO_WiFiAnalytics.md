# `RoamMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EventMO`
- 0 instance variables, 32 properties, 1 instance methods, 9 class methods

## Properties

```
@property (Ts,D,N) cacheChannel;
@property (Ti,D,N) cacheChannelFlags;
@property (Ts,D,N) cacheRssiBin;
@property (T@"NSObject",&,D,N) channelsScanned;
@property (TB,D,N) displayOn;
@property (Ts,D,N) hostReason;
@property (TB,D,N) isLateRoam;
@property (TB,D,N) isPingPong;
@property (TB,D,N) isSleepRoam;
@property (T@"NSObject",&,D,N) neighborCache;
@property (Ts,D,N) roamDelta;
@property (Tq,D,N) roamLatencyMs;
@property (Ts,D,N) roamProfileType;
@property (Ts,D,N) sourceBand;
@property (Ts,D,N) sourceCcaOther;
@property (Ts,D,N) sourceCcaSelf;
@property (Ts,D,N) sourceCcaTotal;
@property (Ts,D,N) sourceChannel;
@property (Ts,D,N) sourceChannelWidth;
@property (Ti,D,N) sourcePhyMode;
@property (Ts,D,N) sourceRssi;
@property (Ts,D,N) sourceSnr;
@property (Tq,D,N) sourceTimeSpentSecs;
@property (Ts,D,N) targetCca;
@property (TB,D,N) targetDhcpFailed;
@property (Ti,D,N) targetDhcpLatencyMs;
@property (Ti,D,N) targetDhcpLeaseMins;
@property (Ti,D,N) targetPhyMode;
@property (Ts,D,N) targetSnr;
@property (TB,D,N) userInteractive;
@property (TB,D,N) voipActive;
@property (T@"BSSMO",&,D,N) source;
```

## Class methods

```
+[RoamMO fetchRequest];
+[RoamMO successfulRoams];
+[RoamMO roamsIntoBssid:];
+[RoamMO dwellTimeInBand:bandIs24:bssid:maxAgeInDays:moc:];
+[RoamMO roamsOutOf:];
+[RoamMO roamsOutOfBssid:];
+[RoamMO successfulRoamsInOrOutOf:];
+[RoamMO successfulRoamsOutOf:];
+[RoamMO successfulRoamsOutOf:since:];
```

## Instance methods

```
-[RoamMO attributeDescription:];
```
