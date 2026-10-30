# `SBPressPrecedenceArbiter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAVSystemControllerCacheObserver`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _volumeAndLockButtonPriority;
q _homeButtonType;
B _isAudioPlayingSomewhere;
@"NSArray" _hardwareButtons;
```

## Properties

```
@property (T@"NSArray",&,N,V_hardwareButtons) hardwareButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPressPrecedenceArbiter cache:didUpdateAudioSessionPlaying:];
-[SBPressPrecedenceArbiter hardwareButtons];
-[SBPressPrecedenceArbiter _applyButtonPriority:];
-[SBPressPrecedenceArbiter _currentButtonPriority];
-[SBPressPrecedenceArbiter _shouldArbitrateLockAndVolumeHardwareButtonPriorities];
-[SBPressPrecedenceArbiter _updateButtonPrioritiesForNotification:];
-[SBPressPrecedenceArbiter _updateButtonPriority];
-[SBPressPrecedenceArbiter initWithHomeButtonType:];
-[SBPressPrecedenceArbiter setHardwareButtons:];
```
