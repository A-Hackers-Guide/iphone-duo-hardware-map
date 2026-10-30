# `TCAttributedStringFormatter`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSAttributedString" _digestedAttributedString;
@"NSString" _inputFormattedString;
@"TCAttributedStringFormatOptions" _formatOptions;
```

## Properties

```
@property (T@"NSAttributedString",R,C,V_digestedAttributedString) digestedAttributedString;
@property (T@"NSString",R,C,V_inputFormattedString) inputFormattedString;
@property (T@"TCAttributedStringFormatOptions",R,C,V_formatOptions) formatOptions;
```

## Class methods

```
+[TCAttributedStringFormatter supportsSecureCoding];
+[TCAttributedStringFormatter digestedAttributedStringFromFormattedString:formatOptions:];
```

## Instance methods

```
-[TCAttributedStringFormatter encodeWithCoder:];
-[TCAttributedStringFormatter hash];
-[TCAttributedStringFormatter description];
-[TCAttributedStringFormatter initWithCoder:];
-[TCAttributedStringFormatter copyWithZone:];
-[TCAttributedStringFormatter isEqual:];
-[TCAttributedStringFormatter formatOptions];
-[TCAttributedStringFormatter digestedAttributedString];
-[TCAttributedStringFormatter digestedAttributedStringFromFormattedString:];
-[TCAttributedStringFormatter initWithDigestedAttributedString:formatOptions:];
-[TCAttributedStringFormatter initWithDigestedAttributedString:inputFormattedString:formatOptions:];
-[TCAttributedStringFormatter inputFormattedString];
```
