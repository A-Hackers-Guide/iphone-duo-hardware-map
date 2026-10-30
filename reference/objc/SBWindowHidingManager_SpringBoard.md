# `SBWindowHidingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`
- 7 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIWindowScene" _windowScene;
@"NSMapTable" _windowStateMap;
@"NSMapTable" _hidingContextMap;
@"FBScene" _keyboardScene;
@"<BSInvalidatable>" _keyboardSceneObserverToken;
{SBWindowLevelRange_struct="start"d"end"d} _hideRange;
@"<UIScenePresenter>" _keyboardPresenter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowHidingManager scene:didUpdateSettings:];
-[SBWindowHidingManager dealloc];
-[SBWindowHidingManager initWithWindowScene:];
-[SBWindowHidingManager dumpHidingState];
-[SBWindowHidingManager _captureWindow:];
-[SBWindowHidingManager _releaseWindow:];
-[SBWindowHidingManager _adjustWindowsForActiveHideRange];
-[SBWindowHidingManager _isHidingWindowLevel:];
-[SBWindowHidingManager _isHidingWindows];
-[SBWindowHidingManager _recomputeHideRangeAndAdjustWindows];
-[SBWindowHidingManager _takeNoteOfWindow:onScene:];
-[SBWindowHidingManager _window:willAttachToScene:];
-[SBWindowHidingManager _window:willDetachFromScene:];
-[SBWindowHidingManager dumpKnownWindows];
-[SBWindowHidingManager setAlpha:forWindow:];
-[SBWindowHidingManager startHidingWindowsExclusivelyFromLevel:toLevel:forContext:reason:];
-[SBWindowHidingManager stopHidingWindowsForContext:];
```
