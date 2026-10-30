# `SBStartupTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 11 instance variables, 16 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
@"NSString" _fromApplicationBundleID;
@"NSURL" _applicationLaunchURL;
B _fromLocked;
B _isDark;
B _isLogin;
B _isLogout;
B _isLoginSession;
@"NSArray" _overlays;
B _fromUserPowerDown;
B _hasUserSwitchOverlayMismatch;
```

## Properties

```
@property (T@"NSString",C,N,V_reason) reason;
@property (T@"NSURL",C,N,V_applicationLaunchURL) applicationLaunchURL;
@property (T@"NSString",C,N,V_fromApplicationBundleID) fromApplicationBundleID;
@property (TB,N,V_fromLocked) fromLocked;
@property (TB,N,V_fromUserPowerDown) fromUserPowerDown;
@property (TB,N,GisDark,V_isDark) dark;
@property (TB,N,GisLogin,V_isLogin) login;
@property (TB,N,GisLogout,V_isLogout) logout;
@property (TB,N,V_hasUserSwitchOverlayMismatch) hasUserSwitchOverlayMismatch;
@property (T@"NSArray",C,N,V_overlays) overlays;
@property (Tq,R,N) snapshotInterfaceOrientation;
@property (T@"CADisplay",R,N) snapshotDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStartupTransitionContext succinctDescriptionBuilder];
-[SBStartupTransitionContext setReason:];
-[SBStartupTransitionContext descriptionWithMultilinePrefix:];
-[SBStartupTransitionContext succinctDescription];
-[SBStartupTransitionContext overlays];
-[SBStartupTransitionContext description];
-[SBStartupTransitionContext reason];
-[SBStartupTransitionContext setOverlays:];
-[SBStartupTransitionContext isEqual:];
-[SBStartupTransitionContext isDark];
-[SBStartupTransitionContext descriptionBuilderWithMultilinePrefix:];
-[SBStartupTransitionContext applicationLaunchURL];
-[SBStartupTransitionContext setLogin:];
-[SBStartupTransitionContext setDark:];
-[SBStartupTransitionContext _representation];
-[SBStartupTransitionContext isLogin];
-[SBStartupTransitionContext snapshotDisplay];
-[SBStartupTransitionContext _initWithRebootContext:];
-[SBStartupTransitionContext _initWithRepresentation:loginSession:];
-[SBStartupTransitionContext _initWithRestartRequest:fromLocked:fromApplication:];
-[SBStartupTransitionContext _initWithShutdownContext:];
-[SBStartupTransitionContext _parseOverlayInfo];
-[SBStartupTransitionContext _reallyInitFromRepresentation:];
-[SBStartupTransitionContext _snapshotOverlay];
-[SBStartupTransitionContext fromApplicationBundleID];
-[SBStartupTransitionContext fromLocked];
-[SBStartupTransitionContext fromUserPowerDown];
-[SBStartupTransitionContext hasUserSwitchOverlayMismatch];
-[SBStartupTransitionContext isLogout];
-[SBStartupTransitionContext setApplicationLaunchURL:];
-[SBStartupTransitionContext setFromApplicationBundleID:];
-[SBStartupTransitionContext setFromLocked:];
-[SBStartupTransitionContext setFromUserPowerDown:];
-[SBStartupTransitionContext setHasUserSwitchOverlayMismatch:];
-[SBStartupTransitionContext setLogout:];
-[SBStartupTransitionContext snapshotInterfaceOrientation];
```
