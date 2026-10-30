# `CBPresetsParser`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _displayList;
@"NSMutableDictionary" _displayPresets;
@"NSObject<OS_os_log>" _logHandle;
```

## Class methods

```
+[CBPresetsParser sharedInstance];
```

## Instance methods

```
-[CBPresetsParser init];
-[CBPresetsParser dealloc];
-[CBPresetsParser setDisplayList:];
-[CBPresetsParser alwaysRequestMaxHeadroom:];
-[CBPresetsParser autoBrightnessDisabledForDisplay:];
-[CBPresetsParser brightnessDisabledForDisplay:];
-[CBPresetsParser luminanceThrottleLimitForDisplay:];
-[CBPresetsParser luminanceThrottlePolicyForDisplay:];
-[CBPresetsParser maxAutobrightnessSDRLuminanceForDisplay:];
-[CBPresetsParser maxPotentialEDRHeadroomForDisplay:];
-[CBPresetsParser maxSDRLuminanceForDisplay:];
-[CBPresetsParser nightShiftDisabled];
-[CBPresetsParser referenceMode:];
-[CBPresetsParser refreshPresetState];
-[CBPresetsParser trueToneDisabled];
```
