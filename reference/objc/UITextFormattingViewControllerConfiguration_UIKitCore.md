# `UITextFormattingViewControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 15 properties, 39 instance methods, 2 class methods

## Instance variables

```
B __textAnimationsConfiguration;
B __textViewConfiguration;
B __useReducedMetrics;
B __hasPopoverPresentation;
B __useLandscapeLayout;
B __hasParentViewController;
B __hasSubstituteKeyboardPadPresentation;
B __preferringDimmingVisible;
B __allowContentToScroll;
B __includeDefaultFont;
@"NSArray" _groups;
@"NSArray" _formattingStyles;
@"UIFontPickerViewControllerConfiguration" _fontPickerConfiguration;
d __substituteKeyboardHeight;
@"NSArray" __emphasisStyles;
```

## Properties

```
@property (TB,N,V__textAnimationsConfiguration) _textAnimationsConfiguration;
@property (TB,N,V__textViewConfiguration) _textViewConfiguration;
@property (TB,N,V__useReducedMetrics) _useReducedMetrics;
@property (TB,N,S_setHasPopoverPresentation:,V__hasPopoverPresentation) _hasPopoverPresentation;
@property (TB,N,S_setUseLandscapeLayout:,V__useLandscapeLayout) _useLandscapeLayout;
@property (TB,N,S_setHasParentViewController:,V__hasParentViewController) _hasParentViewController;
@property (TB,N,V__hasSubstituteKeyboardPadPresentation) _hasSubstituteKeyboardPadPresentation;
@property (Td,N,V__substituteKeyboardHeight) _substituteKeyboardHeight;
@property (TB,N,V__preferringDimmingVisible) _preferringDimmingVisible;
@property (TB,N,V__allowContentToScroll) _allowContentToScroll;
@property (TB,N,V__includeDefaultFont) _includeDefaultFont;
@property (T@"NSArray",C,N,V__emphasisStyles) _emphasisStyles;
@property (T@"NSArray",R,C,N,V_groups) groups;
@property (T@"NSArray",C,N,V_formattingStyles) formattingStyles;
@property (T@"UIFontPickerViewControllerConfiguration",C,N,V_fontPickerConfiguration) fontPickerConfiguration;
```

## Class methods

```
+[UITextFormattingViewControllerConfiguration supportsSecureCoding];
+[UITextFormattingViewControllerConfiguration _forTextAnimationsUIWithSupportedAnimationNames:titles:accessibilityHints:];
```

## Instance methods

```
-[UITextFormattingViewControllerConfiguration set_hasSubstituteKeyboardPadPresentation:];
-[UITextFormattingViewControllerConfiguration _textViewConfiguration];
-[UITextFormattingViewControllerConfiguration init];
-[UITextFormattingViewControllerConfiguration _allowContentToScroll];
-[UITextFormattingViewControllerConfiguration _hasParentViewController];
-[UITextFormattingViewControllerConfiguration _hasPopoverPresentation];
-[UITextFormattingViewControllerConfiguration _hasSubstituteKeyboardPadPresentation];
-[UITextFormattingViewControllerConfiguration _isUsingReducedMetrics];
-[UITextFormattingViewControllerConfiguration _emphasisStyles];
-[UITextFormattingViewControllerConfiguration set_preferringDimmingVisible:];
-[UITextFormattingViewControllerConfiguration set_textAnimationsConfiguration:];
-[UITextFormattingViewControllerConfiguration setFormattingStyles:];
-[UITextFormattingViewControllerConfiguration set_allowContentToScroll:];
-[UITextFormattingViewControllerConfiguration _preferringDimmingVisible];
-[UITextFormattingViewControllerConfiguration _setUseLandscapeLayout:];
-[UITextFormattingViewControllerConfiguration _setHasPopoverPresentation:];
-[UITextFormattingViewControllerConfiguration formattingStyles];
-[UITextFormattingViewControllerConfiguration groups];
-[UITextFormattingViewControllerConfiguration _useLandscapeLayout];
-[UITextFormattingViewControllerConfiguration set_textViewConfiguration:];
-[UITextFormattingViewControllerConfiguration set_useReducedMetrics:];
-[UITextFormattingViewControllerConfiguration set_emphasisStyles:];
-[UITextFormattingViewControllerConfiguration initWithGroups:];
-[UITextFormattingViewControllerConfiguration _isTextViewConfiguration];
-[UITextFormattingViewControllerConfiguration encodeWithCoder:];
-[UITextFormattingViewControllerConfiguration hash];
-[UITextFormattingViewControllerConfiguration initWithCoder:];
-[UITextFormattingViewControllerConfiguration _setHasParentViewController:];
-[UITextFormattingViewControllerConfiguration _substituteKeyboardHeight];
-[UITextFormattingViewControllerConfiguration set_includeDefaultFont:];
-[UITextFormattingViewControllerConfiguration _includeDefaultFont];
-[UITextFormattingViewControllerConfiguration _useReducedMetrics];
-[UITextFormattingViewControllerConfiguration copyWithZone:];
-[UITextFormattingViewControllerConfiguration fontPickerConfiguration];
-[UITextFormattingViewControllerConfiguration set_substituteKeyboardHeight:];
-[UITextFormattingViewControllerConfiguration setFontPickerConfiguration:];
-[UITextFormattingViewControllerConfiguration isEqual:];
-[UITextFormattingViewControllerConfiguration _textAnimationsConfiguration];
-[UITextFormattingViewControllerConfiguration _isTextAnimationsConfiguration];
```
