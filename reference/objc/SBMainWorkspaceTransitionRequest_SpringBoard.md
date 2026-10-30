# `SBMainWorkspaceTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceTransitionRequest`
- 12 instance variables, 13 properties, 36 instance methods, 1 class methods

## Instance variables

```
q _source;
@? _transactionProvider;
@? _transactionConfigurator;
@"NSMutableArray" _completionTasks;
B _shouldPreventEmergencyNotificationBannerDismissal;
B _shouldPreventDismissalOfUnrelatedTransientOverlays;
B _preservesTransientOverlaysMovingToNewWindowScene;
B _shouldBypassAgeRestriction;
B _crossingDisplays;
@"<SBBannerUnfurlSourceContextProviding>" _bannerUnfurlSourceContextProvider;
q _centerConfiguration;
@"NSString" _centerWindowSourceSceneID;
```

## Properties

```
@property (T@"SBMainWorkspace",R,D,N) workspace;
@property (Tq,N,V_source) source;
@property (TB,N,V_shouldPreventEmergencyNotificationBannerDismissal) shouldPreventEmergencyNotificationBannerDismissal;
@property (T@"<SBBannerUnfurlSourceContextProviding>",&,N,V_bannerUnfurlSourceContextProvider) bannerUnfurlSourceContextProvider;
@property (TB,N,V_shouldPreventDismissalOfUnrelatedTransientOverlays) shouldPreventDismissalOfUnrelatedTransientOverlays;
@property (TB,N,V_preservesTransientOverlaysMovingToNewWindowScene) preservesTransientOverlaysMovingToNewWindowScene;
@property (TB,N,GisCrossingDisplays,V_crossingDisplays) crossingDisplays;
@property (TB,N,V_shouldBypassAgeRestriction) shouldBypassAgeRestriction;
@property (Tq,N,V_centerConfiguration) centerConfiguration;
@property (T@"NSString",&,N,V_centerWindowSourceSceneID) centerWindowSourceSceneID;
@property (T@?,C,N,V_transactionProvider) transactionProvider;
@property (T@?,C,N,V_transactionConfigurator) transactionConfigurator;
@property (T@?,R,C,N) completionBlock;
```

## Class methods

```
+[SBMainWorkspaceTransitionRequest ancillaryTransitionRequestsForTransitionRequest:];
```

## Instance methods

```
-[SBMainWorkspaceTransitionRequest finalize];
-[SBMainWorkspaceTransitionRequest centerConfiguration];
-[SBMainWorkspaceTransitionRequest addCompletionHandler:];
-[SBMainWorkspaceTransitionRequest setShouldPreventEmergencyNotificationBannerDismissal:];
-[SBMainWorkspaceTransitionRequest setCenterConfiguration:];
-[SBMainWorkspaceTransitionRequest compactDescriptionBuilder];
-[SBMainWorkspaceTransitionRequest completionBlock];
-[SBMainWorkspaceTransitionRequest preservesTransientOverlaysMovingToNewWindowScene];
-[SBMainWorkspaceTransitionRequest setShouldBypassAgeRestriction:];
-[SBMainWorkspaceTransitionRequest succinctDescriptionBuilder];
-[SBMainWorkspaceTransitionRequest setShouldPreventDismissalOfUnrelatedTransientOverlays:];
-[SBMainWorkspaceTransitionRequest isMainWorkspaceTransitionRequest];
-[SBMainWorkspaceTransitionRequest dealloc];
-[SBMainWorkspaceTransitionRequest _performAndInvalidateCompletionTasksWithSuccess:];
-[SBMainWorkspaceTransitionRequest shouldBypassAgeRestriction];
-[SBMainWorkspaceTransitionRequest initWithDisplayConfiguration:];
-[SBMainWorkspaceTransitionRequest setBannerUnfurlSourceContextProvider:];
-[SBMainWorkspaceTransitionRequest setCrossingDisplays:];
-[SBMainWorkspaceTransitionRequest modifyTransientOverlayContext:];
-[SBMainWorkspaceTransitionRequest setTransactionConfigurator:];
-[SBMainWorkspaceTransitionRequest transactionConfigurator];
-[SBMainWorkspaceTransitionRequest setSource:];
-[SBMainWorkspaceTransitionRequest shouldPreventEmergencyNotificationBannerDismissal];
-[SBMainWorkspaceTransitionRequest setTransientOverlayContext:];
-[SBMainWorkspaceTransitionRequest setCenterWindowSourceSceneID:];
-[SBMainWorkspaceTransitionRequest setPreservesTransientOverlaysMovingToNewWindowScene:];
-[SBMainWorkspaceTransitionRequest transactionProvider];
-[SBMainWorkspaceTransitionRequest centerWindowSourceSceneID];
-[SBMainWorkspaceTransitionRequest _initWithWorkspace:displayConfiguration:];
-[SBMainWorkspaceTransitionRequest declineWithReason:];
-[SBMainWorkspaceTransitionRequest shouldPreventDismissalOfUnrelatedTransientOverlays];
-[SBMainWorkspaceTransitionRequest setTransactionProvider:];
-[SBMainWorkspaceTransitionRequest copyMainWorkspaceTransitionRequest];
-[SBMainWorkspaceTransitionRequest isCrossingDisplays];
-[SBMainWorkspaceTransitionRequest source];
-[SBMainWorkspaceTransitionRequest bannerUnfurlSourceContextProvider];
```
