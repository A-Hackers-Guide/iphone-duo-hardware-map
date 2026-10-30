# `HIDRMUIUserAuthorizationManager`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 11 instance methods, 8 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _completionQueue;
@"NSMutableDictionary" _authRequests;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",R,N) log;
@property (T@"NSMutableDictionary",&,N,V_authRequests) authRequests;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_completionQueue) completionQueue;
@property (T@"NSArray",R,N) userAuthorizationRequests;
```

## Class methods

```
+[HIDRMUIUserAuthorizationManager shouldShowInternalUI];
+[HIDRMUIUserAuthorizationManager sharedManager];
+[HIDRMUIUserAuthorizationManager log];
+[HIDRMUIUserAuthorizationManager digitFromCharacter:digit:];
+[HIDRMUIUserAuthorizationManager digitsArrayFromNumber:];
+[HIDRMUIUserAuthorizationManager launchTTRForNotificationType:andDeviceName:];
+[HIDRMUIUserAuthorizationManager randomNumberWithDigitCount:];
+[HIDRMUIUserAuthorizationManager userNotificationForType:deviceName:];
```

## Instance methods

```
-[HIDRMUIUserAuthorizationManager completionQueue];
-[HIDRMUIUserAuthorizationManager init];
-[HIDRMUIUserAuthorizationManager setCompletionQueue:];
-[HIDRMUIUserAuthorizationManager log];
-[HIDRMUIUserAuthorizationManager addUserAuthorizationRequest:completion:];
-[HIDRMUIUserAuthorizationManager handleInputCharacter:forUserAuthorizationRequest:error:];
-[HIDRMUIUserAuthorizationManager removeUserAuthorizationRequest:error:];
-[HIDRMUIUserAuthorizationManager userAuthorizationRequests];
-[HIDRMUIUserAuthorizationManager authRequests];
-[HIDRMUIUserAuthorizationManager removeAllUserAuthorizationRequests:];
-[HIDRMUIUserAuthorizationManager setAuthRequests:];
```
