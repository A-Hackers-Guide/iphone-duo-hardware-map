# `LACDTOMutableNotificationAction`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUNNotificationAction`
- 4 instance variables, 8 properties, 9 instance methods, 2 class methods

## Instance variables

```
B _isDestructive;
B _isTitleLocalized;
@"NSString" _identifier;
@"NSString" _title;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSString",&,N,V_title) title;
@property (TB,N,V_isDestructive) isDestructive;
@property (TB,N,V_isTitleLocalized) isTitleLocalized;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOMutableNotificationAction doNotStartNewDelayAction];
+[LACDTOMutableNotificationAction startNewDelayAction];
```

## Instance methods

```
-[LACDTOMutableNotificationAction identifier];
-[LACDTOMutableNotificationAction setIdentifier:];
-[LACDTOMutableNotificationAction title];
-[LACDTOMutableNotificationAction isDestructive];
-[LACDTOMutableNotificationAction setTitle:];
-[LACDTOMutableNotificationAction setIsDestructive:];
-[LACDTOMutableNotificationAction initWithIdentifier:title:isTitleLocalized:isDestructive:];
-[LACDTOMutableNotificationAction isTitleLocalized];
-[LACDTOMutableNotificationAction setIsTitleLocalized:];
```
