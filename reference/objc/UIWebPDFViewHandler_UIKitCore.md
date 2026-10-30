# `UIWebPDFViewHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIWebPDFViewPrivateDelegate`, `UIDocumentPasswordViewDelegate`, `_UIRotatingAlertControllerDelegate`, `UIWebPDFViewDelegate`, `_UIWebDoubleTapDelegate`, `_UIWebRotationDelegate`
- 21 instance variables, 12 properties, 105 instance methods, 0 class methods

## Instance variables

```
@"UIWebPDFView" _pdfView;
B _scalesPageToFit;
d _initialZoomScale;
@"NSObject<UIWebPDFViewHandlerDelegate>" _pdfHandlerDelegate;
@"_UIHighlightView" _linkHighlightView;
@"UIWebPDFLabelView" _pageLabelView;
B _showPageLabels;
B _showsShadowsForHTMLContent;
B _cachedScrollViewShadowsState;
@"UIDocumentPasswordView" _passwordEntryView;
@"NSMapTable" _searchControllers;
@"UIColor" _backgroundColorForUnRenderedContent;
B _hideActivityIndicatorForUnRenderedContent;
B _hidePageViewsUntilReadyToRender;
@"WebPDFNSNumberFormatter" _labelViewFormatter;
{_PDFHistoryItem="restorePending"B"isInitialScale"B"zoomScale"d"contentOffset"{CGPoint="x"d"y"d}} _pendingHistoryItemRestore;
@"_UIRotatingAlertController" _linkActionSheet;
@"NSDictionary" _linkActionInfo;
@"NSArray" _linkActions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rectOfInterest;
B _rectOfInterestConsidersHeight;
```

## Properties

