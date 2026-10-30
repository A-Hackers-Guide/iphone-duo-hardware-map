# `AVAudioRemoteNotificationPayload`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _notification;
@"NSArray" _subscribedDelegates;
@"NSDictionary" _delegatePayload;
```

## Properties

```
@property (T@"NSString",C,N,V_notification) notification;
@property (T@"NSArray",C,N,V_subscribedDelegates) subscribedDelegates;
@property (T@"NSDictionary",C,N,V_delegatePayload) delegatePayload;
```

## Class methods

```
+[AVAudioRemoteNotificationPayload supportsSecureCoding];
```

## Instance methods

```
-[AVAudioRemoteNotificationPayload notification];
-[AVAudioRemoteNotificationPayload setNotification:];
-[AVAudioRemoteNotificationPayload encodeWithCoder:];
-[AVAudioRemoteNotificationPayload initWithCoder:];
-[AVAudioRemoteNotificationPayload delegatePayload];
-[AVAudioRemoteNotificationPayload subscribedDelegates];
-[AVAudioRemoteNotificationPayload initWithNotification:forSubscribers:withPayload:];
-[AVAudioRemoteNotificationPayload setDelegatePayload:];
-[AVAudioRemoteNotificationPayload setSubscribedDelegates:];
```
