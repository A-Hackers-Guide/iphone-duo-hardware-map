# `_UISwipeActionDynamicButtonView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UISwipeActionDynamicButtonDelegate`
- 16 instance variables, 20 properties, 35 instance methods, 6 class methods

## Instance variables

```
B _canUseInlineStyle;
B _canUseUniformInlineWidth;
@"UIButtonConfiguration" _buttonConfiguration;
d _uniformInlineWidth;
d _uniformWidth;
d _uniformHeight;
@"NSSet" _buttonTypes;
@"<_UISwipeActionDynamicButtonViewDelegate>" _delegate;
@"NSString" _title;
@"UIImage" _buttonImage;
@"UIColor" _buttonBackgroundColor;
@"UIMenu" _buttonMenu;
Q _state;
@"_UISwipeActionDynamicButton" _button;
@"UILabel" _titleLabel;
{CGSize="width"d"height"d} _preferredSize;
```

## Properties

```
@property (T@"_UISwipeActionDynamicButton",R,N,V_button) button;
@property (T@"UIButtonConfiguration",R,N,V_buttonConfiguration) buttonConfiguration;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (T{CGSize=dd},R,N,V_preferredSize) preferredSize;
@property (Td,N,V_uniformInlineWidth) uniformInlineWidth;
@property (Td,N,V_uniformWidth) uniformWidth;
@property (Td,N,V_uniformHeight) uniformHeight;
@property (T@"NSSet",&,N,V_buttonTypes) buttonTypes;
@property (TB,N,V_canUseInlineStyle) canUseInlineStyle;
@property (TB,N,V_canUseUniformInlineWidth) canUseUniformInlineWidth;
@property (T@"<_UISwipeActionDynamicButtonViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",C,N,V_title) title;
@property (T@"UIImage",&,N,V_buttonImage) buttonImage;
@property (T@"UIColor",&,N,V_buttonBackgroundColor) buttonBackgroundColor;
@property (T@"UIMenu",&,N,V_buttonMenu) buttonMenu;
@property (TQ,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISwipeActionDynamicButtonView defaultButtonConfiguration];
+[_UISwipeActionDynamicButtonView defaultTitleLabel];
+[_UISwipeActionDynamicButtonView imageOnlyButtonWidth:buttonTypes:];
+[_UISwipeActionDynamicButtonView maximumButtonHeight];
+[_UISwipeActionDynamicButtonView preferredSymbolConfigurationForImage];
+[_UISwipeActionDynamicButtonView preferredTitleFont];
```

## Instance methods

```
-[_UISwipeActionDynamicButtonView setState:];
-[_UISwipeActionDynamicButtonView titleLabel];
-[_UISwipeActionDynamicButtonView button];
-[_UISwipeActionDynamicButtonView layoutSubviews];
-[_UISwipeActionDynamicButtonView setBounds:];
-[_UISwipeActionDynamicButtonView setDelegate:];
-[_UISwipeActionDynamicButtonView title];
-[_UISwipeActionDynamicButtonView delegate];
-[_UISwipeActionDynamicButtonView setFrame:];
-[_UISwipeActionDynamicButtonView setTitle:];
-[_UISwipeActionDynamicButtonView initWithFrame:];
-[_UISwipeActionDynamicButtonView preferredSize];
-[_UISwipeActionDynamicButtonView state];
-[_UISwipeActionDynamicButtonView setButtonImage:];
-[_UISwipeActionDynamicButtonView setButtonTypes:];
-[_UISwipeActionDynamicButtonView _buttonDidTouchUpInInside:];
-[_UISwipeActionDynamicButtonView buttonBackgroundColor];
-[_UISwipeActionDynamicButtonView buttonConfiguration];
-[_UISwipeActionDynamicButtonView buttonImage];
-[_UISwipeActionDynamicButtonView buttonMenu];
-[_UISwipeActionDynamicButtonView buttonTypes];
-[_UISwipeActionDynamicButtonView canUseInlineStyle];
-[_UISwipeActionDynamicButtonView canUseUniformInlineWidth];
-[_UISwipeActionDynamicButtonView setButtonBackgroundColor:];
-[_UISwipeActionDynamicButtonView setButtonMenu:];
-[_UISwipeActionDynamicButtonView setCanUseInlineStyle:];
-[_UISwipeActionDynamicButtonView setCanUseUniformInlineWidth:];
-[_UISwipeActionDynamicButtonView setUniformHeight:];
-[_UISwipeActionDynamicButtonView setUniformInlineWidth:];
-[_UISwipeActionDynamicButtonView setUniformWidth:];
-[_UISwipeActionDynamicButtonView swipeActionWillDisplayMenuForButton:];
-[_UISwipeActionDynamicButtonView uniformHeight];
-[_UISwipeActionDynamicButtonView uniformInlineWidth];
-[_UISwipeActionDynamicButtonView uniformWidth];
-[_UISwipeActionDynamicButtonView updateButtonConfiguration];
```
