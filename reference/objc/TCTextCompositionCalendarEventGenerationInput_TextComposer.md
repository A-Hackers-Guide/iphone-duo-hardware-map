# `TCTextCompositionCalendarEventGenerationInput`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _textBoxes;
@"NSArray" _paragraphBoxes;
@"NSArray" _paragraphGroupBoxes;
@"NSArray" _blockBoxes;
@"NSDictionary" _options;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_textBoxes) textBoxes;
@property (T@"NSArray",R,C,N,V_paragraphBoxes) paragraphBoxes;
@property (T@"NSArray",R,C,N,V_paragraphGroupBoxes) paragraphGroupBoxes;
@property (T@"NSArray",R,C,N,V_blockBoxes) blockBoxes;
@property (T@"NSDictionary",R,C,V_options) options;
```

## Class methods

```
+[TCTextCompositionCalendarEventGenerationInput supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionCalendarEventGenerationInput encodeWithCoder:];
-[TCTextCompositionCalendarEventGenerationInput initWithCoder:];
-[TCTextCompositionCalendarEventGenerationInput options];
-[TCTextCompositionCalendarEventGenerationInput copyWithZone:];
-[TCTextCompositionCalendarEventGenerationInput isEqual:];
-[TCTextCompositionCalendarEventGenerationInput blockBoxes];
-[TCTextCompositionCalendarEventGenerationInput initWithTextBoxes:paragraphBoxes:paragraphGroupBoxes:blockBoxes:options:];
-[TCTextCompositionCalendarEventGenerationInput paragraphBoxes];
-[TCTextCompositionCalendarEventGenerationInput paragraphGroupBoxes];
-[TCTextCompositionCalendarEventGenerationInput textBoxes];
```
