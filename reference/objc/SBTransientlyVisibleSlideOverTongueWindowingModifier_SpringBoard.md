# `SBTransientlyVisibleSlideOverTongueWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 5 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _tonguePresentationReason;
B _didCollapseSlideOverTongue;
B _hasBegunEdgeProtect;
@"NSString" _finishedReason;
@"NSUUID" _transitionIDForStashingItem;
```

## Instance methods

```
-[SBTransientlyVisibleSlideOverTongueWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier isSwitcherWindowVisible];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier transitionWillBegin:];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier wantsSlideOverTongue];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier timerFired:];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier slideOverTongueState];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier willBegin];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier _collapseAndPrepareForDismiss];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier _collapseSettlingDuration];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier didEdgeProtectSlideOverTongue:];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier gestureWillBegin:];
-[SBTransientlyVisibleSlideOverTongueWindowingModifier initWithTonguePresentationReason:];
```
