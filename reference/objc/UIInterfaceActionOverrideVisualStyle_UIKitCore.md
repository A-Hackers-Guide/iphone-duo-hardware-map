# `UIInterfaceActionOverrideVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInterfaceActionVisualStyle`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _alignActionSeparatorLeadingEdgeWithContent;
d _customSelectionHighlightContinuousCornerRadius;
@"UIInterfaceActionSeparatorAttributes" _customSeparatorAttributes;
@"UIInterfaceActionHighlightAttributes" _customActionHighlightAttributes;
@? _customTitleLabelFontProviderForViewState;
```

## Properties

```
@property (Td,V_customSelectionHighlightContinuousCornerRadius) customSelectionHighlightContinuousCornerRadius;
@property (TB,N,V_alignActionSeparatorLeadingEdgeWithContent) alignActionSeparatorLeadingEdgeWithContent;
@property (T@"UIInterfaceActionSeparatorAttributes",&,N,V_customSeparatorAttributes) customSeparatorAttributes;
@property (T@"UIInterfaceActionHighlightAttributes",&,N,V_customActionHighlightAttributes) customActionHighlightAttributes;
@property (T@?,C,N,V_customTitleLabelFontProviderForViewState) customTitleLabelFontProviderForViewState;
```

## Class methods

```
+[UIInterfaceActionOverrideVisualStyle styleOverride];
```

## Instance methods

```
-[UIInterfaceActionOverrideVisualStyle customSelectionHighlightContinuousCornerRadius];
-[UIInterfaceActionOverrideVisualStyle customActionHighlightAttributes];
-[UIInterfaceActionOverrideVisualStyle customTitleLabelFontProviderForViewState];
-[UIInterfaceActionOverrideVisualStyle setCustomSeparatorAttributes:];
-[UIInterfaceActionOverrideVisualStyle actionTitleLabelFontForViewState:];
-[UIInterfaceActionOverrideVisualStyle setCustomActionHighlightAttributes:];
-[UIInterfaceActionOverrideVisualStyle customSeparatorAttributes];
-[UIInterfaceActionOverrideVisualStyle setCustomSelectionHighlightContinuousCornerRadius:];
-[UIInterfaceActionOverrideVisualStyle newActionBackgroundViewForViewState:];
-[UIInterfaceActionOverrideVisualStyle setCustomTitleLabelFontProviderForViewState:];
-[UIInterfaceActionOverrideVisualStyle alignActionSeparatorLeadingEdgeWithContent];
-[UIInterfaceActionOverrideVisualStyle setAlignActionSeparatorLeadingEdgeWithContent:];
-[UIInterfaceActionOverrideVisualStyle copyWithZone:];
-[UIInterfaceActionOverrideVisualStyle newActionSeparatorViewForGroupViewState:];
-[UIInterfaceActionOverrideVisualStyle isEqual:];
```
