# `SBNubView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- Protocols: `SBDeviceApplicationSceneHandleObserver`
- 4 instance variables, 7 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"UIApplicationSceneClientSettingsDiffInspector" _applicationSceneClientSettingsDiffInspector;
@"UIView" _nubView;
B _highlighted;
@"SBDeviceApplicationSceneHandle" _deviceApplicationSceneHandle;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_deviceApplicationSceneHandle) deviceApplicationSceneHandle;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (T@"UIView",R,N) contentView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBNubView contentHeight];
+[SBNubView height];
+[SBNubView hitTestPadding];
+[SBNubView hitTestWidth];
```

## Instance methods

```
-[SBNubView sceneHandle:clientConnectedForScene:];
-[SBNubView sceneHandle:didUpdateClientSettings:];
-[SBNubView intrinsicContentSize];
-[SBNubView isHighlighted];
-[SBNubView dealloc];
-[SBNubView initWithNibName:bundle:];
-[SBNubView setHighlighted:];
-[SBNubView contentView];
-[SBNubView initWithCoder:];
-[SBNubView traitCollectionDidChange:];
-[SBNubView _updateNubViewBackgroundColor];
-[SBNubView _updateNubViewOverrideUserInterfaceStyleAndBackgroundColor];
-[SBNubView deviceApplicationSceneHandle];
-[SBNubView initWithDeviceApplicationSceneHandle:];
```
