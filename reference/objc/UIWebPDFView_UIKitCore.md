# `UIWebPDFView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPDFPageViewDelegate`, `UIPDFAnnotationControllerDelegate`, `WebPDFViewPlaceholderDelegate`, `UIPopoverControllerDelegate`, `UIGestureRecognizerDelegate`
- 25 instance variables, 23 properties, 84 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _backingLayerImageViews;
^{CGPDFDocument=} _cgPDFDocument;
@"UIPDFDocument" _document;
B _hasScheduledCacheUpdate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _documentBounds;
@"NSObject<UIWebPDFViewDelegate>" _pdfDelegate;
B _delegateRespondsToDidScroll;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"NSURL" _documentURL;
B _rotating;
B _zooming;
d _initialZoomScale;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _documentTransform;
d _documentScale;
q _ignoreContentOffsetChanges;
{CGPoint="x"d"y"d} _contentOffsetAtScrollStart;
@"NSMutableArray" _pageViews;
@"NSArray" _pageMinYs;
B hidePageViewsUntilReadyToRender;
B hideActivityIndicatorForUnRenderedContent;
B readyForSnapshot;
@"WebPDFViewPlaceholder" pdfPlaceHolderView;
@"UIColor" backgroundColorForUnRenderedContent;
@"NSString" documentPassword;
@"NSArray" pageRects;
```

## Properties

```
@property (T@"WebPDFViewPlaceholder",VpdfPlaceHolderView) pdfPlaceHolderView;
@property (T@"NSURL",&,N,V_documentURL) documentURL;
@property (Td,N,V_initialZoomScale) initialZoomScale;
@property (T@"UIColor",&,N,VbackgroundColorForUnRenderedContent) backgroundColorForUnRenderedContent;
@property (TB,N,VhideActivityIndicatorForUnRenderedContent) hideActivityIndicatorForUnRenderedContent;
@property (TB,N,VhidePageViewsUntilReadyToRender) hidePageViewsUntilReadyToRender;
@property (Tq,N,V_ignoreContentOffsetChanges) ignoreContentOffsetChanges;
@property (T{CGAffineTransform=dddddd},N,V_documentTransform) documentTransform;
@property (T@"NSString",&,N,VdocumentPassword) documentPassword;
@property (Td,R,N,V_documentScale) documentScale;
@property (T@"NSArray",&,N,VpageRects) pageRects;
@property (TB,N,VreadyForSnapshot) readyForSnapshot;
@property (T@"NSArray",&,N,V_pageMinYs) pageMinYs;
@property (T@"NSObject<UIWebPDFViewDelegate>",N,V_pdfDelegate) pdfDelegate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_documentBounds) documentBounds;
@property (TQ,R,N) totalPages;
@property (T^{CGPDFDocument=},R,N) cgPDFDocument;
@property (T@"UIPDFDocument",R,N) document;
@property (T@"NSData",R,N) documentData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIWebPDFView initialize];
+[UIWebPDFView setAsPDFDocRepAndView];
```

## Instance methods

```
-[UIWebPDFView _share:];
-[UIWebPDFView clearSelection];
-[UIWebPDFView _define:];
-[UIWebPDFView _translate:];
-[UIWebPDFView observeValueForKeyPath:ofObject:change:context:];
-[UIWebPDFView document];
-[UIWebPDFView dealloc];
-[UIWebPDFView documentURL];
-[UIWebPDFView gestureRecognizerShouldBegin:];
-[UIWebPDFView _tapGestureRecognized:];
-[UIWebPDFView canPerformAction:withSender:];
-[UIWebPDFView setDocumentURL:];
-[UIWebPDFView ensureCorrectPagesAreInstalled:];
-[UIWebPDFView hidePageViewsUntilReadyToRender];
-[UIWebPDFView setPdfDelegate:];
-[UIWebPDFView _addPageAtIndex:];
-[UIWebPDFView _addSubViewsInViewCoordsBounds:force:];
-[UIWebPDFView _checkIfDocumentNeedsUnlock];
-[UIWebPDFView _didLongPress:inRect:atPoint:linkingToPageIndex:];
-[UIWebPDFView _didLongPress:inRect:atPoint:linkingToURL:];
-[UIWebPDFView _didScroll];
-[UIWebPDFView _didTouch:inRect:atPoint:linkingToPageIndex:];
-[UIWebPDFView _didTouch:inRect:atPoint:linkingToURL:];
-[UIWebPDFView _hasPageRects];
-[UIWebPDFView _installViewAtIndex:inFrame:];
-[UIWebPDFView _pageNumberForRect:];
-[UIWebPDFView _pageWithSelection];
-[UIWebPDFView _recreateUIPDFDocument];
-[UIWebPDFView _removeBackgroundImageObserverIfNeeded:];
-[UIWebPDFView _removePageViewsNotInCurrentViewCoordsRect];
-[UIWebPDFView _removePageViewsNotInViewCoordsRect:];
-[UIWebPDFView _scheduleRemovePageViewsNotInViewCoordsRect];
-[UIWebPDFView _selection];
-[UIWebPDFView _tryToUnlockDocumentWithPassword:];
-[UIWebPDFView _viewCachingBoundsInUIViewCoords];
-[UIWebPDFView _viewportBoundsInUIVIewCoordsWithView:];
-[UIWebPDFView _viewportBoundsInUIViewCoords];
-[UIWebPDFView annotation:isBeingPressedAtPoint:controller:];
-[UIWebPDFView annotation:wasTouchedAtPoint:controller:];
-[UIWebPDFView backgroundColorForUnRenderedContent];
-[UIWebPDFView cgPDFDocument];
-[UIWebPDFView didCompleteLayout];
-[UIWebPDFView didReceiveMemoryWarning:];
-[UIWebPDFView didRotate:];
-[UIWebPDFView didZoom:];
-[UIWebPDFView documentBounds];
-[UIWebPDFView documentData];
-[UIWebPDFView documentPassword];
-[UIWebPDFView documentScale];
-[UIWebPDFView documentTransform];
-[UIWebPDFView firstVisiblePageNumber];
-[UIWebPDFView hideActivityIndicatorForUnRenderedContent];
-[UIWebPDFView ignoreContentOffsetChanges];
-[UIWebPDFView imageForContactRect:onPageInViewRect:destinationRect:];
-[UIWebPDFView initWithWebPDFViewPlaceholder:];
-[UIWebPDFView initialZoomScale];
-[UIWebPDFView pageMinYs];
-[UIWebPDFView pageRects];
-[UIWebPDFView pdfDelegate];
-[UIWebPDFView pdfPlaceHolderView];
-[UIWebPDFView prepareForSnapshot:];
-[UIWebPDFView readyForSnapshot];
-[UIWebPDFView resetZoom:];
-[UIWebPDFView setBackgroundColorForUnRenderedContent:];
-[UIWebPDFView setDocumentPassword:];
-[UIWebPDFView setDocumentTransform:];
-[UIWebPDFView setHideActivityIndicatorForUnRenderedContent:];
-[UIWebPDFView setHidePageViewsUntilReadyToRender:];
-[UIWebPDFView setIgnoreContentOffsetChanges:];
-[UIWebPDFView setInitialZoomScale:];
-[UIWebPDFView setPageMinYs:];
-[UIWebPDFView setPageRects:];
-[UIWebPDFView setPdfPlaceHolderView:];
-[UIWebPDFView setReadyForSnapshot:];
-[UIWebPDFView snapshotComplete];
-[UIWebPDFView totalPages];
-[UIWebPDFView uiPDFDocument];
-[UIWebPDFView viewAtIndex:];
-[UIWebPDFView viewWillClose];
-[UIWebPDFView viewportView];
-[UIWebPDFView willRotate:];
-[UIWebPDFView willScroll:];
-[UIWebPDFView willZoom:];
-[UIWebPDFView zoom:to:atPoint:kind:];
```
