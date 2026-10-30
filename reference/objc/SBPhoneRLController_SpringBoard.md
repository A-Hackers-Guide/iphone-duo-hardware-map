# `SBPhoneRLController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SDUDisplayRegionBlankingObserver`
- 12 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"SDUDisplayRegionBlankingCoordinator" _displayRegionBlankingCoordinator;
@"UIWindow" _window;
@"SBPhoneRLViewController" _viewController;
Q _displayRegionBlankingState;
@"NSString" _displayRegionBlankingAssociatedBundleID;
@"SBSystemApertureLayoutMetrics" _systemApertureLayout;
@"NSTimer" _windowHideTimer;
@"SBTestingDefaults" _testingDefaults;
@"<BSDefaultObserver>" _forcePhoneRLActivateObserver;
@"<BSDefaultObserver>" _preservePhoneRLInCapturesObserver;
B _phoneRLActive;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TB,N,GisPhoneRLActive,S_setPhoneRLActive:,V_phoneRLActive) phoneRLActive;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBPhoneRLController isSupportedOnWindowScene:];
```

## Instance methods

```
-[SBPhoneRLController dealloc];
-[SBPhoneRLController invalidate];
-[SBPhoneRLController windowScene];
-[SBPhoneRLController blankingBundleIDsDidChangeForDisplayRegion:onWindowScene:forBundleIDs:];
-[SBPhoneRLController blankingStateDidChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBPhoneRLController blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBPhoneRLController isPhoneRLActive];
-[SBPhoneRLController _createPhoneRLWindow];
-[SBPhoneRLController _handleWindowHideTimer:];
-[SBPhoneRLController _phoneRLEnabledDidChange:];
-[SBPhoneRLController _phoneRLModeDidChange:];
-[SBPhoneRLController _phoneRLRecommendedNitsDidChange:];
-[SBPhoneRLController _reevaluatePhoneRLActivationStateForReason:];
-[SBPhoneRLController _setPhoneRLActive:];
-[SBPhoneRLController _tearDownPhoneRLWindow];
-[SBPhoneRLController _updatePhoneRLWindowCaptureVisibility];
-[SBPhoneRLController initWithWindowScene:displayRegionBlankingCoordinator:];
```
