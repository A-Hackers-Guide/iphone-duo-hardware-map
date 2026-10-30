# `BSSMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UniqueMO`
- Protocols: `UniqueMoProtocol`
- 0 instance variables, 42 properties, 0 instance methods, 16 class methods

## Properties

```
@property (T@"NSUUID",C,D,N) apid;
@property (Ts,D,N) apPhysicalScopeId;
@property (T@"NSString",C,D,N) apProfileID;
@property (Ts,D,N) autoLeaveRssi;
@property (Ts,D,N) autoLeaveRssiTelemetry;
@property (TB,D,N) beaconMetricSubmitted;
@property (T@"NSString",C,D,N) bssid;
@property (Ts,D,N) disBcnLossCount;
@property (Ts,D,N) disTrgDisCount;
@property (Ts,D,N) disUsrForcedInWeakRssiCount;
@property (T@"NSUUID",C,D,N) idUsedInMetric;
@property (TB,D,N) isEdgeForJoin;
@property (Tq,D,N) knownChannelsBitmap2And5;
@property (Tq,D,N) knownChannelsBitmap6;
@property (TB,D,N) isEdgeForLeave;
@property (TB,D,N) isEdgeForLeaveTelemetry;
@property (TB,D,N) isTCPGood;
@property (T@"NSDate",C,D,N) lastSeen;
@property (TB,D,N) manualJoinAfterAutoLeave;
@property (Ts,D,N) mostRecentBand;
@property (Ts,D,N) mostRecentChannel;
@property (T@"NSObject",&,D,N) neighborBSSIDs;
@property (T@"NSObject",&,D,N) neighborChannels;
@property (T@"NSObject",&,D,N) opaque;
@property (T@"NSObject",&,D,N) parsedBeacon;
@property (Ti,D,N) phyMode;
@property (Ts,D,N) roamTriggerRssi;
@property (Ts,D,N) tdEdgeParamsVersion;
@property (T@"NSSet",&,D,N) events;
@property (T@"NSSet",&,D,N) geoTags;
@property (T@"LANMO",&,D,N) lan;
@property (T@"NetworkMO",&,D,N) network;
@property (T@"NSSet",&,D,N) roamsFrom;
@property (T@"NSSet",&,D,N) scanResult;
@property (T@"NSSet",&,D,N) scansFrom;
@property (T@"NSSet",&,D,N) usageStatsMonthly;
@property (T@"NSSet",&,D,N) usageStatsWeekly;
@property (T@"NSOrderedSet",R,D,N) faults;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BSSMO fetchRequest];
+[BSSMO defaultPropertiesToFetch];
+[BSSMO copyDeploymentUuidsForSsid:moc:];
+[BSSMO numBssInBand:bandIs24:moc:];
+[BSSMO accumulator];
+[BSSMO constraintsWithBSSID:];
+[BSSMO copyBssidsForDeployment:deploymentUuid:moc:];
+[BSSMO coalesceBssidsIntoDeployment:moc:];
+[BSSMO allBssidsForSsid:moc:];
+[BSSMO getDeploymentUuidForBssids:moc:];
+[BSSMO allSsidsForBssid:moc:];
+[BSSMO formattedMACAddressNotation:as:];
+[BSSMO verifyConstraints:withError:];
+[BSSMO setBssManagedObjectPropertyValueForKey:forKey:withValue:];
+[BSSMO propertyForAging];
+[BSSMO bssManagedObjectPropertyValue:forKey:];
```
