# `SBStatusBarReusePool`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 6 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _statusBars;
@"UIWindow" _recycledStatusBarsContainerWindow;
@"NSMutableArray" _recycledStatusBars;
@? _newStatusBarConfigurationHandler;
Q _preferredStatusBarAutoresizingMask;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@?,C,N,V_newStatusBarConfigurationHandler) newStatusBarConfigurationHandler;
@property (TQ,R,N,V_preferredStatusBarAutoresizingMask) preferredStatusBarAutoresizingMask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStatusBarReusePool setWindowScene:];
-[SBStatusBarReusePool debugDescription];
-[SBStatusBarReusePool succinctDescriptionBuilder];
-[SBStatusBarReusePool descriptionWithMultilinePrefix:];
-[SBStatusBarReusePool initWithWindowScene:];
-[SBStatusBarReusePool succinctDescription];
-[SBStatusBarReusePool description];
-[SBStatusBarReusePool windowScene];
-[SBStatusBarReusePool descriptionBuilderWithMultilinePrefix:];
-[SBStatusBarReusePool getReusableStatusBarWithReason:];
-[SBStatusBarReusePool _resetStatusBar:clearOverrides:];
-[SBStatusBarReusePool _attachContainerToStatusBar:coordinateSpaceProvider:];
-[SBStatusBarReusePool _getReusableStatusBarWithReason:withFrame:coordinateSpaceProvider:];
-[SBStatusBarReusePool _getReusableStatusBarWithReason:withinBounds:coordinateSpaceProvider:];
-[SBStatusBarReusePool _removeStatusBarContainer:];
-[SBStatusBarReusePool _statusBarInstanceLimit];
-[SBStatusBarReusePool coordinateSpaceForHostedStatusBar:];
-[SBStatusBarReusePool enumerateStatusBars:];
-[SBStatusBarReusePool getReusableStatusBarWithReason:coordinateSpaceProvider:];
-[SBStatusBarReusePool getReusableStatusBarWithReason:withinBounds:];
-[SBStatusBarReusePool newStatusBarConfigurationHandler];
-[SBStatusBarReusePool preferredStatusBarAutoresizingMask];
-[SBStatusBarReusePool recycleStatusBar:];
-[SBStatusBarReusePool setNewStatusBarConfigurationHandler:];
-[SBStatusBarReusePool setPreferredStatusBarAutoresizingMask:];
```
