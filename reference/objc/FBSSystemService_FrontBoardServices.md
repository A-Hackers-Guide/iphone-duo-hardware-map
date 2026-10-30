# `FBSSystemService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"FBSSystemAppProxy" _systemAppProxy;
@"FBSOpenApplicationService" _defaultOpenApplicationService;
```

## Class methods

```
+[FBSSystemService clientCallbackQueue];
+[FBSSystemService sharedService];
```

## Instance methods

```
-[FBSSystemService terminateApplication:forReason:andReport:withDescription:completion:];
-[FBSSystemService systemApplicationBundleIdentifier];
-[FBSSystemService init];
-[FBSSystemService isPasscodeLockedOrBlocked];
-[FBSSystemService dealloc];
-[FBSSystemService _initWithEndpoint:];
-[FBSSystemService initWithEndpoint:];
-[FBSSystemService shutdownWithOptions:];
-[FBSSystemService canOpenApplication:reason:];
-[FBSSystemService sendActions:withResult:];
-[FBSSystemService terminateApplicationGroup:forReason:andReport:withDescription:completion:];
-[FBSSystemService openApplication:options:withResult:];
-[FBSSystemService cleanupClientPort:];
-[FBSSystemService createClientPort];
-[FBSSystemService openApplication:options:clientPort:withResult:];
-[FBSSystemService openURL:application:options:clientPort:withResult:];
-[FBSSystemService pidForApplication:];
-[FBSSystemService terminateApplication:forReason:andReport:withDescription:];
-[FBSSystemService badgeValueForBundleID:];
-[FBSSystemService dataResetWithRequest:completion:];
-[FBSSystemService processHandleForApplication:];
-[FBSSystemService setBadgeValue:forBundleID:];
-[FBSSystemService setKeyboardFocusApplicationPID:completion:];
-[FBSSystemService setKeyboardFocusApplicationPID:deferringToken:completion:];
-[FBSSystemService setKeyboardFocusApplicationWithBundleID:pid:completion:];
-[FBSSystemService terminateApplicationGroup:forReason:andReport:withDescription:];
```
