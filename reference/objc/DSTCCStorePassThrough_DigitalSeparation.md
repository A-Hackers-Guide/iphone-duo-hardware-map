# `DSTCCStorePassThrough`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSTCCStore`
- 1 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NEConfiguration" _pathControllerConfiguration;
```

## Properties

```
@property (T@"NEConfiguration",&,N,V_pathControllerConfiguration) pathControllerConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSTCCStorePassThrough initialize];
```

## Instance methods

```
-[DSTCCStorePassThrough pathRuleForBundleID:create:];
-[DSTCCStorePassThrough setPathControllerConfiguration:];
-[DSTCCStorePassThrough allAppsWithFileAccess:handler:];
-[DSTCCStorePassThrough allAppsWithLocalNetworkAccess:queue:handler:];
-[DSTCCStorePassThrough appsWithLocationService];
-[DSTCCStorePassThrough appsWithPermissionGrantedForService:queue:completionHandler:];
-[DSTCCStorePassThrough deleteApp:forTest:];
-[DSTCCStorePassThrough healthAuthorizationForApp:andAuthorizationStore:withCompletionHandler:];
-[DSTCCStorePassThrough isEntityClassApplication:];
-[DSTCCStorePassThrough isServiceGranted:forApp:];
-[DSTCCStorePassThrough loadConfigurations:handler:];
-[DSTCCStorePassThrough locationAuthorizationForApp:];
-[DSTCCStorePassThrough pathControllerConfiguration];
-[DSTCCStorePassThrough resetFilePermissionForApp:completionHandler:];
-[DSTCCStorePassThrough resetHealthPermissionsForApp:withAuthorizationStore:andCompletionHandler:];
-[DSTCCStorePassThrough resetLocalNetworkPermissionForApp:queue:handler:];
-[DSTCCStorePassThrough resetLocationPermissionForApp:];
-[DSTCCStorePassThrough resetTCCCategory:forApp:];
-[DSTCCStorePassThrough resetTCCPermission:forApp:];
-[DSTCCStorePassThrough saveConfiguration:handler:];
```
