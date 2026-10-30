# `_UIFocusContainerGuideRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusGuideRegion`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<_UIFocusRegionContainer>" _fallbackRootRegionContainer;
@"<_UIFocusRegionContainer>" _contentFocusRegionContainer;
```

## Properties

```
@property (T@"<_UIFocusRegionContainer>",&,N,V_fallbackRootRegionContainer) fallbackRootRegionContainer;
@property (T@"<_UIFocusRegionContainer>",&,N,V_contentFocusRegionContainer) contentFocusRegionContainer;
```

## Instance methods

```
-[_UIFocusContainerGuideRegion isEqual:];
-[_UIFocusContainerGuideRegion setContentFocusRegionContainer:];
-[_UIFocusContainerGuideRegion setFallbackRootRegionContainer:];
-[_UIFocusContainerGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:];
-[_UIFocusContainerGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusContainerGuideRegion _focusableBoundaries];
-[_UIFocusContainerGuideRegion contentFocusRegionContainer];
-[_UIFocusContainerGuideRegion fallbackRootRegionContainer];
```
