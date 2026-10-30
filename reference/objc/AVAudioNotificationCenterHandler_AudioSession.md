# `AVAudioNotificationCenterHandler`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioNotificationCenterServerDelegate`
- 3 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@? _propertyNotificationHandler;
@? _interruptionHandler;
{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _mutex;
```

## Properties

```
@property (T@?,C,N) propertyNotificationHandler;
@property (T@?,C,N) interruptionHandler;
```

## Instance methods

```
-[AVAudioNotificationCenterHandler interruptionHandler];
-[AVAudioNotificationCenterHandler setInterruptionHandler:];
-[AVAudioNotificationCenterHandler setPropertyNotificationHandler:];
-[AVAudioNotificationCenterHandler handleInterruptionNotifications:];
-[AVAudioNotificationCenterHandler handlePropertyNotifications:];
-[AVAudioNotificationCenterHandler propertyNotificationHandler];
```
