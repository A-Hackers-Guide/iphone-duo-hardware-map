# `_UIFocusMapSnapshotter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _snapshotFrameIsEmpty;
B _ignoresRootContainerClippingRect;
B _clipToSnapshotRect;
@"UIFocusSystem" _focusSystem;
@"<_UIFocusRegionContainer>" _rootContainer;
@"<UICoordinateSpace>" _coordinateSpace;
@"_UIFocusRegion" _focusedRegion;
@"<_UIFocusRegionContainer>" _regionsContainer;
@"_UIFocusSearchInfo" _searchInfo;
@"_UIFocusMovementInfo" _movementInfo;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _snapshotFrame;
```

## Properties

```
@property (T@"_UIFocusSearchInfo",&,N,V_searchInfo) searchInfo;
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (T@"<_UIFocusRegionContainer>",R,W,N,V_rootContainer) rootContainer;
@property (T@"<UICoordinateSpace>",R,W,N,V_coordinateSpace) coordinateSpace;
@property (T@"_UIFocusRegion",&,N,V_focusedRegion) focusedRegion;
@property (T@"<_UIFocusRegionContainer>",W,N,V_regionsContainer) regionsContainer;
@property (T@"_UIFocusMovementInfo",&,N,V_movementInfo) movementInfo;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_snapshotFrame) snapshotFrame;
@property (TB,N,V_clipToSnapshotRect) clipToSnapshotRect;
@property (TB,N,V_ignoresRootContainerClippingRect) ignoresRootContainerClippingRect;
```

## Instance methods

```
-[_UIFocusMapSnapshotter coordinateSpace];
-[_UIFocusMapSnapshotter init];
-[_UIFocusMapSnapshotter focusSystem];
-[_UIFocusMapSnapshotter captureSnapshot];
-[_UIFocusMapSnapshotter _searchAreaForContainerSearchRect:];
-[_UIFocusMapSnapshotter clipToSnapshotRect];
-[_UIFocusMapSnapshotter focusedRegion];
-[_UIFocusMapSnapshotter ignoresRootContainerClippingRect];
-[_UIFocusMapSnapshotter initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:];
-[_UIFocusMapSnapshotter movementInfo];
-[_UIFocusMapSnapshotter regionsContainer];
-[_UIFocusMapSnapshotter rootContainer];
-[_UIFocusMapSnapshotter searchInfo];
-[_UIFocusMapSnapshotter setClipToSnapshotRect:];
-[_UIFocusMapSnapshotter setFocusedRegion:];
-[_UIFocusMapSnapshotter setIgnoresRootContainerClippingRect:];
-[_UIFocusMapSnapshotter setMovementInfo:];
-[_UIFocusMapSnapshotter setRegionsContainer:];
-[_UIFocusMapSnapshotter setSearchInfo:];
-[_UIFocusMapSnapshotter setSnapshotFrame:];
-[_UIFocusMapSnapshotter snapshotFrame];
```
