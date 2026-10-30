# `SBSystemActionSimplePreviewPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBannerBasePresentableViewController`
- Protocols: `SBBannerManagerPresentable`, `SBControlSystemActionObserver`
- 4 instance variables, 17 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"PLPillView" _pillView;
B _popped;
@"SBSystemAction" _systemAction;
@"SBBannerCustomTransitioningDelegate" _customTransitioningDelegate;
```

## Properties

```
@property (T@"SBBannerCustomTransitioningDelegate",&,N,V_customTransitioningDelegate) customTransitioningDelegate;
@property (T@"SBSystemAction",R,N,V_systemAction) systemAction;
@property (TB,N,GisPopped,V_popped) popped;
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N) requestIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemActionSimplePreviewPresentableViewController requesterIdentifier];
```

## Instance methods

```
-[SBSystemActionSimplePreviewPresentableViewController requestIdentifier];
-[SBSystemActionSimplePreviewPresentableViewController viewDidLoad];
-[SBSystemActionSimplePreviewPresentableViewController requesterIdentifier];
-[SBSystemActionSimplePreviewPresentableViewController shouldAcquireWindowLevelAssertion];
-[SBSystemActionSimplePreviewPresentableViewController initWithSystemAction:];
-[SBSystemActionSimplePreviewPresentableViewController systemAction];
-[SBSystemActionSimplePreviewPresentableViewController setCustomTransitioningDelegate:];
-[SBSystemActionSimplePreviewPresentableViewController _leadingView];
-[SBSystemActionSimplePreviewPresentableViewController _previewPrimaryText];
-[SBSystemActionSimplePreviewPresentableViewController _previewSecondaryText];
-[SBSystemActionSimplePreviewPresentableViewController _previewSecondaryTextColor];
-[SBSystemActionSimplePreviewPresentableViewController _updatePillViewContentItems];
-[SBSystemActionSimplePreviewPresentableViewController controlSystemAction:propertiesDidChange:];
-[SBSystemActionSimplePreviewPresentableViewController customTransitioningDelegate];
-[SBSystemActionSimplePreviewPresentableViewController isPopped];
-[SBSystemActionSimplePreviewPresentableViewController setPopped:];
```
