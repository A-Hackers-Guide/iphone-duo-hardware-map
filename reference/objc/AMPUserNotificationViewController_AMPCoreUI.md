# `AMPUserNotificationViewController`

- Image: [`/System/Library/PrivateFrameworks/AMPCoreUI.framework/AMPCoreUI`](../userland/System__Library__PrivateFrameworks__AMPCoreUI.framework__AMPCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `AMPUserNotificationContentDelegate`, `UNNotificationContentExtension`
- 2 instance variables, 9 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<AMSURLBagContract>" _bagContract;
@"AMPUserNotificationContentViewController" _contentViewController;
```

## Properties

```
@property (T@"AMPUserNotificationContentViewController",&,N,V_contentViewController) contentViewController;
@property (T@"<AMSURLBagContract>",&,N,V_bagContract) bagContract;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,R,N) mediaPlayPauseButtonType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) mediaPlayPauseButtonFrame;
@property (T@"UIColor",?,R,C,N) mediaPlayPauseButtonTintColor;
```

## Class methods

```
+[AMPUserNotificationViewController userNotificationFromNotification:];
```

## Instance methods

```
-[AMPUserNotificationViewController setBagContract:];
-[AMPUserNotificationViewController setContentViewController:];
-[AMPUserNotificationViewController viewWillDisappear:];
-[AMPUserNotificationViewController contentViewController];
-[AMPUserNotificationViewController viewWillLayoutSubviews];
-[AMPUserNotificationViewController bagContract];
-[AMPUserNotificationViewController didReceiveNotification:];
-[AMPUserNotificationViewController didReceiveNotificationResponse:completionHandler:];
-[AMPUserNotificationViewController openNotification];
-[AMPUserNotificationViewController renderUserNotification:];
-[AMPUserNotificationViewController viewController:didUpdatePreferredContentSize:];
```
