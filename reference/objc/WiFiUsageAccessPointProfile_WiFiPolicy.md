# `WiFiUsageAccessPointProfile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 34 class methods

## Instance variables

```
B _hasColocatedMLOs;
@"NSString" _bssid;
@"NSString" _apProfile;
```

## Properties

```
@property (T@"NSString",&,N,V_bssid) bssid;
@property (T@"NSString",&,N,V_apProfile) apProfile;
@property (TB,N,V_hasColocatedMLOs) hasColocatedMLOs;
```

## Class methods

```
+[WiFiUsageAccessPointProfile initialize];
+[WiFiUsageAccessPointProfile _defaults];
+[WiFiUsageAccessPointProfile updateConfig];
+[WiFiUsageAccessPointProfile _cachedProfile:];
+[WiFiUsageAccessPointProfile apNameForBSSID:];
+[WiFiUsageAccessPointProfile _config];
+[WiFiUsageAccessPointProfile setMaxProfiles:];
+[WiFiUsageAccessPointProfile shortProfileForBSSID:withError:];
+[WiFiUsageAccessPointProfile _applyMask:FromStart:WithLen:WithMask:AppendTo:];
+[WiFiUsageAccessPointProfile _cleanUpStaleProfiles];
+[WiFiUsageAccessPointProfile _compareBytes:FromStart:WithLen:With:];
+[WiFiUsageAccessPointProfile _endPrevAssoc];
+[WiFiUsageAccessPointProfile _extractFieldsFor:From:Into:];
+[WiFiUsageAccessPointProfile _getBinTimeInterval:As:];
+[WiFiUsageAccessPointProfile _getDefaults];
+[WiFiUsageAccessPointProfile _isProfileValidForStorage:];
+[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:onlyIfCurrent:withError:];
+[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:withError:];
+[WiFiUsageAccessPointProfile _loadFromUserDefaults:withKey:withCachedData:];
+[WiFiUsageAccessPointProfile _loadFromUserDefaults:withKey:withCachedData:withError:];
+[WiFiUsageAccessPointProfile _saveToUserDefaults:withKey:andValue:];
+[WiFiUsageAccessPointProfile _submitProfileFor:withCachedDict:AndEraseWithLog:];
+[WiFiUsageAccessPointProfile _toMobileAssetsProfile:];
+[WiFiUsageAccessPointProfile beaconsAndWPSInfo];
+[WiFiUsageAccessPointProfile errorStringForTelemetry:];
+[WiFiUsageAccessPointProfile longProfileForBSSID:withError:];
+[WiFiUsageAccessPointProfile prefixForCA];
+[WiFiUsageAccessPointProfile profileForBSSID:];
+[WiFiUsageAccessPointProfile profileForBSSID:onlyIfCurrent:withError:];
+[WiFiUsageAccessPointProfile profileForBSSID:withError:];
+[WiFiUsageAccessPointProfile profileFromBeaconData:andParsedIE:];
+[WiFiUsageAccessPointProfile submitToCAForBSSID:];
+[WiFiUsageAccessPointProfile updateWithAssocTime:forBssid:];
+[WiFiUsageAccessPointProfile updateWithWPS:];
```

## Instance methods

```
-[WiFiUsageAccessPointProfile setApProfile:];
-[WiFiUsageAccessPointProfile apProfile];
-[WiFiUsageAccessPointProfile setBssid:];
-[WiFiUsageAccessPointProfile hasColocatedMLOs];
-[WiFiUsageAccessPointProfile bssid];
-[WiFiUsageAccessPointProfile setHasColocatedMLOs:];
```
