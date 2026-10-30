# `_UICalendarDateViewCellState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _outOfRange;
B _overhangMonth;
B _highlightsToday;
B _today;
B _selected;
B _highlighted;
B _forceEmphasizedFont;
@"UITraitCollection" _traits;
```

## Properties

```
@property (T@"UITraitCollection",R,N,V_traits) traits;
@property (TB,N,GisOutOfRange,V_outOfRange) outOfRange;
@property (TB,N,GisOverhangMonth,V_overhangMonth) overhangMonth;
@property (TB,N,V_highlightsToday) highlightsToday;
@property (TB,N,GisToday,V_today) today;
@property (TB,N,GisSelected,V_selected) selected;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TB,N,V_forceEmphasizedFont) forceEmphasizedFont;
```

## Instance methods

```
-[_UICalendarDateViewCellState initWithTraits:];
-[_UICalendarDateViewCellState setSelected:];
-[_UICalendarDateViewCellState traits];
-[_UICalendarDateViewCellState isHighlighted];
-[_UICalendarDateViewCellState setHighlightsToday:];
-[_UICalendarDateViewCellState setHighlighted:];
-[_UICalendarDateViewCellState isSelected];
-[_UICalendarDateViewCellState hash];
-[_UICalendarDateViewCellState isEqual:];
-[_UICalendarDateViewCellState highlightsToday];
-[_UICalendarDateViewCellState isOverhangMonth];
-[_UICalendarDateViewCellState isToday];
-[_UICalendarDateViewCellState forceEmphasizedFont];
-[_UICalendarDateViewCellState isOutOfRange];
-[_UICalendarDateViewCellState setForceEmphasizedFont:];
-[_UICalendarDateViewCellState setOutOfRange:];
-[_UICalendarDateViewCellState setOverhangMonth:];
-[_UICalendarDateViewCellState setToday:];
```
