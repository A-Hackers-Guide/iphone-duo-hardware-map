# `PNPLockScreenViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PNPPlatterViewController`, `PNPDeviceStateConfigurable`, `PNPViewController`
- 4 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"PNPPlatterTransitioningDelegate" _platterTransitioningDelegate;
@"<PNPPlatterViewControllerPlatterDelegate>" platterDelegate;
@"<PNPViewControllerAppearanceDelegate>" appearanceDelegate;
@"UIView<PNPDeviceStateConfigurable>" _pillView;
```

## Properties

```
@property (T@"UIView<PNPDeviceStateConfigurable>",&,N,V_pillView) pillView;
@property (TQ,R,N) preferredEdge;
@property (T@"<PNPPlatterViewControllerPlatterDelegate>",W,N,VplatterDelegate) platterDelegate;
@property (Td,?,R,N) preferredCornerRadius;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<PNPViewControllerAppearanceDelegate>",W,N,VappearanceDelegate) appearanceDelegate;
```

## Instance methods

```
-[PNPLockScreenViewController pillView];
-[PNPLockScreenViewController setPillView:];
-[PNPLockScreenViewController deviceState];
-[PNPLockScreenViewController viewDidLoad];
-[PNPLockScreenViewController initWithNibName:bundle:];
-[PNPLockScreenViewController setDeviceState:];
-[PNPLockScreenViewController _canShowWhileLocked];
-[PNPLockScreenViewController viewDidAppear:];
-[PNPLockScreenViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[PNPLockScreenViewController loadView];
-[PNPLockScreenViewController setAppearanceDelegate:];
-[PNPLockScreenViewController viewDidDisappear:];
-[PNPLockScreenViewController preferredContentSize];
-[PNPLockScreenViewController appearanceDelegate];
-[PNPLockScreenViewController platterDelegate];
-[PNPLockScreenViewController setPlatterDelegate:];
-[PNPLockScreenViewController _platterContainerView];
-[PNPLockScreenViewController dismissPill];
-[PNPLockScreenViewController preferredEdge];
```
