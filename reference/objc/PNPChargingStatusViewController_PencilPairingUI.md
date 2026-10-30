# `PNPChargingStatusViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PNPPlatterViewController`, `PNPDeviceStateConfigurable`, `PNPViewController`
- 4 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"PNPPlatterTransitioningDelegate" _platterTransitioningDelegate;
@"PNPChargingStatusView" _chargingStatusView;
@"<PNPPlatterViewControllerPlatterDelegate>" platterDelegate;
@"<PNPViewControllerAppearanceDelegate>" appearanceDelegate;
```

## Properties

```
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
-[PNPChargingStatusViewController deviceState];
-[PNPChargingStatusViewController viewDidLoad];
-[PNPChargingStatusViewController initWithNibName:bundle:];
-[PNPChargingStatusViewController setDeviceState:];
-[PNPChargingStatusViewController viewDidAppear:];
-[PNPChargingStatusViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[PNPChargingStatusViewController loadView];
-[PNPChargingStatusViewController setAppearanceDelegate:];
-[PNPChargingStatusViewController viewDidDisappear:];
-[PNPChargingStatusViewController preferredContentSize];
-[PNPChargingStatusViewController appearanceDelegate];
-[PNPChargingStatusViewController platterDelegate];
-[PNPChargingStatusViewController setPlatterDelegate:];
-[PNPChargingStatusViewController _configureAutoDismiss];
-[PNPChargingStatusViewController _platterContainerView];
-[PNPChargingStatusViewController preferredEdge];
```
