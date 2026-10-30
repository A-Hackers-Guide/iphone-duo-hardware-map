# `SBScrollSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _userInitiated;
Q _phase;
{CGPoint="x"d"y"d} _contentOffset;
```

## Properties

```
@property (T{CGPoint=dd},N,V_contentOffset) contentOffset;
@property (TQ,N,V_phase) phase;
@property (TB,N,GisUserInitiated,V_userInitiated) userInitiated;
```

## Instance methods

```
-[SBScrollSwitcherModifierEvent contentOffset];
-[SBScrollSwitcherModifierEvent phase];
-[SBScrollSwitcherModifierEvent setContentOffset:];
-[SBScrollSwitcherModifierEvent setUserInitiated:];
-[SBScrollSwitcherModifierEvent type];
-[SBScrollSwitcherModifierEvent isUserInitiated];
-[SBScrollSwitcherModifierEvent setPhase:];
-[SBScrollSwitcherModifierEvent copyWithZone:];
-[SBScrollSwitcherModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBScrollSwitcherModifierEvent initWithContentOffset:phase:userInitiated:];
```
