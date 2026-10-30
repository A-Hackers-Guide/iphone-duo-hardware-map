# `UIRecentInputTableCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCell`
- 5 instance variables, 6 properties, 22 instance methods, 5 class methods

## Instance variables

```
@"UILabel" _floatingLabel;
q _blurEffectStyle;
@"UITextInputTraits" _textInputTraits;
@"CALayer" _secureLabelImageLayer;
@"UILexiconEntry" _entry;
```

## Properties

```
@property (Tq,N,V_blurEffectStyle) blurEffectStyle;
@property (T@"UITextInputTraits",&,N,V_textInputTraits) textInputTraits;
@property (T@"CALayer",&,N,V_secureLabelImageLayer) secureLabelImageLayer;
@property (T@"UILexiconEntry",&,N,V_entry) entry;
@property (T@"UILabel",&,N,V_floatingLabel) floatingLabel;
@property (T@"_UIFloatingContentView",R,N) floatingContentView;
```

## Class methods

```
+[UIRecentInputTableCell backgroundColorForBlurEffectStyle:];
+[UIRecentInputTableCell defaultFocusedSecureCandidateRenderTraits];
+[UIRecentInputTableCell defaultUnfocusedSecureCandidateRenderTraitsForUserInterfaceStyle:];
+[UIRecentInputTableCell focusedTextColorForBlurEffectStyle:];
+[UIRecentInputTableCell unfocusedTextColorForBlurEffectStyle:];
```

## Instance methods

```
-[UIRecentInputTableCell textInputTraits];
-[UIRecentInputTableCell setTextInputTraits:];
-[UIRecentInputTableCell blurEffectStyle];
-[UIRecentInputTableCell _updateAppearance];
-[UIRecentInputTableCell didUpdateFocusInContext:withAnimationCoordinator:];
-[UIRecentInputTableCell setHighlighted:animated:];
-[UIRecentInputTableCell dealloc];
-[UIRecentInputTableCell layoutSubviews];
-[UIRecentInputTableCell prepareForReuse];
-[UIRecentInputTableCell floatingContentView];
-[UIRecentInputTableCell traitCollectionDidChange:];
-[UIRecentInputTableCell entry];
-[UIRecentInputTableCell setSecureLabel:];
-[UIRecentInputTableCell _tvIsDarkMode];
-[UIRecentInputTableCell floatingLabel];
-[UIRecentInputTableCell secureLabelImageLayer];
-[UIRecentInputTableCell setBlurEffectStyle:];
-[UIRecentInputTableCell setEntry:];
-[UIRecentInputTableCell setFloatingLabel:];
-[UIRecentInputTableCell setInputText:withBlurStyle:];
-[UIRecentInputTableCell setSecureLabelImageLayer:];
-[UIRecentInputTableCell teardownSecureLabelImageLayerIfNeeded];
```
