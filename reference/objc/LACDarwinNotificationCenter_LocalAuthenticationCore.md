# `LACDarwinNotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDarwinNotificationCenter`
- 2 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"LACThreadSafeCollection" _observers;
@"LACThreadSafeCollection" _subscriptions;
```

## Properties

```
@property (Tq,R,N) observerCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDarwinNotificationCenter sharedInstance];
```

## Instance methods

```
-[LACDarwinNotificationCenter removeAllObservers];
-[LACDarwinNotificationCenter _postNotification:];
-[LACDarwinNotificationCenter postNotification:];
-[LACDarwinNotificationCenter removeObserver:];
-[LACDarwinNotificationCenter init];
-[LACDarwinNotificationCenter addObserver:notification:];
-[LACDarwinNotificationCenter addObserver:];
-[LACDarwinNotificationCenter observerCount];
-[LACDarwinNotificationCenter hasObserver:];
-[LACDarwinNotificationCenter _stopObservingAllNotifications];
-[LACDarwinNotificationCenter _addSubscriptionToNotification:];
-[LACDarwinNotificationCenter _hasSubscriptionToNotification:];
-[LACDarwinNotificationCenter stopListeningToAllNotifications];
-[LACDarwinNotificationCenter _notifyObserversAboutNotification:];
-[LACDarwinNotificationCenter _startObservingNotification:];
-[LACDarwinNotificationCenter listenToLaunchNotifications];
```
