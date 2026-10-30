# `UIPDFPage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 32 instance methods, 0 class methods

## Instance variables

```
^{CGPDFPage=} _cgPage;
Q _pageNumber;
@"NSString" _stringInReadingOrder;
@"UIPDFSelection" _selection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"UIPDFDocument" _document;
Q _pageIndex;
@"UIImage" _pageImage;
@"NSMutableArray" _annotations;
```

## Properties

```
@property (T^{CGPDFPage=},R,V_cgPage) CGPage;
@property (TQ,R,V_pageNumber) pageNumber;
@property (TQ,R,V_pageIndex) pageIndex;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) cropBox;
@property (T@"UIPDFDocument",R,V_document) document;
@property (T@"UIImage",&,V_pageImage) pageImage;
@property (T@"UIPDFSelection",&,V_selection) selection;
```

## Instance methods

```
-[UIPDFPage selection];
-[UIPDFPage setSelection:];
-[UIPDFPage annotations];
-[UIPDFPage rotation];
-[UIPDFPage document];
-[UIPDFPage refresh];
-[UIPDFPage dealloc];
-[UIPDFPage string];
-[UIPDFPage setDocument:];
-[UIPDFPage size];
-[UIPDFPage pageIndex];
-[UIPDFPage addAnnotation:];
-[UIPDFPage pageNumber];
-[UIPDFPage cropBox];
-[UIPDFPage CGPage];
-[UIPDFPage annotationIn:withIndex:];
-[UIPDFPage cfCompareFlagsFromNSOptions:];
-[UIPDFPage clearAnnotations];
-[UIPDFPage copyPage];
-[UIPDFPage cropBoxAccountForRotation];
-[UIPDFPage deliverImageWithWidth:height:receiver:selector:info:];
-[UIPDFPage drawInRect:context:];
-[UIPDFPage findString:fromSelection:options:];
-[UIPDFPage getImageIfAvailable];
-[UIPDFPage initWithCGPDFPage:];
-[UIPDFPage initWithDocument:pageNumber:];
-[UIPDFPage mediaBox];
-[UIPDFPage mediaBoxAccountForRotation];
-[UIPDFPage pageImage];
-[UIPDFPage removeAllAnnotations];
-[UIPDFPage removeAnnotation:];
-[UIPDFPage setPageImage:];
```
