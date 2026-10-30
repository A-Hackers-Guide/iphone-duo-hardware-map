# `_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBABCurvePreferencesProtocol`
- 15 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
CoreBrightness.ABCurvePoint darkSegmentStart;
CoreBrightness.ABCurvePoint darkSegmentEnd;
CoreBrightness.ABCurvePoint midSegmentStart;
CoreBrightness.ABCurvePoint midSegmentEnd;
_$sSf brightSlope;
CoreBrightness.PreferenceRegionMap preferences;
CoreBrightness.PendingOverride ? pendingOverride;
Swift.Bool justOverriddenBrightValue;
_$sSd updateTimestamp;
_$sSa -> CoreBrightness.CurveUpdate curveUpdates;
CoreBrightness.ThreeSegmentDefaultSegmentsConfig defaultSegmentsConfig;
_$sSS curvePrefsKey;
_$sSS UUID;
_$sSi displayID;
os.Logger log;
```

## Instance methods

```
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences init];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences copyWithZone:];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences copyUserPreferences];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences isPrefsDictComplete:];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences loadPreferencesForUUID:andCurvePrefsKey:];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences resetPrefs];
-[_TtC14CoreBrightness31ThreeSegmentAABCurvePreferences setPreferencesFromDictionary:];
```
