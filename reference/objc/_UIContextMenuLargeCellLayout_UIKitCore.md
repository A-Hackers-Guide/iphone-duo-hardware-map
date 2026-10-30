# `_UIContextMenuLargeCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 13 instance variables, 26 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" _contentView;
@"NSArray" _managedConstraints;
@"NSLayoutConstraint" _topToFirstBaseline;
@"NSLayoutConstraint" _lastBaselineToBottom;
@"NSLayoutConstraint" _leadingToLabelStackViewLeading;
@"NSLayoutConstraint" _selectionIndicatorViewCenterX;
@"NSLayoutConstraint" _childIndicatorViewCenterX;
@"NSLayoutConstraint" _iconViewCenterXToTrailing;
@"NSLayoutConstraint" _labelStackViewTrailingToIconViewCenterX;
@"NSLayoutConstraint" _minHeightConstraint;
@"NSLayoutConstraint" _labelStackViewTrailingToChildIndicatorViewLeading;
@"NSLayoutConstraint" _keyboardShortcutTrailingToTrailing;
@"NSLayoutConstraint" _labelStackViewTrailingToKeyboardShortcutLeading;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",W,N,V_contentView) contentView;
@property (T@"NSArray",&,N,V_managedConstraints) managedConstraints;
@property (T@"NSLayoutConstraint",&,N,V_topToFirstBaseline) topToFirstBaseline;
@property (T@"NSLayoutConstraint",&,N,V_lastBaselineToBottom) lastBaselineToBottom;
@property (T@"NSLayoutConstraint",&,N,V_leadingToLabelStackViewLeading) leadingToLabelStackViewLeading;
@property (T@"NSLayoutConstraint",&,N,V_selectionIndicatorViewCenterX) selectionIndicatorViewCenterX;
@property (T@"NSLayoutConstraint",&,N,V_childIndicatorViewCenterX) childIndicatorViewCenterX;
@property (T@"NSLayoutConstraint",&,N,V_iconViewCenterXToTrailing) iconViewCenterXToTrailing;
@property (T@"NSLayoutConstraint",&,N,V_labelStackViewTrailingToIconViewCenterX) labelStackViewTrailingToIconViewCenterX;
@property (T@"NSLayoutConstraint",&,N,V_minHeightConstraint) minHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_labelStackViewTrailingToChildIndicatorViewLeading) labelStackViewTrailingToChildIndicatorViewLeading;
@property (T@"NSLayoutConstraint",&,N,V_keyboardShortcutTrailingToTrailing) keyboardShortcutTrailingToTrailing;
@property (T@"NSLayoutConstraint",&,N,V_labelStackViewTrailingToKeyboardShortcutLeading) labelStackViewTrailingToKeyboardShortcutLeading;
@property (Tq,R,N) layoutSize;
@property (Tq,R,N) labelTextAlignment;
@property (TQ,R,N) labelMaximumNumberOfLines;
@property (T@"UIColor",R,N) preferredContentColorForCurrentState;
@property (T@"UIColor",R,N) preferredBackgroundColorForCurrentState;
@property (T@"UIHoverStyle",R,N) hoverStyle;
@property (T@"UIShape",R,N) contentShape;
@property (TB,R,N) useContentShapeForSelectionHighlight;
@property (Tq,R,N) focusStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuLargeCellLayout initWithContentView:];
-[_UIContextMenuLargeCellLayout setContentView:];
-[_UIContextMenuLargeCellLayout layoutSize];
-[_UIContextMenuLargeCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuLargeCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuLargeCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuLargeCellLayout contentShape];
-[_UIContextMenuLargeCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuLargeCellLayout labelTextAlignment];
-[_UIContextMenuLargeCellLayout managedConstraints];
-[_UIContextMenuLargeCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuLargeCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuLargeCellLayout focusStyle];
-[_UIContextMenuLargeCellLayout removeConstraints];
-[_UIContextMenuLargeCellLayout contentView];
-[_UIContextMenuLargeCellLayout updateConstraints];
-[_UIContextMenuLargeCellLayout hoverStyle];
-[_UIContextMenuLargeCellLayout setManagedConstraints:];
-[_UIContextMenuLargeCellLayout installConstraints];
-[_UIContextMenuLargeCellLayout _hasTrailingAccessory];
-[_UIContextMenuLargeCellLayout _itemInternalPadding];
-[_UIContextMenuLargeCellLayout childIndicatorViewCenterX];
-[_UIContextMenuLargeCellLayout iconViewCenterXToTrailing];
-[_UIContextMenuLargeCellLayout keyboardShortcutTrailingToTrailing];
-[_UIContextMenuLargeCellLayout labelStackViewTrailingToChildIndicatorViewLeading];
-[_UIContextMenuLargeCellLayout labelStackViewTrailingToIconViewCenterX];
-[_UIContextMenuLargeCellLayout labelStackViewTrailingToKeyboardShortcutLeading];
-[_UIContextMenuLargeCellLayout lastBaselineToBottom];
-[_UIContextMenuLargeCellLayout leadingToLabelStackViewLeading];
-[_UIContextMenuLargeCellLayout minHeightConstraint];
-[_UIContextMenuLargeCellLayout selectionIndicatorViewCenterX];
-[_UIContextMenuLargeCellLayout setChildIndicatorViewCenterX:];
-[_UIContextMenuLargeCellLayout setIconViewCenterXToTrailing:];
-[_UIContextMenuLargeCellLayout setKeyboardShortcutTrailingToTrailing:];
-[_UIContextMenuLargeCellLayout setLabelStackViewTrailingToChildIndicatorViewLeading:];
-[_UIContextMenuLargeCellLayout setLabelStackViewTrailingToIconViewCenterX:];
-[_UIContextMenuLargeCellLayout setLabelStackViewTrailingToKeyboardShortcutLeading:];
-[_UIContextMenuLargeCellLayout setLastBaselineToBottom:];
-[_UIContextMenuLargeCellLayout setLeadingToLabelStackViewLeading:];
-[_UIContextMenuLargeCellLayout setMinHeightConstraint:];
-[_UIContextMenuLargeCellLayout setSelectionIndicatorViewCenterX:];
-[_UIContextMenuLargeCellLayout setTopToFirstBaseline:];
-[_UIContextMenuLargeCellLayout topToFirstBaseline];
```
