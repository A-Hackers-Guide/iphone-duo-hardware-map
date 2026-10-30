# `SBShelfSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 9 instance variables, 1 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _layoutRole;
@"SBAppLayout" _activeFullScreenAppLayout;
Q _contentOptions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _presentationTargetFrame;
@"SBAppLayout" _presentedFromAppLayout;
Q _animationStyle;
B _isPendingDismissal;
B _isPendingDismissalFromGesture;
@"SBSwitcherShelf" _shelf;
```

## Properties

```
@property (T@"SBSwitcherShelf",R,N,V_shelf) shelf;
```

## Class methods

```
+[SBShelfSwitcherModifier contentOptionsForTransitionEvent:context:];
```

## Instance methods

```
-[SBShelfSwitcherModifier handleGestureEvent:];
-[SBShelfSwitcherModifier frameForShelf:];
-[SBShelfSwitcherModifier visibleShelves];
-[SBShelfSwitcherModifier topMostLayoutElements];
-[SBShelfSwitcherModifier presentationAttributesForShelf:];
-[SBShelfSwitcherModifier handleTransitionEvent:];
-[SBShelfSwitcherModifier containerLeafAppLayoutForShelf:];
-[SBShelfSwitcherModifier ignoredDisplayItemsForShelf:];
-[SBShelfSwitcherModifier homeAffordanceLayoutElementToPortalIntoShelf:];
-[SBShelfSwitcherModifier focusedAppLayoutForShelf:];
-[SBShelfSwitcherModifier _responseForDismissingIfNeededGestureInitiated:];
-[SBShelfSwitcherModifier initWithShelf:contentOptions:activeFullScreenAppLayout:presentationTargetFrame:presentedFromAppLayout:];
-[SBShelfSwitcherModifier shelf];
```
