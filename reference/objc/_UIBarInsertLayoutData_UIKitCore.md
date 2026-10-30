# `_UIBarInsertLayoutData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_UIBarInsertLayoutDataProtocol`
- 10 instance variables, 21 properties, 32 instance methods, 5 class methods

## Instance variables

```
{?="collapsible"b1"prefersExpanded"b1"ignoredForCollapsingBehaviors"b1"active"b1"verticalOriginValid"b1} _flags;
d _verticalOrigin;
@"NSString" _identifier;
d _minimumHeight;
d _preferredHeight;
d _bottomInsetForTransitionProgress;
d _assignedHeight;
d _collapsingHeight;
q _priority;
q _order;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Td,N,V_minimumHeight) minimumHeight;
@property (Td,N,V_preferredHeight) preferredHeight;
@property (TB,N,GisCollapsible) collapsible;
@property (TB,N) prefersExpanded;
@property (Td,R,N) transitionProgress;
@property (Td,N,V_bottomInsetForTransitionProgress) bottomInsetForTransitionProgress;
@property (Td,R,N) layoutMinimumHeight;
@property (TB,R,N,GisVariableHeight) variableHeight;
@property (Td,R,N,V_assignedHeight) assignedHeight;
@property (Td,R,N,V_collapsingHeight) collapsingHeight;
@property (Td,R,N,V_verticalOrigin) verticalOrigin;
@property (Td,R,N) maxY;
@property (Tq,N,V_priority) priority;
@property (Tq,N,V_order) order;
@property (TB,N) ignoredForCollapsingBehaviors;
@property (TB,N) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBarInsertLayoutData assignVerticalOriginsToItemsInLayouts:];
+[_UIBarInsertLayoutData calculateLayoutHeights:];
+[_UIBarInsertLayoutData calculateRestingHeightsForLayouts:];
+[_UIBarInsertLayoutData layoutPriorToItemWithOrder:inLayouts:];
+[_UIBarInsertLayoutData updateLayoutParameters:overflowLayout:forAvailableHeight:];
```

## Instance methods

```
-[_UIBarInsertLayoutData active];
-[_UIBarInsertLayoutData priority];
-[_UIBarInsertLayoutData setMinimumHeight:];
-[_UIBarInsertLayoutData identifier];
-[_UIBarInsertLayoutData preferredHeight];
-[_UIBarInsertLayoutData init];
-[_UIBarInsertLayoutData setOrder:];
-[_UIBarInsertLayoutData minimumHeight];
-[_UIBarInsertLayoutData setPriority:];
-[_UIBarInsertLayoutData order];
-[_UIBarInsertLayoutData setActive:];
-[_UIBarInsertLayoutData setIdentifier:];
-[_UIBarInsertLayoutData isCollapsible];
-[_UIBarInsertLayoutData setCollapsible:];
-[_UIBarInsertLayoutData transitionProgress];
-[_UIBarInsertLayoutData description];
-[_UIBarInsertLayoutData prefersExpanded];
-[_UIBarInsertLayoutData setPrefersExpanded:];
-[_UIBarInsertLayoutData copyWithZone:];
-[_UIBarInsertLayoutData setPreferredHeight:];
-[_UIBarInsertLayoutData setFixedHeight:];
-[_UIBarInsertLayoutData assignedHeight];
-[_UIBarInsertLayoutData bottomInsetForTransitionProgress];
-[_UIBarInsertLayoutData collapsingHeight];
-[_UIBarInsertLayoutData ignoredForCollapsingBehaviors];
-[_UIBarInsertLayoutData isVariableHeight];
-[_UIBarInsertLayoutData layoutFrameInWidth:];
-[_UIBarInsertLayoutData layoutMinimumHeight];
-[_UIBarInsertLayoutData maxY];
-[_UIBarInsertLayoutData setBottomInsetForTransitionProgress:];
-[_UIBarInsertLayoutData setIgnoredForCollapsingBehaviors:];
-[_UIBarInsertLayoutData verticalOrigin];
```
