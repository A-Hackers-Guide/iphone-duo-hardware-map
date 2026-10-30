# `SBInProcessSecureAppAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSLockScreenContentAction`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationSceneEntity" _applicationSceneEntity;
@"<CSHostableEntity>" _hostableEntity;
```

## Properties

```
@property (T@"SBApplicationSceneEntity",&,N,V_applicationSceneEntity) applicationSceneEntity;
@property (T@"<CSHostableEntity>",&,N,V_hostableEntity) hostableEntity;
```

## Instance methods

```
-[SBInProcessSecureAppAction abortForUsageViolation:];
-[SBInProcessSecureAppAction applicationSceneEntity];
-[SBInProcessSecureAppAction hostableEntity];
-[SBInProcessSecureAppAction initWithType:applicationSceneEntity:handler:];
-[SBInProcessSecureAppAction initWithType:hostableEntity:handler:];
-[SBInProcessSecureAppAction isInProcessAction];
-[SBInProcessSecureAppAction setApplicationSceneEntity:];
-[SBInProcessSecureAppAction setHostableEntity:];
```
