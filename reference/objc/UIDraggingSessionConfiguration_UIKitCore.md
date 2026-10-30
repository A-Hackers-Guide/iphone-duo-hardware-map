# `UIDraggingSessionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 27 instance variables, 28 properties, 57 instance methods, 2 class methods

## Instance variables

```
B _supportsSystemDrag;
B _initiatedWithPointer;
B _avoidsKeyboardSuppression;
B _rotatable;
B _resizable;
B _wantsElasticEffects;
B _wantsPresentationUpdates;
B _sessionIsRestrictedToSourceApplication;
B _sessionIsRestrictedToLocalDevice;
@"NSArray" _touchIDs;
@"_DUITargetLayerDescriptor" _coordinateSpaceSourceLayerContext;
@"UIDraggingSystemTouchRoutingPolicy" _routingPolicy;
@"PBItemCollection" _itemCollection;
@"NSXPCListenerEndpoint" _dataProviderEndpoint;
@"NSXPCListenerEndpoint" _axEndpoint;
@"NSString" _sceneIdentifier;
@"NSString" _persistentSceneIdentifier;
@"NSIndexSet" _preferredPreviewIndexes;
d _originalRotation;
Q _associatedObjectManipulationSessionIdentifier;
{CGSize="width"d"height"d} _minimumResizableSize;
{CGSize="width"d"height"d} _maximumResizableSize;
{CGSize="width"d"height"d} _originalScale;
{CAPoint3D="x"d"y"d"z"d} _initialCentroid;
{CAPoint3D="x"d"y"d"z"d} _initialCentroid3D;
{CAPoint3D="x"d"y"d"z"d} _initialCentroidInSourceWindow;
{?="width"d"height"d"depth"d} _associatedObjectManipulationDragItemSize;
```

## Properties

```
@property (T@"NSArray",&,N,V_touchIDs) touchIDs;
@property (T{CGPoint=dd},D,N) initialCentroid;
@property (T{CAPoint3D=ddd},N,V_initialCentroid) _initialCentroid;
@property (T{CAPoint3D=ddd},N,V_initialCentroidInSourceWindow) initialCentroidInSourceWindow;
@property (T@"UIDraggingSystemTouchRoutingPolicy",&,N,V_routingPolicy) routingPolicy;
@property (T@"NSXPCListenerEndpoint",&,N,V_axEndpoint) axEndpoint;
@property (T@"NSIndexSet",&,N,V_preferredPreviewIndexes) preferredPreviewIndexes;
@property (T@"_DUITargetLayerDescriptor",&,N,V_coordinateSpaceSourceLayerContext) coordinateSpaceSourceLayerContext;
@property (T@"PBItemCollection",&,N,V_itemCollection) itemCollection;
@property (T@"NSXPCListenerEndpoint",&,N,V_dataProviderEndpoint) dataProviderEndpoint;
@property (TB,N,V_supportsSystemDrag) supportsSystemDrag;
@property (T@"NSString",&,N,V_sceneIdentifier) sceneIdentifier;
@property (T@"NSString",&,N,V_persistentSceneIdentifier) persistentSceneIdentifier;
@property (TB,N,V_initiatedWithPointer) initiatedWithPointer;
@property (TB,N,V_avoidsKeyboardSuppression) avoidsKeyboardSuppression;
@property (TB,N,V_rotatable) rotatable;
@property (TB,N,V_resizable) resizable;
@property (T{CGSize=dd},N,V_minimumResizableSize) minimumResizableSize;
@property (T{CGSize=dd},N,V_maximumResizableSize) maximumResizableSize;
@property (TB,N,V_wantsElasticEffects) wantsElasticEffects;
@property (Td,N,V_originalRotation) originalRotation;
@property (T{CGSize=dd},N,V_originalScale) originalScale;
@property (TB,N,V_wantsPresentationUpdates) wantsPresentationUpdates;
@property (TB,N,V_sessionIsRestrictedToSourceApplication) sessionIsRestrictedToSourceApplication;
@property (TB,N,V_sessionIsRestrictedToLocalDevice) sessionIsRestrictedToLocalDevice;
@property (TQ,N,V_associatedObjectManipulationSessionIdentifier) associatedObjectManipulationSessionIdentifier;
@property (T{?=ddd},N,V_associatedObjectManipulationDragItemSize) associatedObjectManipulationDragItemSize;
@property (T{CAPoint3D=ddd},R,N,V_initialCentroid3D) initialCentroid3D;
```