```
@property (T@"UIWebPDFView",R,N) pdfView;
@property (T@"UIView",R,N) frontView;
@property (TB,N,V_scalesPageToFit) scalesPageToFit;
@property (TB,N,V_showPageLabels) showPageLabels;
@property (T@"NSObject<UIWebPDFViewHandlerDelegate>",N,V_pdfHandlerDelegate) pdfHandlerDelegate;
@property (T@"UIColor",&,N,V_backgroundColorForUnRenderedContent) backgroundColorForUnRenderedContent;
@property (TB,N,V_hideActivityIndicatorForUnRenderedContent) hideActivityIndicatorForUnRenderedContent;
@property (TB,N,V_hidePageViewsUntilReadyToRender) hidePageViewsUntilReadyToRender;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWebPDFViewHandler init];
-[UIWebPDFViewHandler enclosingScrollView];
-[UIWebPDFViewHandler dealloc];
-[UIWebPDFViewHandler pdfView];
-[UIWebPDFViewHandler _keyboardDidShow:];
-[UIWebPDFViewHandler contentView];
-[UIWebPDFViewHandler _actionForType:];
-[UIWebPDFViewHandler _postdidDetermineDocumentBounds];
-[UIWebPDFViewHandler createPageLabel];
-[UIWebPDFViewHandler ensureCorrectPagesAreInstalled:];
-[UIWebPDFViewHandler hidePageViewsUntilReadyToRender];
-[UIWebPDFViewHandler _showLinkSheet:];
-[UIWebPDFViewHandler didBeginEditingPassword:inView:];
-[UIWebPDFViewHandler scalesPageToFit];
-[UIWebPDFViewHandler searchControllerForHighlighter:];
-[UIWebPDFViewHandler _absoluteUrlRelativeToDocumentURL:];
-[UIWebPDFViewHandler _actionForType:withActionInfo:];
-[UIWebPDFViewHandler _actionsForInteractionInfo:];
-[UIWebPDFViewHandler _adjustContentOffsetForKeyboardIfNeeded];
-[UIWebPDFViewHandler _adjustZoomScalesForScrollViewInternal:];
-[UIWebPDFViewHandler _completeLinkClickWithURL:];
-[UIWebPDFViewHandler _completeLinkClickWithURLString:];
-[UIWebPDFViewHandler _createPDFViewIfNeeded:];
-[UIWebPDFViewHandler _ensurePDFViewInHierarchyForWebDocView:];
-[UIWebPDFViewHandler _frameForDocumentBounds:];
-[UIWebPDFViewHandler _getLabelViewFormatter];
-[UIWebPDFViewHandler _getPDFDocumentViewForWebView:];
-[UIWebPDFViewHandler _notifyDelegateDidClickLink:];
-[UIWebPDFViewHandler _notifyDelegateWillClickLink:];
-[UIWebPDFViewHandler _pinValueForVerticalEdge:inScrollView:];
-[UIWebPDFViewHandler _rectForPasswordView:];
-[UIWebPDFViewHandler _rectForPdfView:];
-[UIWebPDFViewHandler _removePDFViewIfWebDocViewIsNotPDF:];
-[UIWebPDFViewHandler _removePDFViewIfWebDocViewIsNotSamePDF:];
-[UIWebPDFViewHandler _replacePDFViewIfPresentWithWebDocView:];
-[UIWebPDFViewHandler _resultRects:andResultViews:forSearchResult:inViewCoordinates:];
-[UIWebPDFViewHandler _scroller:];
-[UIWebPDFViewHandler _setSearchControllerDocumentToSearch:];
-[UIWebPDFViewHandler _showPasswordEntryViewForFile:];
-[UIWebPDFViewHandler _showPasswordErrorAlert];
-[UIWebPDFViewHandler _updateViewHierarchyForDocumentView:ignoreIfSame:];
-[UIWebPDFViewHandler _verticalEdgeForContentOffsetInScrollView:];
-[UIWebPDFViewHandler activeRectForRectOfInterest:];
-[UIWebPDFViewHandler adjustZoomScalesForScrollView];
-[UIWebPDFViewHandler backgroundColorForUnRenderedContent];
-[UIWebPDFViewHandler clearActionSheet];
-[UIWebPDFViewHandler clearAllViews];
-[UIWebPDFViewHandler clearLinkHighlight];
-[UIWebPDFViewHandler clearPageLabel];
-[UIWebPDFViewHandler clearSearchControllerForHighlighter:];
-[UIWebPDFViewHandler considerHeightForDoubleTap];
-[UIWebPDFViewHandler considerHeightOfRectOfInterestForRotation];
-[UIWebPDFViewHandler createLinkHighlight];
-[UIWebPDFViewHandler currentDocumentScale];
-[UIWebPDFViewHandler didDetermineDocumentBounds:];
-[UIWebPDFViewHandler didEndEditingPassword:inView:];
-[UIWebPDFViewHandler didReceiveMemoryWarning:];
-[UIWebPDFViewHandler didScroll:];
-[UIWebPDFViewHandler doubleTapScalesForSize:];
-[UIWebPDFViewHandler findOnPageHighlighter];
-[UIWebPDFViewHandler frontView];
-[UIWebPDFViewHandler handleLinkClick:inRect:];
-[UIWebPDFViewHandler handleLongPressOnLink:atPoint:inRect:contentRect:];
-[UIWebPDFViewHandler handleScrollToAnchor:];
-[UIWebPDFViewHandler heightToKeepVisible];
-[UIWebPDFViewHandler hideActivityIndicatorForUnRenderedContent];
-[UIWebPDFViewHandler highlightRect:];
-[UIWebPDFViewHandler hostViewForSheet:];
-[UIWebPDFViewHandler initialPresentationRectInHostViewForSheet:];
-[UIWebPDFViewHandler minimumScaleForSize:];
-[UIWebPDFViewHandler minimumVerticalContentOffset];
-[UIWebPDFViewHandler passwordForPDFView:];
-[UIWebPDFViewHandler pdfHandlerDelegate];
-[UIWebPDFViewHandler pdfView:zoomToRect:forPoint:considerHeight:];
-[UIWebPDFViewHandler performAction:fromAlertController:];
-[UIWebPDFViewHandler presentationRectInHostViewForSheet:];
-[UIWebPDFViewHandler rectOfInterestForPoint:];
-[UIWebPDFViewHandler rectOfInterestForRotation];
-[UIWebPDFViewHandler removeViewFromSuperview];
-[UIWebPDFViewHandler resetZoom:];
-[UIWebPDFViewHandler restoreStateFromHistoryItem:forWebView:];
-[UIWebPDFViewHandler restoreStateFromPendingHistoryItem];
-[UIWebPDFViewHandler revealSearchResult:andZoomIn:];
-[UIWebPDFViewHandler rotateEnclosingScrollViewToFrame:];
-[UIWebPDFViewHandler saveStateToHistoryItem:forWebView:];
-[UIWebPDFViewHandler scalesForContainerSize:];
-[UIWebPDFViewHandler scrollToPageNumber:animate:];
-[UIWebPDFViewHandler setBackgroundColorForUnRenderedContent:];
-[UIWebPDFViewHandler setHideActivityIndicatorForUnRenderedContent:];
-[UIWebPDFViewHandler setHidePageViewsUntilReadyToRender:];
-[UIWebPDFViewHandler setPdfHandlerDelegate:];
-[UIWebPDFViewHandler setScalesPageToFit:];
-[UIWebPDFViewHandler setShowPageLabels:];
-[UIWebPDFViewHandler showPageLabels];
-[UIWebPDFViewHandler updateBoundariesOfScrollView:withScales:];
-[UIWebPDFViewHandler updatePageNumberLabelWithUserScrolling:animated:];
-[UIWebPDFViewHandler updateViewHierarchyForDocumentViewLoadComplete:];
-[UIWebPDFViewHandler updateViewHierarchyForDocumentViewNewLoad:];
-[UIWebPDFViewHandler updateViewHierarchyForDocumentViewTabSwitch:];
-[UIWebPDFViewHandler updateViewHierarchyForDocumentViewTabSwitch:restoringZoomScale:andScrollPt:];
-[UIWebPDFViewHandler updateViewHierarchyForFirstNonEmptyLayoutInFrame:];
-[UIWebPDFViewHandler updateViewSettings];
-[UIWebPDFViewHandler userDidEnterPassword:forPasswordView:];
-[UIWebPDFViewHandler visibleContentRect];
-[UIWebPDFViewHandler zoomedDocumentScale];
```
