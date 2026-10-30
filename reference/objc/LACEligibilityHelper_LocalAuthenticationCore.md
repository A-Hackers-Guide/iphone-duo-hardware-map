# `LACEligibilityHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenterObserver`, `LACEligibilityHelping`
- 3 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
cache;
registeredNotificationsForDomains;
@"LACDarwinNotificationCenter" darwinNotificationCenter;
```

## Properties

```
@property (T@"LACDarwinNotificationCenter",N,R,VdarwinNotificationCenter) darwinNotificationCenter;
```

## Class methods

```
+[LACEligibilityHelper sharedInstance];
```

## Instance methods

```
-[LACEligibilityHelper init];
-[LACEligibilityHelper dealloc];
-[LACEligibilityHelper darwinNotificationCenter];
-[LACEligibilityHelper isEligibleForDomain:];
-[LACEligibilityHelper notificationCenter:didReceiveNotification:];
```
