# `_UIKeyboardIntelligenceElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _isEditableText;
B _isTextLabel;
@"NSString" _text;
@"NSString" _contentType;
@"NSString" _prompt;
@"NSString" _accessibilityLabel;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_boundingBox) boundingBox;
@property (T@"NSString",C,N,V_text) text;
@property (T@"NSString",C,N,V_contentType) contentType;
@property (T@"NSString",C,N,V_prompt) prompt;
@property (TB,N,V_isEditableText) isEditableText;
@property (TB,N,V_isTextLabel) isTextLabel;
@property (T@"NSString",C,N,V_accessibilityLabel) accessibilityLabel;
```

## Instance methods

```
-[_UIKeyboardIntelligenceElement setContentType:];
-[_UIKeyboardIntelligenceElement prompt];
-[_UIKeyboardIntelligenceElement setBoundingBox:];
-[_UIKeyboardIntelligenceElement text];
-[_UIKeyboardIntelligenceElement init];
-[_UIKeyboardIntelligenceElement contentType];
-[_UIKeyboardIntelligenceElement boundingBox];
-[_UIKeyboardIntelligenceElement accessibilityLabel];
-[_UIKeyboardIntelligenceElement setText:];
-[_UIKeyboardIntelligenceElement setAccessibilityLabel:];
-[_UIKeyboardIntelligenceElement setPrompt:];
-[_UIKeyboardIntelligenceElement setIsTextLabel:];
-[_UIKeyboardIntelligenceElement isEditableText];
-[_UIKeyboardIntelligenceElement isTextLabel];
-[_UIKeyboardIntelligenceElement setIsEditableText:];
```
