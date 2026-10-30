# `_TtC14CoreBrightness20ThreeSegmentAABCurve`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAABCurveProtocol`
- 6 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
_$sSf scaleFactor;
CoreBrightness.ThreeSegmentAABCurveConfig config;
CoreBrightness.ThreeSegmentAABCurvePreferences prefs;
os.Logger log;
_$sSi displayID;
_$sSS curveName;
```

## Properties

```
@property (Tf,N,VscaleFactor) scaleFactor;
@property (TQ,N,R) version;
```

## Instance methods

```
-[_TtC14CoreBrightness20ThreeSegmentAABCurve init];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve setScaleFactor:];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve version];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve scaleFactor];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve copyWithZone:];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve resetToDefaultState];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve copyUserPrefState];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve getNitsForLux:];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve setSavedPreferences:];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve transferStateFrom:];
-[_TtC14CoreBrightness20ThreeSegmentAABCurve updateALSParametersForNits:andLux:];
```
