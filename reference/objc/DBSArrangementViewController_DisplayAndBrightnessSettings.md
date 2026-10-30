# `DBSArrangementViewController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSViewController`
- Protocols: `DBSArrangementLayoutViewControllerDelegate`
- 8 instance variables, 8 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBSConnectedDisplayInfo" _externalDisplayInfo;
@"SBSExternalDisplayService" _displayService;
B _wasMirrored;
@"<DBSArrangementViewControllerDelegate>" _delegate;
@"UIView" _containerView;
@"DBSArrangementLayoutViewController" _layoutController;
@"UISwitch" _mirroredSwitch;
Q _currentDisplayLocation;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"DBSArrangementLayoutViewController",&,N,V_layoutController) layoutController;
@property (T@"UISwitch",&,N,V_mirroredSwitch) mirroredSwitch;
@property (TQ,N,V_currentDisplayLocation) currentDisplayLocation;
@property (TB,N,V_wasMirrored) wasMirrored;
@property (T@"SBSConnectedDisplayInfo",&,N) externalDisplayInfo;
@property (T@"SBSExternalDisplayService",&,N) displayService;
@property (T@"<DBSArrangementViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[DBSArrangementViewController setContainerView:];
-[DBSArrangementViewController dismissViewControllerAnimated:completion:];
-[DBSArrangementViewController init];
-[DBSArrangementViewController dealloc];
-[DBSArrangementViewController layoutController];
-[DBSArrangementViewController containerView];
-[DBSArrangementViewController setDelegate:];
-[DBSArrangementViewController loadView];
-[DBSArrangementViewController delegate];
-[DBSArrangementViewController preferredContentSize];
-[DBSArrangementViewController setLayoutController:];
-[DBSArrangementViewController cancelPressed];
-[DBSArrangementViewController setDisplayService:];
-[DBSArrangementViewController nativeDisplayLocationDidChange:];
-[DBSArrangementViewController setWasMirrored:];
-[DBSArrangementViewController currentDisplayLocation];
-[DBSArrangementViewController displayLayoutMonitorDidUpdateLayout:];
-[DBSArrangementViewController displayService];
-[DBSArrangementViewController externalDisplayInfo];
-[DBSArrangementViewController externalDisplayName];
-[DBSArrangementViewController externalDisplaySize];
-[DBSArrangementViewController mirroredSwitch];
-[DBSArrangementViewController mirroredToggled:];
-[DBSArrangementViewController nativeDisplayImageWithWidth:];
-[DBSArrangementViewController nativeDisplayName];
-[DBSArrangementViewController nativeDisplaySize];
-[DBSArrangementViewController setCurrentDisplayLocation:];
-[DBSArrangementViewController setExternalDisplayInfo:];
-[DBSArrangementViewController setMirroredSwitch:];
-[DBSArrangementViewController setPressed];
-[DBSArrangementViewController updateComponentsWithConnectedDispalyInfo:];
-[DBSArrangementViewController updateSetButtonEnablement];
-[DBSArrangementViewController wasMirrored];
```
