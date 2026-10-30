# `AVAudioNotificationFilter`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _wantsInterruptions;
@"NSSet" _propertyNotificationsOfInterest;
```

## Properties

```
@property (T@"NSSet",R,N,V_propertyNotificationsOfInterest) propertyNotificationsOfInterest;
@property (TB,R,N,V_wantsInterruptions) wantsInterruptions;
```

## Class methods

```
+[AVAudioNotificationFilter supportsSecureCoding];
```

## Instance methods

```
-[AVAudioNotificationFilter encodeWithCoder:];
-[AVAudioNotificationFilter initWithCoder:];
-[AVAudioNotificationFilter copyWithZone:];
-[AVAudioNotificationFilter isEqual:];
-[AVAudioNotificationFilter initWithPropertyNotificationsOfInterest:wantsInterruptions:];
-[AVAudioNotificationFilter propertyNotificationsOfInterest];
-[AVAudioNotificationFilter filterPropertyNotifications:];
-[AVAudioNotificationFilter wantsInterruptions];
```
