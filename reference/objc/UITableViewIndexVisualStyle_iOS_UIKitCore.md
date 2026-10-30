# `UITableViewIndexVisualStyle_iOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITableViewIndexVisualStyle`
- 3 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"UITableViewIndex" _tableViewIndex;
@"UIFont" _font;
d _verticalTextHeightEstimate;
```

## Properties

```
@property (Td,N,V_verticalTextHeightEstimate) verticalTextHeightEstimate;
@property (T@"UITableViewIndex",W,N,V_tableViewIndex) tableViewIndex;
@property (T@"UIFont",&,N,V_font) font;
@property (Td,R,N) indexWidth;
@property (Td,R,N) lineSpacing;
@property (Td,R,N) minLineSpacing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITableViewIndexVisualStyle_iOS containerViewForTableViewIndex:];
```

## Instance methods

```
-[UITableViewIndexVisualStyle_iOS font];
-[UITableViewIndexVisualStyle_iOS lineSpacing];
-[UITableViewIndexVisualStyle_iOS setFont:];
-[UITableViewIndexVisualStyle_iOS _lineSpacingForCurrentIdiom];
-[UITableViewIndexVisualStyle_iOS didDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
-[UITableViewIndexVisualStyle_iOS handleTouch:withEvent:touchedEntryIndex:];
-[UITableViewIndexVisualStyle_iOS indexWidth];
-[UITableViewIndexVisualStyle_iOS initWithTableViewIndex:];
-[UITableViewIndexVisualStyle_iOS legibilityWeightOrPreferredContentSizeUpdated];
-[UITableViewIndexVisualStyle_iOS minLineSpacing];
-[UITableViewIndexVisualStyle_iOS selectedSectionDidChange:];
-[UITableViewIndexVisualStyle_iOS setTableViewIndex:];
-[UITableViewIndexVisualStyle_iOS setVerticalTextHeightEstimate:];
-[UITableViewIndexVisualStyle_iOS tableViewIndex];
-[UITableViewIndexVisualStyle_iOS trackingDidBegin];
-[UITableViewIndexVisualStyle_iOS trackingDidEnd];
-[UITableViewIndexVisualStyle_iOS verticalTextHeightEstimate];
-[UITableViewIndexVisualStyle_iOS willDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
```
