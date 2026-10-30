# `_UIFocusRegionSearchContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"UIFocusSystem",R,W,N) focusSystem;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (T@"<_UIFocusMapArea>",R,N) searchArea;
@property (T@"_UIFocusSearchInfo",R,N) searchInfo;
@property (T@"_UIFocusMovementInfo",R,N) movementInfo;
```

## Instance methods

```
-[_UIFocusRegionSearchContext coordinateSpace];
-[_UIFocusRegionSearchContext addRegions:];
-[_UIFocusRegionSearchContext addRegion:];
-[_UIFocusRegionSearchContext focusSystem];
-[_UIFocusRegionSearchContext addFocusGuideContainers:];
-[_UIFocusRegionSearchContext addRegionsInContainer:];
-[_UIFocusRegionSearchContext addRegionsInContainers:];
-[_UIFocusRegionSearchContext markContainerAsProvidingDynamicContent];
-[_UIFocusRegionSearchContext movementInfo];
-[_UIFocusRegionSearchContext searchArea];
-[_UIFocusRegionSearchContext searchInfo];
```
