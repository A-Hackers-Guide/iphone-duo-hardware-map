# `UITextInputAssistantItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIBarButtonItemViewOwner`
- 13 instance variables, 20 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _allowsHidingShortcuts;
B _showsBarButtonItemsInline;
B _visibleWhenMinimized;
B _independentGroupSizes;
@"NSArray" _leadingBarButtonGroups;
@"NSArray" _trailingBarButtonGroups;
@"UIBarButtonItem" _keyboardActionButtonItem;
@"NSArray" _centerBarButtonGroups;
d _marginOverride;
@"UIColor" _detachedBackgroundColor;
@"UIBlurEffect" _detachedBackgroundEffect;
@"UIColor" _detachedTintColor;
@"UIAction" _dictationReplacementAction;
```

## Properties

```
@property (TB,R,N,G_isSystemItem) systemItem;
@property (TB,R,N,G_hasItemsToDisplay) hasItemsToDisplay;
@property (TB,R,N,G_requiresPredictionDisabled) requiresPredictionDisabled;
@property (TB,N,G_showsBarButtonItemsInline,S_setShowsBarButtonItemsInline:,V_showsBarButtonItemsInline) showsBarButtonItemsInline;
@property (TB,N,G_isVisibleWhenMinimized,S_setVisibleWhenMinimized:,V_visibleWhenMinimized) visibleWhenMinimized;
@property (T@"NSArray",C,N,G_centerBarButtonGroups,S_setCenterBarButtonGroups:,V_centerBarButtonGroups) centerBarButtonGroups;
@property (TB,N,G_independentGroupSizes,S_setIndependentGroupSizes:,V_independentGroupSizes) independentGroupSizes;
@property (Td,N,G_marginOverride,S_setMarginOverride:,V_marginOverride) marginOverride;
@property (T@"UIColor",&,N,G_detachedBackgroundColor,S_setDetachedBackgroundColor:,V_detachedBackgroundColor) detachedBackgroundColor;
@property (T@"UIBlurEffect",C,N,G_detachedBackgroundEffect,S_setDetachedBackgroundEffect:,V_detachedBackgroundEffect) detachedBackgroundEffect;
@property (T@"UIColor",&,N,G_detachedTintColor,S_setDetachedTintColor:,V_detachedTintColor) detachedTintColor;
@property (T@"UIAction",&,N,G_dictationReplacementAction,S_setDictationReplacementAction:,V_dictationReplacementAction) dictationReplacementAction;
@property (TB,N,V_allowsHidingShortcuts) allowsHidingShortcuts;
@property (T@"NSArray",C,N,V_leadingBarButtonGroups) leadingBarButtonGroups;
@property (T@"NSArray",C,N,V_trailingBarButtonGroups) trailingBarButtonGroups;
@property (T@"UIBarButtonItem",&,N,V_keyboardActionButtonItem) keyboardActionButtonItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextInputAssistantItem _keyboardDeleteItem];
```

## Instance methods

```
-[UITextInputAssistantItem _itemDidChangeWidth:];
-[UITextInputAssistantItem _itemDidChangeSelectionState:];
-[UITextInputAssistantItem _itemStandardViewNeedsUpdate:];
-[UITextInputAssistantItem _itemDidChangeEnabledState:];
-[UITextInputAssistantItem _itemCustomViewDidChange:fromView:];
-[UITextInputAssistantItem _itemDidChangeHiddenState:];
-[UITextInputAssistantItem init];
-[UITextInputAssistantItem _isSystemItem];
-[UITextInputAssistantItem setTrailingBarButtonGroups:];
-[UITextInputAssistantItem description];
-[UITextInputAssistantItem setLeadingBarButtonGroups:];
-[UITextInputAssistantItem _marginOverride];
-[UITextInputAssistantItem _setDictationReplacementAction:];
-[UITextInputAssistantItem _centerBarButtonGroups];
-[UITextInputAssistantItem _detachedBackgroundColor];
-[UITextInputAssistantItem _detachedBackgroundEffect];
-[UITextInputAssistantItem _detachedTintColor];
-[UITextInputAssistantItem _dictationReplacementAction];
-[UITextInputAssistantItem _hasItemsToDisplay];
-[UITextInputAssistantItem _independentGroupSizes];
-[UITextInputAssistantItem _isVisibleWhenMinimized];
-[UITextInputAssistantItem _requiresPredictionDisabled];
-[UITextInputAssistantItem _setCenterBarButtonGroups:];
-[UITextInputAssistantItem _setDetachedBackgroundColor:];
-[UITextInputAssistantItem _setDetachedBackgroundEffect:];
-[UITextInputAssistantItem _setDetachedTintColor:];
-[UITextInputAssistantItem _setIndependentGroupSizes:];
-[UITextInputAssistantItem _setMarginOverride:];
-[UITextInputAssistantItem _setShowsBarButtonItemsInline:];
-[UITextInputAssistantItem _setVisibleWhenMinimized:];
-[UITextInputAssistantItem _showsBarButtonItemsInline];
-[UITextInputAssistantItem allowsHidingShortcuts];
-[UITextInputAssistantItem keyboardActionButtonItem];
-[UITextInputAssistantItem leadingBarButtonGroups];
-[UITextInputAssistantItem setAllowsHidingShortcuts:];
-[UITextInputAssistantItem setKeyboardActionButtonItem:];
-[UITextInputAssistantItem trailingBarButtonGroups];
```
