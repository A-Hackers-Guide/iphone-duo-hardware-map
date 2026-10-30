# `UIWillPresentNotificationAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isDeliverable;
@"UNNotification" _notification;
```

## Properties

```
@property (T@"UNNotification",R,&,N,V_notification) notification;
@property (TB,R,N,V_isDeliverable) isDeliverable;
@property (TB,R,N) isLocal;
@property (TB,R,N) isRemote;
```

## Instance methods

```
-[UIWillPresentNotificationAction notification];
-[UIWillPresentNotificationAction UIActionType];
-[UIWillPresentNotificationAction abortForUsageViolation:];
-[UIWillPresentNotificationAction initWithNotification:deliverable:timeout:withHandler:];
-[UIWillPresentNotificationAction initWithXPCDictionary:];
-[UIWillPresentNotificationAction isDeliverable];
-[UIWillPresentNotificationAction isRemote];
-[UIWillPresentNotificationAction valueDescriptionForFlag:object:ofSetting:];
-[UIWillPresentNotificationAction keyDescriptionForSetting:];
-[UIWillPresentNotificationAction isLocal];
-[UIWillPresentNotificationAction _trigger];
-[UIWillPresentNotificationAction initWithNotification:timeout:withHandler:];
```
