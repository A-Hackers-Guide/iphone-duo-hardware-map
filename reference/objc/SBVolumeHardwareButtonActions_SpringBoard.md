# `SBVolumeHardwareButtonActions`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _volumeIncreaseIsDown;
B _volumeDecreaseIsDown;
@"NSHashTable" _volumePressBandits;
@? _volumeIncreaseUpEventBlock;
@? _volumeDecreaseUpEventBlock;
```

## Instance methods

```
-[SBVolumeHardwareButtonActions _handleVolumeButtonDownForIncrease:modifiers:];
-[SBVolumeHardwareButtonActions _handleVolumeButtonUpForIncrease:];
-[SBVolumeHardwareButtonActions _handleVolumeDecreaseUp];
-[SBVolumeHardwareButtonActions _handleVolumeIncreaseUp];
-[SBVolumeHardwareButtonActions _launchVolumeSettings];
-[SBVolumeHardwareButtonActions _sendBanditsVolumeDecreased];
-[SBVolumeHardwareButtonActions _sendBanditsVolumeIncreased];
-[SBVolumeHardwareButtonActions _sendVolumeButtonDownToLegacyRegisteredClientsForIncrease:];
-[SBVolumeHardwareButtonActions _sendVolumeButtonDownToOverridingSceneForIncrease:];
-[SBVolumeHardwareButtonActions _sendVolumeButtonDownToSBAppForIncrease:];
-[SBVolumeHardwareButtonActions _sendVolumeButtonDownToSoundControllerForIncrease:];
-[SBVolumeHardwareButtonActions _sendVolumeButtonDownToSpringBoardInternalUIForIncrease:];
-[SBVolumeHardwareButtonActions _sendVolumeButtonToSBAppForIncrease:down:];
-[SBVolumeHardwareButtonActions addVolumePressBandit:];
-[SBVolumeHardwareButtonActions cancelVolumePress];
-[SBVolumeHardwareButtonActions removeVolumePressBandit:];
-[SBVolumeHardwareButtonActions volumeDecreasePressDownWithModifiers:];
-[SBVolumeHardwareButtonActions volumeDecreasePressUp];
-[SBVolumeHardwareButtonActions volumeIncreasePressDownWithModifiers:];
-[SBVolumeHardwareButtonActions volumeIncreasePressUp];
```
