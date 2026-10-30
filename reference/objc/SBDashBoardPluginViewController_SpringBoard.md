# `SBDashBoardPluginViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `SBLockScreenPluginDelegate`
- 1 instance variables, 5 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"SBLockScreenPlugin" _plugin;
```

## Properties

```
@property (T@"SBLockScreenPlugin",R,N,V_plugin) plugin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDashBoardPluginViewController viewClass];
```

## Instance methods

```
-[SBDashBoardPluginViewController presentationType];
-[SBDashBoardPluginViewController _updateLegibility];
-[SBDashBoardPluginViewController updateForPresentation:];
-[SBDashBoardPluginViewController handleEvent:];
-[SBDashBoardPluginViewController performCustomTransitionToVisible:withAnimationSettings:completion:];
-[SBDashBoardPluginViewController aggregateBehavior:];
-[SBDashBoardPluginViewController succinctDescriptionBuilder];
-[SBDashBoardPluginViewController presentationPriority];
-[SBDashBoardPluginViewController presentationStyle];
-[SBDashBoardPluginViewController viewDidLoad];
-[SBDashBoardPluginViewController _newDisplayLayoutElement];
-[SBDashBoardPluginViewController presentationTransition];
-[SBDashBoardPluginViewController viewWillAppear:];
-[SBDashBoardPluginViewController view];
-[SBDashBoardPluginViewController plugin];
-[SBDashBoardPluginViewController aggregateAppearance:];
-[SBDashBoardPluginViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBDashBoardPluginViewController viewDidDisappear:];
-[SBDashBoardPluginViewController coverSheetIdentifier];
-[SBDashBoardPluginViewController viewControllerForCoordinatingStateWithCoverSheetViewController:];
-[SBDashBoardPluginViewController willTransitionToPresented:];
-[SBDashBoardPluginViewController _presentationPriority];
-[SBDashBoardPluginViewController initWithLockScreenPlugin:];
-[SBDashBoardPluginViewController pluginAppearanceDidChange:];
```
