# `UIPDFAnnotationParserDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXMLParserDelegate`
- 3 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableString" _characters;
B _parseError;
@"UIPDFAnnotation" _annotation;
```

## Properties

```
@property (T@"UIPDFAnnotation",&,N,V_annotation) annotation;
@property (TB,R,N,V_parseError) parseError;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFAnnotationParserDelegate init];
-[UIPDFAnnotationParserDelegate dealloc];
-[UIPDFAnnotationParserDelegate annotation];
-[UIPDFAnnotationParserDelegate setAnnotation:];
-[UIPDFAnnotationParserDelegate parser:didEndElement:namespaceURI:qualifiedName:];
-[UIPDFAnnotationParserDelegate parser:didStartElement:namespaceURI:qualifiedName:attributes:];
-[UIPDFAnnotationParserDelegate parser:foundCharacters:];
-[UIPDFAnnotationParserDelegate parser:parseErrorOccurred:];
-[UIPDFAnnotationParserDelegate parserDidStartDocument:];
-[UIPDFAnnotationParserDelegate parseError];
```
