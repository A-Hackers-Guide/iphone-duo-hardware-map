# `UIWebPDFSearchResult`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSArray" rotationAngles;
Q pageIndex;
@"NSArray" strings;
@"NSString" string;
@"NSArray" rects;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} boundingBox;
```

## Properties

```
@property (TQ,N,VpageIndex) pageIndex;
@property (T@"NSString",&,N,Vstring) string;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,VboundingBox) boundingBox;
@property (T@"NSArray",&,N,Vstrings) strings;
@property (T@"NSArray",&,N,Vrects) rects;
@property (T@"NSArray",&,N,VrotationAngles) rotationAngles;
```

## Instance methods

```
-[UIWebPDFSearchResult setBoundingBox:];
-[UIWebPDFSearchResult setPageIndex:];
-[UIWebPDFSearchResult dealloc];
-[UIWebPDFSearchResult string];
-[UIWebPDFSearchResult setString:];
-[UIWebPDFSearchResult boundingBox];
-[UIWebPDFSearchResult pageIndex];
-[UIWebPDFSearchResult strings];
-[UIWebPDFSearchResult setStrings:];
-[UIWebPDFSearchResult rects];
-[UIWebPDFSearchResult rotationAngles];
-[UIWebPDFSearchResult setRects:];
-[UIWebPDFSearchResult setRotationAngles:];
```
