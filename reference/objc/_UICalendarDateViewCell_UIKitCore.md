# `_UICalendarDateViewCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- Protocols: `UIPointerInteractionDelegate`
- 10 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"UIPointerInteraction" _pointerInteraction;
{?="overhangMonth"b1"outOfRange"b1"isToday"b1"highlightsToday"b1"wantsRoundedSquare"b1} _flags;
@"NSString" _fontDesign;
@"NSArray" _decorations;
@"UILabel" _dayLabel;
@"UIView" _decorationContentView;
@"UIVisualEffectView" _backgroundView;
@"UIView" _labelContentView;
Q _selectionRoundedEdge;
@"UICalendarView" _calendarView;
```

## Properties

```
@property (TQ,N,V_selectionRoundedEdge) selectionRoundedEdge;
@property (T@"UICalendarView",W,N,V_calendarView) calendarView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICalendarDateViewCell reuseIdentifier];
```

## Instance methods

```
-[_UICalendarDateViewCell setSelected:];
-[_UICalendarDateViewCell pointerInteraction:styleForRegion:];
-[_UICalendarDateViewCell _updateBackgroundView];
-[_UICalendarDateViewCell layoutSubviews];
-[_UICalendarDateViewCell tintColorDidChange];
-[_UICalendarDateViewCell setHighlighted:];
-[_UICalendarDateViewCell _updateLabelColor];
-[_UICalendarDateViewCell initWithFrame:];
-[_UICalendarDateViewCell _currentCellState];
-[_UICalendarDateViewCell _updateFontDesign];
-[_UICalendarDateViewCell _updateForPreferredContentSizeCategoryChange];
-[_UICalendarDateViewCell calendarView];
-[_UICalendarDateViewCell configureWithDay:formatter:fontDesign:decorations:outOfRange:renderOverhangDays:highlightsToday:];
-[_UICalendarDateViewCell selectionRoundedEdge];
-[_UICalendarDateViewCell setCalendarView:];
-[_UICalendarDateViewCell setSelectionRoundedEdge:];
```
