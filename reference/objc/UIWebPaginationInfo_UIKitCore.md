# `UIWebPaginationInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<WebDocumentView>" _documentView;
d _scaleFactor;
{CGSize="width"d"height"d} _layoutSize;
@"NSArray" _pageRects;
@"UIWebDocumentView" _webDocumentView;
```

## Properties

```
@property (TQ,R,N) pageCount;
@property (Td,R,N) lastPageHeight;
@property (T@"UIWebDocumentView",&,N,V_webDocumentView) webDocumentView;
```

## Instance methods

```
-[UIWebPaginationInfo pageCount];
-[UIWebPaginationInfo layoutSize];
-[UIWebPaginationInfo dealloc];
-[UIWebPaginationInfo scaleFactor];
-[UIWebPaginationInfo webDocumentView];
-[UIWebPaginationInfo documentView];
-[UIWebPaginationInfo initWithDocumentView:scaleFactor:layoutSize:pageRects:];
-[UIWebPaginationInfo lastPageHeight];
-[UIWebPaginationInfo pageRects];
-[UIWebPaginationInfo setWebDocumentView:];
-[UIWebPaginationInfo sizeForPageAtIndex:];
```
