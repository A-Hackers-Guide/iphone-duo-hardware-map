# `SBBannerAuthority`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BNConsideringDelegate`, `BNConsidering`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _requesterIDsToAuthorities;
@"NSMutableDictionary" _sinks;
@"NSObject<OS_dispatch_queue>" _biomeQueue;
B _isConfiguringSinks;
@"NSHashTable" _bannerControllerDelegates;
B _screenSharingActive;
```

## Properties

```
@property (TB,G_isScreenSharingActive,S_setScreenSharingActive:,V_screenSharingActive) screenSharingActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BNConsideringDelegate>",?,W,N) delegate;
```

## Instance methods

```
-[SBBannerAuthority init];
-[SBBannerAuthority shouldNewTierBeAddedToTopForPresentable:withPresentable:];
-[SBBannerAuthority setDelegate:];
-[SBBannerAuthority registerAuthority:forRequesterIdentifier:];
-[SBBannerAuthority shouldOverlapPresentable:withPresentable:];
-[SBBannerAuthority bannerAuthority:mayChangeDecisionForResponsiblePresentable:];
-[SBBannerAuthority shouldMorphToPresentable:withPresentedPresentables:responsiblePresentable:];
-[SBBannerAuthority shouldMorphToPresentable:withPresentedPresentables:responsiblePresentable:stateChange:];
-[SBBannerAuthority shouldPostPresentable:userInfo:reason:];
-[SBBannerAuthority shouldPresentPresentable:withPresentedPresentables:responsiblePresentable:];
-[SBBannerAuthority _configureSinksIfNecessary];
-[SBBannerAuthority _isScreenSharingActive];
-[SBBannerAuthority _mediatedDecisionFromDecisions:defaultDecision:];
-[SBBannerAuthority _setScreenSharingActive:];
-[SBBannerAuthority _shouldDropPresentableDuringScreenSharing:userInfo:];
-[SBBannerAuthority _shouldDropPresentablesDuringScreenSharing];
```
