# `CBThreeSegmentAABCurve`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAABCurveProtocol`, `NSCopying`
- 7 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
aabCurve;
capabilities;
minNits;
maxNits;
UUID;
displayID;
curvePrefsKey;
```

## Properties

```
@property (Tf,N) scaleFactor;
@property (TQ,N,R) version;
```

## Instance methods

```
-[CBThreeSegmentAABCurve init];
-[CBThreeSegmentAABCurve setScaleFactor:];
-[CBThreeSegmentAABCurve version];
-[CBThreeSegmentAABCurve scaleFactor];
-[CBThreeSegmentAABCurve copyWithZone:];
-[CBThreeSegmentAABCurve resetToDefaultState];
-[CBThreeSegmentAABCurve copyUserPrefState];
-[CBThreeSegmentAABCurve getNitsForLux:];
-[CBThreeSegmentAABCurve initWithCapabilities:minNits:maxNits:UUID:displayID:curvePrefsKey:];
-[CBThreeSegmentAABCurve setSavedPreferences:];
-[CBThreeSegmentAABCurve transferStateFrom:];
-[CBThreeSegmentAABCurve updateALSParametersForNits:andLux:];
```
