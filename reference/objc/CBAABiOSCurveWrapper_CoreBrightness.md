# `CBAABiOSCurveWrapper`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAABCurveProtocol`
- 2 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
f _scaleFactor;
^{AAB=^^?[3{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}]{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{?=B{?=ff}{?=ff}{?=ff}f}{CurveCap=[4f][4f]d}{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}B[3{CustomCurve=[20f][20f]i}][3{CustomCurve=[20f][20f]i}]{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}ffffffffffffff{mutex={_opaque_pthread_mutex_t=q[56c]}}^{UpdateCurveStrategy}} _aab;
```

## Properties

```
@property (T^{AAB=^^?[3{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}]{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{Curve=ffffffff{CurvePrefs=[3f][3f]ffI[3I]Bfdif}}{?=B{?=ff}{?=ff}{?=ff}f}{CurveCap=[4f][4f]d}{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}B[3{CustomCurve=[20f][20f]i}][3{CustomCurve=[20f][20f]i}]{CustomCurve=[20f][20f]i}{CustomCurve=[20f][20f]i}ffffffffffffff{mutex={_opaque_pthread_mutex_t=q[56c]}}^{UpdateCurveStrategy}},R,V_aab) aab;
@property (Tf,N) scaleFactor;
@property (TQ,R,N) version;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBAABiOSCurveWrapper setScaleFactor:];
-[CBAABiOSCurveWrapper dealloc];
-[CBAABiOSCurveWrapper version];
-[CBAABiOSCurveWrapper scaleFactor];
-[CBAABiOSCurveWrapper description];
-[CBAABiOSCurveWrapper copyWithZone:];
-[CBAABiOSCurveWrapper resetToDefaultState];
-[CBAABiOSCurveWrapper aab];
-[CBAABiOSCurveWrapper copyUserPrefState];
-[CBAABiOSCurveWrapper getNitsForLux:];
-[CBAABiOSCurveWrapper initWithAAB:];
-[CBAABiOSCurveWrapper resetToGoodCurve];
-[CBAABiOSCurveWrapper setSavedPreferences:];
-[CBAABiOSCurveWrapper transferStateFrom:];
-[CBAABiOSCurveWrapper updateALSParametersForNits:andLux:];
```
