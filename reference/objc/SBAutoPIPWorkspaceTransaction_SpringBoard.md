# `SBAutoPIPWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspaceTransaction`
- 8 instance variables, 2 properties, 9 instance methods, 7 class methods

## Instance variables

```
i _pidToPIP;
q _inferredTransitionStyle;
@"SBPIPControllerCoordinator" _pipCoordinator;
@"SBPIPController" _pipController;
@"NSString" _reason;
B _startPictureInPictureDidComplete;
q _transitionStyle;
@"SBApplicationSceneEntity" _entityToPIP;
```

## Properties

```
@property (T@"SBApplicationSceneEntity",R,C,N,V_entityToPIP) entityToPIP;
@property (Tq,N,V_transitionStyle) transitionStyle;
```

## Class methods

```
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:tetheringMode:reason:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:foundEntity:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:foundEntity:tetheringMode:transitionStyle:reason:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:foundEntity:transitionStyle:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:reason:];
+[SBAutoPIPWorkspaceTransaction shouldAutoPIPEnteringBackgroundForRequest:transitionStyle:];
```

## Instance methods

```
-[SBAutoPIPWorkspaceTransaction _canBeInterrupted];
-[SBAutoPIPWorkspaceTransaction _didComplete];
-[SBAutoPIPWorkspaceTransaction _begin];
-[SBAutoPIPWorkspaceTransaction _customizedDescriptionProperties];
-[SBAutoPIPWorkspaceTransaction transitionStyle];
-[SBAutoPIPWorkspaceTransaction initWithTransitionRequest:];
-[SBAutoPIPWorkspaceTransaction setTransitionStyle:];
-[SBAutoPIPWorkspaceTransaction entityToPIP];
-[SBAutoPIPWorkspaceTransaction initWithTransitionRequest:includeActiveAppEntity:reason:];
```
