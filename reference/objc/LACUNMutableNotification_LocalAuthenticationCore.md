# `LACUNMutableNotification`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACUNNotification`
- 14 instance variables, 18 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _shouldDisplayActionsInline;
B _isTitleLocalized;
B _isSubtitleLocalized;
B _isBodyLocalized;
B _isTimeSensitive;
@"NSString" _identifier;
@"NSString" _categoryIdentifier;
@"NSString" _title;
@"NSString" _subtitle;
@"NSString" _body;
@"NSString" _systemIconName;
@"NSURL" _defaultActionURL;
d _withdrawInterval;
d _triggerInterval;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSString",&,N,V_categoryIdentifier) categoryIdentifier;
@property (TB,N,V_shouldDisplayActionsInline) shouldDisplayActionsInline;
@property (T@"NSString",&,N,V_title) title;
@property (TB,N,V_isTitleLocalized) isTitleLocalized;
@property (T@"NSString",&,N,V_subtitle) subtitle;
@property (TB,N,V_isSubtitleLocalized) isSubtitleLocalized;
@property (T@"NSString",&,N,V_body) body;
@property (TB,N,V_isBodyLocalized) isBodyLocalized;
@property (T@"NSString",&,N,V_systemIconName) systemIconName;
@property (T@"NSURL",&,N,V_defaultActionURL) defaultActionURL;
@property (TB,N,V_isTimeSensitive) isTimeSensitive;
@property (Td,N,V_withdrawInterval) withdrawInterval;
@property (Td,N,V_triggerInterval) triggerInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUNMutableNotification setShouldDisplayActionsInline:];
-[LACUNMutableNotification body];
-[LACUNMutableNotification setDefaultActionURL:];
-[LACUNMutableNotification setBody:];
-[LACUNMutableNotification subtitle];
-[LACUNMutableNotification identifier];
-[LACUNMutableNotification setTriggerInterval:];
-[LACUNMutableNotification setCategoryIdentifier:];
-[LACUNMutableNotification setSubtitle:];
-[LACUNMutableNotification setIdentifier:];
-[LACUNMutableNotification triggerInterval];
-[LACUNMutableNotification title];
-[LACUNMutableNotification isTimeSensitive];
-[LACUNMutableNotification description];
-[LACUNMutableNotification setTitle:];
-[LACUNMutableNotification defaultActionURL];
-[LACUNMutableNotification isEqual:];
-[LACUNMutableNotification shouldDisplayActionsInline];
-[LACUNMutableNotification categoryIdentifier];
-[LACUNMutableNotification setIsTimeSensitive:];
-[LACUNMutableNotification systemIconName];
-[LACUNMutableNotification isBodyLocalized];
-[LACUNMutableNotification isSubtitleLocalized];
-[LACUNMutableNotification isTitleLocalized];
-[LACUNMutableNotification setIsBodyLocalized:];
-[LACUNMutableNotification setIsSubtitleLocalized:];
-[LACUNMutableNotification setIsTitleLocalized:];
-[LACUNMutableNotification setSystemIconName:];
-[LACUNMutableNotification setWithdrawInterval:];
-[LACUNMutableNotification withdrawInterval];
```
