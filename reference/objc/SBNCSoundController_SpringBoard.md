# `SBNCSoundController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneAttachmentObserving`
- 7 instance variables, 11 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@"NSHashTable" _windowScenes;
@"AVSpeechSynthesizer" _speechSynthesizer;
@"NSMutableDictionary" _playingSounds;
@"NSMutableSet" _requestsRequiringExplicitKill;
@"NSMutableDictionary" _playingNotifications;
```

## Properties

```
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"SBWindowSceneManager",&,N,V_windowSceneManager) windowSceneManager;
@property (T@"NSHashTable",&,N,V_windowScenes) windowScenes;
@property (T@"AVSpeechSynthesizer",&,N,V_speechSynthesizer) speechSynthesizer;
@property (T@"NSMutableDictionary",&,N,V_playingSounds) playingSounds;
@property (T@"NSMutableSet",&,N,V_requestsRequiringExplicitKill) requestsRequiringExplicitKill;
@property (T@"NSMutableDictionary",&,N,V_playingNotifications) playingNotifications;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNCSoundController _lockStateChanged:];
-[SBNCSoundController _mediaServicesWereReset:];
-[SBNCSoundController playSoundForNotificationRequest:presentingDestination:];
-[SBNCSoundController requestsRequiringExplicitKill];
-[SBNCSoundController canPlaySoundForNotificationRequest:];
-[SBNCSoundController init];
-[SBNCSoundController windowSceneDidDisconnect:];
-[SBNCSoundController playingNotifications];
-[SBNCSoundController playSoundAndReadOutForNotificationRequest:presentingDestination:];
-[SBNCSoundController setPlayingSounds:];
-[SBNCSoundController _preventVibrations];
-[SBNCSoundController setWindowScenes:];
-[SBNCSoundController windowSceneManager];
-[SBNCSoundController _ambientPresentationController];
-[SBNCSoundController playingSounds];
-[SBNCSoundController windowScenes];
-[SBNCSoundController setPlayingNotifications:];
-[SBNCSoundController setSpeechSynthesizer:];
-[SBNCSoundController _isDeviceUILocked];
-[SBNCSoundController setWindowSceneManager:];
-[SBNCSoundController _playSoundForNotificationRequest:presentingDestination:completion:];
-[SBNCSoundController _hardwareButtonPressed:];
-[SBNCSoundController _killSounds];
-[SBNCSoundController windowSceneDidConnect:];
-[SBNCSoundController setRequestsRequiringExplicitKill:];
-[SBNCSoundController stopSoundForNotificationRequest:];
-[SBNCSoundController lockScreenCoordinator];
-[SBNCSoundController setLockScreenCoordinator:];
-[SBNCSoundController _playSoundIfPossibleForNotificationRequest:presentingDestination:completion:];
-[SBNCSoundController playSoundIfPossibleForNotificationRequest:presentingDestination:];
-[SBNCSoundController initWithLockScreenCoordinator:windowSceneManager:];
-[SBNCSoundController speechSynthesizer];
```
