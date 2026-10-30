# `SBDeviceApplicationSceneOverlayBasicWrapperViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBDeviceApplicationSceneOverlayViewControllerPrivate`, `SBDeviceApplicationCounterRotatableSceneOverlayViewDelegate`
- 5 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _contentViewController;
@"TRAParticipant" _containerTraitsParticipant;
@"SBDeviceApplicationCounterRotatableSceneOverlayView" _contentWrapperView;
B _rendersWhileLocked;
B _needsCounterRotation;
```

## Properties

```
@property (T@"UIView<SBDeviceApplicationSceneOverlayView>",R,N) overlayView;
@property (Tq,R,N) containerOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController containerOrientation];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController viewWillDisappear:];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController overlayView];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController viewWillAppear:];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController _canShowWhileLocked];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController viewDidAppear:];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController loadView];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController viewDidDisappear:];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController containerDidUpdateTraitsParticipant:];
-[SBDeviceApplicationSceneOverlayBasicWrapperViewController initWithContentViewController:rendersWhileLocked:needsCounterRotation:containerTraitsParticipant:];
```
