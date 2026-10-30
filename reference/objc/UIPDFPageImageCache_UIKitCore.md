# `UIPDFPageImageCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIPDFDocument" _document;
Q _lookAhead;
d _lookAheadResolution;
Q _jobCount;
^@ _jobsPrioritized;
Q _nextJobIndex;
Q _pageCount;
^@ _jobsByPage;
@"NSOperationQueue" _renderQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
i jobsComplete;
```

## Properties

```
@property (T@"UIPDFDocument",R,V_document) document;
@property (TQ,R,V_pageCount) pageCount;
@property (TQ,R,V_lookAhead) lookAhead;
@property (Td,R,V_lookAheadResolution) lookAheadResolution;
```

## Instance methods

```
-[UIPDFPageImageCache clearCache];
-[UIPDFPageImageCache pageCount];
-[UIPDFPageImageCache document];
-[UIPDFPageImageCache initWithDocument:];
-[UIPDFPageImageCache dealloc];
-[UIPDFPageImageCache addRenderJob:];
-[UIPDFPageImageCache cacheImageOfPage:maxSize:];
-[UIPDFPageImageCache cancelPendingRenderOperations];
-[UIPDFPageImageCache cancelPendingRenderOperationsForTarget:];
-[UIPDFPageImageCache deliverImageOfPage:maxSize:quality:receiver:selector:info:];
-[UIPDFPageImageCache didReceiveMemoryWarning:];
-[UIPDFPageImageCache getImageIfAvailableForPage:];
-[UIPDFPageImageCache getRenderQueueJobsCount];
-[UIPDFPageImageCache initWithDocument:cacheCount:lookAhead:withLookAheadResolution:];
-[UIPDFPageImageCache lookAhead];
-[UIPDFPageImageCache lookAheadResolution];
```
