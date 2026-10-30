# `LACAuthenticationUINotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAuthenticationUINotifying`
- 1 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{__CFString=} _lastNotification;
```

## Properties

```
@property (T^{__CFString=},N,V_lastNotification) lastNotification;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACAuthenticationUINotificationCenter postNotification:];
-[LACAuthenticationUINotificationCenter _checkIsRedundantNotification:];
-[LACAuthenticationUINotificationCenter _postDarwinNotificationWithIdentifier:];
-[LACAuthenticationUINotificationCenter lastNotification];
-[LACAuthenticationUINotificationCenter postNotificationUIDidAppear];
-[LACAuthenticationUINotificationCenter postNotificationUIDidDisappear];
-[LACAuthenticationUINotificationCenter setLastNotification:];
```
