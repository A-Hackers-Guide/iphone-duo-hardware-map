# `_UINavigationBarLargeTitleViewLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UINavigationBarLayoutParticipating`
- 18 instance variables, 16 properties, 54 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _titleHeightCache;
@"NSMutableDictionary" _restingHeightCache;
d _cachedRestingHeight;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
B _alignAccessoryViewToTitleBaseline;
B _providesExtraSpaceForExcessiveLineHeights;
B _overlaysContentView;
@"_UINavigationBarLargeTitleView" _contentView;
q _titleType;
@"UIView" _customTitleView;
@"UIView" _subtitleView;
@"NSAttributedString" _subtitle;
Q _twoLineMode;
d _titleRestingHeight;
@"UIView" _accessoryView;
Q _accessoryViewHorizontalAlignment;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _layoutMargins;
```

## Properties

```
@property (T@"_UINavigationBarLargeTitleView",N,V_contentView) contentView;
@property (Tq,N,V_titleType) titleType;
@property (T@"NSAttributedString",C,N) title;
@property (T@"UIView",R,N,V_titleLabel) titleLabel;
@property (T@"UIView",&,N,V_customTitleView) customTitleView;
@property (T@"UIView",&,N,V_subtitleView) subtitleView;
@property (T@"NSAttributedString",C,N,V_subtitle) subtitle;
@property (TQ,N,V_twoLineMode) twoLineMode;
@property (Td,R,N,V_titleRestingHeight) titleRestingHeight;
@property (T@"UIView",&,N,V_accessoryView) accessoryView;
@property (TB,N,V_alignAccessoryViewToTitleBaseline) alignAccessoryViewToTitleBaseline;
@property (TB,N,V_providesExtraSpaceForExcessiveLineHeights) providesExtraSpaceForExcessiveLineHeights;
@property (TQ,N,V_accessoryViewHorizontalAlignment) accessoryViewHorizontalAlignment;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_layoutMargins) layoutMargins;
@property (TB,N,V_overlaysContentView) overlaysContentView;
@property (T@"UIFont",R,N) titleLabelFont;
```

## Instance methods

```
-[_UINavigationBarLargeTitleViewLayout subtitleView];
-[_UINavigationBarLargeTitleViewLayout setSubtitleView:];
-[_UINavigationBarLargeTitleViewLayout titleLabelFont];
-[_UINavigationBarLargeTitleViewLayout layoutMargins];
-[_UINavigationBarLargeTitleViewLayout accessoryView];
-[_UINavigationBarLargeTitleViewLayout initWithContentView:];
-[_UINavigationBarLargeTitleViewLayout setContentView:];
-[_UINavigationBarLargeTitleViewLayout setTitleType:];
-[_UINavigationBarLargeTitleViewLayout updateRestingTitleHeight];
-[_UINavigationBarLargeTitleViewLayout _baselineAlignView:withSize:inBounds:baselineOffsetFromBottom:distanceToBaseline:scale:displayScale:offset:];
-[_UINavigationBarLargeTitleViewLayout providesExtraSpaceForExcessiveLineHeights];
-[_UINavigationBarLargeTitleViewLayout accessoryViewHorizontalAlignment];
-[_UINavigationBarLargeTitleViewLayout setLayoutMargins:];
-[_UINavigationBarLargeTitleViewLayout overlaysContentView];
-[_UINavigationBarLargeTitleViewLayout subtitle];
-[_UINavigationBarLargeTitleViewLayout _heightForSize:titleType:];
-[_UINavigationBarLargeTitleViewLayout updateLayoutData:layoutWidth:];
-[_UINavigationBarLargeTitleViewLayout titleLabel];
-[_UINavigationBarLargeTitleViewLayout titleType];
-[_UINavigationBarLargeTitleViewLayout layoutViewsWithOffsetSupportingMultiLineShrinkToFit:useRestingTitleHeight:];
-[_UINavigationBarLargeTitleViewLayout setContentAlpha:];
-[_UINavigationBarLargeTitleViewLayout alignAccessoryViewToTitleBaseline];
-[_UINavigationBarLargeTitleViewLayout layoutViewsWithOffset:useRestingTitleHeight:];
-[_UINavigationBarLargeTitleViewLayout setAccessoryView:];
-[_UINavigationBarLargeTitleViewLayout _enforceLayoutOrdering];
-[_UINavigationBarLargeTitleViewLayout _updateEffectiveTitleView];
-[_UINavigationBarLargeTitleViewLayout cleanupAfterLayoutTransitionCompleted];
-[_UINavigationBarLargeTitleViewLayout _systemLayoutSizeForView:fittingMaximumWidth:flexibleHeight:];
-[_UINavigationBarLargeTitleViewLayout _contentLayoutBoundsUsingRestingTitleHeight:];
-[_UINavigationBarLargeTitleViewLayout _cachedTitleHeightSizeAndUpdateRestingSizeForWidthSupportingMultiLineShrinkToFit:];
-[_UINavigationBarLargeTitleViewLayout layoutViews];
-[_UINavigationBarLargeTitleViewLayout setSubtitle:];
-[_UINavigationBarLargeTitleViewLayout setAlignAccessoryViewToTitleBaseline:];
-[_UINavigationBarLargeTitleViewLayout _contentLayoutBounds];
-[_UINavigationBarLargeTitleViewLayout textRectForTitleLabelInBounds:limitedToNumberOfLines:];
-[_UINavigationBarLargeTitleViewLayout title];
-[_UINavigationBarLargeTitleViewLayout twoLineMode];
-[_UINavigationBarLargeTitleViewLayout setTwoLineMode:];
-[_UINavigationBarLargeTitleViewLayout contentView];
-[_UINavigationBarLargeTitleViewLayout _updateEffectiveSubtitleView];
-[_UINavigationBarLargeTitleViewLayout sizeFittingSize:titleType:];
-[_UINavigationBarLargeTitleViewLayout setOverlaysContentView:];
-[_UINavigationBarLargeTitleViewLayout setAccessoryViewHorizontalAlignment:];
-[_UINavigationBarLargeTitleViewLayout description];
-[_UINavigationBarLargeTitleViewLayout titleRestingHeight];
-[_UINavigationBarLargeTitleViewLayout setTitle:];
-[_UINavigationBarLargeTitleViewLayout removeContent];
-[_UINavigationBarLargeTitleViewLayout setContentHidden:];
-[_UINavigationBarLargeTitleViewLayout _invalidateTitleHeightCache];
-[_UINavigationBarLargeTitleViewLayout restingHeightForSize:type:];
-[_UINavigationBarLargeTitleViewLayout setCustomTitleView:];
-[_UINavigationBarLargeTitleViewLayout customTitleView];
-[_UINavigationBarLargeTitleViewLayout setProvidesExtraSpaceForExcessiveLineHeights:];
-[_UINavigationBarLargeTitleViewLayout _cachedTitleHeightSizeAndUpdateRestingSizeForWidth:];
```
