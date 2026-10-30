# `SBHighlightSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _hoverEvent;
B _pencilHoverEvent;
q _layoutRole;
@"SBAppLayout" _appLayout;
Q _phase;
```

## Properties

```
@property (Tq,R,N,V_layoutRole) layoutRole;
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (TQ,R,N,V_phase) phase;
@property (TB,R,N,GisHoverEvent,V_hoverEvent) hoverEvent;
@property (TB,R,N,GisPencilHoverEvent,V_pencilHoverEvent) pencilHoverEvent;
```

## Instance methods

```
-[SBHighlightSwitcherModifierEvent layoutRole];
-[SBHighlightSwitcherModifierEvent phase];
-[SBHighlightSwitcherModifierEvent appLayout];
-[SBHighlightSwitcherModifierEvent type];
-[SBHighlightSwitcherModifierEvent copyWithZone:];
-[SBHighlightSwitcherModifierEvent initWithLayoutRole:inAppLayout:phase:hover:pencilHover:];
-[SBHighlightSwitcherModifierEvent isHoverEvent];
-[SBHighlightSwitcherModifierEvent isPencilHoverEvent];
```
