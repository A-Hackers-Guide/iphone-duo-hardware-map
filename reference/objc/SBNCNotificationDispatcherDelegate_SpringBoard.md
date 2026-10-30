# `SBNCNotificationDispatcherDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCNotificationDispatcherDelegate`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBUnlockRequestHandling>" _unlockRequestHandler;
@"SBNotificationBannerDestination" _bannerDestination;
```

## Properties

```
@property (T@"SBNotificationBannerDestination",W,N,V_bannerDestination) bannerDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNCNotificationDispatcherDelegate bannerDestination];
-[SBNCNotificationDispatcherDelegate _requestAuthenticationWithCompletion:];
-[SBNCNotificationDispatcherDelegate dispatcher:didExecuteAction:forNotificationRequest:];
-[SBNCNotificationDispatcherDelegate dispatcher:requestPermissionToExecuteAction:forDestination:notificationRequest:withParameters:completionBlock:];
-[SBNCNotificationDispatcherDelegate dispatcher:willExecuteAction:forDestination:notificationRequest:requestAuthentication:withParameters:completionBlock:];
-[SBNCNotificationDispatcherDelegate dispatcher:launchBackgroundApplicationForAction:notificationRequest:fromDestination:withParameters:];
-[SBNCNotificationDispatcherDelegate dispatcher:launchForegroundApplicationForAction:notificationRequest:fromDestination:withParameters:];
-[SBNCNotificationDispatcherDelegate initWithUnlockRequester:];
-[SBNCNotificationDispatcherDelegate setBannerDestination:];
```
