# `UIWebPDFSearchController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIWebPDFSearchOperationDelegate`
- 11 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
Q _resultIndexWhenLimitHit;
B _notifiedThatSearchBegin;
Q _pageIndexWhenLimitHit;
@"NSOperationQueue" _searchQueue;
@"NSMutableArray" _results;
@"NSString" _searchString;
@"UIPDFDocument" _documentToSearch;
@"NSObject<UIWebPDFSearchControllerDelegate>" searchDelegate;
Q startingPageIndex;
d documentScale;
Q resultLimit;
```

## Properties

```
@property (T@"NSArray",&,N,V_results) results;
@property (T@"NSString",&,N,V_searchString) searchString;
@property (T@"NSObject<UIWebPDFSearchControllerDelegate>",N,VsearchDelegate) searchDelegate;
@property (T@"UIPDFDocument",&,N,V_documentToSearch) documentToSearch;
@property (Td,N,VdocumentScale) documentScale;
@property (TQ,N,VstartingPageIndex) startingPageIndex;
@property (TQ,N,VresultLimit) resultLimit;
@property (TB,R,N) searching;
@property (TB,R,N) paused;
```

## Instance methods

```
-[UIWebPDFSearchController pause];
-[UIWebPDFSearchController searchString];
-[UIWebPDFSearchController setSearchString:];
-[UIWebPDFSearchController paused];
-[UIWebPDFSearchController init];
-[UIWebPDFSearchController dealloc];
-[UIWebPDFSearchController resultLimit];
-[UIWebPDFSearchController setResultLimit:];
-[UIWebPDFSearchController setSearchDelegate:];
-[UIWebPDFSearchController results];
-[UIWebPDFSearchController searchDelegate];
-[UIWebPDFSearchController cancel];
-[UIWebPDFSearchController setResults:];
-[UIWebPDFSearchController resume];
-[UIWebPDFSearchController search:];
-[UIWebPDFSearchController searchDidBegin:];
-[UIWebPDFSearchController searchLimitHit:];
-[UIWebPDFSearchController _actualStartingPageIndex];
-[UIWebPDFSearchController _clearSearchQueue];
-[UIWebPDFSearchController documentScale];
-[UIWebPDFSearchController documentToSearch];
-[UIWebPDFSearchController search:hasPartialResults:];
-[UIWebPDFSearchController searchDidFinish:];
-[UIWebPDFSearchController searchDidTimeOut:];
-[UIWebPDFSearchController searchWasCancelled:];
-[UIWebPDFSearchController searching];
-[UIWebPDFSearchController setDocumentScale:];
-[UIWebPDFSearchController setDocumentToSearch:];
-[UIWebPDFSearchController setStartingPageIndex:];
-[UIWebPDFSearchController startingPageIndex];
```
