# `UIPDFPageRenderJob`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIPDFPage" _page;
Q _pageIndex;
{CGSize="width"d"height"d} _size;
q _priority;
@"UIImage" _image;
@"UIPDFPageRenderOperation" _operation;
@ _target;
: _callback;
@ _userData;
B _sendPending;
B _releaseWhenDone;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@"UIImage",R,&,D) image;
@property (T@"UIPDFPageRenderOperation",D) operation;
@property (TQ,R,V_pageIndex) pageIndex;
@property (Tq,R,V_priority) priority;
@property (TB,V_releaseWhenDone) releaseWhenDone;
@property (T{CGSize=dd},R,V_size) size;
```

## Instance methods

```
-[UIPDFPageRenderJob priority];
-[UIPDFPageRenderJob setOperation:];
-[UIPDFPageRenderJob operation];
-[UIPDFPageRenderJob hasPage];
-[UIPDFPageRenderJob dealloc];
-[UIPDFPageRenderJob size];
-[UIPDFPageRenderJob pageIndex];
-[UIPDFPageRenderJob image];
-[UIPDFPageRenderJob cancel];
-[UIPDFPageRenderJob cancelOperation];
-[UIPDFPageRenderJob releaseWhenDone];
-[UIPDFPageRenderJob cancelOperationForTarget:];
-[UIPDFPageRenderJob initWithPage:maxSize:queuePriority:];
-[UIPDFPageRenderJob releaseOperation];
-[UIPDFPageRenderJob renderImage];
-[UIPDFPageRenderJob sendImage];
-[UIPDFPageRenderJob sendImageTo:callback:userData:];
-[UIPDFPageRenderJob setReleaseWhenDone:];
-[UIPDFPageRenderJob setTarget:callback:userData:];
```
