# `_UIDatePickerLinkedLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIContentSizeCategoryAdjusting`
- 11 instance variables, 16 properties, 40 instance methods, 0 class methods

## Instance variables

```
{?="needsStorageSync"b1} _flags;
@"UILabel" _renderingLabel;
{CGSize="width"d"height"d} _lastSize;
@"NSMapTable" _longestPossibleTitle;
@"NSMapTable" _longestPossibleWidth;
@"NSLayoutConstraint" _renderLabelXConstraint;
@"_UIDatePickerLinkedLabelStorage" _storage;
@"UILayoutGuide" _contentLayoutGuide;
@"NSArray" _titles;
@"NSArray" _possibleTitles;
@"NSDictionary" _overrideAttributes;
```

## Properties

```
@property (T@"_UIDatePickerLinkedLabelStorage",&,N,V_storage) storage;
@property (T@"UILayoutGuide",R,N,V_contentLayoutGuide) contentLayoutGuide;
@property (T@"NSArray",&,N,V_titles) titles;
@property (T@"NSArray",&,N,V_possibleTitles) possibleTitles;
@property (T@"NSDictionary",&,N,V_overrideAttributes) overrideAttributes;
@property (T@"UIFont",&,N) font;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (T@"UIColor",&,N) textColor;
@property (TB,N) textColorFollowsTintColor;
@property (Tq,N) textAlignment;
@property (TB,N) adjustsFontForContentSizeCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDatePickerLinkedLabel setTextAlignment:];
-[_UIDatePickerLinkedLabel setTextColorFollowsTintColor:];
-[_UIDatePickerLinkedLabel didMoveToWindow];
-[_UIDatePickerLinkedLabel adjustsFontForContentSizeCategory];
-[_UIDatePickerLinkedLabel setAdjustsFontForContentSizeCategory:];
-[_UIDatePickerLinkedLabel textAlignment];
-[_UIDatePickerLinkedLabel _intrinsicSizeWithinSize:];
-[_UIDatePickerLinkedLabel textColor];
-[_UIDatePickerLinkedLabel setTextColor:];
-[_UIDatePickerLinkedLabel setAdjustsFontSizeToFitWidth:];
-[_UIDatePickerLinkedLabel layoutSubviews];
-[_UIDatePickerLinkedLabel setBounds:];
-[_UIDatePickerLinkedLabel _preferredContentSizeCategoryDidChange];
-[_UIDatePickerLinkedLabel storage];
-[_UIDatePickerLinkedLabel sizeThatFits:];
-[_UIDatePickerLinkedLabel minimumScaleFactor];
-[_UIDatePickerLinkedLabel adjustsFontSizeToFitWidth];
-[_UIDatePickerLinkedLabel setFrame:];
-[_UIDatePickerLinkedLabel setStorage:];
-[_UIDatePickerLinkedLabel font];
-[_UIDatePickerLinkedLabel textColorFollowsTintColor];
-[_UIDatePickerLinkedLabel setMinimumScaleFactor:];
-[_UIDatePickerLinkedLabel initWithFrame:];
-[_UIDatePickerLinkedLabel setFont:];
-[_UIDatePickerLinkedLabel _invalidatePossibleTitleCaches];
-[_UIDatePickerLinkedLabel _longestPossibleTitleForPriority:width:];
-[_UIDatePickerLinkedLabel _renderPriorityForContainerWidth:initialPriority:];
-[_UIDatePickerLinkedLabel _setNeedsStorageSync];
-[_UIDatePickerLinkedLabel _storageSyncIfNecessaryWithContainerSize:];
-[_UIDatePickerLinkedLabel _storageSyncWithContainerSize:];
-[_UIDatePickerLinkedLabel _updateAlignmentConstraint];
-[_UIDatePickerLinkedLabel contentLayoutGuide];
-[_UIDatePickerLinkedLabel overrideAttributes];
-[_UIDatePickerLinkedLabel possibleTitles];
-[_UIDatePickerLinkedLabel setContentCompressionResistancePriority:forAxis:];
-[_UIDatePickerLinkedLabel setContentHuggingPriority:forAxis:];
-[_UIDatePickerLinkedLabel setOverrideAttributes:];
-[_UIDatePickerLinkedLabel setPossibleTitles:];
-[_UIDatePickerLinkedLabel setTitles:];
-[_UIDatePickerLinkedLabel titles];
```
