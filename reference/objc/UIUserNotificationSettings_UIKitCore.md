# `UIUserNotificationSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 14 instance methods, 4 class methods

## Instance variables

```
Q _types;
@"NSSet" _categories;
```

## Properties

```
@property (TQ,R,N,V_types) types;
@property (T@"NSSet",R,C,N,V_categories) categories;
```

## Class methods

```
+[UIUserNotificationSettings supportsSecureCoding];
+[UIUserNotificationSettings settingsForRegisteredSettings:requestedSettings:];
+[UIUserNotificationSettings settingsForTypes:categories:];
+[UIUserNotificationSettings settingsForUserNotificationTypes:userNotificationActionSettings:];
```

## Instance methods

```
-[UIUserNotificationSettings types];
-[UIUserNotificationSettings encodeWithCoder:];
-[UIUserNotificationSettings hash];
-[UIUserNotificationSettings description];
-[UIUserNotificationSettings initWithCoder:];
-[UIUserNotificationSettings copyWithZone:];
-[UIUserNotificationSettings isEqual:];
-[UIUserNotificationSettings categories];
-[UIUserNotificationSettings allowedUserNotificationTypes];
-[UIUserNotificationSettings initWithTypes:categories:];
-[UIUserNotificationSettings initWithUserNotificationTypes:userNotificationActionSettings:];
-[UIUserNotificationSettings mayPresentUserNotificationOfType:];
-[UIUserNotificationSettings userNotificationActionSettings];
-[UIUserNotificationSettings validatedSettings];
```
