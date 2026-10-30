# `UIWebBrowserFindOnPageHighlighter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIWebFindOnPageHighlighter`
- 10 instance variables, 8 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _highlightBubbleViews;
@"NSArray" _pdfHighlightViews;
@"UIView" _highlightHostView;
@"UIWebBrowserView" _browserView;
@"UIWebPDFViewHandler" _pdfHandler;
B _zoomToHighlightSelection;
@"<UIWebFindOnPageHighlighterDelegate>" _delegate;
@"NSString" _searchText;
Q _numberOfMatches;
Q _highlightedMatchIndex;
```

## Properties

```
@property (T@"NSString",R,C,N,V_searchText) searchText;
@property (T@"<UIWebFindOnPageHighlighterDelegate>",N,V_delegate) delegate;
@property (TQ,R,N,V_numberOfMatches) numberOfMatches;
@property (TQ,R,N,V_highlightedMatchIndex) highlightedMatchIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIWebBrowserFindOnPageHighlighter expandedRectsWouldIntersect:];
```

## Instance methods

```
-[UIWebBrowserFindOnPageHighlighter numberOfMatches];
-[UIWebBrowserFindOnPageHighlighter dealloc];
-[UIWebBrowserFindOnPageHighlighter searchText];
-[UIWebBrowserFindOnPageHighlighter setDelegate:];
-[UIWebBrowserFindOnPageHighlighter delegate];
-[UIWebBrowserFindOnPageHighlighter searchDidBegin:];
-[UIWebBrowserFindOnPageHighlighter searchLimitHit:];
-[UIWebBrowserFindOnPageHighlighter _addContentViewAtIndex:withRect:];
-[UIWebBrowserFindOnPageHighlighter _clearHighlightViews];
-[UIWebBrowserFindOnPageHighlighter _commonInitialize];
-[UIWebBrowserFindOnPageHighlighter _currentPDFSearchResult];
-[UIWebBrowserFindOnPageHighlighter _highlightFindOnPageMatch:];
-[UIWebBrowserFindOnPageHighlighter _highlightFindOnPageMatchForPDF:withPDFHandler:];
-[UIWebBrowserFindOnPageHighlighter _highlightSelection];
-[UIWebBrowserFindOnPageHighlighter _setSelectionRect:textRects:contentImage:contentViews:wobble:];
-[UIWebBrowserFindOnPageHighlighter _updateHighlightedMatchIndex:];
-[UIWebBrowserFindOnPageHighlighter clearBrowserView];
-[UIWebBrowserFindOnPageHighlighter findOnPageOptions];
-[UIWebBrowserFindOnPageHighlighter highlightNextMatch];
-[UIWebBrowserFindOnPageHighlighter highlightPreviousMatch];
-[UIWebBrowserFindOnPageHighlighter highlightedMatchIndex];
-[UIWebBrowserFindOnPageHighlighter initWithBrowserView:];
-[UIWebBrowserFindOnPageHighlighter initWithPDFViewHandler:];
-[UIWebBrowserFindOnPageHighlighter search:hasPartialResults:];
-[UIWebBrowserFindOnPageHighlighter searchDidFinish:];
-[UIWebBrowserFindOnPageHighlighter searchDidTimeOut:];
-[UIWebBrowserFindOnPageHighlighter searchWasCancelled:];
-[UIWebBrowserFindOnPageHighlighter setSearchText:matchLimit:];
-[UIWebBrowserFindOnPageHighlighter setSelectionRect:textRects:contentImage:wobble:];
-[UIWebBrowserFindOnPageHighlighter setSelectionRect:textRects:contentViews:wobble:];
-[UIWebBrowserFindOnPageHighlighter updateHighlightBubbleWobble:];
```
