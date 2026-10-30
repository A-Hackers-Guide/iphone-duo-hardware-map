# `UIFindSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 13 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UIResponder" _divergentResponderForSession;
B _allowsReplacement;
q _resultCount;
q _searchResultDisplayStyle;
@"NSString" _searchText;
@"NSString" _replacementText;
@"UITextSearchOptions" _configuredSearchOptions;
@"UIFindInteraction" _parentInteraction;
@"UIResponder" _searchableResponder;
```

## Properties

```
@property (T@"NSString",C,N,V_searchText) searchText;
@property (T@"NSString",C,N,V_replacementText) replacementText;
@property (T@"UITextSearchOptions",&,N,V_configuredSearchOptions) configuredSearchOptions;
@property (T@"UIFindInteraction",W,N,V_parentInteraction) parentInteraction;
@property (T@"UIResponder",W,N,V_searchableResponder) searchableResponder;
@property (T@"UIView",R,N) searchableResponderAsView;
@property (T@"UIResponder",R,N) divergentResponder;
@property (Tq,R,N,V_resultCount) resultCount;
@property (Tq,R,N) highlightedResultIndex;
@property (Tq,N,V_searchResultDisplayStyle) searchResultDisplayStyle;
@property (TB,R,N) supportsReplacement;
@property (TB,R,N) allowsReplacementForCurrentlyHighlightedResult;
@property (TB,R,N,V_allowsReplacement) allowsReplacement;
```

## Instance methods

```
-[UIFindSession searchText];
-[UIFindSession resultCount];
-[UIFindSession setSearchText:];
-[UIFindSession replacementText];
-[UIFindSession setReplacementText:];
-[UIFindSession replaceAllInstancesOfSearchQuery:withReplacementString:options:];
-[UIFindSession highlightNextResultInDirection:];
-[UIFindSession performSearchWithQuery:options:];
-[UIFindSession allowsReplacement];
-[UIFindSession allowsReplacementForCurrentlyHighlightedResult];
-[UIFindSession configuredSearchOptions];
-[UIFindSession divergentResponder];
-[UIFindSession highlightedResultIndex];
-[UIFindSession invalidateFoundResults];
-[UIFindSession parentInteraction];
-[UIFindSession performSingleReplacementWithSearchQuery:replacementString:options:];
-[UIFindSession searchResultDisplayStyle];
-[UIFindSession searchableResponder];
-[UIFindSession searchableResponderAsView];
-[UIFindSession setConfiguredSearchOptions:];
-[UIFindSession setParentInteraction:];
-[UIFindSession setSearchResultDisplayStyle:];
-[UIFindSession setSearchableResponder:];
-[UIFindSession supportsReplacement];
```
