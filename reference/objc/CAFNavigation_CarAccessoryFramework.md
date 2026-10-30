# `CAFNavigation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFSystemInformation",R,N) systemInformationService;
@property (T@"CAFRouteStatus",R,N) routeStatusService;
@property (T@"CAFRouteSharing",R,N) routeSharingService;
@property (T@"CAFSystemInformation",R,N) systemInformation;
@property (T@"CAFRouteStatus",R,N) routeStatus;
@property (T@"CAFRouteSharing",R,N) routeSharing;
```

## Class methods

```
+[CAFNavigation accessoryIdentifier];
+[CAFNavigation observerProtocol];
```

## Instance methods

```
-[CAFNavigation removeObserver:];
-[CAFNavigation addObserver:];
-[CAFNavigation registerObserver:];
-[CAFNavigation unregisterObserver:];
-[CAFNavigation systemInformation];
-[CAFNavigation routeSharing];
-[CAFNavigation routeStatus];
-[CAFNavigation routeSharingService];
-[CAFNavigation routeStatusService];
-[CAFNavigation systemInformationService];
```
