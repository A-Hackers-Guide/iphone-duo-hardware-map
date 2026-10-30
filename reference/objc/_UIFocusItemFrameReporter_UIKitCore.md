# `_UIFocusItemFrameReporter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _focusedFrameUpdateTimer;
B _hasStagedFocusFrameUpdate;
B _enabled;
@"UIFocusSystem" _focusSystem;
```

## Properties

```
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Instance methods

```
-[_UIFocusItemFrameReporter dealloc];
-[_UIFocusItemFrameReporter isEnabled];
-[_UIFocusItemFrameReporter setEnabled:];
-[_UIFocusItemFrameReporter focusSystem];
-[_UIFocusItemFrameReporter _focusSystemEnabledStateDidChange:];
-[_UIFocusItemFrameReporter _cancelRepeatingFrameUpdate];
-[_UIFocusItemFrameReporter _globalFrameForFocusedItemInSystem:];
-[_UIFocusItemFrameReporter _rect:differsFromRect:lowerThreshold:upperThreshold:];
-[_UIFocusItemFrameReporter _reportFocusFrameForCurrentlyFocusedItem];
-[_UIFocusItemFrameReporter _reportFocusFrameUpdateForGlobalFrame:];
-[_UIFocusItemFrameReporter _scheduleRepeatingFrameUpdate];
-[_UIFocusItemFrameReporter initWithFocusSystem:];
```
