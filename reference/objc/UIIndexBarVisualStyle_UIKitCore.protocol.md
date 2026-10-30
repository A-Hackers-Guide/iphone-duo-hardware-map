# `UIIndexBarVisualStyle` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 31 instance methods, 0 class methods

## Properties

```
@property (T@"UIIndexBarView",W,N) indexBarView;
@property (TB,R,N) canBecomeFocused;
@property (TB,R,N) overlay;
@property (Td,R,N) minLineHeight;
@property (Td,R,N) indexWidth;
@property (Td,R,N) lineSpacing;
@property (TB,?,N) expanded;
@property (Td,?,R,N) trackingChangeHysteresis;
```

## Instance methods

```
-[UIIndexBarVisualStyle initWithView:];
-[UIIndexBarVisualStyle canBecomeFocused];
-[UIIndexBarVisualStyle sizeThatFits:];
-[UIIndexBarVisualStyle overlay];
-[UIIndexBarVisualStyle lineSpacing];
-[UIIndexBarVisualStyle renderingHeightForDisplayEntry:];
-[UIIndexBarVisualStyle displayEntryFromEntry:];
-[UIIndexBarVisualStyle indexBarView];
-[UIIndexBarVisualStyle indexWidth];
-[UIIndexBarVisualStyle minLineHeight];
-[UIIndexBarVisualStyle setIndexBarView:];
-[UIIndexBarVisualStyle setExpanded:];
-[UIIndexBarVisualStyle drawRect:];
-[UIIndexBarVisualStyle layoutSubviews];
-[UIIndexBarVisualStyle expanded];
-[UIIndexBarVisualStyle _accessibility_indexForEntryAtPoint:];
-[UIIndexBarVisualStyle deflectionReset:];
-[UIIndexBarVisualStyle deflectionUpdated];
-[UIIndexBarVisualStyle displayEntriesUpdated];
-[UIIndexBarVisualStyle entriesUpdated];
-[UIIndexBarVisualStyle handleTouch:withEvent:touchedEntryIndex:];
-[UIIndexBarVisualStyle highlightStyleUpdated];
-[UIIndexBarVisualStyle highlightedIndexUpdated];
-[UIIndexBarVisualStyle indexColorUpdated];
-[UIIndexBarVisualStyle legibilityWeightOrPreferredContentSizeUpdated];
-[UIIndexBarVisualStyle selectedSectionDidChange:];
-[UIIndexBarVisualStyle sizeUpdated];
-[UIIndexBarVisualStyle trackingChangeHysteresis];
-[UIIndexBarVisualStyle trackingDidBegin];
-[UIIndexBarVisualStyle trackingDidEnd];
-[UIIndexBarVisualStyle updateSectionForTouch:withEvent:];
```
