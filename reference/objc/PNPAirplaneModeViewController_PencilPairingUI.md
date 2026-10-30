# `PNPAirplaneModeViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PNPAirplaneModeBluetoothViewDelegate`, `PNPPlatterViewController`, `PNPDeviceStateConfigurable`, `PNPViewController`
- 5 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"PNPPlatterTransitioningDelegate" _platterTransitioningDelegate;
@"PNPAirplaneModeView" _airplaneModeView;
@"<PNPPlatterViewControllerPlatterDelegate>" platterDelegate;
@"<PNPViewControllerAppearanceDelegate>" appearanceDelegate;
@"<PNPAirplaneModeBluetoothDelegate>" _delegate;
```

## Properties

```
@property (T@"<PNPAirplaneModeBluetoothDelegate>",W,N,V_delegate) delegate;
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
-[PNPAirplaneModeViewController deviceState];
-[PNPAirplaneModeViewController viewDidLoad];
-[PNPAirplaneModeViewController initWithNibName:bundle:];
-[PNPAirplaneModeViewController setDeviceState:];
-[PNPAirplaneModeViewController setDelegate:];
-[PNPAirplaneModeViewController viewDidAppear:];
-[PNPAirplaneModeViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[PNPAirplaneModeViewController loadView];
-[PNPAirplaneModeViewController delegate];
-[PNPAirplaneModeViewController setAppearanceDelegate:];
-[PNPAirplaneModeViewController viewDidDisappear:];
-[PNPAirplaneModeViewController preferredContentSize];
-[PNPAirplaneModeViewController appearanceDelegate];
-[PNPAirplaneModeViewController platterDelegate];
-[PNPAirplaneModeViewController setPlatterDelegate:];
-[PNPAirplaneModeViewController _platterContainerView];
-[PNPAirplaneModeViewController didTapOnBluetoothButton];
-[PNPAirplaneModeViewController dismissPill];
-[PNPAirplaneModeViewController preferredEdge];
```
