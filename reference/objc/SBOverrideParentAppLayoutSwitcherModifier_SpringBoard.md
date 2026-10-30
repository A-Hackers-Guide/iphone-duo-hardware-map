# `SBOverrideParentAppLayoutSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _childAppLayout;
@"SBAppLayout" _parentAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_childAppLayout) childAppLayout;
@property (T@"SBAppLayout",R,N,V_parentAppLayout) parentAppLayout;
```

## Instance methods

```
-[SBOverrideParentAppLayoutSwitcherModifier parentAppLayout];
-[SBOverrideParentAppLayoutSwitcherModifier appLayoutContainingAppLayout:];
-[SBOverrideParentAppLayoutSwitcherModifier appLayoutsContainedWithinAppLayout:];
-[SBOverrideParentAppLayoutSwitcherModifier childAppLayout];
-[SBOverrideParentAppLayoutSwitcherModifier initWithChildAppLayout:newParentAppLayout:];
```
