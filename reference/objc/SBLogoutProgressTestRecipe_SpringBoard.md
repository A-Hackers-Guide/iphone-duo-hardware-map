# `SBLogoutProgressTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLogoutProgressDataSource`, `SBTestRecipe`
- 4 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _tasks;
@"SBLogoutProgressTransientOverlayViewController" _logoutProgressTransientOverlayViewController;
@"NSArray" _remainingApplications;
@"NSDictionary" _remainingBlockingTasks;
```

## Properties

```
@property (T@"SBLogoutProgressTransientOverlayViewController",&,N,V_logoutProgressTransientOverlayViewController) logoutProgressTransientOverlayViewController;
@property (T@"NSArray",C,N,V_remainingApplications) remainingApplications;
@property (T@"NSDictionary",&,N,V_remainingBlockingTasks) remainingBlockingTasks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLogoutProgressTestRecipe title];
-[SBLogoutProgressTestRecipe _defaultBlockingTasks];
-[SBLogoutProgressTestRecipe _defaultPendingApplications];
-[SBLogoutProgressTestRecipe debugBlockingTasksForLogoutProgressTransientOverlayViewController:];
-[SBLogoutProgressTestRecipe handleVolumeDecrease];
-[SBLogoutProgressTestRecipe handleVolumeIncrease];
-[SBLogoutProgressTestRecipe logoutProgressTransientOverlayViewController];
-[SBLogoutProgressTestRecipe pendingApplicationsForLogoutProgressTransientOverlayViewController:];
-[SBLogoutProgressTestRecipe remainingApplications];
-[SBLogoutProgressTestRecipe remainingBlockingTasks];
-[SBLogoutProgressTestRecipe setLogoutProgressTransientOverlayViewController:];
-[SBLogoutProgressTestRecipe setRemainingApplications:];
-[SBLogoutProgressTestRecipe setRemainingBlockingTasks:];
```
