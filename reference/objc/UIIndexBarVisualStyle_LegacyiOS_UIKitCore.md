# `UIIndexBarVisualStyle_LegacyiOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIIndexBarVisualStyle_Base`
- 11 instance variables, 1 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _titles;
@"UIFont" _font;
q _selectedSection;
B _pastTop;
B _pastBottom;
{CGSize="width"d"height"d} _cachedSize;
{CGSize="width"d"height"d} _cachedSizeToFit;
d _topPadding;
d _bottomPadding;
d _verticalTextHeightEstimate;
@"UIColor" _nonTrackingBackgroundColor;
```

## Properties

```
@property (T@"UIColor",C,N,V_nonTrackingBackgroundColor) nonTrackingBackgroundColor;
```

## Instance methods

```
-[UIIndexBarVisualStyle_LegacyiOS initWithView:];
-[UIIndexBarVisualStyle_LegacyiOS drawRect:];
-[UIIndexBarVisualStyle_LegacyiOS canBecomeFocused];
-[UIIndexBarVisualStyle_LegacyiOS sizeThatFits:];
-[UIIndexBarVisualStyle_LegacyiOS overlay];
-[UIIndexBarVisualStyle_LegacyiOS font];
-[UIIndexBarVisualStyle_LegacyiOS lineSpacing];
-[UIIndexBarVisualStyle_LegacyiOS renderingHeightForDisplayEntry:];
-[UIIndexBarVisualStyle_LegacyiOS _accessibility_indexForEntryAtPoint:];
-[UIIndexBarVisualStyle_LegacyiOS _lineSpacingForCurrentIdiom];
-[UIIndexBarVisualStyle_LegacyiOS _visibleBoundsForRect:stride:];
-[UIIndexBarVisualStyle_LegacyiOS didDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
-[UIIndexBarVisualStyle_LegacyiOS displayEntriesUpdated];
-[UIIndexBarVisualStyle_LegacyiOS displayEntryFromEntry:];
-[UIIndexBarVisualStyle_LegacyiOS indexColorUpdated];
-[UIIndexBarVisualStyle_LegacyiOS indexWidth];
-[UIIndexBarVisualStyle_LegacyiOS legibilityWeightOrPreferredContentSizeUpdated];
-[UIIndexBarVisualStyle_LegacyiOS minLineHeight];
-[UIIndexBarVisualStyle_LegacyiOS nonTrackingBackgroundColor];
-[UIIndexBarVisualStyle_LegacyiOS selectedSectionDidChange:];
-[UIIndexBarVisualStyle_LegacyiOS setNonTrackingBackgroundColor:];
-[UIIndexBarVisualStyle_LegacyiOS sizeUpdated];
-[UIIndexBarVisualStyle_LegacyiOS trackingChangeHysteresis];
-[UIIndexBarVisualStyle_LegacyiOS trackingDidBegin];
-[UIIndexBarVisualStyle_LegacyiOS trackingDidEnd];
-[UIIndexBarVisualStyle_LegacyiOS updateSectionForTouch:withEvent:];
-[UIIndexBarVisualStyle_LegacyiOS willDrawEntryAtIndex:indexBounds:entryBounds:context:originalColor:];
```
