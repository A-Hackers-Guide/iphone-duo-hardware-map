# `UIUserNotificationActionSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _category;
@"NSDictionary" _actionsByContext;
```

## Properties

```
@property (T@"NSString",C,N,V_category) category;
@property (T@"NSDictionary",C,N,V_actionsByContext) actionsByContext;
```

## Class methods

```
+[UIUserNotificationActionSettings supportsSecureCoding];
```

## Instance methods

```
-[UIUserNotificationActionSettings setCategory:];
-[UIUserNotificationActionSettings mutableCopyWithZone:];
-[UIUserNotificationActionSettings category];
-[UIUserNotificationActionSettings actions];
-[UIUserNotificationActionSettings encodeWithCoder:];
-[UIUserNotificationActionSettings hash];
-[UIUserNotificationActionSettings description];
-[UIUserNotificationActionSettings initWithCoder:];
-[UIUserNotificationActionSettings copyWithZone:];
-[UIUserNotificationActionSettings isEqual:];
-[UIUserNotificationActionSettings _maximumActionsForContext:];
-[UIUserNotificationActionSettings actionsByContext];
-[UIUserNotificationActionSettings actionsForContext:];
-[UIUserNotificationActionSettings initWithCategory:actionsByContext:];
-[UIUserNotificationActionSettings setActionsByContext:];
-[UIUserNotificationActionSettings validatedSettings];
```
