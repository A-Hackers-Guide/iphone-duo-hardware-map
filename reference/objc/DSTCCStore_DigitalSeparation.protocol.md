# `DSTCCStore` (protocol)

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[DSTCCStore allAppsWithFileAccess:handler:];
-[DSTCCStore allAppsWithLocalNetworkAccess:queue:handler:];
-[DSTCCStore appsWithLocationService];
-[DSTCCStore appsWithPermissionGrantedForService:queue:completionHandler:];
-[DSTCCStore deleteApp:forTest:];
-[DSTCCStore healthAuthorizationForApp:andAuthorizationStore:withCompletionHandler:];
-[DSTCCStore isEntityClassApplication:];
-[DSTCCStore isServiceGranted:forApp:];
-[DSTCCStore locationAuthorizationForApp:];
-[DSTCCStore resetFilePermissionForApp:completionHandler:];
-[DSTCCStore resetHealthPermissionsForApp:withAuthorizationStore:andCompletionHandler:];
-[DSTCCStore resetLocalNetworkPermissionForApp:queue:handler:];
-[DSTCCStore resetLocationPermissionForApp:];
-[DSTCCStore resetTCCPermission:forApp:];
-[DSTCCStore saveConfiguration:handler:];
```
