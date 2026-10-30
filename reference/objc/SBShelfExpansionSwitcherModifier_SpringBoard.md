# `SBShelfExpansionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 21 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _expand;
Q _style;
{CGPoint="x"d"y"d} _target;
d _perIndexResponseIncrement;
d _dismissalScale;
@"SBFFluidBehaviorSettings" _settings;
@"SBFFluidBehaviorSettings" _ropeSettings;
d _bezierCurvePointYDeltaFromTarget;
d _bezierCurveXExponent;
d _bezierCurveYExponent;
d _bezierCurveScaleExponent;
{CGPoint="x"d"y"d} _cached_scrollViewContentOffset;
Q _cached_appLayoutsGenCount;
@"NSArray" _cached_visibleOrderedAppLayouts;
Q _topMostLayoutElements_lastAppLayoutsGenCount;
q _topMostLayoutElements_lastOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _topMostLayoutElements_lastContainerViewBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _topMostLayoutElements_lastSwitcherViewBounds;
{CGPoint="x"d"y"d} _topMostLayoutElements_lastContentOffset;
@"NSArray" _topMostLayoutElements_lastElements;
@"<SBShelfExpansionSwitcherModifierDelegate>" _animationDelegate;
```

## Properties

```
@property (T@"<SBShelfExpansionSwitcherModifierDelegate>",R,W,N,V_animationDelegate) animationDelegate;
```

## Instance methods

```
-[SBShelfExpansionSwitcherModifier scaleForIndex:];
-[SBShelfExpansionSwitcherModifier didMoveToParentModifier:];
-[SBShelfExpansionSwitcherModifier transactionCompletionOptions];
-[SBShelfExpansionSwitcherModifier animationAttributesForLayoutElement:];
-[SBShelfExpansionSwitcherModifier animatablePropertyIdentifiers];
-[SBShelfExpansionSwitcherModifier topMostLayoutElements];
-[SBShelfExpansionSwitcherModifier updateModeForAnimatableProperty:];
-[SBShelfExpansionSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBShelfExpansionSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBShelfExpansionSwitcherModifier frameForIndex:];
-[SBShelfExpansionSwitcherModifier transitionWillBegin];
-[SBShelfExpansionSwitcherModifier shouldUpdateAnimatableProperty:];
-[SBShelfExpansionSwitcherModifier isFocusEnabledForAppLayout:];
-[SBShelfExpansionSwitcherModifier shelfBackgroundBlurOpacity];
-[SBShelfExpansionSwitcherModifier settingsForAnimatableProperty:];
-[SBShelfExpansionSwitcherModifier modelValueForAnimatableProperty:currentValue:creating:];
-[SBShelfExpansionSwitcherModifier animationDelegate];
-[SBShelfExpansionSwitcherModifier shouldInterruptForRemovalEvent:];
-[SBShelfExpansionSwitcherModifier _bezierPointFromTime:start:target:];
-[SBShelfExpansionSwitcherModifier _isEffectivelyInShelf];
-[SBShelfExpansionSwitcherModifier _isMovingFromLeadingToTrailing];
-[SBShelfExpansionSwitcherModifier _presentationValueForIndex:];
-[SBShelfExpansionSwitcherModifier _visibleOrderedAppLayouts];
-[SBShelfExpansionSwitcherModifier handleAnimatablePropertyChangedEvent:];
-[SBShelfExpansionSwitcherModifier initWithTransitionID:expand:style:target:animationDelegate:];
```
