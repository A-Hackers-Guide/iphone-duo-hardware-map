# `UIPDFWidget`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
i queueIndex;
i queueCount;
[60{?="byteCount"i"currentPageCount"i"renderJobsCount"i"memWarning"B}] queueData;
i currentPageCount;
i totalPageCount;
i renderJobsCount;
@"NSTimer" heartbeatTimer;
@"UILabel" infoLabel;
@"UIPDFDocument" activeDocument;
@"NSMutableSet" trackedPages;
```

## Instance methods

```
-[UIPDFWidget dealloc];
-[UIPDFWidget drawRect:];
-[UIPDFWidget addedPageView:];
-[UIPDFWidget didReceiveMemoryWarning:];
-[UIPDFWidget heartbeat];
-[UIPDFWidget initWithFrame:withDocument:];
-[UIPDFWidget removedPageView:];
```
