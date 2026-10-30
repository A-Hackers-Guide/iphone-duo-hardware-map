# `UIWebPDFSearchOperation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- 12 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _results;
Q _pageIndex;
Q _numberOfResultsToSkip;
Q _totalResultsCount;
Q _currentPageResultCount;
B _complete;
Q startingPageIndex;
@"UIPDFDocument" documentToSearch;
@"NSObject<UIWebPDFSearchOperationDelegate>" searchDelegate;
d documentScale;
@"NSString" searchString;
Q resultLimit;
```

## Properties

```
@property (T@"NSObject<UIWebPDFSearchOperationDelegate>",VsearchDelegate) searchDelegate;
@property (TQ,R,N,V_currentPageResultCount) currentPageResultCount;
@property (T@"UIPDFDocument",&,VdocumentToSearch) documentToSearch;
@property (TQ,R,N,V_pageIndex) currentPageIndex;
@property (TQ,N,VstartingPageIndex) startingPageIndex;
@property (TQ,N,V_numberOfResultsToSkip) numberOfResultsToSkip;
@property (TQ,N,VresultLimit) resultLimit;
@property (T@"NSString",&,N,VsearchString) searchString;
@property (Td,N,VdocumentScale) documentScale;
```

## Instance methods

```
-[UIWebPDFSearchOperation searchString];
-[UIWebPDFSearchOperation setSearchString:];
-[UIWebPDFSearchOperation init];
-[UIWebPDFSearchOperation dealloc];
-[UIWebPDFSearchOperation main];
-[UIWebPDFSearchOperation currentPageIndex];
-[UIWebPDFSearchOperation resultLimit];
-[UIWebPDFSearchOperation setResultLimit:];
-[UIWebPDFSearchOperation setSearchDelegate:];
-[UIWebPDFSearchOperation searchDelegate];
-[UIWebPDFSearchOperation cancel];
-[UIWebPDFSearchOperation _hitSearchLimit];
-[UIWebPDFSearchOperation _search];
-[UIWebPDFSearchOperation _fontWithPDFFont:size:];
-[UIWebPDFSearchOperation _notifyDelegateOfStatus];
-[UIWebPDFSearchOperation currentPageResultCount];
-[UIWebPDFSearchOperation documentScale];
-[UIWebPDFSearchOperation documentToSearch];
-[UIWebPDFSearchOperation numberOfResultsToSkip];
-[UIWebPDFSearchOperation sanitizedAttributedStringForAttributedString:];
-[UIWebPDFSearchOperation setDocumentScale:];
-[UIWebPDFSearchOperation setDocumentToSearch:];
-[UIWebPDFSearchOperation setNumberOfResultsToSkip:];
-[UIWebPDFSearchOperation setStartingPageIndex:];
-[UIWebPDFSearchOperation startingPageIndex];
```
