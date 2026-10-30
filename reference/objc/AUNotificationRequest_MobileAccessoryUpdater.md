# `AUNotificationRequest`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _type;
@"NSString" _accessoryName;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",&,N,V_accessoryName) accessoryName;
```

## Class methods

```
+[AUNotificationRequest supportsSecureCoding];
```

## Instance methods

```
-[AUNotificationRequest accessoryName];
-[AUNotificationRequest dealloc];
-[AUNotificationRequest setType:];
-[AUNotificationRequest type];
-[AUNotificationRequest encodeWithCoder:];
-[AUNotificationRequest initWithCoder:];
-[AUNotificationRequest setAccessoryName:];
-[AUNotificationRequest initUnplugReplugNotificationWithAccessoryName:];
```
