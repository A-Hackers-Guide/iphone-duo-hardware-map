# `SBDDisplayProfileManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardDisplay.framework/SpringBoardDisplay`](../userland/System__Library__PrivateFrameworks__SpringBoardDisplay.framework__SpringBoardDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneDelegate`
- 10 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
registration;
eventSources;
hardwareIdentifiersToBacklightOn;
scenes;
$__lazy_storage_$_managedDisplaysController;
$__lazy_storage_$_extendedDisplaysController;
$__lazy_storage_$_mirroredDisplaysController;
resizableDisplayProfileDescriptor;
? delegate;
startupOrientation;
```

## Properties

```
@property (T@"<SBDDisplayProfileManagerDelegate>",N,W,Vdelegate) delegate;
@property (T@"NSSet",N,R) fbScenes;
@property (T@"CAContext",N,R) rootWindowCAContext;
@property (T@"NSString",N,C) resizableDisplayUUID;
```

## Instance methods

```
-[SBDDisplayProfileManager sceneDidDeactivate:withContext:];
-[SBDDisplayProfileManager setResizableDisplayUUID:initialFrame:];
-[SBDDisplayProfileManager sceneDidInvalidate:withContext:];
-[SBDDisplayProfileManager rootWindowCAContext];
-[SBDDisplayProfileManager init];
-[SBDDisplayProfileManager start];
-[SBDDisplayProfileManager fbScenes];
-[SBDDisplayProfileManager updateBacklightState:forEmbeddedDisplayConfiguration:];
-[SBDDisplayProfileManager setDelegate:];
-[SBDDisplayProfileManager updateTransform:forDisplayConfiguration:];
-[SBDDisplayProfileManager delegate];
-[SBDDisplayProfileManager initWithStartupOrientation:];
-[SBDDisplayProfileManager resizableDisplayUUID];
-[SBDDisplayProfileManager setResizableDisplayUUID:];
```
