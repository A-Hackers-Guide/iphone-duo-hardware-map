# `UITextFormattingViewControllerChangeValue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 14 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSString" _changeType;
@"NSString" _formattingStyleKey;
@"UIFont" _font;
@"UIColor" _color;
@"NSNumber" _numberValue;
@"NSString" _textList;
q _textAlignment;
@"NSString" _highlight;
@"NSString" __customComponentKey;
@"NSString" __emphasisStyleKey;
@"NSString" __textAnimationName;
@"NSDictionary" __textAnimationAttributes;
```

## Properties

```
@property (T@"NSString",N,R) _textAnimationName;
@property (T@"NSDictionary",N,R) _textAnimationAttributes;
@property (T@"NSString",R,C,N,V__customComponentKey) _customComponentKey;
@property (T@"NSString",R,C,N,V__emphasisStyleKey) _emphasisStyleKey;
@property (T@"NSString",R,N,V__textAnimationName) _textAnimationName;
@property (T@"NSDictionary",R,N,V__textAnimationAttributes) _textAnimationAttributes;
@property (T@"NSString",R,N,V_changeType) changeType;
@property (T@"NSString",R,C,N,V_formattingStyleKey) formattingStyleKey;
@property (T@"UIFont",R,C,N,V_font) font;
@property (T@"UIColor",R,C,N,V_color) color;
@property (T@"NSNumber",R,C,N,V_numberValue) numberValue;
@property (T@"NSString",R,C,N,V_textList) textList;
@property (Tq,R,N,V_textAlignment) textAlignment;
@property (T@"NSString",R,C,N,V_highlight) highlight;
```

## Class methods

```
+[UITextFormattingViewControllerChangeValue supportsSecureCoding];
```

## Instance methods

```
-[UITextFormattingViewControllerChangeValue textAlignment];
-[UITextFormattingViewControllerChangeValue numberValue];
-[UITextFormattingViewControllerChangeValue textList];
-[UITextFormattingViewControllerChangeValue color];
-[UITextFormattingViewControllerChangeValue changeType];
-[UITextFormattingViewControllerChangeValue encodeWithCoder:];
-[UITextFormattingViewControllerChangeValue _textAnimationName];
-[UITextFormattingViewControllerChangeValue _textAnimationName];
-[UITextFormattingViewControllerChangeValue initWithCoder:];
-[UITextFormattingViewControllerChangeValue font];
-[UITextFormattingViewControllerChangeValue highlight];
-[UITextFormattingViewControllerChangeValue copyWithZone:];
-[UITextFormattingViewControllerChangeValue initWithChangeType:numberValue:];
-[UITextFormattingViewControllerChangeValue _customComponentKey];
-[UITextFormattingViewControllerChangeValue _emphasisStyleKey];
-[UITextFormattingViewControllerChangeValue _textAnimationAttributes];
-[UITextFormattingViewControllerChangeValue _textAnimationAttributes];
-[UITextFormattingViewControllerChangeValue formattingStyleKey];
-[UITextFormattingViewControllerChangeValue initWithChangeType:];
-[UITextFormattingViewControllerChangeValue initWithChangeType:customComponentKey:];
-[UITextFormattingViewControllerChangeValue initWithEmphasisStyleKey:];
-[UITextFormattingViewControllerChangeValue initWithFont:];
-[UITextFormattingViewControllerChangeValue initWithFormattingStyleKey:];
-[UITextFormattingViewControllerChangeValue initWithHighlight:];
-[UITextFormattingViewControllerChangeValue initWithTextAlignment:];
-[UITextFormattingViewControllerChangeValue initWithTextColor:];
-[UITextFormattingViewControllerChangeValue initWithTextList:];
```
