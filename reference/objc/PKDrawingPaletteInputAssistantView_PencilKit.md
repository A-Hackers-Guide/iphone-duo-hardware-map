# `PKDrawingPaletteInputAssistantView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteButtonIntrinsicContentSizeObserver`, `PKPaletteEdgeLocating`, `PKPaletteViewSizeScaling`
- 14 instance variables, 19 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _useCompactLayout;
B _shouldShowKeyboardButton;
B _shouldShowReturnKeyButton;
B _enableKeyboardButtons;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"NSArray" _buttons;
@"PKPaletteKeyboardButton" _keyboardButton;
@"PKPaletteButton" _returnKeyButton;
@"UIStackView" _contentStackView;
@"PKPaletteButtonGroupView" _topOrTrailingGroupView;
@"PKPaletteButtonGroupView" _bottomOrLeadingGroupView;
@"NSHashTable" _viewStateObservers;
```

## Properties

```
@property (T@"UIStackView",&,N,V_contentStackView) contentStackView;
@property (T@"PKPaletteButtonGroupView",&,N,V_topOrTrailingGroupView) topOrTrailingGroupView;
@property (T@"PKPaletteButtonGroupView",&,N,V_bottomOrLeadingGroupView) bottomOrLeadingGroupView;
@property (T@"PKPaletteKeyboardButton",&,N,V_keyboardButton) keyboardButton;
@property (T@"PKPaletteButton",&,N,V_returnKeyButton) returnKeyButton;
@property (T@"NSHashTable",&,N,V_viewStateObservers) viewStateObservers;
@property (T@"NSArray",C,N,V_buttons) buttons;
@property (TB,R,N) hasInputAssistantItems;
@property (TB,N,V_useCompactLayout) useCompactLayout;
@property (TB,N,V_shouldShowKeyboardButton) shouldShowKeyboardButton;
@property (TB,N,V_shouldShowReturnKeyButton) shouldShowReturnKeyButton;
@property (TB,N,V_enableKeyboardButtons) enableKeyboardButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Instance methods

```
-[PKDrawingPaletteInputAssistantView buttons];
-[PKDrawingPaletteInputAssistantView intrinsicContentSize];
-[PKDrawingPaletteInputAssistantView scalingFactor];
-[PKDrawingPaletteInputAssistantView setButtons:];
-[PKDrawingPaletteInputAssistantView _updateContentOrientation];
-[PKDrawingPaletteInputAssistantView setScalingFactor:];
-[PKDrawingPaletteInputAssistantView _updateUI];
-[PKDrawingPaletteInputAssistantView initWithFrame:];
-[PKDrawingPaletteInputAssistantView contentStackView];
-[PKDrawingPaletteInputAssistantView keyboardButton];
-[PKDrawingPaletteInputAssistantView setContentStackView:];
-[PKDrawingPaletteInputAssistantView setKeyboardButton:];
-[PKDrawingPaletteInputAssistantView useCompactLayout];
-[PKDrawingPaletteInputAssistantView setUseCompactLayout:];
-[PKDrawingPaletteInputAssistantView returnKeyButton];
-[PKDrawingPaletteInputAssistantView _contentStackViewAlignment];
-[PKDrawingPaletteInputAssistantView _contentStackViewSpacing];
-[PKDrawingPaletteInputAssistantView _notifyViewStateDidChange];
-[PKDrawingPaletteInputAssistantView _topOrTrailingGroupViewButtons];
-[PKDrawingPaletteInputAssistantView _updateContentScalingFactor];
-[PKDrawingPaletteInputAssistantView _updateContentViewSpacing];
-[PKDrawingPaletteInputAssistantView _updateGroupViewContents];
-[PKDrawingPaletteInputAssistantView _useThreeButtonLayout];
-[PKDrawingPaletteInputAssistantView addViewStateObserver:];
-[PKDrawingPaletteInputAssistantView bottomOrLeadingGroupView];
-[PKDrawingPaletteInputAssistantView buttonDidChangeIntrinsicContentSize:];
-[PKDrawingPaletteInputAssistantView cornerLocation];
-[PKDrawingPaletteInputAssistantView edgeLocation];
-[PKDrawingPaletteInputAssistantView enableKeyboardButtons];
-[PKDrawingPaletteInputAssistantView hasInputAssistantItems];
-[PKDrawingPaletteInputAssistantView removeViewStateObserver:];
-[PKDrawingPaletteInputAssistantView setBottomOrLeadingGroupView:];
-[PKDrawingPaletteInputAssistantView setCornerLocation:];
-[PKDrawingPaletteInputAssistantView setEdgeLocation:];
-[PKDrawingPaletteInputAssistantView setEnableKeyboardButtons:];
-[PKDrawingPaletteInputAssistantView setReturnKeyButton:];
-[PKDrawingPaletteInputAssistantView setShouldShowKeyboardButton:];
-[PKDrawingPaletteInputAssistantView setShouldShowReturnKeyButton:];
-[PKDrawingPaletteInputAssistantView setTopOrTrailingGroupView:];
-[PKDrawingPaletteInputAssistantView setViewStateObservers:];
-[PKDrawingPaletteInputAssistantView shouldShowKeyboardButton];
-[PKDrawingPaletteInputAssistantView shouldShowReturnKeyButton];
-[PKDrawingPaletteInputAssistantView topOrTrailingGroupView];
-[PKDrawingPaletteInputAssistantView viewStateObservers];
```
