# `SBUISystemApertureElement` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 27 properties, 31 instance methods, 0 class methods

## Properties

```
@property (Tq,N) activeLayoutMode;
@property (Tq,R,N) contentRole;
@property (Tq,R,N) preferredLayoutMode;
@property (Tq,R,N) maximumLayoutMode;
@property (Td,?,R,N) preferredHeightForBottomSafeArea;
@property (T@"NSString",?,R,C,N) elementIdentifier;
@property (T@"NSString",?,R,C,N) associatedAppBundleIdentifier;
@property (T@"NSString",?,R,C,N) associatedScenePersistenceIdentifier;
@property (T@"NSURL",?,R,C,N) launchURL;
@property (T@"BSAction",?,R,N) launchAction;
@property (TB,?,R,N) preventsInteractiveDismissal;
@property (TB,?,R,N) preventsAutomaticDismissal;
@property (Tq,?,R,N) minimumLayoutMode;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) leadingView;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) trailingView;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) minimalView;
@property (TQ,?,R,N) statusBarStyleOverridesToSuppress;
@property (T@"NSSet",?,R,C,N) backgroundActivitiesToSuppress;
@property (T{CGSize=dd},?,R,N) preferredCustomAspectRatio;
@property (Tq,?,R,N) preferredCustomLayout;
@property (TQ,?,R,N) presentationBehaviors;
@property (T@"UIColor",?,R,C,N) keyColor;
@property (TQ,?,N) minimalViewLayoutAxis;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) detachedMinimalView;
@property (TB,?,N) canRequestAlertingAssertion;
@property (TB,?,R,N) attachedMinimalViewRequiresZeroPadding;
@property (TB,?,R,N) prefersFixedPortraitOrientation;
```

## Instance methods

```
-[SBUISystemApertureElement setActiveLayoutMode:];
-[SBUISystemApertureElement contentRole];
-[SBUISystemApertureElement maximumLayoutMode];
-[SBUISystemApertureElement activeLayoutMode];
-[SBUISystemApertureElement preferredLayoutMode];
-[SBUISystemApertureElement detachedMinimalView];
-[SBUISystemApertureElement presentationBehaviors];
-[SBUISystemApertureElement associatedAppBundleIdentifier];
-[SBUISystemApertureElement keyColor];
-[SBUISystemApertureElement minimalView];
-[SBUISystemApertureElement trailingView];
-[SBUISystemApertureElement leadingView];
-[SBUISystemApertureElement preventsAutomaticDismissal];
-[SBUISystemApertureElement launchAction];
-[SBUISystemApertureElement elementIdentifier];
-[SBUISystemApertureElement preventsInteractiveDismissal];
-[SBUISystemApertureElement viewWillLayoutSubviewsWithTransitionCoordinator:];
-[SBUISystemApertureElement preferredHeightForBottomSafeArea];
-[SBUISystemApertureElement preferredCustomLayout];
-[SBUISystemApertureElement backgroundActivitiesToSuppress];
-[SBUISystemApertureElement setCanRequestAlertingAssertion:];
-[SBUISystemApertureElement associatedScenePersistenceIdentifier];
-[SBUISystemApertureElement canRequestAlertingAssertion];
-[SBUISystemApertureElement attachedMinimalViewRequiresZeroPadding];
-[SBUISystemApertureElement prefersFixedPortraitOrientation];
-[SBUISystemApertureElement minimumLayoutMode];
-[SBUISystemApertureElement launchURL];
-[SBUISystemApertureElement preferredCustomAspectRatio];
-[SBUISystemApertureElement statusBarStyleOverridesToSuppress];
-[SBUISystemApertureElement minimalViewLayoutAxis];
-[SBUISystemApertureElement setMinimalViewLayoutAxis:];
```
