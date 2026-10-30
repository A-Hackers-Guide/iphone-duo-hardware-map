# `LACUNNotification` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) categoryIdentifier;
@property (TB,R,N) shouldDisplayActionsInline;
@property (T@"NSString",R,N) title;
@property (TB,R,N) isTitleLocalized;
@property (T@"NSString",R,N) subtitle;
@property (TB,R,N) isSubtitleLocalized;
@property (T@"NSString",R,N) body;
@property (TB,R,N) isBodyLocalized;
@property (T@"NSString",R,N) systemIconName;
@property (T@"NSURL",R,N) defaultActionURL;
@property (TB,R,N) isTimeSensitive;
@property (Td,R,N) withdrawInterval;
@property (Td,R,N) triggerInterval;
```

## Instance methods

```
-[LACUNNotification body];
-[LACUNNotification subtitle];
-[LACUNNotification identifier];
-[LACUNNotification triggerInterval];
-[LACUNNotification title];
-[LACUNNotification isTimeSensitive];
-[LACUNNotification defaultActionURL];
-[LACUNNotification shouldDisplayActionsInline];
-[LACUNNotification categoryIdentifier];
-[LACUNNotification systemIconName];
-[LACUNNotification isBodyLocalized];
-[LACUNNotification isSubtitleLocalized];
-[LACUNNotification isTitleLocalized];
-[LACUNNotification withdrawInterval];
```
