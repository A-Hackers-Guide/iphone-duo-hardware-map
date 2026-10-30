# `_UIKBFeedbackGenerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIKBFeedbackGenerating`
- 25 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSUserDefaults" _soundsDefaults;
i _ringerStateNotifyToken;
B _isActive;
@"NSDate" _engineStartDate;
d _engineActiveDuration;
Q _engineStartCount;
Q _actionCount;
@"AVSystemController" _avSystemController;
f _volume;
B _isFeedbackDisabled;
B _isAudioOnly;
B _usesCoreHapticsForAudioOnly;
@"CHHapticEngine" _engine;
@"NSDictionary" _players;
@"NSDictionary" _systemSounds;
d _lastActionTime;
d _lastVolume;
d _lastHapticIntensity;
d _lastPitch;
d _lastPan;
d _lastBrightness;
q _textLength;
B __isEngineRunning;
q __mode;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKBFeedbackGenerator actionOccurred:textLength:atLocation:];
-[_UIKBFeedbackGenerator deactivate];
-[_UIKBFeedbackGenerator observeValueForKeyPath:ofObject:change:context:];
-[_UIKBFeedbackGenerator activateWithCompletionBlock:];
-[_UIKBFeedbackGenerator init];
-[_UIKBFeedbackGenerator dealloc];
-[_UIKBFeedbackGenerator _stopEngineDueToIdle];
-[_UIKBFeedbackGenerator _effectiveVolumeDidChangeNotification:];
-[_UIKBFeedbackGenerator _keyboardPreferencesDidUpdateNotification:];
-[_UIKBFeedbackGenerator _serverConnectionDiedNotification:];
-[_UIKBFeedbackGenerator _stopEngineForApplicationNotification:];
-[_UIKBFeedbackGenerator isActive];
-[_UIKBFeedbackGenerator actionOccurred:];
-[_UIKBFeedbackGenerator actionOccurred:atLocation:];
-[_UIKBFeedbackGenerator _dictationDidEndNotification:];
-[_UIKBFeedbackGenerator _dictationDidBeginNotification:];
```
