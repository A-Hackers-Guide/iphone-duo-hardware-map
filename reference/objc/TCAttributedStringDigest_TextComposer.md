# `TCAttributedStringDigest`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 13 instance methods, 10 class methods

## Instance variables

```
@"NSDictionary" _attributeDictionary;
@"NSDictionary" _attachmentDictionary;
@"TCAttributedStringFormatter" _attributedStringFormatter;
```

## Properties

```
@property (T@"NSAttributedString",R,C) digestedAttributedString;
@property (T@"TCAttributedStringFormatter",R,C,V_attributedStringFormatter) attributedStringFormatter;
@property (T@"NSString",R,C) inputFormattedString;
@property (T@"TCAttributedStringFormatOptions",R,C) formatOptions;
```

## Class methods

```
+[TCAttributedStringDigest presentableAttributedString:withAttributes:];
+[TCAttributedStringDigest reconstituteAttributedStringFromDigestedAttributedString:formatOptions:attributes:];
+[TCAttributedStringDigest reconstituteAttributedStringFromDigestedAttributedString:formatOptions:attributes:attachments:];
+[TCAttributedStringDigest reconstituteAttributedStringFromFormattedString:formatOptions:attributes:];
+[TCAttributedStringDigest reconstituteAttributedStringFromFormattedString:formatOptions:attributes:attachments:];
+[TCAttributedStringDigest useFontStyles];
+[TCAttributedStringDigest useTextAttachments];
+[TCAttributedStringDigest useTextLists];
+[TCAttributedStringDigest useTextTables];
+[TCAttributedStringDigest useUTTypes];
```

## Instance methods

```
-[TCAttributedStringDigest initWithAttributedString:range:];
-[TCAttributedStringDigest formatOptions];
-[TCAttributedStringDigest attributedStringFormatter];
-[TCAttributedStringDigest digestedAttributedString];
-[TCAttributedStringDigest initWithAttributedString:formatOptions:];
-[TCAttributedStringDigest initWithAttributedString:range:formatOptions:];
-[TCAttributedStringDigest inputFormattedString];
-[TCAttributedStringDigest reconstituteAttributedString:];
-[TCAttributedStringDigest reconstituteAttributedString:addAttributes:];
-[TCAttributedStringDigest reconstituteAttributedStringFromDigestedAttributedString:];
-[TCAttributedStringDigest reconstituteAttributedStringFromDigestedAttributedString:attachments:];
-[TCAttributedStringDigest reconstituteAttributedStringFromFormattedString:];
-[TCAttributedStringDigest reconstituteAttributedStringFromFormattedString:attachments:];
```
