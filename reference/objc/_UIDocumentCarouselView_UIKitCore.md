# `_UIDocumentCarouselView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 12 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _containerViews;
@"UIViewFloatAnimatableProperty" _pagingFractionAnimatableProperty;
@"UIViewFloatAnimatableProperty" _revealAnimatableProperty;
Q _animationCount;
d _pagingFractionPanStart;
d _centerItemFraction;
Q _centerItemIndex;
B _pagingEnabled;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UITapGestureRecognizer" _tapGestureRecognizer;
B _lockedFocusEnvironmentForAnimation;
@"NSArray" _items;
```

## Properties

```
@property (T@"NSArray",&,N,V_items) items;
@property (TB,R,N) isPagingEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDocumentCarouselView _layoutMarginsDidChangeFromOldMargins:];
-[_UIDocumentCarouselView setItems:];
-[_UIDocumentCarouselView dealloc];
-[_UIDocumentCarouselView items];
-[_UIDocumentCarouselView setBounds:];
-[_UIDocumentCarouselView gestureRecognizerShouldBegin:];
-[_UIDocumentCarouselView willMoveToWindow:];
-[_UIDocumentCarouselView setFrame:];
-[_UIDocumentCarouselView initWithFrame:];
-[_UIDocumentCarouselView isPagingEnabled];
-[_UIDocumentCarouselView _handlePanNavigation:];
-[_UIDocumentCarouselView _handleTapNavigation:];
-[_UIDocumentCarouselView scrollToItemAtIndex:animated:];
-[_UIDocumentCarouselView setPagingEnabled:animated:];
```
