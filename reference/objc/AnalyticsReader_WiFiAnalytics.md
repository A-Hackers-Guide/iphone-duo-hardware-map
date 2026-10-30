# `AnalyticsReader`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"WAPersistentContainer" _persistentContainer;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
```

## Class methods

```
+[AnalyticsReader networksFromResults:];
```

## Instance methods

```
-[AnalyticsReader moc];
-[AnalyticsReader insideOutsideClassifierForSSID:];
-[AnalyticsReader copyAllStoredNetworkSsids];
-[AnalyticsReader copyAllBSSEssentialInfoForNetwork:];
-[AnalyticsReader lanForBssid:withError:];
-[AnalyticsReader copyLocationsForNetwork:];
-[AnalyticsReader eventSequencesFor:since:until:sortingAsc:limit:withError:];
-[AnalyticsReader setPersistentContainer:];
-[AnalyticsReader deploymentCongestionForSSID:withError:];
-[AnalyticsReader deploymentCoverageForSSID:withError:];
-[AnalyticsReader countNetworksHavingBand:inLan:withError:];
-[AnalyticsReader adaptiveRoamingParamsForBSS:];
-[AnalyticsReader copyGeoTagsForNetwork:location:];
-[AnalyticsReader isBandRelevantForSSID:onBand:];
-[AnalyticsReader bssidCountByBandInLAN:withError:];
-[AnalyticsReader usageForNetwork:withError:];
-[AnalyticsReader persistentContainer];
-[AnalyticsReader usageOf:timeSpan:around:withError:];
-[AnalyticsReader bandsInNetwork:withError:];
-[AnalyticsReader lansForSsid:withError:];
-[AnalyticsReader apProfileForBssid:];
-[AnalyticsReader usageForLAN:withError:];
-[AnalyticsReader networksInSameLanAsBssid:withError:];
-[AnalyticsReader parsedBeaconInfoIsStored:ssid:];
-[AnalyticsReader networkSsidsByTraits:withError:];
-[AnalyticsReader networksInLan:withError:];
-[AnalyticsReader usageOf:during:timeSpan:withError:];
-[AnalyticsReader knownChannelsBitmapForSSID:withError:];
-[AnalyticsReader countNetworksInSameLanAsBssid:withError:];
-[AnalyticsReader knownChannelsBitmapForBSSID:withError:];
-[AnalyticsReader networksAvailableAtLocation:withinDistance:inBand:];
-[AnalyticsReader networkCountForLAN:withError:];
-[AnalyticsReader initWithPersistentContainer:];
-[AnalyticsReader bssForBSSID:withError:];
-[AnalyticsReader bssidCountByBandInUniqueMO:withError:];
-[AnalyticsReader edgeParametersForBSS:];
-[AnalyticsReader isNetworkWithinRangeOfLocation:range:location:count:];
-[AnalyticsReader lanFor:withError:];
-[AnalyticsReader networkForSSID:withError:];
-[AnalyticsReader networksInSameLansAsSsid:withError:];
-[AnalyticsReader networksWithPredicate:withError:];
```
