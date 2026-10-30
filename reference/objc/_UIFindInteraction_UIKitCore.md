# `_UIFindInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFindInteractionDelegate`, `UIInteraction`
- 3 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<_UITextSearching>" _searchableObject;
@"UIFindInteraction" _wrappedFindInteraction;
```

## Properties

```
@property (T@"UIFindInteraction",&,N,V_wrappedFindInteraction) wrappedFindInteraction;
@property (T@"<_UITextSearching>",W,N,V_searchableObject) searchableObject;
@property (TB,R,N,GisFindNavigatorVisible) findNavigatorVisible;
@property (T@"NSString",C,N) searchText;
@property (T@"NSString",C,N) replacementText;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIFindInteraction searchableObject];
-[_UIFindInteraction findNext];
-[_UIFindInteraction presentFindNavigatorShowingReplace:];
-[_UIFindInteraction init];
-[_UIFindInteraction searchText];
-[_UIFindInteraction view];
-[_UIFindInteraction willMoveToView:];
-[_UIFindInteraction setSearchText:];
-[_UIFindInteraction setSearchableObject:];
-[_UIFindInteraction replacementText];
-[_UIFindInteraction setReplacementText:];
-[_UIFindInteraction dismissFindNavigator];
-[_UIFindInteraction isFindNavigatorVisible];
-[_UIFindInteraction didMoveToView:];
-[_UIFindInteraction findPrevious];
-[_UIFindInteraction findInteraction:sessionForView:];
-[_UIFindInteraction findInteraction:didBeginFindSession:];
-[_UIFindInteraction findInteraction:didEndFindSession:];
-[_UIFindInteraction setWrappedFindInteraction:];
-[_UIFindInteraction wrappedFindInteraction];
```
