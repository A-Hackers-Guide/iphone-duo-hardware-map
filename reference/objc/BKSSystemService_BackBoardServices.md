# `BKSSystemService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FBSSystemService" _fbsSystemService;
```

## Instance methods

```
-[BKSSystemService systemApplicationBundleIdentifier];
-[BKSSystemService init];
-[BKSSystemService canOpenApplication:reason:];
-[BKSSystemService openApplication:options:withResult:];
-[BKSSystemService cleanupClientPort:];
-[BKSSystemService createClientPort];
-[BKSSystemService openApplication:options:clientPort:withResult:];
-[BKSSystemService openURL:application:options:clientPort:withResult:];
-[BKSSystemService pidForApplication:];
-[BKSSystemService terminateApplication:forReason:andReport:withDescription:];
```
