# `SBDashBoardStatusBarController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSStatusBarControlling`
- 8 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _statusBarHiddenReasons;
@"SBWindowSceneStatusBarSettingsAssertion" _hideStatusBarAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarParametersAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _hideMenuBarStatusBarPartAssertion;
@"SBWindowScene" _windowScene;
@"SBWindowSceneStatusBarManager" _windowSceneStatusBarManager;
@"NSMutableSet" _statusBars;
@"NSMapTable" _statusBarsToVisibilityAssertions;
```

## Properties

```
@property (TB,R,N,GisShowingFakeStatusBar) showingFakeStatusBar;
@property (T@"NSNumber",R,N) statusBarAlpha;
@property (Tq,R,N) statusBarStyle;
@property (T@"_UILegibilitySettings",R,N) statusBarLegibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardStatusBarController statusBarAlpha];
-[SBDashBoardStatusBarController dealloc];
-[SBDashBoardStatusBarController initWithWindowScene:];
-[SBDashBoardStatusBarController statusBarStyle];
-[SBDashBoardStatusBarController clearStatusBarParameters];
-[SBDashBoardStatusBarController createFakeStatusBarWithReason:withFrame:];
-[SBDashBoardStatusBarController destroyFakeStatusBar:];
-[SBDashBoardStatusBarController effectiveStatusBarStyleRequestForAlpha:style:legibilitySettings:];
-[SBDashBoardStatusBarController setStatusBarAlpha:style:legibilitySettings:];
-[SBDashBoardStatusBarController setStatusBarHidden:forReason:];
-[SBDashBoardStatusBarController setStatusBarPart:hidden:animationDuration:];
-[SBDashBoardStatusBarController statusBarLegibilitySettings];
-[SBDashBoardStatusBarController _enumerateStatusBarsAndPartAssertions:];
-[SBDashBoardStatusBarController isShowingFakeStatusBar];
```
