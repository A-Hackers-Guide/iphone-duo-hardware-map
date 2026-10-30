# `KeyboardBacklightHIDCurve`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `KeyboardBacklight`
- 5 instance variables, 9 properties, 42 instance methods, 0 class methods

## Instance variables

```
i _color;
f _curveVersion;
f _chicletCurveCoefficient;
f _chicletCurvePower;
f _luxHysteresis;
```

## Properties

```
@property (T@"NSDictionary",R) brightnessCurve;
@property (Tf,R) maxCurveNits;
@property (Tf,R,V_chicletCurveCoefficient) chicletCurveCoefficient;
@property (Tf,R,V_chicletCurvePower) chicletCurvePower;
@property (Tf,V_luxHysteresis) luxHysteresis;
@property (Tf,R) level;
@property (Tf,R) maxLevelPercentage;
@property (Tf,R) maxCapableNits;
@property (Tf,R) minCapableNits;
```

## Instance methods

```
-[KeyboardBacklightHIDCurve copyPropertyForKey:];
-[KeyboardBacklightHIDCurve setProperty:forKey:];
-[KeyboardBacklightHIDCurve setColor:];
-[KeyboardBacklightHIDCurve initWithQueue:];
-[KeyboardBacklightHIDCurve setBacklightLevel:];
-[KeyboardBacklightHIDCurve setBrightness:];
-[KeyboardBacklightHIDCurve dealloc];
-[KeyboardBacklightHIDCurve brightness];
-[KeyboardBacklightHIDCurve level];
-[KeyboardBacklightHIDCurve color];
-[KeyboardBacklightHIDCurve description];
-[KeyboardBacklightHIDCurve KBBrightnessLuxHysteresisPropertyHandler:];
-[KeyboardBacklightHIDCurve brightnessCurve];
-[KeyboardBacklightHIDCurve getKeyboardBacklightPreferences];
-[KeyboardBacklightHIDCurve KBBrightnessCurvePropertyHandler:];
-[KeyboardBacklightHIDCurve calculateLevelPercentageAtAmbient:];
-[KeyboardBacklightHIDCurve chicletCurveCoefficient];
-[KeyboardBacklightHIDCurve chicletCurvePower];
-[KeyboardBacklightHIDCurve convertNitsToLevelPercentage:];
-[KeyboardBacklightHIDCurve convertPWMPercentageToNits:];
-[KeyboardBacklightHIDCurve currentLuxToAmbient];
-[KeyboardBacklightHIDCurve currentLuxToNits];
-[KeyboardBacklightHIDCurve defaultBrightnessCurve];
-[KeyboardBacklightHIDCurve handleLuxUpdate:];
-[KeyboardBacklightHIDCurve initWithQueue:device:];
-[KeyboardBacklightHIDCurve isBrightnessCurveValid:];
-[KeyboardBacklightHIDCurve luxHysteresis];
-[KeyboardBacklightHIDCurve maxCapableNits];
-[KeyboardBacklightHIDCurve maxCurveNits];
-[KeyboardBacklightHIDCurve maxLevelPercentage];
-[KeyboardBacklightHIDCurve maxUserLevel];
-[KeyboardBacklightHIDCurve minCapableNits];
-[KeyboardBacklightHIDCurve perceptualBrightnessForLevel:];
-[KeyboardBacklightHIDCurve reconfigureSettingsForColor:];
-[KeyboardBacklightHIDCurve setBrightness:withFadeSpeed:commit:];
-[KeyboardBacklightHIDCurve setLuxHysteresis:];
-[KeyboardBacklightHIDCurve storeKeyboardBacklightCurveToPreferences];
-[KeyboardBacklightHIDCurve storeKeyboardBacklightPreferences];
-[KeyboardBacklightHIDCurve updateBrightnessCurve:];
-[KeyboardBacklightHIDCurve updateDefaultBrightnessCurve:];
-[KeyboardBacklightHIDCurve updateDefaultCurveForColor:];
-[KeyboardBacklightHIDCurve updateLuxToNitsCurve];
```