## Class methods

```
+[UIDraggingSessionConfiguration supportsSecureCoding];
+[UIDraggingSessionConfiguration configurationWithItemCollection:dataProviderEndpoint:initialCentroidInSourceWindow:sourceView:];
```

## Instance methods

```
-[UIDraggingSessionConfiguration setSceneIdentifier:];
-[UIDraggingSessionConfiguration sceneIdentifier];
-[UIDraggingSessionConfiguration setInitialCentroid:];
-[UIDraggingSessionConfiguration encodeWithCoder:];
-[UIDraggingSessionConfiguration initWithCoder:];
-[UIDraggingSessionConfiguration initialCentroid];
-[UIDraggingSessionConfiguration _initialCentroid];
-[UIDraggingSessionConfiguration associatedObjectManipulationDragItemSize];
-[UIDraggingSessionConfiguration associatedObjectManipulationSessionIdentifier];
-[UIDraggingSessionConfiguration avoidsKeyboardSuppression];
-[UIDraggingSessionConfiguration axEndpoint];
-[UIDraggingSessionConfiguration coordinateSpaceSourceLayerContext];
-[UIDraggingSessionConfiguration dataProviderEndpoint];
-[UIDraggingSessionConfiguration initialCentroid3D];
-[UIDraggingSessionConfiguration initialCentroidInSourceWindow];
-[UIDraggingSessionConfiguration initiatedWithPointer];
-[UIDraggingSessionConfiguration itemCollection];
-[UIDraggingSessionConfiguration maximumResizableSize];
-[UIDraggingSessionConfiguration minimumResizableSize];
-[UIDraggingSessionConfiguration originalRotation];
-[UIDraggingSessionConfiguration originalScale];
-[UIDraggingSessionConfiguration persistentSceneIdentifier];
-[UIDraggingSessionConfiguration preferredPreviewIndexes];
-[UIDraggingSessionConfiguration resizable];
-[UIDraggingSessionConfiguration rotatable];
-[UIDraggingSessionConfiguration routingPolicy];
-[UIDraggingSessionConfiguration sessionIsRestrictedToLocalDevice];
-[UIDraggingSessionConfiguration sessionIsRestrictedToSourceApplication];
-[UIDraggingSessionConfiguration setAssociatedObjectManipulationDragItemSize:];
-[UIDraggingSessionConfiguration setAssociatedObjectManipulationSessionIdentifier:];
-[UIDraggingSessionConfiguration setAvoidsKeyboardSuppression:];
-[UIDraggingSessionConfiguration setAxEndpoint:];
-[UIDraggingSessionConfiguration setCoordinateSpaceSourceLayerContext:];
-[UIDraggingSessionConfiguration setDataProviderEndpoint:];
-[UIDraggingSessionConfiguration setInitialCentroidInSourceWindow:];
-[UIDraggingSessionConfiguration setInitiatedWithPointer:];
-[UIDraggingSessionConfiguration setItemCollection:];
-[UIDraggingSessionConfiguration setMaximumResizableSize:];
-[UIDraggingSessionConfiguration setMinimumResizableSize:];
-[UIDraggingSessionConfiguration setOriginalRotation:];
-[UIDraggingSessionConfiguration setOriginalScale:];
-[UIDraggingSessionConfiguration setPersistentSceneIdentifier:];
-[UIDraggingSessionConfiguration setPreferredPreviewIndexes:];
-[UIDraggingSessionConfiguration setResizable:];
-[UIDraggingSessionConfiguration setRotatable:];
-[UIDraggingSessionConfiguration setRoutingPolicy:];
-[UIDraggingSessionConfiguration setSessionIsRestrictedToLocalDevice:];
-[UIDraggingSessionConfiguration setSessionIsRestrictedToSourceApplication:];
-[UIDraggingSessionConfiguration setSupportsSystemDrag:];
-[UIDraggingSessionConfiguration setTouchIDs:];
-[UIDraggingSessionConfiguration setWantsElasticEffects:];
-[UIDraggingSessionConfiguration setWantsPresentationUpdates:];
-[UIDraggingSessionConfiguration set_initialCentroid:];
-[UIDraggingSessionConfiguration supportsSystemDrag];
-[UIDraggingSessionConfiguration touchIDs];
-[UIDraggingSessionConfiguration wantsElasticEffects];
-[UIDraggingSessionConfiguration wantsPresentationUpdates];
```
