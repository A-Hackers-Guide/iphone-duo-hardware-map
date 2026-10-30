# `SBLockScreenPlugin`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessObserver`, `SBLockScreenPluginAgent`, `SBLockScreenPluginController`
- 11 instance variables, 21 properties, 45 instance methods, 2 class methods

## Instance variables

```
@"BSPluginBundle" _bundle;
@"NSString" _bundleName;
@"FBProcess" _process;
@"<SBLockScreenPluginController>" _controller;
@"<SBLockScreenPluginAgent>" _agent;
@"SBLockScreenPluginAppearanceContext" _appearance;
@"NSMutableArray" _lifecycleObservers;
@"SBLockOverlayContext" _overlay;
@? _auxiliaryActivationAnimationBlock;
@? _auxiliaryDeactivationAnimationBlock;
@"<SBLockScreenPluginDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLockScreenPluginDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_bundleName) name;
@property (T@"<SBLockScreenPluginController>",R,N,V_controller) controller;
@property (T@"UIViewController<SBLockScreenPluginViewController>",R,N) viewController;
@property (T@"SBLockScreenPluginAppearanceContext",R,N) appearance;
@property (T@"SBLockScreenPluginAction",R,N) unlockAction;
@property (T@"CSAppearance",R,N) coverSheetAppearance;
@property (T@"CSBehavior",R,N) coverSheetBehavior;
@property (T@"SBLockOverlayContext",&,N,V_overlay) overlay;
@property (T@?,C,N,V_auxiliaryActivationAnimationBlock) auxiliaryActivationAnimationBlock;
@property (T@?,C,N,V_auxiliaryDeactivationAnimationBlock) auxiliaryDeactivationAnimationBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBLockScreenPluginAgent>",W,N,V_agent) pluginAgent;
@property (Tq,R,N) pluginPriority;
@property (T@"UIViewController<SBLockScreenPluginViewController>",R,N) pluginViewController;
@property (T@"<SBLockScreenPluginAppearance>",R,N) pluginAppearance;
@property (T@"SBLockScreenPluginAction",?,R,&,N) pluginUnlockAction;
@property (T@"_UILegibilitySettings",?,&,N) legibilitySettings;
```

## Class methods

```
+[SBLockScreenPlugin _pluginBundleForPluginWithName:];
+[SBLockScreenPlugin pluginWithName:activationContext:];
```

## Instance methods

```
-[SBLockScreenPlugin setOverlay:];
-[SBLockScreenPlugin controller];
-[SBLockScreenPlugin succinctDescriptionBuilder];
-[SBLockScreenPlugin dealloc];
-[SBLockScreenPlugin descriptionWithMultilinePrefix:];
-[SBLockScreenPlugin viewController];
-[SBLockScreenPlugin succinctDescription];
-[SBLockScreenPlugin setDelegate:];
-[SBLockScreenPlugin processDidExit:];
-[SBLockScreenPlugin overlay];
-[SBLockScreenPlugin delegate];
-[SBLockScreenPlugin description];
-[SBLockScreenPlugin appearance];
-[SBLockScreenPlugin name];
-[SBLockScreenPlugin descriptionBuilderWithMultilinePrefix:];
-[SBLockScreenPlugin pluginViewController];
-[SBLockScreenPlugin _updateAppearance:];
-[SBLockScreenPlugin unlockAction];
-[SBLockScreenPlugin overrideForElement:];
-[SBLockScreenPlugin pluginDidDeactivateWithContext:];
-[SBLockScreenPlugin setPluginAgent:];
-[SBLockScreenPlugin activatePluginController:];
-[SBLockScreenPlugin addLifecycleObserver:];
-[SBLockScreenPlugin auxiliaryActivationAnimationBlock];
-[SBLockScreenPlugin auxiliaryDeactivationAnimationBlock];
-[SBLockScreenPlugin coverSheetAppearance];
-[SBLockScreenPlugin coverSheetBehavior];
-[SBLockScreenPlugin deactivatePluginController:];
-[SBLockScreenPlugin enumerateLifecycleObserversUsingBlock:];
-[SBLockScreenPlugin handleDashBoardEvent:];
-[SBLockScreenPlugin hidesLockScreenComplications];
-[SBLockScreenPlugin initWithBundle:activationContext:];
-[SBLockScreenPlugin isCapabilityRestricted:];
-[SBLockScreenPlugin isElementHidden:];
-[SBLockScreenPlugin pluginAgent];
-[SBLockScreenPlugin pluginAppearance];
-[SBLockScreenPlugin pluginController:sendAction:];
-[SBLockScreenPlugin pluginController:updateAppearance:];
-[SBLockScreenPlugin pluginHandleEvent:];
-[SBLockScreenPlugin pluginPriority];
-[SBLockScreenPlugin pluginUnlockAction];
-[SBLockScreenPlugin pluginWillActivateWithContext:];
-[SBLockScreenPlugin removeLifecycleObserver:];
-[SBLockScreenPlugin setAuxiliaryActivationAnimationBlock:];
-[SBLockScreenPlugin setAuxiliaryDeactivationAnimationBlock:];
```
