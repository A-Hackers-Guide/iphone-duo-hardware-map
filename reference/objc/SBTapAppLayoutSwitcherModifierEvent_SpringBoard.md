# `SBTapAppLayoutSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
q _layoutRole;
q _modifierFlags;
q _source;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (Tq,R,N,V_layoutRole) layoutRole;
@property (Tq,R,N,V_modifierFlags) modifierFlags;
@property (Tq,R,N,V_source) source;
```

## Instance methods

```
-[SBTapAppLayoutSwitcherModifierEvent layoutRole];
-[SBTapAppLayoutSwitcherModifierEvent appLayout];
-[SBTapAppLayoutSwitcherModifierEvent modifierFlags];
-[SBTapAppLayoutSwitcherModifierEvent type];
-[SBTapAppLayoutSwitcherModifierEvent copyWithZone:];
-[SBTapAppLayoutSwitcherModifierEvent source];
-[SBTapAppLayoutSwitcherModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBTapAppLayoutSwitcherModifierEvent initWithAppLayout:layoutRole:modifierFlags:];
-[SBTapAppLayoutSwitcherModifierEvent initWithAppLayout:layoutRole:modifierFlags:source:];
```
