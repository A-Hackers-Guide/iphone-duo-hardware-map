# `UIInterfaceActionVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInterfaceActionConcreteVisualStyleImplInternal`, `UIInterfaceActionConcreteVisualStyleImpl`, `NSCopying`
- 4 instance variables, 8 properties, 59 instance methods, 1 class methods

## Instance variables

```
@"UIInterfaceActionGroupViewState" _groupViewState;
@"UIInterfaceActionConcreteVisualStyle<UIInterfaceActionConcreteVisualStyleImpl>" _concreteVisualStyle;
@? _fontForViewStateBlock;
@"UIInterfaceActionOverrideVisualStyle" _visualStyleOverride;
```

## Properties

```
@property (T@"UIInterfaceActionConcreteVisualStyle<UIInterfaceActionConcreteVisualStyleImpl>",&,N,V_concreteVisualStyle) concreteVisualStyle;
@property (T@?,C,N,V_fontForViewStateBlock) fontForViewStateBlock;
@property (T@"UIInterfaceActionOverrideVisualStyle",&,N,V_visualStyleOverride) visualStyleOverride;
@property (T@"UIInterfaceActionGroupViewState",R,N,V_groupViewState) groupViewState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInterfaceActionVisualStyle idiomSpecificStyleForTraitCollection:presentationStyle:];
```

## Instance methods

```
-[UIInterfaceActionVisualStyle allowsZeroSizedSectionSeparators];
-[UIInterfaceActionVisualStyle configureForDismissingGroupView:alongsideTransitionCoordinator:];
-[UIInterfaceActionVisualStyle defaultScreen];
-[UIInterfaceActionVisualStyle actionBackgroundColorForViewState:];
-[UIInterfaceActionVisualStyle defaultConcreteActionTitleLabelPreferredFont];
-[UIInterfaceActionVisualStyle actionPropertiesAffectingLabelStyling];
-[UIInterfaceActionVisualStyle selectByPressGestureRequired];
-[UIInterfaceActionVisualStyle actionClassificationLabelFontForViewState:];
-[UIInterfaceActionVisualStyle actionTitleLabelFontForViewState:];
-[UIInterfaceActionVisualStyle actionPropertiesAffectingActionRepresentationViewStyling];
-[UIInterfaceActionVisualStyle init];
-[UIInterfaceActionVisualStyle actionGroupPropertiesAffectingActionsScrollViewStyling];
-[UIInterfaceActionVisualStyle _base_actionPropertiesAffectingLabelStyling];
-[UIInterfaceActionVisualStyle actionImageViewTintColorForImageProperty:actionViewState:];
-[UIInterfaceActionVisualStyle actionTitleLabelCompositingFilterForViewState:];
-[UIInterfaceActionVisualStyle copyWithGroupViewState:];
-[UIInterfaceActionVisualStyle concreteVisualStyle];
-[UIInterfaceActionVisualStyle newActionBackgroundViewForViewState:];
-[UIInterfaceActionVisualStyle newSectionSeparatorViewForGroupViewState:];
-[UIInterfaceActionVisualStyle _base_configureAttributesForImageView:imageProperty:actionViewState:];
-[UIInterfaceActionVisualStyle actionTitleLabelColorForViewState:];
-[UIInterfaceActionVisualStyle actionSequenceEdgeInsets];
-[UIInterfaceActionVisualStyle newGroupBackgroundViewWithGroupViewState:];
-[UIInterfaceActionVisualStyle configureAttributesForTitleLabel:classificationLabel:actionViewState:];
-[UIInterfaceActionVisualStyle configureForPresentingGroupView:alongsideTransitionCoordinator:];
-[UIInterfaceActionVisualStyle actionTitleLabelMinimumScaleFactor];
-[UIInterfaceActionVisualStyle configureAttributesForImageView:imageProperty:actionViewState:];
-[UIInterfaceActionVisualStyle configureAttributesForActionScrollView:groupViewState:];
-[UIInterfaceActionVisualStyle configureAttributesForActionRepresentationView:actionViewState:];
-[UIInterfaceActionVisualStyle shouldUseVibrantTitleLabels];
-[UIInterfaceActionVisualStyle maximumActionGroupContentSize];
-[UIInterfaceActionVisualStyle contentCornerRadius];
-[UIInterfaceActionVisualStyle actionViewStateForAttachingToActionRepresentationView:];
-[UIInterfaceActionVisualStyle actionSpacingForGroupViewState:];
-[UIInterfaceActionVisualStyle selectionFeedbackEnabled];
-[UIInterfaceActionVisualStyle description];
-[UIInterfaceActionVisualStyle _base_configureAttributesForTitleLabel:classificationLabel:actionViewState:];
-[UIInterfaceActionVisualStyle defaultConcreteActionTitleLabelRegularFont];
-[UIInterfaceActionVisualStyle _base_actionPropertiesAffectingImageViewStyling];
-[UIInterfaceActionVisualStyle horizontalImageContentSpacing];
-[UIInterfaceActionVisualStyle actionClassificationLabelColorForViewState:];
-[UIInterfaceActionVisualStyle minimumActionContentSize];
-[UIInterfaceActionVisualStyle fontForViewStateBlock];
-[UIInterfaceActionVisualStyle _contrastingColorForColor:];
-[UIInterfaceActionVisualStyle copyWithZone:];
-[UIInterfaceActionVisualStyle newActionSeparatorViewForGroupViewState:];
-[UIInterfaceActionVisualStyle visualStyleOverride];
-[UIInterfaceActionVisualStyle initWithConcreteVisualStyle:];
-[UIInterfaceActionVisualStyle isEqual:];
-[UIInterfaceActionVisualStyle setConcreteVisualStyle:];
-[UIInterfaceActionVisualStyle contentMargin];
-[UIInterfaceActionVisualStyle verticalImageContentSpacing];
-[UIInterfaceActionVisualStyle actionPropertiesAffectingImageViewStyling];
-[UIInterfaceActionVisualStyle _styleForVisualProperties];
-[UIInterfaceActionVisualStyle setFontForViewStateBlock:];
-[UIInterfaceActionVisualStyle groupViewState];
-[UIInterfaceActionVisualStyle selectByIndirectPointerTouchRequired];
-[UIInterfaceActionVisualStyle setVisualStyleOverride:];
-[UIInterfaceActionVisualStyle actionSectionSpacing];
```
