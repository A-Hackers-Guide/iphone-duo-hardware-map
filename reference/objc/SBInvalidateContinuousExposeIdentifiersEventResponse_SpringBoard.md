# `SBInvalidateContinuousExposeIdentifiersEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 3 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _animated;
@"SBAppLayout" _transitioningFromAppLayout;
@"SBAppLayout" _transitioningToAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_transitioningFromAppLayout) transitioningFromAppLayout;
@property (T@"SBAppLayout",R,N,V_transitioningToAppLayout) transitioningToAppLayout;
@property (TB,R,N,V_animated) animated;
```

## Instance methods

```
-[SBInvalidateContinuousExposeIdentifiersEventResponse transitioningToAppLayout];
-[SBInvalidateContinuousExposeIdentifiersEventResponse animated];
-[SBInvalidateContinuousExposeIdentifiersEventResponse transitioningFromAppLayout];
-[SBInvalidateContinuousExposeIdentifiersEventResponse type];
-[SBInvalidateContinuousExposeIdentifiersEventResponse initWithTransitioningFromAppLayout:transitioningToAppLayout:animated:];
```
