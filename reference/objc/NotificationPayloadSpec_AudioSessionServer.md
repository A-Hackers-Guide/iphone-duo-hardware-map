# `NotificationPayloadSpec`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _removeDuplicates;
@"NSDictionary" _payload;
@"NSDictionary" _avasPayload;
@"NSString" _avasNotificationName;
```

## Properties

```
@property (TB,R,N,V_removeDuplicates) removeDuplicates;
@property (T@"NSDictionary",R,N,V_payload) payload;
@property (T@"NSDictionary",&,N,V_avasPayload) avasPayload;
@property (T@"NSString",&,N,V_avasNotificationName) avasNotificationName;
```

## Instance methods

```
-[NotificationPayloadSpec payload];
-[NotificationPayloadSpec setAvasPayload:];
-[NotificationPayloadSpec avasNotificationName];
-[NotificationPayloadSpec avasPayload];
-[NotificationPayloadSpec initWithRemoveDuplicates:payload:];
-[NotificationPayloadSpec removeDuplicates];
-[NotificationPayloadSpec setAvasNotificationName:];
```
