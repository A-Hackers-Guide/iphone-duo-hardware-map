# `UITableViewIndexVisualStyle` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"UITableViewIndex",W,N) tableViewIndex;
@property (T@"UIFont",&,N) font;
@property (Td,R,N) indexWidth;
@property (Td,R,N) lineSpacing;
@property (Td,R,N) minLineSpacing;
```

## Instance methods

```
-[UITableViewIndexVisualStyle font];
-[UITableViewIndexVisualStyle lineSpacing];
-[UITableViewIndexVisualStyle setFont:];
-[UITableViewIndexVisualStyle indexWidth];
-[UITableViewIndexVisualStyle initWithTableViewIndex:];
-[UITableViewIndexVisualStyle minLineSpacing];
-[UITableViewIndexVisualStyle setTableViewIndex:];
-[UITableViewIndexVisualStyle tableViewIndex];
-[UITableViewIndexVisualStyle drawRect:];
-[UITableViewIndexVisualStyle didDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
-[UITableViewIndexVisualStyle handleTouch:withEvent:touchedEntryIndex:];
-[UITableViewIndexVisualStyle legibilityWeightOrPreferredContentSizeUpdated];
-[UITableViewIndexVisualStyle selectedSectionDidChange:];
-[UITableViewIndexVisualStyle trackingDidBegin];
-[UITableViewIndexVisualStyle trackingDidEnd];
-[UITableViewIndexVisualStyle willDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
```
