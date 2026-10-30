# `SBButterflyEntityRemovalCrossblurWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 5 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _animateOpacity;
@"NSUUID" _transitionID;
@"SBAppLayout" _removalAppLayout;
@"SBWindowingModifier" _multitaskingModifier;
@"SBButterflyEntityRemovalToHomeWindowingModifier" _toHomeRemovalModifier;
```

## Instance methods

```
-[SBButterflyEntityRemovalCrossblurWindowingModifier transitionDidUpdate:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier transitionWillBegin:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier visibleItems];
-[SBButterflyEntityRemovalCrossblurWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyEntityRemovalCrossblurWindowingModifier animationAttributesForItem:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier opacityForItem:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier shouldAllowGroupOpacityForAppLayout:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier timerFired:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier topMostItems];
-[SBButterflyEntityRemovalCrossblurWindowingModifier frameForItem:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier willBegin];
-[SBButterflyEntityRemovalCrossblurWindowingModifier didComplete];
-[SBButterflyEntityRemovalCrossblurWindowingModifier initWithRemovalAppLayout:multitaskingModifier:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier shouldInterruptForActivity:];
-[SBButterflyEntityRemovalCrossblurWindowingModifier transitionDidComplete:];
```
