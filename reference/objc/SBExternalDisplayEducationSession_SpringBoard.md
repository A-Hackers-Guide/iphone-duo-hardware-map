# `SBExternalDisplayEducationSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBExternalDisplayEducationPillViewControllerDelegate`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
@"<BNPosting>" _bannerPoster;
B _isPresentingEducationBanner;
@"SBExternalDisplayEducationPillViewController" _educationBannerViewController;
@"BSAbsoluteMachTimer" _autoDismissTimer;
```

## Properties

```
@property (T@"FBSDisplayIdentity",R,N,V_displayIdentity) displayIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExternalDisplayEducationSession dealloc];
-[SBExternalDisplayEducationSession displayIdentity];
-[SBExternalDisplayEducationSession _presentBanner];
-[SBExternalDisplayEducationSession _dismissBanner:];
-[SBExternalDisplayEducationSession displayDidConnect];
-[SBExternalDisplayEducationSession displayDidDisconnect];
-[SBExternalDisplayEducationSession initWithDisplayIdentity:bannerPoster:];
-[SBExternalDisplayEducationSession pillViewControllerDidReceiveUserTap:];
-[SBExternalDisplayEducationSession updateHardwareAvailability:withinConnectionWindow:];
```
