# `UITargetedDragPreview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITargetedPreview`
- Protocols: `_UIDragPreviewProvider`
- 11 instance variables, 16 properties, 25 instance methods, 2 class methods

## Instance variables

```
B _didSetLiftAnchorPoint;
@"_DUIPreview" _duiPreview;
@"_UIDraggingImageComponent" _imageComponent;
B __applyTargetTransformToFlock;
B _preventAfterScreenUpdatesSnapshot;
q __preferredStackOrder;
@? __fenceHandler;
@"UIView<_UIDragPreviewContainer>" __previewContainer;
@"NSDictionary" __springboardParameters;
{CGPoint="x"d"y"d} __initialBadgeLocation;
{CGPoint="x"d"y"d} _liftAnchorPoint;
```

## Properties

```
@property (TB,D,N,G_isDefaultPreview,S_setDefaultPreview:) defaultPreview;
@property (TB,N,G_applyTargetTransformToFlock,S_setApplyTargetTransformToFlock:,V__applyTargetTransformToFlock) _applyTargetTransformToFlock;
@property (TB,N,G_preventAfterScreenUpdatesSnapshot,S_setPreventAfterScreenUpdatesSnapshot:,V_preventAfterScreenUpdatesSnapshot) preventAfterScreenUpdatesSnapshot;
@property (T@"UIView",W,D,N,G_viewToSnapshot,S_setViewToSnapshot:) viewToSnapshot;
@property (T@"<_UIDragPreviewProvider>",R,N) _dragPreviewProvider;
@property (Tq,N,S_setPreferredStackOrder:,V__preferredStackOrder) _preferredStackOrder;
@property (T{CGPoint=dd},N,S_setInitialBadgeLocation:,V__initialBadgeLocation) _initialBadgeLocation;
@property (T@?,C,N,V__fenceHandler) _fenceHandler;
@property (T{CGPoint=dd},N,V_liftAnchorPoint) liftAnchorPoint;
@property (T@"_DUIPreview",R,N) _duiPreview;
@property (T@"UIView<_UIDragPreviewContainer>",&,N,S_setPreviewContainer:,V__previewContainer) _previewContainer;
@property (T@"NSDictionary",C,N,V__springboardParameters) _springboardParameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITargetedDragPreview previewForURL:target:];
+[UITargetedDragPreview previewForURL:title:target:];
```

## Instance methods

```
-[UITargetedDragPreview set_fenceHandler:];
-[UITargetedDragPreview _fenceHandler];
-[UITargetedDragPreview _setPreviewContainer:];
-[UITargetedDragPreview initWithView:];
-[UITargetedDragPreview liftAnchorPoint];
-[UITargetedDragPreview _setPreviewMode:];
-[UITargetedDragPreview set_springboardParameters:];
-[UITargetedDragPreview _setInitialBadgeLocation:];
-[UITargetedDragPreview _springboardParameters];
-[UITargetedDragPreview takeLiftAnchorPoint:fromView:];
-[UITargetedDragPreview _setPreventAfterScreenUpdatesSnapshot:];
-[UITargetedDragPreview _previewContainer];
-[UITargetedDragPreview _preventAfterScreenUpdatesSnapshot];
-[UITargetedDragPreview _setApplyTargetTransformToFlock:];
-[UITargetedDragPreview imageComponent];
-[UITargetedDragPreview retargetedPreviewWithTarget:];
-[UITargetedDragPreview _preferredStackOrder];
-[UITargetedDragPreview _duiPreview];
-[UITargetedDragPreview _resetPreview];
-[UITargetedDragPreview setLiftAnchorPoint:];
-[UITargetedDragPreview _setPreferredStackOrder:];
-[UITargetedDragPreview _dragPreviewProvider];
-[UITargetedDragPreview initWithView:parameters:target:];
-[UITargetedDragPreview _initialBadgeLocation];
-[UITargetedDragPreview _applyTargetTransformToFlock];
```
