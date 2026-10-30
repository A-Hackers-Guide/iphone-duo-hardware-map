# `SBPrototypeBasicActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SAElement`, `SBSystemApertureSuppressible`, `SAActivityBehavior`, `SAUIElementViewProviding`, `SAUILayoutSpecifying`
- 8 instance variables, 32 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _startTime;
@"NSDateComponentsFormatter" _formatter;
@"NSTimer" _timer;
B _displayedWithLimitedSize;
@"UIView" _leadingView;
@"UIView" _trailingView;
q _layoutMode;
@"<SAUILayoutHosting>" _layoutHost;
```

## Properties

```
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (TB,?,N,GisSuppressed) suppressed;
@property (T@"<SAActivityHosting>",?,W,N) activityHost;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,?,N) layoutAxis;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (Tq,R,N) minimumSupportedLayoutMode;
@property (Tq,R,N) maximumSupportedLayoutMode;
@property (Tq,R,N) preferredLayoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize,V_displayedWithLimitedSize) displayedWithLimitedSize;
```

## Instance methods

```
-[SBPrototypeBasicActivityElement setDisplayedWithLimitedSize:];
-[SBPrototypeBasicActivityElement layoutHost];
-[SBPrototypeBasicActivityElement keyColor];
-[SBPrototypeBasicActivityElement minimalView];
-[SBPrototypeBasicActivityElement trailingView];
-[SBPrototypeBasicActivityElement setLayoutMode:reason:];
-[SBPrototypeBasicActivityElement layoutMode];
-[SBPrototypeBasicActivityElement leadingView];
-[SBPrototypeBasicActivityElement setLayoutHost:];
-[SBPrototypeBasicActivityElement clientIdentifier];
-[SBPrototypeBasicActivityElement acceptsFullScreenTransitionFromSceneWithIdentifier:ofBundleId:];
-[SBPrototypeBasicActivityElement element];
-[SBPrototypeBasicActivityElement preferredLayoutMode];
-[SBPrototypeBasicActivityElement isDisplayedWithLimitedSize];
-[SBPrototypeBasicActivityElement elementIdentifier];
-[SBPrototypeBasicActivityElement init];
-[SBPrototypeBasicActivityElement viewProvider];
-[SBPrototypeBasicActivityElement handleElementViewEvent:];
-[SBPrototypeBasicActivityElement _updateLabel];
-[SBPrototypeBasicActivityElement _canShowWhileLocked];
-[SBPrototypeBasicActivityElement shouldSuppressElementWhilePresentingAppWithBundleId:];
-[SBPrototypeBasicActivityElement minimumSupportedLayoutMode];
-[SBPrototypeBasicActivityElement hasActivityBehavior];
-[SBPrototypeBasicActivityElement maximumSupportedLayoutMode];
-[SBPrototypeBasicActivityElement _activateApplication];
```
