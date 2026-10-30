# `UserNotificationManager`

- Image: [`/usr/lib/libBasebandManagerDAL.dylib`](../userland/usr__lib__libBasebandManagerDAL.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UNUserNotificationCenterDelegate`
- 3 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"UNUserNotificationCenter" fUserNotificationCenter;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} fQueue;
{map<std::string, CallBackData, std::less<std::string>, std::allocator<std::pair<const std::string, CallBackData>>>="__tree_"{__tree<std::__value_type<std::string, CallBackData>, std::__map_value_compare<std::string, std::pair<const std::string, CallBackData>, std::less<std::string>>, std::allocator<std::pair<const std::string, CallBackData>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} fCallBackMapWithQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UserNotificationManager sharedInstance:];
```

## Instance methods

```
-[UserNotificationManager userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:];
-[UserNotificationManager init:];
-[UserNotificationManager setActionForHeader:notificationContent:callbackData:];
-[UserNotificationManager setUpNotificationCenter:];
-[UserNotificationManager showNotification:withCallBackData:];
-[UserNotificationManager updateAnalyticsEvent:withUserReponse:];
```
