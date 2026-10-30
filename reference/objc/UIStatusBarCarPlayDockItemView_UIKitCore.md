# `UIStatusBarCarPlayDockItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- 10 instance variables, 10 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _showingCallTimer;
@"UILabel" _inCallDurationLabel;
@"UIStatusBarCarPlayDockAppItemButton" _itemOneButton;
@"UIStatusBarCarPlayDockAppItemButton" _itemTwoButton;
@"UIStatusBarCarPlayDockAppItemButton" _itemThreeButton;
@"NSLayoutConstraint" _inCallLabelSpacingConstraint;
@"NSLayoutConstraint" _itemOneTopConstraint;
@"NSArray" _currentBundleIdentifiers;
@"NSString" _currentActiveBundleIdentifier;
@"UIView" _preferredItemViewToFocus;
```

## Properties

```
@property (T@"UILabel",&,N,V_inCallDurationLabel) inCallDurationLabel;
@property (T@"UIStatusBarCarPlayDockAppItemButton",&,N,V_itemOneButton) itemOneButton;
@property (T@"UIStatusBarCarPlayDockAppItemButton",&,N,V_itemTwoButton) itemTwoButton;
@property (T@"UIStatusBarCarPlayDockAppItemButton",&,N,V_itemThreeButton) itemThreeButton;
@property (T@"NSLayoutConstraint",&,N,V_inCallLabelSpacingConstraint) inCallLabelSpacingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_itemOneTopConstraint) itemOneTopConstraint;
@property (T@"NSArray",C,N,V_currentBundleIdentifiers) currentBundleIdentifiers;
@property (T@"NSString",C,N,V_currentActiveBundleIdentifier) currentActiveBundleIdentifier;
@property (T@"UIView",W,N,V_preferredItemViewToFocus) preferredItemViewToFocus;
@property (TB,N,GisShowingCallTimer,V_showingCallTimer) showingCallTimer;
```

## Instance methods

```
-[UIStatusBarCarPlayDockItemView layoutSubviews];
-[UIStatusBarCarPlayDockItemView hitTest:withEvent:];
-[UIStatusBarCarPlayDockItemView preferredFocusEnvironments];
-[UIStatusBarCarPlayDockItemView initWithFrame:];
-[UIStatusBarCarPlayDockItemView allowsUserInteraction];
-[UIStatusBarCarPlayDockItemView _toItemViewForBundleIdentifier:];
-[UIStatusBarCarPlayDockItemView itemThreeButton];
-[UIStatusBarCarPlayDockItemView _neededSizeWithCallTimer];
-[UIStatusBarCarPlayDockItemView _neededSizeWithoutCallTimer];
-[UIStatusBarCarPlayDockItemView _numberOfEnabledItems];
-[UIStatusBarCarPlayDockItemView _updateInCallDurationIfNecessary:];
-[UIStatusBarCarPlayDockItemView animatesDataChange];
-[UIStatusBarCarPlayDockItemView currentActiveBundleIdentifier];
-[UIStatusBarCarPlayDockItemView currentBundleIdentifiers];
-[UIStatusBarCarPlayDockItemView extraLeftPadding];
-[UIStatusBarCarPlayDockItemView extraRightPadding];
-[UIStatusBarCarPlayDockItemView inCallDurationLabel];
-[UIStatusBarCarPlayDockItemView inCallLabelSpacingConstraint];
-[UIStatusBarCarPlayDockItemView isShowingCallTimer];
-[UIStatusBarCarPlayDockItemView itemOneButton];
-[UIStatusBarCarPlayDockItemView itemOneTopConstraint];
-[UIStatusBarCarPlayDockItemView itemTwoButton];
-[UIStatusBarCarPlayDockItemView neededSizeForImageSet:];
-[UIStatusBarCarPlayDockItemView preferredItemViewToFocus];
-[UIStatusBarCarPlayDockItemView setCurrentActiveBundleIdentifier:];
-[UIStatusBarCarPlayDockItemView setCurrentBundleIdentifiers:];
-[UIStatusBarCarPlayDockItemView setInCallDurationLabel:];
-[UIStatusBarCarPlayDockItemView setInCallLabelSpacingConstraint:];
-[UIStatusBarCarPlayDockItemView setItemOneButton:];
-[UIStatusBarCarPlayDockItemView setItemOneTopConstraint:];
-[UIStatusBarCarPlayDockItemView setItemThreeButton:];
-[UIStatusBarCarPlayDockItemView setItemTwoButton:];
-[UIStatusBarCarPlayDockItemView setPreferredItemViewToFocus:];
-[UIStatusBarCarPlayDockItemView setShowingCallTimer:];
-[UIStatusBarCarPlayDockItemView updateForNewData:actions:];
-[UIStatusBarCarPlayDockItemView updateForNewStyle:];
```
