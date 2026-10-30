# `SBFlashlightPreviewPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBannerBasePresentableViewController`
- Protocols: `SBBannerManagerPresentable`
- 3 instance variables, 16 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"PLPillView" _pillView;
B _flashlightOn;
@"SBBannerCustomTransitioningDelegate" _customTransitioningDelegate;
```

## Properties

```
@property (T@"SBBannerCustomTransitioningDelegate",&,N,V_customTransitioningDelegate) customTransitioningDelegate;
@property (TB,N,GisFlashlightOn,V_flashlightOn) flashlightOn;
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
+[SBFlashlightPreviewPresentableViewController requesterIdentifier];
```

## Instance methods

```
-[SBFlashlightPreviewPresentableViewController requestIdentifier];
-[SBFlashlightPreviewPresentableViewController viewDidLoad];
-[SBFlashlightPreviewPresentableViewController requesterIdentifier];
-[SBFlashlightPreviewPresentableViewController shouldAcquireWindowLevelAssertion];
-[SBFlashlightPreviewPresentableViewController setFlashlightOn:];
-[SBFlashlightPreviewPresentableViewController setCustomTransitioningDelegate:];
-[SBFlashlightPreviewPresentableViewController _pillSubtitleContentItem];
-[SBFlashlightPreviewPresentableViewController _pillTitleContentItem];
-[SBFlashlightPreviewPresentableViewController customTransitioningDelegate];
-[SBFlashlightPreviewPresentableViewController initWithFlashlightOn:];
-[SBFlashlightPreviewPresentableViewController isFlashlightOn];
```
