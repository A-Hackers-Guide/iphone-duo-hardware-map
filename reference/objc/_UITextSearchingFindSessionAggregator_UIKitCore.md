# `_UITextSearchingFindSessionAggregator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextSearchAggregator`
- 2 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _valid;
@"UITextSearchingFindSession" _session;
```

## Properties

```
@property (TB,GisValid,V_valid) valid;
@property (T@"UITextSearchingFindSession",R,W,N,V_session) session;
@property (T@"NSOrderedSet",R,N) allFoundRanges;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextSearchingFindSessionAggregator setValid:];
-[_UITextSearchingFindSessionAggregator invalidate];
-[_UITextSearchingFindSessionAggregator isValid];
-[_UITextSearchingFindSessionAggregator initWithSession:];
-[_UITextSearchingFindSessionAggregator session];
-[_UITextSearchingFindSessionAggregator _performOnMainIfValid:];
-[_UITextSearchingFindSessionAggregator allFoundRanges];
-[_UITextSearchingFindSessionAggregator finishedSearching];
-[_UITextSearchingFindSessionAggregator foundRange:forSearchString:inDocument:];
-[_UITextSearchingFindSessionAggregator invalidateFoundRange:inDocument:];
```
