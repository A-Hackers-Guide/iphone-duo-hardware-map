# `SBBannerBasePresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `BNPresentable`, `BNPresentableObservable`
- 2 instance variables, 15 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
B _presentableAppearingOrAppeared;
```

## Properties

```
@property (TB,N,GisPresentableAppearingOrAppeared,V_presentableAppearingOrAppeared) presentableAppearingOrAppeared;
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

## Instance methods

```
-[SBBannerBasePresentableViewController requestIdentifier];
-[SBBannerBasePresentableViewController requesterIdentifier];
-[SBBannerBasePresentableViewController viewController];
-[SBBannerBasePresentableViewController userInteractionWillBeginForBannerForPresentable:];
-[SBBannerBasePresentableViewController userInteractionDidEndForBannerForPresentable:];
-[SBBannerBasePresentableViewController presentableWillAppearAsBanner:];
-[SBBannerBasePresentableViewController _enumerateObserversRespondingToSelector:usingBlock:];
-[SBBannerBasePresentableViewController presentableWillDisappearAsBanner:withReason:];
-[SBBannerBasePresentableViewController addPresentableObserver:];
-[SBBannerBasePresentableViewController removePresentableObserver:];
-[SBBannerBasePresentableViewController isPresentableAppearingOrAppeared];
-[SBBannerBasePresentableViewController setPresentableAppearingOrAppeared:];
```
