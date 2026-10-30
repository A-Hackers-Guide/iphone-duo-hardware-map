# `LACDTOMutableNotificationCategory`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUNNotificationCategory`
- 3 instance variables, 8 properties, 8 instance methods, 2 class methods

## Instance variables

```
B _hiddenPreviewShowsTitle;
@"NSString" _identifier;
@"NSArray" _actions;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSArray",&,N,V_actions) actions;
@property (TB,N,V_hiddenPreviewShowsTitle) hiddenPreviewShowsTitle;
@property (TB,R,N) hiddenPreviewShowsSubtitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACDTOMutableNotificationCategory newSecurityDelayRequiredCategory];
+[LACDTOMutableNotificationCategory securityDelayEndedCategory];
```

## Instance methods

```
-[LACDTOMutableNotificationCategory identifier];
-[LACDTOMutableNotificationCategory setActions:];
-[LACDTOMutableNotificationCategory actions];
-[LACDTOMutableNotificationCategory setIdentifier:];
-[LACDTOMutableNotificationCategory hiddenPreviewShowsSubtitle];
-[LACDTOMutableNotificationCategory hiddenPreviewShowsTitle];
-[LACDTOMutableNotificationCategory initWithIdentifier:actions:hiddenPreviewShowsTitle:];
-[LACDTOMutableNotificationCategory setHiddenPreviewShowsTitle:];
```
