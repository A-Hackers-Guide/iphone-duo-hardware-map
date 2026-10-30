# `UIUserNotificationCategory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSDictionary" _actionsByContext;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_actionsByContext) actionsByContext;
@property (T@"NSString",C,N,V_identifier) identifier;
```

## Class methods

```
+[UIUserNotificationCategory supportsSecureCoding];
```

## Instance methods

```
-[UIUserNotificationCategory mutableCopyWithZone:];
-[UIUserNotificationCategory identifier];
-[UIUserNotificationCategory init];
-[UIUserNotificationCategory actions];
-[UIUserNotificationCategory setIdentifier:];
-[UIUserNotificationCategory encodeWithCoder:];
-[UIUserNotificationCategory hash];
-[UIUserNotificationCategory description];
-[UIUserNotificationCategory initWithCoder:];
-[UIUserNotificationCategory copyWithZone:];
-[UIUserNotificationCategory isEqual:];
-[UIUserNotificationCategory _maximumActionsForContext:];
-[UIUserNotificationCategory actionsByContext];
-[UIUserNotificationCategory actionsForContext:];
-[UIUserNotificationCategory initWithIdentifier:actionsByContext:];
-[UIUserNotificationCategory setActionsByContext:];
-[UIUserNotificationCategory validatedCategory];
```
