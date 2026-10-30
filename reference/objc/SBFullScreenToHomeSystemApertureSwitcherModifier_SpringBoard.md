# `SBFullScreenToHomeSystemApertureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 18 instance variables, 0 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBCoplanarSwitcherModifier" _coplanarModifier;
@"SBFullScreenToHomeIconZoomSwitcherModifier" _zoomModifier;
Q _direction;
@"NSUUID" _suppressionIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _expandedCardFrame;
{CGPoint="x"d"y"d} _expandedCardCenter;
{CGPoint="x"d"y"d} _liftOffCardVelocity;
d _initialCardScale;
{CGPoint="x"d"y"d} _cachedTrajectoryStartPosition;
{CGPoint="x"d"y"d} _cachedTrajectoryStartVelocity;
{CGPoint="x"d"y"d} _cachedSwoopTarget;
B _showShadow;
B _bounced;
B _tucked;
B _jindoIntersectsIntialCardFrame;
B _shouldClipRegionAboveSystemAperture;
B _unblurred;
```

## Instance methods

```
-[SBFullScreenToHomeSystemApertureSwitcherModifier scaleForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier rotationAngleForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFullScreenToHomeSystemApertureSwitcherModifier meshTransformForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier repositionProgressNotificationsForLayoutRole:inAppLayout:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier didMoveToParentModifier:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier systemApertureTransitioningAppLayouts];
-[SBFullScreenToHomeSystemApertureSwitcherModifier cornerRadiiForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier rootContentViewMaskRect];
-[SBFullScreenToHomeSystemApertureSwitcherModifier systemApertureRequiresHeavyShadowForTransition];
-[SBFullScreenToHomeSystemApertureSwitcherModifier animationAttributesForLayoutElement:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier expandedSourcePositionForSystemApertureTransition];
-[SBFullScreenToHomeSystemApertureSwitcherModifier initWithTransitionID:zoomModifier:appLayout:direction:expandedCardFrame:cardScale:cardVelocity:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier rootContentViewMaskPath];
-[SBFullScreenToHomeSystemApertureSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBFullScreenToHomeSystemApertureSwitcherModifier topMostLayoutElements];
-[SBFullScreenToHomeSystemApertureSwitcherModifier isSwitcherWindowVisible];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _jindoZoomUpOriginCenter];
-[SBFullScreenToHomeSystemApertureSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFullScreenToHomeSystemApertureSwitcherModifier visibleAppLayouts];
-[SBFullScreenToHomeSystemApertureSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _getCurrentTrajectoryStart:velocity:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier transitionDidEnd];
-[SBFullScreenToHomeSystemApertureSwitcherModifier frameForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier transitionWillBegin];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _shouldApplyEffectsToIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier completesWhenChildrenComplete];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _clippingBezierPathInPaddedContainer:aroundJindoCenter:towardReferencePoint:favorTowardReference:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _collapsedTransitionTargetForZoomDown:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _tuckInAtEndMeshForNormalizedXDelta:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier handleRepositionProgressEvent:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _isIndexZoomAppLayout:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _expandMeshForIndex:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _slidThroughPointAlongJindoCenterlineForJindoFrame:phase1Equilibrium:startPosition:startVelocity:params:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _systemApertureSettings];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _swoopTrajectoryCollapsedTargetInFrame:];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _blurItemContainerParameters];
-[SBFullScreenToHomeSystemApertureSwitcherModifier rootContentViewBlurRadius];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _isEffectivelyHome];
-[SBFullScreenToHomeSystemApertureSwitcherModifier _collapseMeshForNormalizedXDelta:];
```
