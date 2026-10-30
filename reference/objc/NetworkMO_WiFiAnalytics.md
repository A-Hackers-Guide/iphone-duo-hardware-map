# `NetworkMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UniqueMO`
- Protocols: `UniqueMoProtocol`, `DeploymentProtocol`
- 0 instance variables, 43 properties, 2 instance methods, 19 class methods

## Properties

```
@property (Ts,D,N) authFlags;
@property (Ti,R,D,N) bssCount;
@property (T@"NSUUID",C,D,N) colocatedScopeId;
@property (Tq,D,N) colocatedState;
@property (Ts,D,N) congestionDetermination;
@property (Ts,D,N) coverageDetermination;
@property (TB,D,N) didDeploymentChange;
@property (TB,D,N) has2GHz;
@property (TB,D,N) has5GHz;
@property (TB,D,N) has6GHz;
@property (Ts,D,N) insideOutsideClassifierBestBand;
@property (Tf,D,N) insideOutsideClassifierFPR;
@property (Ts,D,N) insideOutsideClassifierInsideCount;
@property (Ts,D,N) insideOutsideClassifierOutsideCount;
@property (Ts,D,N) insideOutsideClassifierRssiThreshold;
@property (Tf,D,N) insideOutsideClassifierTPR;
@property (TB,D,N) is2GHzResidencyLow;
@property (TB,D,N) is5GHzResidencyLow;
@property (TB,D,N) is6GHzResidencyLow;
@property (TB,D,N) isHome;
@property (Tq,D,N) knownChannelsBitmap2And5;
@property (Tq,D,N) knownChannelsBitmap6;
@property (TB,D,N) isLongTermNetwork;
@property (TB,D,N) isMoving;
@property (TB,D,N) isOmnipresent;
@property (TB,D,N) isPublic;
@property (TB,D,N) isWork;
@property (Ts,D,N) latestCompleteWeekUsageCumulativePercentage;
@property (Tq,D,N) latestCompleteWeekUsageCumulativeSeconds;
@property (Ts,D,N) latestCompleteWeekUsagePercentage;
@property (Tq,D,N) latestCompleteWeekUsageSeconds;
@property (Tq,D,N) networkScore;
@property (T@"NSObject",&,D,N) opaque;
@property (T@"NSString",C,D,N) ssid;
@property (Tq,D,N) switchedAwayFromCount;
@property (Tq,D,N) switchedToCount;
@property (Ti,D,N) t_lansCount;
@property (T@"NSSet",&,D,N) bss;
@property (T@"NSSet",&,D,N) events;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NetworkMO predicateForNetworkHavingBand:];
+[NetworkMO fetchRequest];
+[NetworkMO predicateForNetworkInLAN:];
+[NetworkMO defaultPropertiesToFetch];
+[NetworkMO predicateForNetworkContainingBSSID:];
+[NetworkMO copyAllSsidsWithColocatedScopeId:moc:];
+[NetworkMO invalidateColocatedScopeForSsidArray:moc:];
+[NetworkMO setNetworkManagedObjectPropertyValueForKey:forKey:withValue:];
+[NetworkMO accumulator];
+[NetworkMO networkManagedObjectPropertyValue:forKey:];
+[NetworkMO allStoredSsids:];
+[NetworkMO coalesceSsidsIntoColocatedScope:moc:];
+[NetworkMO getFirstColocatedScopeUuidForSsids:moc:];
+[NetworkMO copyAllSsids:];
+[NetworkMO copyAllSsidsWithColocatedScopeIdStr:moc:];
+[NetworkMO propertiesForTraits:];
+[NetworkMO verifyConstraints:withError:];
+[NetworkMO removeNetwork:moc:];
+[NetworkMO predicateForNetworkWithTrait:];
```

## Instance methods

```
-[NetworkMO isEnterprise];
-[NetworkMO classifyTraitsWithDistanceFilter:container:];
```
