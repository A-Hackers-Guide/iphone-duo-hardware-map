# `_UIFindNavigatorViewLayout_Mac`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFindNavigatorViewLayout`
- 10 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIStackView" _verticalStackView;
@"UIStackView" _findStackView;
@"UIStackView" _replaceStackView;
@"UIStackView" _firstLineControlsStackView;
@"UIStackView" _secondLineControlsStackView;
@"UIView" _doneButtonSpacer;
@"NSLayoutConstraint" _lineEqualWidthsConstraint;
@"UISwitch" _replaceToggleSwitch;
@"UISegmentedControl" _nextPreviousSegmentedControl;
@"UISegmentedControl" _replaceReplaceAllSegmentedControl;
```

## Properties

```
@property (T@"UISwitch",&,N,V_replaceToggleSwitch) replaceToggleSwitch;
@property (T@"UISegmentedControl",&,N,V_nextPreviousSegmentedControl) nextPreviousSegmentedControl;
@property (T@"UISegmentedControl",&,N,V_replaceReplaceAllSegmentedControl) replaceReplaceAllSegmentedControl;
```

## Instance methods

```
-[_UIFindNavigatorViewLayout_Mac layoutSubviews];
-[_UIFindNavigatorViewLayout_Mac preferredContentSize];
-[_UIFindNavigatorViewLayout_Mac initWithFrame:];
-[_UIFindNavigatorViewLayout_Mac nextPreviousSegmentedControl];
-[_UIFindNavigatorViewLayout_Mac prepareForLayout];
-[_UIFindNavigatorViewLayout_Mac replaceReplaceAllSegmentedControl];
-[_UIFindNavigatorViewLayout_Mac replaceToggleSwitch];
-[_UIFindNavigatorViewLayout_Mac setNextPreviousSegmentedControl:];
-[_UIFindNavigatorViewLayout_Mac setReplaceFieldVisible:];
-[_UIFindNavigatorViewLayout_Mac setReplaceReplaceAllSegmentedControl:];
-[_UIFindNavigatorViewLayout_Mac setReplaceToggleSwitch:];
-[_UIFindNavigatorViewLayout_Mac showsReplaceInOptionsMenu];
```
