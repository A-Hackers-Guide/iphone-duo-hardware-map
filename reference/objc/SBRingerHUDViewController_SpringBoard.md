# `SBRingerHUDViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBBannerBasePresentableViewController`
- Protocols: `SBBannerManagerPresentable`, `SBRingerNoticeUICoordinating`
- 10 instance variables, 25 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _ringerSilent;
B _activatedForPreviewing;
B _lastEventIsAVolumeChange;
B _shouldExtendDismissalTimerUponDidAppear;
f _volume;
@"<SBRingerHUDViewControllerDelegate>" _delegate;
@"SBRingerPillView" _pillView;
d _overshoot;
@"NSTimer" _dismissalTimer;
@"SBBannerCustomTransitioningDelegate" _customTransitioningDelegate;
```

## Properties

```
@property (T@"SBRingerPillView",&,N,V_pillView) pillView;
@property (TB,N,V_lastEventIsAVolumeChange) lastEventIsAVolumeChange;
@property (Td,N,V_overshoot) overshoot;
@property (TB,N,V_shouldExtendDismissalTimerUponDidAppear) shouldExtendDismissalTimerUponDidAppear;
@property (T@"NSTimer",&,N,V_dismissalTimer) dismissalTimer;
@property (T@"SBBannerCustomTransitioningDelegate",&,N,V_customTransitioningDelegate) customTransitioningDelegate;
@property (T@"<SBRingerHUDViewControllerDelegate>",W,N,V_delegate) delegate;
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
@property (TB,N,GisRingerSilent,V_ringerSilent) ringerSilent;
@property (Tf,N,V_volume) volume;
@property (TB,R,N,GisPresented) presented;
@property (TB,R,N,GisActivatedForPreviewing,V_activatedForPreviewing) activatedForPreviewing;
```

## Instance methods

```
-[SBRingerHUDViewController pillView];
-[SBRingerHUDViewController _dismiss];
-[SBRingerHUDViewController setPillView:];
-[SBRingerHUDViewController isPresented];
-[SBRingerHUDViewController presentableDidAppearAsBanner:];
-[SBRingerHUDViewController volume];
-[SBRingerHUDViewController requestIdentifier];
-[SBRingerHUDViewController presentableBehavior];
-[SBRingerHUDViewController viewDidLoad];
-[SBRingerHUDViewController setVolume:];
-[SBRingerHUDViewController viewDidLayoutSubviews];
-[SBRingerHUDViewController requesterIdentifier];
-[SBRingerHUDViewController viewController];
-[SBRingerHUDViewController viewWillAppear:];
-[SBRingerHUDViewController _canShowWhileLocked];
-[SBRingerHUDViewController setDelegate:];
-[SBRingerHUDViewController delegate];
-[SBRingerHUDViewController shouldAcquireWindowLevelAssertion];
-[SBRingerHUDViewController dismissalTimer];
-[SBRingerHUDViewController setDismissalTimer:];
-[SBRingerHUDViewController presentableDescription];
-[SBRingerHUDViewController initWithActivatedForPreviewing:];
-[SBRingerHUDViewController setCustomTransitioningDelegate:];
-[SBRingerHUDViewController setVolume:animated:forKeyPress:];
-[SBRingerHUDViewController _layoutPillView];
-[SBRingerHUDViewController _extendDismissalTimer];
-[SBRingerHUDViewController _updateStateAnimated:invert:];
-[SBRingerHUDViewController _updateVolumeSliderAnimated:];
-[SBRingerHUDViewController buttonReleased];
-[SBRingerHUDViewController customTransitioningDelegate];
-[SBRingerHUDViewController isActivatedForPreviewing];
-[SBRingerHUDViewController isRingerSilent];
-[SBRingerHUDViewController lastEventIsAVolumeChange];
-[SBRingerHUDViewController nudgeUp:];
-[SBRingerHUDViewController overshoot];
-[SBRingerHUDViewController presentForMuteChange:];
-[SBRingerHUDViewController setLastEventIsAVolumeChange:];
-[SBRingerHUDViewController setOvershoot:];
-[SBRingerHUDViewController setRingerSilent:];
-[SBRingerHUDViewController setShouldExtendDismissalTimerUponDidAppear:];
-[SBRingerHUDViewController shouldExtendDismissalTimerUponDidAppear];
```
