# `IOUserNotificationButton`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _selected;
@"NSString" _title;
@"NSString" _identifier;
```

## Properties

```
@property (TB,N,V_selected) selected;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",C,N,V_identifier) identifier;
```

## Class methods

```
+[IOUserNotificationButton buttonWithTitle:];
+[IOUserNotificationButton buttonWithTitle:andIdentifier:];
```

## Instance methods

```
-[IOUserNotificationButton setSelected:];
-[IOUserNotificationButton identifier];
-[IOUserNotificationButton init];
-[IOUserNotificationButton setIdentifier:];
-[IOUserNotificationButton title];
-[IOUserNotificationButton hash];
-[IOUserNotificationButton description];
-[IOUserNotificationButton setTitle:];
-[IOUserNotificationButton isEqual:];
-[IOUserNotificationButton selected];
-[IOUserNotificationButton initWithTitle:andIdentifier:];
```
