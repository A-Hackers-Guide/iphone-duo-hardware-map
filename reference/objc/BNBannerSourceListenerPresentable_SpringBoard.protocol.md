# `BNBannerSourceListenerPresentable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`, `BNPresentable`, `BNPresentableUniquelyIdentifying`, `BNPresentableObservable`
- 0 instance variables, 6 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"<BNPresentable>",R,N) presentable;
@property (TB,R,N,GisReady) ready;
@property (Ti,R,N) bannerAppearState;
@property (T@"<BNBannerSourceListenerPresentableDelegate>",W,N) delegate;
@property (TB,?,R,N,GisContentHosted) contentHosted;
@property (T@"FBScene",?,R,N) scene;
```

## Instance methods

```
-[BNBannerSourceListenerPresentable isReady];
-[BNBannerSourceListenerPresentable bannerAppearState];
-[BNBannerSourceListenerPresentable setDelegate:];
-[BNBannerSourceListenerPresentable presentable];
-[BNBannerSourceListenerPresentable delegate];
-[BNBannerSourceListenerPresentable handleTemplateContentEvent:];
-[BNBannerSourceListenerPresentable initWithPresentable:];
-[BNBannerSourceListenerPresentable initWithSpecification:serviceDomain:readyCompletion:];
-[BNBannerSourceListenerPresentable makeReadyIfPossible];
-[BNBannerSourceListenerPresentable scene];
-[BNBannerSourceListenerPresentable isContentHosted];
-[BNBannerSourceListenerPresentable initWithWithPresentable:];
-[BNBannerSourceListenerPresentable initWithWithSpecification:serviceDomain:readyCompletion:];
```
