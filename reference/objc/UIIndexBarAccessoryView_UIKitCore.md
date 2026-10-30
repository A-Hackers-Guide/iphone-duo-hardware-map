# `UIIndexBarAccessoryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIIndexBarView`
- Protocols: `UIScrollAccessory`
- 2 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
q _edge;
```

## Properties

```
@property (T@"<UIIndexBarAccessoryViewDelegate>",W,D,N) delegate;
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (Tq,N,V_edge) edge;
@property (TB,R,N) overlay;
```

## Class methods

```
+[UIIndexBarAccessoryView makeIndexBarView:scrollAccessoryContainerView:forTraits:];
```

## Instance methods

```
-[UIIndexBarAccessoryView setEdge:];
-[UIIndexBarAccessoryView _horizontalSizeClassDidChange];
-[UIIndexBarAccessoryView edge];
-[UIIndexBarAccessoryView setEntries:];
-[UIIndexBarAccessoryView update];
-[UIIndexBarAccessoryView scrollView];
-[UIIndexBarAccessoryView setScrollView:];
-[UIIndexBarAccessoryView overlay];
-[UIIndexBarAccessoryView _shouldAnimatePropertyWithKey:];
-[UIIndexBarAccessoryView _selectEntry:atIndex:];
-[UIIndexBarAccessoryView displayEntryNearestToContentOffset:];
```
