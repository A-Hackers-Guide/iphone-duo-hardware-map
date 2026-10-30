# `SBVolumeControlState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _isAudioPlayingSomewhere;
B _isCallOrFaceTimeActive;
B _currentRouteHasVolumeControl;
B _isFullyMuted;
B _isRingerMuted;
B _isLocked;
B _isHostingAppOnLockScreen;
B _isShowingLockScreenMediaControls;
@"NSString" _activeVolumeCategoryName;
```

## Properties

```
@property (T@"NSString",C,N,V_activeVolumeCategoryName) activeVolumeCategoryName;
@property (TB,N,SsetAudioPlayingSomewhere:,V_isAudioPlayingSomewhere) isAudioPlayingSomewhere;
@property (TB,N,SsetCallOrFaceTimeActive:,V_isCallOrFaceTimeActive) isCallOrFaceTimeActive;
@property (TB,N,SsetCurrentRouteHasVolumeControl:,V_currentRouteHasVolumeControl) currentRouteHasVolumeControl;
@property (TB,N,SsetFullyMuted:,V_isFullyMuted) isFullyMuted;
@property (TB,N,SsetRingerMuted:,V_isRingerMuted) isRingerMuted;
@property (TB,N,SsetLocked:,V_isLocked) isLocked;
@property (TB,N,SsetHostingAppOnLockScreen:,V_isHostingAppOnLockScreen) isHostingAppOnLockScreen;
@property (TB,N,SsetShowingLockScreenMediaControls:,V_isShowingLockScreenMediaControls) isShowingLockScreenMediaControls;
```

## Instance methods

```
-[SBVolumeControlState isLocked];
-[SBVolumeControlState setLocked:];
-[SBVolumeControlState isFullyMuted];
-[SBVolumeControlState isRingerMuted];
-[SBVolumeControlState description];
-[SBVolumeControlState copyWithZone:];
-[SBVolumeControlState currentRouteHasVolumeControl];
-[SBVolumeControlState setCurrentRouteHasVolumeControl:];
-[SBVolumeControlState setRingerMuted:];
-[SBVolumeControlState activeVolumeCategoryName];
-[SBVolumeControlState isAudioPlayingSomewhere];
-[SBVolumeControlState isCallOrFaceTimeActive];
-[SBVolumeControlState isHostingAppOnLockScreen];
-[SBVolumeControlState isShowingLockScreenMediaControls];
-[SBVolumeControlState setActiveVolumeCategoryName:];
-[SBVolumeControlState setAudioPlayingSomewhere:];
-[SBVolumeControlState setCallOrFaceTimeActive:];
-[SBVolumeControlState setFullyMuted:];
-[SBVolumeControlState setHostingAppOnLockScreen:];
-[SBVolumeControlState setShowingLockScreenMediaControls:];
```
