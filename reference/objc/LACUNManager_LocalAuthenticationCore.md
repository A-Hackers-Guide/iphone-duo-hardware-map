# `LACUNManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UNUserNotificationCenterDelegate`, `LACUNManager`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UNUserNotificationCenter" _notificationCenter;
@"<LACUNManagerDelegate>" delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACUNManagerDelegate>",W,N,Vdelegate) delegate;
```

## Instance methods

```
-[LACUNManager userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:];
-[LACUNManager setDelegate:];
-[LACUNManager delegate];
-[LACUNManager initWithBundleIdentifier:];
-[LACUNManager _makeNotificationRequestWithConfiguration:];
-[LACUNManager cancelAllNotificationsWithCompletion:];
-[LACUNManager cancelNotificationsWithIdentifiers:scheduledOnly:completion:];
-[LACUNManager initWithBundleIdentifier:categories:];
-[LACUNManager postNotification:completion:];
```
