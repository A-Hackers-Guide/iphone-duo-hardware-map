# `SBRestoreDesktopSpaceWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 2 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppLayout" _launchingOverDesktopSpaceAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_launchingOverDesktopSpaceAppLayout) launchingOverDesktopSpaceAppLayout;
```

## Instance methods

```
-[SBRestoreDesktopSpaceWindowingModifier transitionWillBegin:];
-[SBRestoreDesktopSpaceWindowingModifier frameForItem:];
-[SBRestoreDesktopSpaceWindowingModifier launchingOverDesktopSpaceAppLayout];
-[SBRestoreDesktopSpaceWindowingModifier setLaunchingOverDesktopSpaceAppLayout:];
-[SBRestoreDesktopSpaceWindowingModifier shouldInterruptForActivity:];
-[SBRestoreDesktopSpaceWindowingModifier transitionDidComplete:];
```
