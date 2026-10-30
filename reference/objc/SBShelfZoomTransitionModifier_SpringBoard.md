# `SBShelfZoomTransitionModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 0 properties, 28 instance methods, 0 class methods

## Instance variables

```
Q _direction;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
@"SBSwitcherShelf" _shelf;
@"SBAppLayout" _centerWindowAppLayout;
@"SBAppLayout" _fullScreenSpaceAppLayout;
@"SBAppLayout" _centerWindowBeingReplacedAppLayout;
```

## Instance methods

```
-[SBShelfZoomTransitionModifier handleGestureEvent:];
-[SBShelfZoomTransitionModifier scaleForIndex:];
-[SBShelfZoomTransitionModifier titleOpacityForIndex:];
-[SBShelfZoomTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBShelfZoomTransitionModifier cornerRadiiForIndex:];
-[SBShelfZoomTransitionModifier animationAttributesForLayoutElement:];
-[SBShelfZoomTransitionModifier topMostLayoutElements];
-[SBShelfZoomTransitionModifier titleAndIconOpacityForIndex:];
-[SBShelfZoomTransitionModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBShelfZoomTransitionModifier presentationAttributesForShelf:];
-[SBShelfZoomTransitionModifier visibleAppLayouts];
-[SBShelfZoomTransitionModifier perspectiveAngleForIndex:];
-[SBShelfZoomTransitionModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBShelfZoomTransitionModifier transitionDidEnd];
-[SBShelfZoomTransitionModifier shadowOpacityForLayoutRole:atIndex:];
-[SBShelfZoomTransitionModifier scaleForLayoutRole:inAppLayout:];
-[SBShelfZoomTransitionModifier headerStyleForIndex:];
-[SBShelfZoomTransitionModifier frameForIndex:];
-[SBShelfZoomTransitionModifier transitionWillBegin];
-[SBShelfZoomTransitionModifier hiddenAppLayoutsInShelf:];
-[SBShelfZoomTransitionModifier asyncRenderingAttributesForAppLayout:];
-[SBShelfZoomTransitionModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBShelfZoomTransitionModifier contentPageViewScaleForAppLayout:withScale:];
-[SBShelfZoomTransitionModifier descriptionBuilderWithMultilinePrefix:];
-[SBShelfZoomTransitionModifier initWithTransitionID:direction:fromAppLayout:toAppLayout:shelf:];
-[SBShelfZoomTransitionModifier _frameForCenterWindowInShelf];
-[SBShelfZoomTransitionModifier _isEffectivelyInShelf];
-[SBShelfZoomTransitionModifier _shouldDimLayoutRole:inAppLayout:forZoomDirection:];
```
