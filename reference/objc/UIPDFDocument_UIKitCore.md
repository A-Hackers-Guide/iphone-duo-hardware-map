# `UIPDFDocument`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 6 properties, 24 instance methods, 1 class methods

## Instance variables

```
^{CGPDFDocument=} _cgDocument;
Q _numberOfPages;
d _cachedWidth;
d _cachedHeight;
@"NSString" _documentID;
@"NSString" _documentName;
@"UIPDFPageImageCache" _pageImageCache;
Q _imageCacheCount;
Q _imageCacheLookAhead;
d _imageCacheResolution;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _imageCacheLock;
@"UIPDFPageImageCache" _thumbnailCache;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _thumbnailLock;
@"<NSObject><UIPDFDocumentDelegate>" _delegate;
```

## Properties

```
@property (TQ,R,D) numberOfPages;
@property (T@"UIPDFPageImageCache",&,D) pageImageCache;
@property (T@"UIPDFPageImageCache",&,D) thumbnailCache;
@property (T^{CGPDFDocument=},R,V_cgDocument) CGDocument;
@property (T@"<NSObject><UIPDFDocumentDelegate>",N,V_delegate) delegate;
@property (T@"NSString",R,D) documentID;
```

## Class methods

```
+[UIPDFDocument documentNamed:];
```

## Instance methods

```
-[UIPDFDocument maxWidth];
-[UIPDFDocument dealloc];
-[UIPDFDocument setDelegate:];
-[UIPDFDocument delegate];
-[UIPDFDocument numberOfPages];
-[UIPDFDocument maxHeight];
-[UIPDFDocument initWithURL:];
-[UIPDFDocument CGDocument];
-[UIPDFDocument allowsCopying];
-[UIPDFDocument copyCGPDFDocument];
-[UIPDFDocument copyPageAtIndex:];
-[UIPDFDocument documentID];
-[UIPDFDocument initWithCGPDFDocument:];
-[UIPDFDocument initWithCGPDFDocumentLimitedMemory:];
-[UIPDFDocument pageAtIndex:];
-[UIPDFDocument pageImageCache];
-[UIPDFDocument purgePagesBefore:];
-[UIPDFDocument setImageCacheCount:lookAhead:withResolution:];
-[UIPDFDocument setPageImageCache:];
-[UIPDFDocument setThumbnailCache:];
-[UIPDFDocument sumHeight];
-[UIPDFDocument sumWidth];
-[UIPDFDocument thumbnailCache];
-[UIPDFDocument updateWidthHeightCache];
```
