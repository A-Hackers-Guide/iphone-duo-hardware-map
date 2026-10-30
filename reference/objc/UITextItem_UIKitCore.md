# `UITextItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"<_UITextItemContext>" _context;
q _contentType;
@"NSURL" _link;
@"NSTextAttachment" _textAttachment;
@"NSString" _tagIdentifier;
```

## Properties

```
@property (Tq,R,N,V_contentType) contentType;
@property (T{_NSRange=QQ},R,N) range;
@property (T@"NSURL",R,N,V_link) link;
@property (T@"NSTextAttachment",R,N,V_textAttachment) textAttachment;
@property (T@"NSString",R,N,V_tagIdentifier) tagIdentifier;
```

## Class methods

```
+[UITextItem _itemWithLink:context:];
+[UITextItem _itemWithTag:context:];
+[UITextItem _itemWithTextAttachment:context:];
```

## Instance methods

```
-[UITextItem range];
-[UITextItem contentType];
-[UITextItem hash];
-[UITextItem textAttachment];
-[UITextItem isEqual:];
-[UITextItem link];
-[UITextItem _context];
-[UITextItem _initWithType:context:];
-[UITextItem tagIdentifier];
```
