# `SBUserSessionController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLogoutProgressDataSource`, `SBLogoutProgressDelegate`, `UMCriticalUserSwitchStakeholder`
- 14 instance variables, 11 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"UMUserManager" _userManager;
@"SBRestartManager" _restartManager;
@"SBApplicationController" _applicationController;
@"UMUser" _lazy_user;
@"SBPolicyAggregator" _lazy_policyAggregator;
@"SBLogoutProgressTransientOverlayViewController" _progressTransientOverlayViewController;
@"NSMutableArray" _displayApplications;
@"NSMutableSet" _terminatingApplications;
@"UMUserSwitchBlockingTask" _terminateApplicationsTask;
@"NSDate" _terminateApplicationsStartDate;
@"NSDictionary" _debugBlockingTasks;
@"LKLogoutSupport" _logoutSupport;
B _loginSession;
B _loggingOut;
```

## Properties

```
@property (TB,N,GisLoggingOut,V_loggingOut) loggingOut;
@property (T@"SBPolicyAggregator",&,N,G_policyAggregator,S_setPolicyAggregator:,V_lazy_policyAggregator) policyAggregator;
@property (T@"UMUser",R,&,N) user;
@property (TB,R,N,GisLoginSession,V_loginSession) loginSession;
@property (TB,R,N) isMultiUserSupported;
@property (TB,R,N) canLogout;
@property (Tq,R,N) sessionType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUserSessionController _iconController];
-[SBUserSessionController succinctDescriptionBuilder];
-[SBUserSessionController dealloc];
-[SBUserSessionController policyAggregator];
-[SBUserSessionController descriptionWithMultilinePrefix:];
-[SBUserSessionController succinctDescription];
-[SBUserSessionController sessionType];
-[SBUserSessionController user];
-[SBUserSessionController description];
-[SBUserSessionController logout];
-[SBUserSessionController descriptionBuilderWithMultilinePrefix:];
-[SBUserSessionController isLoginSession];
-[SBUserSessionController readyToSwitchToLoginSession:];
-[SBUserSessionController readyToSwitchToUser:];
-[SBUserSessionController userSwitchBlockingTasksDidUpdate:];
-[SBUserSessionController willSwitchToUser:];
-[SBUserSessionController isMultiUserSupported];
-[SBUserSessionController _displayProgressTransientOverlayIfNeeded];
-[SBUserSessionController _evaluateRunningApplications];
-[SBUserSessionController _initWithUserManager:restartManager:applicationController:];
-[SBUserSessionController _massageApplicationListForDisplay:];
-[SBUserSessionController _noteApplicationDidExit:];
-[SBUserSessionController _noteApplicationDidExitFromNotification:];
-[SBUserSessionController _policyAggregator];
-[SBUserSessionController _portraitOrientedProgressLocationForOrientation:];
-[SBUserSessionController _readyToSwitchToUser:];
-[SBUserSessionController _refetchCurrentUser];
-[SBUserSessionController _setPolicyAggregator:];
-[SBUserSessionController canLogout];
-[SBUserSessionController debugBlockingTasksForLogoutProgressTransientOverlayViewController:];
-[SBUserSessionController disableCurrentUser];
-[SBUserSessionController initWithRestartManager:applicationController:];
-[SBUserSessionController isLoggingOut];
-[SBUserSessionController logoutProgressTransientOverlayPresentationTransitionCoordinatorDidComplete:];
-[SBUserSessionController logoutProgressTransientOverlayViewControllerDidDisappear:];
-[SBUserSessionController logoutWithLogoutSupport:];
-[SBUserSessionController pendingApplicationsForLogoutProgressTransientOverlayViewController:];
-[SBUserSessionController setLoggingOut:];
```
