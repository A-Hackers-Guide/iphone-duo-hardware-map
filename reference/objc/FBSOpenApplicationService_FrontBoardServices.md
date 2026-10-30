# `FBSOpenApplicationService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 5 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _callbackQueue;
@"BSServiceConnection" _connection;
```

## Class methods

```
+[FBSOpenApplicationService serviceName];
+[FBSOpenApplicationService new];
+[FBSOpenApplicationService serviceWithDefaultShellEndpoint];
+[FBSOpenApplicationService currentProcessServicesDefaultShellEndpoint];
+[FBSOpenApplicationService serviceWithEndpoint:];
```

## Instance methods

```
-[FBSOpenApplicationService init];
-[FBSOpenApplicationService dealloc];
-[FBSOpenApplicationService _initWithEndpoint:];
-[FBSOpenApplicationService _openApplication:withOptions:clientHandle:completion:];
-[FBSOpenApplicationService canOpenApplication:reason:];
-[FBSOpenApplicationService _remoteTarget];
-[FBSOpenApplicationService openApplication:withOptions:clientHandle:completion:];
-[FBSOpenApplicationService openApplication:withOptions:completion:];
```
