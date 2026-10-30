# `SBSoundController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TLAlertPlaybackObserver`
- 8 instance variables, 4 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _soundsBySystemSoundIDs;
@"NSMutableSet" _usedNotificationTypes;
@"UINotificationFeedbackGenerator" _hapticFeedbackGenerator;
@"NSMapTable" _toneAlertsBySounds;
@"NSMapTable" _soundsByToneAlerts;
@"NSHashTable" _observers;
Q _pendingCallbacks;
@"NSMutableArray" _pendedCallbacks;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSoundController sharedInstance];
```

## Instance methods

```
-[SBSoundController _ringerStateChanged:];
-[SBSoundController _soundDidFinishPlaying:];
-[SBSoundController isPlayingAnySound];
-[SBSoundController removeObserver:];
-[SBSoundController init];
-[SBSoundController _soundDidStartPlaying:];
-[SBSoundController _enqueueCallback:];
-[SBSoundController _configureWithFeedbackType:];
-[SBSoundController playSoundWithDefaultEnvironment:];
-[SBSoundController _alert:didBeginPlayingWithEvent:];
-[SBSoundController _cleanupSystemSound:andKill:];
-[SBSoundController handleVolumeButtonDownEvent];
-[SBSoundController isPlaying:];
-[SBSoundController addObserver:];
-[SBSoundController _playSystemSound:];
-[SBSoundController _playFeedback:];
-[SBSoundController _playToneAlert:];
-[SBSoundController _activateFeedback:forReason:];
-[SBSoundController alert:didBeginPlayingWithEvent:];
-[SBSoundController _cleanupToneAlertForSound:andKill:];
-[SBSoundController _endPendingCallbacksBlock];
-[SBSoundController activateSound:forReason:];
-[SBSoundController stopSound:];
-[SBSoundController playSound:environments:completion:];
-[SBSoundController stopAllSounds];
-[SBSoundController _beginPendingCallbacksBlock];
```
