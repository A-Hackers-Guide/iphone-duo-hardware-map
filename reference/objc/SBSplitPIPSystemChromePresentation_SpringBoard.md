# `SBSplitPIPSystemChromePresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScenePIPManager" _pipManager;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarAssertion;
B _controlsVisible;
B _invalidated;
```

## Properties

```
@property (TB,N,GareControlsVisible) controlsVisible;
@property (TB,R,N,GisSuppressingSystemChrome) suppressingSystemChrome;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSplitPIPSystemChromePresentation dealloc];
-[SBSplitPIPSystemChromePresentation setControlsVisible:];
-[SBSplitPIPSystemChromePresentation invalidate];
-[SBSplitPIPSystemChromePresentation areControlsVisible];
-[SBSplitPIPSystemChromePresentation _initWithWindowScene:pipManager:controlsVisible:];
-[SBSplitPIPSystemChromePresentation isSuppressingSystemChrome];
```
