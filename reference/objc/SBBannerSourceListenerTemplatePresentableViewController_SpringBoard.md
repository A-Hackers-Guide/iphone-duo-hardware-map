# `SBBannerSourceListenerTemplatePresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BNBannerSourceListenerPresentableViewController`
- Protocols: `SBBannerManagerPresentable`, `BNBannerSourceListenerTemplatePresentable`
- 3 instance variables, 23 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<BNTemplateContentProvidingSpecifying>" _templateContentProvidingSpecification;
@"PLPillView" _pillView;
@"SBBannerCustomTransitioningDelegate" _customTransitioningDelegate;
```

## Properties

```
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
@property (TB,R,N,GisTemplateContent) templateContent;
@property (T@"<BNPresentable>",R,N) presentable;
@property (TB,R,N,GisReady) ready;
@property (Ti,R,N) bannerAppearState;
@property (T@"<BNBannerSourceListenerPresentableDelegate>",W,N) delegate;
@property (TB,?,R,N,GisContentHosted) contentHosted;
@property (T@"FBScene",?,R,N) scene;
@property (T@"NSUUID",?,R,C,N) uniquePresentableIdentifier;
@property (T@"NSUUID",?,R,C,N) uniqueIdentifier;
```

## Instance methods

```
-[SBBannerSourceListenerTemplatePresentableViewController bannerContentOutsets];
-[SBBannerSourceListenerTemplatePresentableViewController trailingTemplateViewProvider];
-[SBBannerSourceListenerTemplatePresentableViewController viewDidLoad];
-[SBBannerSourceListenerTemplatePresentableViewController providesTemplateContent];
-[SBBannerSourceListenerTemplatePresentableViewController leadingTemplateViewProvider];
-[SBBannerSourceListenerTemplatePresentableViewController primaryTemplateItemProvider];
-[SBBannerSourceListenerTemplatePresentableViewController viewWillLayoutSubviews];
-[SBBannerSourceListenerTemplatePresentableViewController shouldAcquireWindowLevelAssertion];
-[SBBannerSourceListenerTemplatePresentableViewController secondaryTemplateItemProvider];
-[SBBannerSourceListenerTemplatePresentableViewController userInterfaceStyleOverride];
-[SBBannerSourceListenerTemplatePresentableViewController initWithPresentable:];
-[SBBannerSourceListenerTemplatePresentableViewController initWithSpecification:serviceDomain:readyCompletion:];
-[SBBannerSourceListenerTemplatePresentableViewController _handleButtonPrimaryAction:forEvent:];
-[SBBannerSourceListenerTemplatePresentableViewController _handleTapOnPillView:];
-[SBBannerSourceListenerTemplatePresentableViewController _pillView];
-[SBBannerSourceListenerTemplatePresentableViewController _templateContentProvider];
-[SBBannerSourceListenerTemplatePresentableViewController isTemplateContent];
```
