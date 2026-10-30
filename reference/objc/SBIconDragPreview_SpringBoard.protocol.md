# `SBIconDragPreview` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 30 instance methods, 0 class methods

## Properties

```
@property (TQ,N) dragState;
@property (TB,N,GisFlocked) flocked;
@property (TB,N) iconAllowsLabelArea;
@property (TB,N) iconAllowsAccessory;
@property (TB,N) iconCanShowCloseBox;
@property (Td,N) iconContentScale;
@property (TB,N) iconIsEditing;
@property (T@"SBIcon",&,N) icon;
@property (T@?,C,N) cleanUpHandler;
@property (TB,?,N) iconCanShowResizeHandle;
```

## Instance methods

```
-[SBIconDragPreview iconContentScale];
-[SBIconDragPreview setIconContentScale:];
-[SBIconDragPreview dragState];
-[SBIconDragPreview setIcon:];
-[SBIconDragPreview setDragState:];
-[SBIconDragPreview icon];
-[SBIconDragPreview isFlocked];
-[SBIconDragPreview cleanUpHandler];
-[SBIconDragPreview delayCleanUpForReason:];
-[SBIconDragPreview draggingSourceCancelAnimationCompleted];
-[SBIconDragPreview draggingSourceDroppedWithOperation:];
-[SBIconDragPreview dropDestinationAnimationCompleted];
-[SBIconDragPreview iconAllowsAccessory];
-[SBIconDragPreview iconAllowsLabelArea];
-[SBIconDragPreview iconCanShowCloseBox];
-[SBIconDragPreview iconIsEditing];
-[SBIconDragPreview setCleanUpHandler:];
-[SBIconDragPreview setFlocked:];
-[SBIconDragPreview setIconAllowsAccessory:];
-[SBIconDragPreview setIconAllowsLabelArea:];
-[SBIconDragPreview setIconCanShowCloseBox:];
-[SBIconDragPreview setIconIsEditing:];
-[SBIconDragPreview setIconIsEditing:animated:];
-[SBIconDragPreview updateDestinationIconLocation:allowsLabelArea:animated:];
-[SBIconDragPreview cleanUp];
-[SBIconDragPreview iconCanShowResizeHandle];
-[SBIconDragPreview setIconCanShowResizeHandle:];
-[SBIconDragPreview setIconViewCustomIconImageViewController:];
-[SBIconDragPreview setIconViewDelegate:];
-[SBIconDragPreview setIconViewListLayoutProvider:];
```
