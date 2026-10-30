# `BKUIHostedJindoPresentable`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKUIJindoPresentableBase`
- Protocols: `BNPresentableObserving`, `BNHostedContentProviding`, `BNPresentable`, `SBUISystemApertureElementProviding`, `SBUISystemApertureElement`
- 15 instance variables, 51 properties, 50 instance methods, 1 class methods

## Instance variables

```
B _canRequestAlertingAssertion;
q _destination;
@"BNBannerSourceLayoutDescription" _layoutDescription;
@"UIViewController" _rootViewController;
@"UIView<SBUISystemApertureAccessoryView>" _trailingView;
@"UIView<SBUISystemApertureAccessoryView>" _leadingView;
@"NSString" _requestIdentifier;
@"<BNPresentableContext>" _presentableContext;
q _activeLayoutMode;
@"UIView" _contentView;
q _preferredLayoutMode;
q _preferredCustomLayout;
@"BKUIPearlEnrollView" _enrollView;
d _height;
@"NSLayoutConstraint" _centerYAnchor;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_centerYAnchor) centerYAnchor;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (Tq,R,N,V_destination) destination;
@property (T@"UIViewController",W,N,V_rootViewController) rootViewController;
@property (T@"BNBannerSourceLayoutDescription",&,N,V_layoutDescription) layoutDescription;
@property (Tq,N,V_preferredLayoutMode) preferredLayoutMode;
@property (Tq,N,V_preferredCustomLayout) preferredCustomLayout;
@property (T@"BKUIPearlEnrollView",&,N,V_enrollView) enrollView;
@property (Td,N,V_height) height;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) providesHostedContent;
@property (T@"UIViewController",R,N) viewController;
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N,V_presentableContext) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N,V_requestIdentifier) requestIdentifier;
@property (T@"UIViewController<SBUISystemApertureElement>",R,N) systemApertureElementViewController;
@property (T@"<SBUISystemApertureElement>",?,R,W,N) systemApertureElement;
@property (Tq,N,V_activeLayoutMode) activeLayoutMode;
@property (Tq,R,N) contentRole;
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
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N,V_leadingView) leadingView;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N,V_trailingView) trailingView;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) minimalView;
@property (TQ,?,R,N) statusBarStyleOverridesToSuppress;
@property (T@"NSSet",?,R,C,N) backgroundActivitiesToSuppress;
@property (T{CGSize=dd},?,R,N) preferredCustomAspectRatio;
@property (TQ,?,R,N) presentationBehaviors;
@property (T@"UIColor",?,R,C,N) keyColor;
@property (TQ,?,N) minimalViewLayoutAxis;
@property (T@"UIView<SBUISystemApertureAccessoryView>",?,R,N) detachedMinimalView;
@property (TB,?,N,V_canRequestAlertingAssertion) canRequestAlertingAssertion;
@property (TB,?,R,N) attachedMinimalViewRequiresZeroPadding;
@property (TB,?,R,N) prefersFixedPortraitOrientation;
```

## Class methods

```
+[BKUIHostedJindoPresentable _bundleID];
```

## Instance methods

```
-[BKUIHostedJindoPresentable isTouchOutsideDismissalEnabled];
-[BKUIHostedJindoPresentable systemApertureElementViewController];
-[BKUIHostedJindoPresentable presentationBehaviors];
-[BKUIHostedJindoPresentable setActiveLayoutMode:];
-[BKUIHostedJindoPresentable minimalView];
-[BKUIHostedJindoPresentable contentRole];
-[BKUIHostedJindoPresentable maximumLayoutMode];
-[BKUIHostedJindoPresentable activeLayoutMode];
-[BKUIHostedJindoPresentable trailingView];
-[BKUIHostedJindoPresentable layoutDescription];
-[BKUIHostedJindoPresentable leadingView];
-[BKUIHostedJindoPresentable rootViewController];
-[BKUIHostedJindoPresentable setRootViewController:];
-[BKUIHostedJindoPresentable setContentView:];
-[BKUIHostedJindoPresentable destination];
-[BKUIHostedJindoPresentable presentableDidAppearAsBanner:];
-[BKUIHostedJindoPresentable preferredLayoutMode];
-[BKUIHostedJindoPresentable requestIdentifier];
-[BKUIHostedJindoPresentable preventsInteractiveDismissal];
-[BKUIHostedJindoPresentable setPreferredCustomLayout:];
-[BKUIHostedJindoPresentable viewDidLoad];
-[BKUIHostedJindoPresentable viewWillLayoutSubviewsWithTransitionCoordinator:];
-[BKUIHostedJindoPresentable requesterIdentifier];
-[BKUIHostedJindoPresentable viewController];
-[BKUIHostedJindoPresentable setPresentableContext:];
-[BKUIHostedJindoPresentable setHeight:];
-[BKUIHostedJindoPresentable presentableWillAppearAsBanner:];
-[BKUIHostedJindoPresentable collapse];
-[BKUIHostedJindoPresentable preferredCustomLayout];
-[BKUIHostedJindoPresentable contentView];
-[BKUIHostedJindoPresentable setCanRequestAlertingAssertion:];
-[BKUIHostedJindoPresentable associatedScenePersistenceIdentifier];
-[BKUIHostedJindoPresentable canRequestAlertingAssertion];
-[BKUIHostedJindoPresentable presentableContext];
-[BKUIHostedJindoPresentable presentableDidDisappearAsBanner:withReason:];
-[BKUIHostedJindoPresentable height];
-[BKUIHostedJindoPresentable setPreferredLayoutMode:];
-[BKUIHostedJindoPresentable presentableWillNotAppearAsBanner:withReason:];
-[BKUIHostedJindoPresentable presentableWillDisappearAsBanner:withReason:];
-[BKUIHostedJindoPresentable centerYAnchor];
-[BKUIHostedJindoPresentable systemApertureElement];
-[BKUIHostedJindoPresentable revoke];
-[BKUIHostedJindoPresentable systemApertureElementProvider];
-[BKUIHostedJindoPresentable providesHostedContent];
-[BKUIHostedJindoPresentable setLayoutDescription:];
-[BKUIHostedJindoPresentable enrollView];
-[BKUIHostedJindoPresentable initWithCustomLayout:enrollView:destination:];
-[BKUIHostedJindoPresentable setCenterYAnchor:];
-[BKUIHostedJindoPresentable setEnrollView:];
-[BKUIHostedJindoPresentable userInfoForPosting];
```
