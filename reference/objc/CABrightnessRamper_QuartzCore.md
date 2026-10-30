# `CABrightnessRamper`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAWindowServerRamper`
- 18 instance variables, 18 properties, 38 instance methods, 0 class methods

## Instance variables

```
d _sdrNitsBegin;
d _sdrNitsEnd;
d _headroomBegin;
d _headroomEnd;
d _limitBegin;
d _limitEnd;
d _contrastEnhancerBegin;
d _contrastEnhancerEnd;
d _lowAmbientStrengthBegin;
d _lowAmbientStrengthEnd;
d _highAmbientStrengthBegin;
d _highAmbientStrengthEnd;
d _contrastPreservationBegin;
d _contrastPreservationEnd;
d _indicatorNitsBegin;
d _indicatorNitsEnd;
d _indicatorLimitBegin;
d _indicatorLimitEnd;
```

## Properties

```
@property (Td,V_sdrNitsBegin) sdrNitsBegin;
@property (Td,V_sdrNitsEnd) sdrNitsEnd;
@property (Td,V_headroomBegin) headroomBegin;
@property (Td,V_headroomEnd) headroomEnd;
@property (Td,V_limitBegin) limitBegin;
@property (Td,V_limitEnd) limitEnd;
@property (Td,V_contrastEnhancerBegin) contrastEnhancerBegin;
@property (Td,V_contrastEnhancerEnd) contrastEnhancerEnd;
@property (Td,V_lowAmbientStrengthBegin) lowAmbientStrengthBegin;
@property (Td,V_lowAmbientStrengthEnd) lowAmbientStrengthEnd;
@property (Td,V_highAmbientStrengthBegin) highAmbientStrengthBegin;
@property (Td,V_highAmbientStrengthEnd) highAmbientStrengthEnd;
@property (Td,V_contrastPreservationBegin) contrastPreservationBegin;
@property (Td,V_contrastPreservationEnd) contrastPreservationEnd;
@property (Td,V_indicatorNitsBegin) indicatorNitsBegin;
@property (Td,V_indicatorNitsEnd) indicatorNitsEnd;
@property (Td,V_indicatorLimitBegin) indicatorLimitBegin;
@property (Td,V_indicatorLimitEnd) indicatorLimitEnd;
```

## Instance methods

```
-[CABrightnessRamper initWithDisplay:];
-[CABrightnessRamper rampCallback:];
-[CABrightnessRamper setHeadroomEnd:];
-[CABrightnessRamper contrastEnhancerBegin];
-[CABrightnessRamper contrastEnhancerEnd];
-[CABrightnessRamper contrastPreservationBegin];
-[CABrightnessRamper contrastPreservationEnd];
-[CABrightnessRamper headroomBegin];
-[CABrightnessRamper headroomEnd];
-[CABrightnessRamper highAmbientStrengthBegin];
-[CABrightnessRamper highAmbientStrengthEnd];
-[CABrightnessRamper indicatorLimitBegin];
-[CABrightnessRamper indicatorLimitEnd];
-[CABrightnessRamper indicatorNitsBegin];
-[CABrightnessRamper indicatorNitsEnd];
-[CABrightnessRamper limitBegin];
-[CABrightnessRamper limitEnd];
-[CABrightnessRamper lowAmbientStrengthBegin];
-[CABrightnessRamper lowAmbientStrengthEnd];
-[CABrightnessRamper sdrNitsBegin];
-[CABrightnessRamper sdrNitsEnd];
-[CABrightnessRamper setContrastEnhancerBegin:];
-[CABrightnessRamper setContrastEnhancerEnd:];
-[CABrightnessRamper setContrastPreservationBegin:];
-[CABrightnessRamper setContrastPreservationEnd:];
-[CABrightnessRamper setHeadroomBegin:];
-[CABrightnessRamper setHighAmbientStrengthBegin:];
-[CABrightnessRamper setHighAmbientStrengthEnd:];
-[CABrightnessRamper setIndicatorLimitBegin:];
-[CABrightnessRamper setIndicatorLimitEnd:];
-[CABrightnessRamper setIndicatorNitsBegin:];
-[CABrightnessRamper setIndicatorNitsEnd:];
-[CABrightnessRamper setLimitBegin:];
-[CABrightnessRamper setLimitEnd:];
-[CABrightnessRamper setLowAmbientStrengthBegin:];
-[CABrightnessRamper setLowAmbientStrengthEnd:];
-[CABrightnessRamper setSdrNitsBegin:];
-[CABrightnessRamper setSdrNitsEnd:];
```
