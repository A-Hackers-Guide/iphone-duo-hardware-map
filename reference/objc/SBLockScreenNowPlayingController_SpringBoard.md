# `SBLockScreenNowPlayingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`
- 7 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"SBMediaController" _mediaController;
@"PCPersistentTimer" _disableTimer;
@"CSLockScreenSettings" _testSettings;
@"PTToggleTestRecipe" _testRecipe;
B _enabled;
q _currentState;
@"<SBLockScreenNowPlayingControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLockScreenNowPlayingControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Tq,R,N,V_currentState) currentState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenNowPlayingController _addObservers];
-[SBLockScreenNowPlayingController dealloc];
-[SBLockScreenNowPlayingController settings:changedValueForKey:];
-[SBLockScreenNowPlayingController isEnabled];
-[SBLockScreenNowPlayingController setDelegate:];
-[SBLockScreenNowPlayingController _timeoutInterval];
-[SBLockScreenNowPlayingController setEnabled:];
-[SBLockScreenNowPlayingController delegate];
-[SBLockScreenNowPlayingController _removeObservers];
-[SBLockScreenNowPlayingController currentState];
-[SBLockScreenNowPlayingController initWithMediaController:];
-[SBLockScreenNowPlayingController _updateToState:];
-[SBLockScreenNowPlayingController _disableTimerFired];
-[SBLockScreenNowPlayingController _invalidateDisableTimer];
-[SBLockScreenNowPlayingController _isMediaRecentlyActive];
-[SBLockScreenNowPlayingController _startDisableTimer];
-[SBLockScreenNowPlayingController _updateNowPlayingPlugin];
-[SBLockScreenNowPlayingController isNowPlayingActive];
```
