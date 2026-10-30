# `_UITextStyleDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `NSCoding`, `BSDescriptionStreaming`
- 2 instance variables, 5 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"UIFontDescriptor" fontDescriptor;
? additionalAttributes;
```

## Properties

```
@property (T@"UIFontDescriptor",N,R,VfontDescriptor) fontDescriptor;
@property (T@"NSDictionary",N,R) additionalAttributes;
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Class methods

```
+[_UITextStyleDescriptor supportsSecureCoding];
+[_UITextStyleDescriptor boldDescriptor];
+[_UITextStyleDescriptor italicsDescriptor];
+[_UITextStyleDescriptor underlineDescriptor];
```

## Instance methods

```
-[_UITextStyleDescriptor debugDescription];
-[_UITextStyleDescriptor init];
-[_UITextStyleDescriptor encodeWithCoder:];
-[_UITextStyleDescriptor fontDescriptor];
-[_UITextStyleDescriptor hash];
-[_UITextStyleDescriptor description];
-[_UITextStyleDescriptor initWithCoder:];
-[_UITextStyleDescriptor appendDescriptionToStream:];
-[_UITextStyleDescriptor copyWithZone:];
-[_UITextStyleDescriptor isEqual:];
-[_UITextStyleDescriptor additionalAttributes];
-[_UITextStyleDescriptor attributedStringByApplyingToAttributedString:];
-[_UITextStyleDescriptor attributedStringByApplyingToAttributedString:fallbackFont:];
-[_UITextStyleDescriptor initWithFontDescriptor:additionalAttributes:];
```
