# `SBResizeGrabberHintingSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 2 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayItem" _displayItem;
Q _corners;
```

## Properties

```
@property (T@"SBDisplayItem",R,N,V_displayItem) displayItem;
@property (TQ,R,N,V_corners) corners;
@property (T@"NSString",R,N) identifier;
```

## Instance methods

```
-[SBResizeGrabberHintingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:];
-[SBResizeGrabberHintingSwitcherModifier identifier];
-[SBResizeGrabberHintingSwitcherModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBResizeGrabberHintingSwitcherModifier handleTimerEvent:];
-[SBResizeGrabberHintingSwitcherModifier displayItem];
-[SBResizeGrabberHintingSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:];
-[SBResizeGrabberHintingSwitcherModifier description];
-[SBResizeGrabberHintingSwitcherModifier corners];
-[SBResizeGrabberHintingSwitcherModifier _isHandlingEvent:];
-[SBResizeGrabberHintingSwitcherModifier initWithDisplayItem:corners:];
```
