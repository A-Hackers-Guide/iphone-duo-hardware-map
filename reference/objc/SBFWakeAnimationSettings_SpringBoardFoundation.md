# `SBFWakeAnimationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 10 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
d _backlightFadeDuration;
d _speedMultiplierForWake;
d _speedMultiplierForLiftToWake;
d _speedMultiplierForMagicKeyboardExtended;
@"SBFAnimationSettings" _contentWakeSettings;
d _awakeColorBrightness;
d _awakeDateAlpha;
@"SBFAnimationSettings" _awakeWallpaperFilterSettings;
d _sleepColorBrightness;
@"SBFAnimationSettings" _sleepWallpaperFilterSettings;
```

## Properties

```
@property (Td,N,V_backlightFadeDuration) backlightFadeDuration;
@property (Td,N,V_speedMultiplierForWake) speedMultiplierForWake;
@property (Td,N,V_speedMultiplierForLiftToWake) speedMultiplierForLiftToWake;
@property (Td,N,V_speedMultiplierForMagicKeyboardExtended) speedMultiplierForMagicKeyboardExtended;
@property (T@"SBFAnimationSettings",&,N,V_contentWakeSettings) contentWakeSettings;
@property (Td,N,V_awakeColorBrightness) awakeColorBrightness;
@property (Td,N,V_awakeDateAlpha) awakeDateAlpha;
@property (T@"SBFAnimationSettings",&,N,V_awakeWallpaperFilterSettings) awakeWallpaperFilterSettings;
@property (Td,N,V_sleepColorBrightness) sleepColorBrightness;
@property (T@"SBFAnimationSettings",&,N,V_sleepWallpaperFilterSettings) sleepWallpaperFilterSettings;
```

## Class methods

```
+[SBFWakeAnimationSettings settingsControllerModule];
```

## Instance methods

```
-[SBFWakeAnimationSettings speedMultiplierForLiftToWake];
-[SBFWakeAnimationSettings setAwakeDateAlpha:];
-[SBFWakeAnimationSettings setSpeedMultiplierForWake:];
-[SBFWakeAnimationSettings setBacklightFadeDuration:];
-[SBFWakeAnimationSettings awakeColorBrightness];
-[SBFWakeAnimationSettings awakeWallpaperFilterSettings];
-[SBFWakeAnimationSettings setSpeedMultiplierForMagicKeyboardExtended:];
-[SBFWakeAnimationSettings setContentWakeSettings:];
-[SBFWakeAnimationSettings speedMultiplierForWake];
-[SBFWakeAnimationSettings setSleepWallpaperFilterSettings:];
-[SBFWakeAnimationSettings setDefaultValues];
-[SBFWakeAnimationSettings setSpeedMultiplierForLiftToWake:];
-[SBFWakeAnimationSettings awakeDateAlpha];
-[SBFWakeAnimationSettings sleepColorBrightness];
-[SBFWakeAnimationSettings speedMultiplierForMagicKeyboardExtended];
-[SBFWakeAnimationSettings backlightFadeDuration];
-[SBFWakeAnimationSettings setSleepColorBrightness:];
-[SBFWakeAnimationSettings setAwakeColorBrightness:];
-[SBFWakeAnimationSettings contentWakeSettings];
-[SBFWakeAnimationSettings sleepWallpaperFilterSettings];
-[SBFWakeAnimationSettings setAwakeWallpaperFilterSettings:];
```
