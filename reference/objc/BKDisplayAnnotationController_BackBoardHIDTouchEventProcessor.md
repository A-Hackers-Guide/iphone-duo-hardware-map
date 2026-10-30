# `BKDisplayAnnotationController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKOrientationObserver`, `BSInvalidatable`, `BKCADisplayDiffObserver`
- 12 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"BKDisplayAnnotationDisplayController" _displayController;
@"<BSInvalidatable>" _displayObserver;
@"<BSInvalidatable>" _orientationObserver;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _lock_externalReferenceCount;
@"NSMutableArray" _annotations;
@"BKNamespaceNode" _rootNode;
@"CADisplay" _display;
@"CAContext" _context;
@"CALayer" _rootLayer;
@"CALayer" _transformLayer;
@"CALayer" _referenceSpaceLayer;
```

## Properties

```
@property (T@"CADisplay",&,N,V_display) display;
@property (T@"CAContext",&,N,V_context) context;
@property (T@"CALayer",&,N,V_rootLayer) rootLayer;
@property (T@"CALayer",&,N,V_transformLayer) transformLayer;
@property (T@"CALayer",&,N,V_referenceSpaceLayer) referenceSpaceLayer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKDisplayAnnotationController annotationControllerForDisplay:displayRenderSpace:orientationProvider:];
```

## Instance methods

```
-[BKDisplayAnnotationController setDisplay:];
-[BKDisplayAnnotationController display];
-[BKDisplayAnnotationController rootLayer];
-[BKDisplayAnnotationController invalidate];
-[BKDisplayAnnotationController setContext:];
-[BKDisplayAnnotationController context];
-[BKDisplayAnnotationController _lock_invalidate];
-[BKDisplayAnnotationController setRootLayer:];
-[BKDisplayAnnotationController monitor:displayDidBecomeActive:];
-[BKDisplayAnnotationController _configureReferenceSpaceLayerTransformWithScale:];
-[BKDisplayAnnotationController _lock_CATransaction:];
-[BKDisplayAnnotationController _lock_locationDidChanges];
-[BKDisplayAnnotationController _lock_removeAnnotation:];
-[BKDisplayAnnotationController _lock_setupLayerTree];
-[BKDisplayAnnotationController _lock_supernodeForRenderingAtKeyPath:];
-[BKDisplayAnnotationController _lock_tearDownLayerTree];
-[BKDisplayAnnotationController _lock_updateLayerTree];
-[BKDisplayAnnotationController allAnnotationsForKeyPath:];
-[BKDisplayAnnotationController annotationForKeyPath:];
-[BKDisplayAnnotationController monitor:activeDisplayPropertiesDidChange:];
-[BKDisplayAnnotationController monitor:displayDidBecomeInactive:];
-[BKDisplayAnnotationController orientationProvider:deviceOrientationMayHaveChanged:changeSource:isDeviceOrientationLocked:];
-[BKDisplayAnnotationController performSynchronized:];
-[BKDisplayAnnotationController performSynchronizedWithCATransaction:];
-[BKDisplayAnnotationController referenceSpaceLayer];
-[BKDisplayAnnotationController removeAnnotationsForKeyPath:];
-[BKDisplayAnnotationController removeAnnotationsForKeyPath:afterDelay:queue:];
-[BKDisplayAnnotationController setAnnotation:forKeyPath:];
-[BKDisplayAnnotationController setReferenceSpaceLayer:];
-[BKDisplayAnnotationController setTransformLayer:];
-[BKDisplayAnnotationController transformLayer];
```
