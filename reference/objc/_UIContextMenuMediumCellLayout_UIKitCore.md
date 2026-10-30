# `_UIContextMenuMediumCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 7 instance variables, 20 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" _contentView;
@"NSArray" _managedConstraints;
@"NSLayoutConstraint" _topConstraint;
@"NSLayoutConstraint" _primaryViewCenterYConstraint;
@"NSLayoutConstraint" _bottomConstraint;
@"NSLayoutConstraint" _fittingBottomConstraint;
@"NSLayoutConstraint" _minimumHeightConstraint;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",W,N,V_contentView) contentView;
@property (T@"NSArray",&,N,V_managedConstraints) managedConstraints;
@property (T@"NSLayoutConstraint",&,N,V_topConstraint) topConstraint;
@property (T@"NSLayoutConstraint",&,N,V_primaryViewCenterYConstraint) primaryViewCenterYConstraint;
@property (T@"NSLayoutConstraint",&,N,V_bottomConstraint) bottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_fittingBottomConstraint) fittingBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_minimumHeightConstraint) minimumHeightConstraint;
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
-[_UIContextMenuMediumCellLayout topConstraint];
-[_UIContextMenuMediumCellLayout setTopConstraint:];
-[_UIContextMenuMediumCellLayout initWithContentView:];
-[_UIContextMenuMediumCellLayout setContentView:];
-[_UIContextMenuMediumCellLayout layoutSize];
-[_UIContextMenuMediumCellLayout _currentPlatformMetrics];
-[_UIContextMenuMediumCellLayout primaryViewCenterYConstraint];
-[_UIContextMenuMediumCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuMediumCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuMediumCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuMediumCellLayout contentShape];
-[_UIContextMenuMediumCellLayout fittingBottomConstraint];
-[_UIContextMenuMediumCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuMediumCellLayout labelTextAlignment];
-[_UIContextMenuMediumCellLayout setPrimaryViewCenterYConstraint:];
-[_UIContextMenuMediumCellLayout managedConstraints];
-[_UIContextMenuMediumCellLayout _hasTitle];
-[_UIContextMenuMediumCellLayout setFittingBottomConstraint:];
-[_UIContextMenuMediumCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuMediumCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuMediumCellLayout setMinimumHeightConstraint:];
-[_UIContextMenuMediumCellLayout focusStyle];
-[_UIContextMenuMediumCellLayout removeConstraints];
-[_UIContextMenuMediumCellLayout contentView];
-[_UIContextMenuMediumCellLayout updateConstraints];
-[_UIContextMenuMediumCellLayout hoverStyle];
-[_UIContextMenuMediumCellLayout setManagedConstraints:];
-[_UIContextMenuMediumCellLayout installConstraints];
-[_UIContextMenuMediumCellLayout setBottomConstraint:];
-[_UIContextMenuMediumCellLayout minimumHeightConstraint];
-[_UIContextMenuMediumCellLayout bottomConstraint];
```
