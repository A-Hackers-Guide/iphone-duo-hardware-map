# `SBSystemApertureStatusBarPillElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SBSystemApertureLayoutCustomizing`, `SAElement`, `SBSystemApertureSuppressible`, `SBSystemApertureBackgroundActivitiesRepresenting`, `SAActivityBehavior`, `SAUIElementViewProviding`, `SAUILayoutSpecifying`
- 9 instance variables, 40 properties, 46 instance methods, 1 class methods

## Instance variables

```
@"NSString" _representedBackgroundActivityIdentifier;
B _displayedWithLimitedSize;
@"NSString" _elementIdentifier;
@"<SAUILayoutHosting>" _layoutHost;
q _layoutMode;
@"UIView" _leadingView;
@"UIView" _trailingView;
@"NSSet" _associatedApplications;
@ _clientStorage;
```

## Properties

```
@property (T@"NSString",R,N) activeSymbolName;
@property (T@"UIColor",R,N) activeTintColor;
@property (T@"NSSet",C,N,V_associatedApplications) associatedApplications;
@property (T@,&,N,V_clientStorage) clientStorage;
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
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (T@"<SAElementHosting>",?,W,N) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
@property (TB,?,N,GisSuppressed) suppressed;
@property (T@"NSSet",R,C,N) representedBackgroundActivityIdentifiers;
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

## Class methods

```
+[SBSystemApertureStatusBarPillElement backgroundActivityIdentifiersThatIgnoreSystemChromeSuppression];
```

## Instance methods

```
-[SBSystemApertureStatusBarPillElement setDisplayedWithLimitedSize:];
-[SBSystemApertureStatusBarPillElement systemApertureLayoutCustomizingOptions];
-[SBSystemApertureStatusBarPillElement layoutHost];
-[SBSystemApertureStatusBarPillElement keyColor];
-[SBSystemApertureStatusBarPillElement minimalView];
-[SBSystemApertureStatusBarPillElement trailingView];
-[SBSystemApertureStatusBarPillElement setLayoutMode:reason:];
-[SBSystemApertureStatusBarPillElement layoutMode];
-[SBSystemApertureStatusBarPillElement leadingView];
-[SBSystemApertureStatusBarPillElement setLayoutHost:];
-[SBSystemApertureStatusBarPillElement clientIdentifier];
-[SBSystemApertureStatusBarPillElement acceptsFullScreenTransitionFromSceneWithIdentifier:ofBundleId:];
-[SBSystemApertureStatusBarPillElement element];
-[SBSystemApertureStatusBarPillElement preferredLayoutMode];
-[SBSystemApertureStatusBarPillElement isDisplayedWithLimitedSize];
-[SBSystemApertureStatusBarPillElement elementIdentifier];
-[SBSystemApertureStatusBarPillElement representedBackgroundActivityIdentifiers];
-[SBSystemApertureStatusBarPillElement viewProvider];
-[SBSystemApertureStatusBarPillElement _textLabel];
-[SBSystemApertureStatusBarPillElement handleElementViewEvent:];
-[SBSystemApertureStatusBarPillElement shouldSuppressElementWhileProximityReaderPresent];
-[SBSystemApertureStatusBarPillElement activeTintColor];
-[SBSystemApertureStatusBarPillElement _canShowWhileLocked];
-[SBSystemApertureStatusBarPillElement shouldSuppressElementWhilePresentingAppWithBundleId:];
-[SBSystemApertureStatusBarPillElement minimumSupportedLayoutMode];
-[SBSystemApertureStatusBarPillElement shouldSuppressElementWhileOnCoversheet];
-[SBSystemApertureStatusBarPillElement hasActivityBehavior];
-[SBSystemApertureStatusBarPillElement maximumSupportedLayoutMode];
-[SBSystemApertureStatusBarPillElement _imageName];
-[SBSystemApertureStatusBarPillElement _accessibilityLabel];
-[SBSystemApertureStatusBarPillElement initWithBackgroundActivityIdentifier:];
-[SBSystemApertureStatusBarPillElement _isAssociatedWithApplicationWithBundleIdentifier:];
-[SBSystemApertureStatusBarPillElement _packageName];
-[SBSystemApertureStatusBarPillElement _representedStatusBarStyleOverrides];
-[SBSystemApertureStatusBarPillElement _representedVisualDescriptor];
-[SBSystemApertureStatusBarPillElement _sizeForPillWithImageName];
-[SBSystemApertureStatusBarPillElement _viewWithImageName:systemApertureSize:tintColor:];
-[SBSystemApertureStatusBarPillElement _viewWithPackageName:];
-[SBSystemApertureStatusBarPillElement _viewWithSymbolName:tintColor:];
-[SBSystemApertureStatusBarPillElement _viewWithTextLabel:tintColor:];
-[SBSystemApertureStatusBarPillElement activeSymbolName];
-[SBSystemApertureStatusBarPillElement associatedApplications];
-[SBSystemApertureStatusBarPillElement clientStorage];
-[SBSystemApertureStatusBarPillElement setAssociatedApplications:];
-[SBSystemApertureStatusBarPillElement setClientStorage:];
-[SBSystemApertureStatusBarPillElement shouldIgnoreSystemChromeSuppression];
```
