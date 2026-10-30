# `_UINavigationBarLargeTitleView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`, `_UINavigationBarTransitionContextParticipant`
- 20 instance variables, 24 properties, 64 instance methods, 0 class methods

## Instance variables

```
@"<_UINavigationBarTransitionContextProtocol>" _transitionContext;
@"NSArray" _titleCandidates;
@"NSAttributedString" __effectiveTitle;
B _providesExtraSpaceForExcessiveLineHeights;
B _alignAccessoryViewToTitleBaseline;
@"NSDictionary" _effectiveTitleAttributes;
@"_UIPointerInteractionAssistant" _assistant;
q _titleType;
@"NSAttributedString" _attributedTitle;
@"UIView" _titleView;
@"NSArray" _alternateTitles;
@"NSDictionary" _titleAttributes;
@"NSDictionary" _subtitleAttributes;
@"NSString" _subtitle;
@"NSAttributedString" _attributedSubtitle;
@"UIView" _subtitleView;
Q _twoLineMode;
@"UIView" _accessoryView;
Q _accessoryViewHorizontalAlignment;
@"_UINavigationBarLargeTitleViewLayout" _layout;
```

## Properties

```
@property (T@"_UIPointerInteractionAssistant",W,N,V_assistant) assistant;
@property (Tq,N,V_titleType) titleType;
@property (T@"NSString",C,N) title;
@property (T@"NSAttributedString",C,N,V_attributedTitle) attributedTitle;
@property (T@"UIView",&,N,V_titleView) titleView;
@property (T@"NSArray",&,N,V_alternateTitles) alternateTitles;
@property (T@"NSDictionary",C,N,V_titleAttributes) titleAttributes;
@property (T@"NSDictionary",R,N,V_effectiveTitleAttributes) effectiveTitleAttributes;
@property (T@"NSDictionary",C,N,V_subtitleAttributes) subtitleAttributes;
@property (T@"NSString",C,N,V_subtitle) subtitle;
@property (T@"NSAttributedString",C,N,V_attributedSubtitle) attributedSubtitle;
@property (T@"UIView",&,N,V_subtitleView) subtitleView;
@property (TQ,N,V_twoLineMode) twoLineMode;
@property (TB,N,V_providesExtraSpaceForExcessiveLineHeights) providesExtraSpaceForExcessiveLineHeights;
@property (Td,R,N) restingHeightOfTitleView;
@property (T@"UIView",&,N,V_accessoryView) accessoryView;
@property (TB,N,V_alignAccessoryViewToTitleBaseline) alignAccessoryViewToTitleBaseline;
@property (TQ,N,V_accessoryViewHorizontalAlignment) accessoryViewHorizontalAlignment;
@property (T@"UIView",R,N) accessibilityTitleView;
@property (T@"_UINavigationBarLargeTitleViewLayout",R,N,V_layout) layout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarLargeTitleView subtitleView];
-[_UINavigationBarLargeTitleView assistant];
-[_UINavigationBarLargeTitleView setSubtitleView:];
-[_UINavigationBarLargeTitleView _newLayout];
-[_UINavigationBarLargeTitleView _setAssistants];
-[_UINavigationBarLargeTitleView prepareToRecordToState:];
-[_UINavigationBarLargeTitleView recordFromStateForTransition:];
-[_UINavigationBarLargeTitleView setTitleAttributes:];
-[_UINavigationBarLargeTitleView accessoryView];
-[_UINavigationBarLargeTitleView adoptNewLayout];
-[_UINavigationBarLargeTitleView titleAttributes];
-[_UINavigationBarLargeTitleView _clearAssistants];
-[_UINavigationBarLargeTitleView adoptLayout:];
-[_UINavigationBarLargeTitleView recordToStateForTransition:];
-[_UINavigationBarLargeTitleView setAssistant:];
-[_UINavigationBarLargeTitleView clearTransitionContext];
-[_UINavigationBarLargeTitleView ensureBackButtonTruncationOccursWithContext:];
-[_UINavigationBarLargeTitleView effectiveTitleAttributes];
-[_UINavigationBarLargeTitleView setTitleView:];
-[_UINavigationBarLargeTitleView setTitleType:];
-[_UINavigationBarLargeTitleView attributedSubtitle];
-[_UINavigationBarLargeTitleView sizeThatFits:titleType:];
-[_UINavigationBarLargeTitleView providesExtraSpaceForExcessiveLineHeights];
-[_UINavigationBarLargeTitleView accessoryViewHorizontalAlignment];
-[_UINavigationBarLargeTitleView restingHeightOfTitleView];
-[_UINavigationBarLargeTitleView intrinsicContentSize];
-[_UINavigationBarLargeTitleView subtitle];
-[_UINavigationBarLargeTitleView alternateTitles];
-[_UINavigationBarLargeTitleView pointerInteraction:styleForRegion:];
-[_UINavigationBarLargeTitleView pointerInteraction:willEnterRegion:animator:];
-[_UINavigationBarLargeTitleView _updateContentAndInvalidate:];
-[_UINavigationBarLargeTitleView _effectiveTitle];
-[_UINavigationBarLargeTitleView titleType];
-[_UINavigationBarLargeTitleView pointerInteraction:willExitRegion:animator:];
-[_UINavigationBarLargeTitleView setAttributedTitle:];
-[_UINavigationBarLargeTitleView alignAccessoryViewToTitleBaseline];
-[_UINavigationBarLargeTitleView setAccessoryView:];
-[_UINavigationBarLargeTitleView _contentSizeCategoryDidChange];
-[_UINavigationBarLargeTitleView updateContent];
-[_UINavigationBarLargeTitleView layoutSubviews];
-[_UINavigationBarLargeTitleView setSubtitle:];
-[_UINavigationBarLargeTitleView setAlignAccessoryViewToTitleBaseline:];
-[_UINavigationBarLargeTitleView subtitleAttributes];
-[_UINavigationBarLargeTitleView sizeThatFits:];
-[_UINavigationBarLargeTitleView _titleForCurrentWidth];
-[_UINavigationBarLargeTitleView finalizeStateFromTransition:];
-[_UINavigationBarLargeTitleView safeAreaInsetsDidChange];
-[_UINavigationBarLargeTitleView title];
-[_UINavigationBarLargeTitleView twoLineMode];
-[_UINavigationBarLargeTitleView accessibilityTitleView];
-[_UINavigationBarLargeTitleView attributedTitle];
-[_UINavigationBarLargeTitleView setTwoLineMode:];
-[_UINavigationBarLargeTitleView _layoutForMeasurement];
-[_UINavigationBarLargeTitleView pointerInteraction:regionForRequest:defaultRegion:];
-[_UINavigationBarLargeTitleView setAttributedSubtitle:];
-[_UINavigationBarLargeTitleView setAccessoryViewHorizontalAlignment:];
-[_UINavigationBarLargeTitleView setTitle:];
-[_UINavigationBarLargeTitleView titleView];
-[_UINavigationBarLargeTitleView layout];
-[_UINavigationBarLargeTitleView setAlternateTitles:];
-[_UINavigationBarLargeTitleView initWithFrame:];
-[_UINavigationBarLargeTitleView setSubtitleAttributes:];
-[_UINavigationBarLargeTitleView _hideScrollPocketContainerModelFromChildren];
-[_UINavigationBarLargeTitleView setProvidesExtraSpaceForExcessiveLineHeights:];
```
