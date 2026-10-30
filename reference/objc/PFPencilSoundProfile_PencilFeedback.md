# `PFPencilSoundProfile`

- Image: [`/System/Library/PrivateFrameworks/PencilFeedback.framework/PencilFeedback`](../userland/System__Library__PrivateFrameworks__PencilFeedback.framework__PencilFeedback.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 33 instance methods, 1 class methods

## Instance variables

```
f _minThickness;
f _maxThickness;
f _thicknessFrequencyRange;
f _originalDirectionValue;
d _velocityFrequencyAddAmount;
d _baseBPFrequency;
d _baseBPBandwidth;
d _baseHPFrequency;
d _baseLPFrequency;
d _directionFrequencyDeviation;
d _forceFrequencyDeviation;
d _fixedGain;
d _velocityRatio;
{CGPoint="x"d"y"d} _controlPoint1;
{CGPoint="x"d"y"d} _controlPoint2;
{CGPoint="x"d"y"d} _controlPoint3;
```

## Properties

```
@property (Td,N,V_velocityFrequencyAddAmount) velocityFrequencyAddAmount;
@property (Td,N,V_baseBPFrequency) baseBPFrequency;
@property (Td,N,V_baseBPBandwidth) baseBPBandwidth;
@property (Td,N,V_baseHPFrequency) baseHPFrequency;
@property (Td,N,V_baseLPFrequency) baseLPFrequency;
@property (Td,N,V_directionFrequencyDeviation) directionFrequencyDeviation;
@property (Td,N,V_forceFrequencyDeviation) forceFrequencyDeviation;
@property (Td,N,V_fixedGain) fixedGain;
@property (Td,N,V_velocityRatio) velocityRatio;
@property (Tf,N,V_minThickness) minThickness;
@property (Tf,N,V_maxThickness) maxThickness;
@property (Tf,N,V_thicknessFrequencyRange) thicknessFrequencyRange;
@property (Tf,N,V_originalDirectionValue) originalDirectionValue;
@property (T{CGPoint=dd},N,V_controlPoint1) controlPoint1;
@property (T{CGPoint=dd},N,V_controlPoint2) controlPoint2;
@property (T{CGPoint=dd},N,V_controlPoint3) controlPoint3;
```

## Class methods

```
+[PFPencilSoundProfile profileWithVelocityFrequencyAddAmount:baseBPFrequency:baseBPBandwidth:baseHPFrequency:baseLPFrequency:directionFrequencyDeviation:forceFrequencyDeviation:fixedGain:velocityRatio:minThickness:maxThickness:thicknessFrequencyRange:originalDirectionValue:controlPoint1:controlPoint2:controlPoint3:];
```

## Instance methods

```
-[PFPencilSoundProfile controlPoint2];
-[PFPencilSoundProfile init];
-[PFPencilSoundProfile controlPoint1];
-[PFPencilSoundProfile maxThickness];
-[PFPencilSoundProfile minThickness];
-[PFPencilSoundProfile setMaxThickness:];
-[PFPencilSoundProfile setMinThickness:];
-[PFPencilSoundProfile setControlPoint1:];
-[PFPencilSoundProfile setControlPoint2:];
-[PFPencilSoundProfile baseBPBandwidth];
-[PFPencilSoundProfile baseHPFrequency];
-[PFPencilSoundProfile baseBPFrequency];
-[PFPencilSoundProfile baseLPFrequency];
-[PFPencilSoundProfile setDirectionFrequencyDeviation:];
-[PFPencilSoundProfile controlPoint3];
-[PFPencilSoundProfile directionFrequencyDeviation];
-[PFPencilSoundProfile fixedGain];
-[PFPencilSoundProfile forceFrequencyDeviation];
-[PFPencilSoundProfile originalDirectionValue];
-[PFPencilSoundProfile setBaseBPBandwidth:];
-[PFPencilSoundProfile setBaseBPFrequency:];
-[PFPencilSoundProfile setBaseHPFrequency:];
-[PFPencilSoundProfile setBaseLPFrequency:];
-[PFPencilSoundProfile setControlPoint3:];
-[PFPencilSoundProfile setFixedGain:];
-[PFPencilSoundProfile setForceFrequencyDeviation:];
-[PFPencilSoundProfile setOriginalDirectionValue:];
-[PFPencilSoundProfile setThicknessFrequencyRange:];
-[PFPencilSoundProfile setVelocityFrequencyAddAmount:];
-[PFPencilSoundProfile setVelocityRatio:];
-[PFPencilSoundProfile thicknessFrequencyRange];
-[PFPencilSoundProfile velocityFrequencyAddAmount];
-[PFPencilSoundProfile velocityRatio];
```
