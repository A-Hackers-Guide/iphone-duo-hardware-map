# `BrightnessUpdate`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 17 properties, 36 instance methods, 0 class methods

## Instance variables

```
Q _ID;
d _timestampOffset;
@"NSNumber" _sdr;
@"NSNumber" _headroom;
@"NSNumber" _limit;
@"NSNumber" _potentialHeadroom;
@"NSNumber" _referenceHeadroom;
@"NSNumber" _adaptationScale;
@"NSNumber" _ambient;
@"NSNumber" _filteredAmbient;
@"NSNumber" _contrastEnhancer;
@"NSNumber" _lowAmbientAdaptation;
@"NSNumber" _highAmbientAdaptation;
@"NSNumber" _indicatorBrightness;
@"NSNumber" _indicatorBrightnessLimit;
@"NSArray" _whitePoint;
@"NSNumber" _contrastPreservation;
```

## Properties

```
@property (TQ,V_ID) ID;
@property (Td,V_timestampOffset) timestampOffset;
@property (T@"NSNumber",&,N,V_sdr) sdr;
@property (T@"NSNumber",&,N,V_headroom) headroom;
@property (T@"NSNumber",&,N,V_limit) limit;
@property (T@"NSNumber",&,N,V_potentialHeadroom) potentialHeadroom;
@property (T@"NSNumber",&,N,V_referenceHeadroom) referenceHeadroom;
@property (T@"NSNumber",&,N,V_adaptationScale) adaptationScale;
@property (T@"NSNumber",&,N,V_ambient) ambient;
@property (T@"NSNumber",&,N,V_filteredAmbient) filteredAmbient;
@property (T@"NSNumber",&,N,V_contrastEnhancer) contrastEnhancer;
@property (T@"NSNumber",&,N,V_lowAmbientAdaptation) lowAmbientAdaptation;
@property (T@"NSNumber",&,N,V_highAmbientAdaptation) highAmbientAdaptation;
@property (T@"NSNumber",&,N,V_indicatorBrightness) indicatorBrightness;
@property (T@"NSNumber",&,N,V_indicatorBrightnessLimit) indicatorBrightnessLimit;
@property (T@"NSArray",&,N,V_whitePoint) whitePoint;
@property (T@"NSNumber",&,N,V_contrastPreservation) contrastPreservation;
```

## Instance methods

```
-[BrightnessUpdate setContrastPreservation:];
-[BrightnessUpdate setPotentialHeadroom:];
-[BrightnessUpdate setIndicatorBrightness:];
-[BrightnessUpdate setIndicatorBrightnessLimit:];
-[BrightnessUpdate headroom];
-[BrightnessUpdate setHeadroom:];
-[BrightnessUpdate setID:];
-[BrightnessUpdate setAmbient:];
-[BrightnessUpdate setContrastEnhancer:];
-[BrightnessUpdate setLowAmbientAdaptation:];
-[BrightnessUpdate setFilteredAmbient:];
-[BrightnessUpdate setHighAmbientAdaptation:];
-[BrightnessUpdate ID];
-[BrightnessUpdate limit];
-[BrightnessUpdate setAdaptationScale:];
-[BrightnessUpdate dealloc];
-[BrightnessUpdate setReferenceHeadroom:];
-[BrightnessUpdate referenceHeadroom];
-[BrightnessUpdate setLimit:];
-[BrightnessUpdate whitePoint];
-[BrightnessUpdate ambient];
-[BrightnessUpdate setWhitePoint:];
-[BrightnessUpdate timestampOffset];
-[BrightnessUpdate adaptationScale];
-[BrightnessUpdate filteredAmbient];
-[BrightnessUpdate sdr];
-[BrightnessUpdate setSdr:];
-[BrightnessUpdate contrastEnhancer];
-[BrightnessUpdate contrastPreservation];
-[BrightnessUpdate highAmbientAdaptation];
-[BrightnessUpdate indicatorBrightness];
-[BrightnessUpdate indicatorBrightnessLimit];
-[BrightnessUpdate initWithUpdateData:];
-[BrightnessUpdate lowAmbientAdaptation];
-[BrightnessUpdate potentialHeadroom];
-[BrightnessUpdate setTimestampOffset:];
```
