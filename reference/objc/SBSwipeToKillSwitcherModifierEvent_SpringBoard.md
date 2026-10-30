# `SBSwipeToKillSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEvent`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _dragging;
q _layoutRole;
@"SBAppLayout" _appLayout;
d _progress;
d _decelerationTargetProgress;
{CGPoint="x"d"y"d} _translation;
```

## Properties

```
@property (Tq,R,N,V_layoutRole) layoutRole;
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (Td,N,V_progress) progress;
@property (T{CGPoint=dd},N,V_translation) translation;
@property (TB,N,GisDragging,V_dragging) dragging;
@property (Td,N,V_decelerationTargetProgress) decelerationTargetProgress;
```

## Instance methods

```
-[SBSwipeToKillSwitcherModifierEvent layoutRole];
-[SBSwipeToKillSwitcherModifierEvent setProgress:];
-[SBSwipeToKillSwitcherModifierEvent appLayout];
-[SBSwipeToKillSwitcherModifierEvent setDragging:];
-[SBSwipeToKillSwitcherModifierEvent progress];
-[SBSwipeToKillSwitcherModifierEvent isDragging];
-[SBSwipeToKillSwitcherModifierEvent type];
-[SBSwipeToKillSwitcherModifierEvent setTranslation:];
-[SBSwipeToKillSwitcherModifierEvent copyWithZone:];
-[SBSwipeToKillSwitcherModifierEvent translation];
-[SBSwipeToKillSwitcherModifierEvent descriptionBuilderWithMultilinePrefix:];
-[SBSwipeToKillSwitcherModifierEvent decelerationTargetProgress];
-[SBSwipeToKillSwitcherModifierEvent initWithLayoutRole:inAppLayout:progress:translation:];
-[SBSwipeToKillSwitcherModifierEvent setDecelerationTargetProgress:];
```
