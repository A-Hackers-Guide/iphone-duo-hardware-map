# `SBActivityBannerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityViewController`
- Protocols: `ACUISActivityHostViewControllerDelegate`, `MTMaterialGrouping`, `BNPresentable`, `BNPresentableObservable`
- 7 instance variables, 22 properties, 45 instance methods, 1 class methods

## Instance variables

```
@"<SBActivityBannerViewControllerDelegate>" _bannerDelegate;
@"PLPlatterView" _platterView;
@"UIView" _backgroundTintView;
@"_UIViewGlass" _glassView;
@"SBWindowSceneStatusBarSettingsAssertion" _appStatusBarSettingsAssertion;
@"NSTimer" _dismissalTimer;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"PLPlatterView",R,N,V_platterView) platterView;
@property (T@"UIView",R,N,V_backgroundTintView) backgroundTintView;
@property (T@"_UIViewGlass",R,N,V_glassView) glassView;
@property (T@"SBWindowSceneStatusBarSettingsAssertion",&,N,V_appStatusBarSettingsAssertion) appStatusBarSettingsAssertion;
@property (T@"NSTimer",&,N,V_dismissalTimer) dismissalTimer;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"<SBActivityBannerViewControllerDelegate>",W,N,V_bannerDelegate) bannerDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",C,N) materialGroupNameBase;
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
```

## Class methods

```
+[SBActivityBannerViewController requesterIdentifier];
```

## Instance methods

```
-[SBActivityBannerViewController platterView];
-[SBActivityBannerViewController _dismiss];
-[SBActivityBannerViewController isDraggingInteractionEnabled];
-[SBActivityBannerViewController userInterfaceStyleChangedForEnvironment:previousTraitCollection:];
-[SBActivityBannerViewController _layoutSubviews];
-[SBActivityBannerViewController presentableDidAppearAsBanner:];
-[SBActivityBannerViewController _updateAppStatusBarSettingsAssertion];
-[SBActivityBannerViewController requestIdentifier];
-[SBActivityBannerViewController isDraggingDismissalEnabled];
-[SBActivityBannerViewController setMaterialGroupNameBase:];
-[SBActivityBannerViewController preferredContentSizeWithPresentationSize:containerSize:];
-[SBActivityBannerViewController _backgroundTintColorForUserInterfaceStyle:];
-[SBActivityBannerViewController viewDidLoad];
-[SBActivityBannerViewController requesterIdentifier];
-[SBActivityBannerViewController viewController];
-[SBActivityBannerViewController preferredBackgroundActivitiesToSuppress];
-[SBActivityBannerViewController _canShowWhileLocked];
-[SBActivityBannerViewController userInteractionWillBeginForBannerForPresentable:];
-[SBActivityBannerViewController userInteractionDidEndForBannerForPresentable:];
-[SBActivityBannerViewController presentableWillAppearAsBanner:];
-[SBActivityBannerViewController materialGroupNameBase];
-[SBActivityBannerViewController _enumerateObserversRespondingToSelector:usingBlock:];
-[SBActivityBannerViewController viewWillLayoutSubviews];
-[SBActivityBannerViewController setObservers:];
-[SBActivityBannerViewController observers];
-[SBActivityBannerViewController presentableDidDisappearAsBanner:withReason:];
-[SBActivityBannerViewController presentableWillDisappearAsBanner:withReason:];
-[SBActivityBannerViewController glassView];
-[SBActivityBannerViewController dismissalTimer];
-[SBActivityBannerViewController setDismissalTimer:];
-[SBActivityBannerViewController activityHostViewControllerBackgroundTintColorDidChange:];
-[SBActivityBannerViewController backgroundTintView];
-[SBActivityBannerViewController addPresentableObserver:];
-[SBActivityBannerViewController removePresentableObserver:];
-[SBActivityBannerViewController _activityIdentifier];
-[SBActivityBannerViewController _extendDismissalTimer];
-[SBActivityBannerViewController _hasBackgroundTintColor];
-[SBActivityBannerViewController _isActionButtonInitiated];
-[SBActivityBannerViewController _shouldHaveBackgroundTint];
-[SBActivityBannerViewController _shouldSetDefaultBackground];
-[SBActivityBannerViewController _shouldShowSystemApertureUI];
-[SBActivityBannerViewController appStatusBarSettingsAssertion];
-[SBActivityBannerViewController bannerDelegate];
-[SBActivityBannerViewController setAppStatusBarSettingsAssertion:];
-[SBActivityBannerViewController setBannerDelegate:];
```
