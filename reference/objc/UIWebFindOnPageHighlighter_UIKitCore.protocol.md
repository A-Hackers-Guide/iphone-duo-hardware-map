# `UIWebFindOnPageHighlighter` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) searchText;
@property (T@"<UIWebFindOnPageHighlighterDelegate>",N) delegate;
@property (TQ,R,N) numberOfMatches;
@property (TQ,R,N) highlightedMatchIndex;
```

## Instance methods

```
-[UIWebFindOnPageHighlighter numberOfMatches];
-[UIWebFindOnPageHighlighter searchText];
-[UIWebFindOnPageHighlighter setDelegate:];
-[UIWebFindOnPageHighlighter delegate];
-[UIWebFindOnPageHighlighter highlightNextMatch];
-[UIWebFindOnPageHighlighter highlightPreviousMatch];
-[UIWebFindOnPageHighlighter highlightedMatchIndex];
-[UIWebFindOnPageHighlighter setSearchText:matchLimit:];
-[UIWebFindOnPageHighlighter setSelectionRect:textRects:contentViews:wobble:];
```
