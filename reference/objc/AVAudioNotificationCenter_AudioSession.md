# `AVAudioNotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _mutex;
@"<AVAudioNotificationCenterServer>" _server;
@"NSMutableSet" _propertiesOfInterest;
B _wantsInterruptions;
@"AVAudioNotificationCenterHandler" _handler;
Q _delegateID;
i _type;
```

## Instance methods

```
-[AVAudioNotificationCenter init];
-[AVAudioNotificationCenter dealloc];
-[AVAudioNotificationCenter invalidate];
-[AVAudioNotificationCenter setPropertyNotificationHandler:];
-[AVAudioNotificationCenter delegateID];
-[AVAudioNotificationCenter initWithServer:type:];
-[AVAudioNotificationCenter locked_calculateFilter];
-[AVAudioNotificationCenter privateSetInterruptionNotificationHandler:];
-[AVAudioNotificationCenter privateSetPropertyNotificationHandler:];
-[AVAudioNotificationCenter privateStartObservingNotifications:];
-[AVAudioNotificationCenter privateStopObservingNotifications:];
-[AVAudioNotificationCenter setInterruptionNotificationHandler:];
-[AVAudioNotificationCenter startObservingNotifications:];
-[AVAudioNotificationCenter stopObservingNotifications:];
-[AVAudioNotificationCenter unlocked_updateServerWithFilter:];
```
