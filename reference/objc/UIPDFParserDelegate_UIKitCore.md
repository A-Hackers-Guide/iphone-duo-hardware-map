# `UIPDFParserDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXMLParserDelegate`
- 3 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
[4{CGPoint="x"d"y"d}] _p;
^{CGPath=} _path;
B _parserError;
```

## Properties

```
@property (T^{CGPath=},R,D) path;
@property (TB,R,V_parserError) parserError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFParserDelegate init];
-[UIPDFParserDelegate dealloc];
-[UIPDFParserDelegate path];
-[UIPDFParserDelegate parser:didEndElement:namespaceURI:qualifiedName:];
-[UIPDFParserDelegate parser:didStartElement:namespaceURI:qualifiedName:attributes:];
-[UIPDFParserDelegate parser:parseErrorOccurred:];
-[UIPDFParserDelegate parserDidStartDocument:];
-[UIPDFParserDelegate parserError];
```
