# `SBTouchRegionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutObserver`, `PTSettingsKeyObserver`
- 15 instance variables, 8 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"SBBackBoardServicesInterface" _queue_bksInterface;
@"FBSDisplayLayoutMonitor" _queue_displayLayoutMonitor;
@"SBMedusa1oSettings" _medusaSettings;
@"SBScreenSharingOverlayUISettings" _screenSharingSettings;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _queue_rootWindowTransform;
d _queue_touchRegionBuffer;
d _queue_edgeTouchRegionBuffer;
@"NSMutableDictionary" _queue_classicLetterboxInnerFramesByIdentifier;
@"NSMutableDictionary" _queue_classicLetterboxRegistrationIdentifiersBySceneIdentifier;
@"NSMutableDictionary" _queue_exclusiveBannerFramesByDisplay;
@"NSMutableDictionary" _queue_exclusivePIPFramesByDisplay;
@"NSMutableDictionary" _queue_lastLayoutByDisplay;
@"NSMutableDictionary" _queue_lastPublishedRegionsByDisplay;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _rootWindowTransform;
```

## Properties

```
@property (T@"FBSDisplayLayoutMonitor",&,N) displayLayoutMonitor;
@property (Td,R,N) touchRegionBuffer;
@property (Td,R,N) edgeTouchRegionBuffer;
@property (T{CGAffineTransform=dddddd},N,V_rootWindowTransform) rootWindowTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTouchRegionManager sharedInstance];
```

## Instance methods

```
-[SBTouchRegionManager init];
-[SBTouchRegionManager dealloc];
-[SBTouchRegionManager settings:changedValueForKey:];
-[SBTouchRegionManager layoutMonitor:didUpdateDisplayLayout:withContext:];
-[SBTouchRegionManager setDisplayLayoutMonitor:];
-[SBTouchRegionManager displayLayoutMonitor];
-[SBTouchRegionManager rootWindowTransform];
-[SBTouchRegionManager setRootWindowTransform:];
-[SBTouchRegionManager _queue_handleButterflyUILayout:];
-[SBTouchRegionManager _updateHitTestRegionsForLayout:];
-[SBTouchRegionManager _initWithBKSInterface:displayLayoutMonitor:];
-[SBTouchRegionManager _invalidateClassicLetterboxRegistration:forSceneIdentifier:];
-[SBTouchRegionManager _queue_butterflyHitTestRegionsForLayout:];
-[SBTouchRegionManager _queue_calculateBorderHitTestRegionsWithDisplayLayout:];
-[SBTouchRegionManager _queue_calculateHitTestRegionsFromTiledSceneRects:];
-[SBTouchRegionManager _queue_calculateTouchRectsFromTiledSceneRects:];
-[SBTouchRegionManager _queue_classicLetterboxHitTestRegionForLayout:innerFrame:clippedToWindowRect:];
-[SBTouchRegionManager _queue_classicLetterboxInnerFrameForElement:];
-[SBTouchRegionManager _queue_displayLayoutDidUpdate:];
-[SBTouchRegionManager _queue_displayLayoutDidUpdate:chamoisEnabled:];
-[SBTouchRegionManager _queue_displayLayoutDidUpdate:chamoisEnabled:butterflyEnabled:];
-[SBTouchRegionManager _queue_exclusiveBannerHitTestRegionForLayout:];
-[SBTouchRegionManager _queue_exclusivePictureInPictureHitTestRegionForLayout:];
-[SBTouchRegionManager _queue_floatingHitTestRegionForLayout:elementRect:];
-[SBTouchRegionManager _queue_fullscreenHitTestRegionForLayout:];
-[SBTouchRegionManager _queue_handleFlexibleWindowingUILayout:];
-[SBTouchRegionManager _queue_handleMedusaUILayout:];
-[SBTouchRegionManager _queue_hitTestRectForElement:layout:];
-[SBTouchRegionManager _queue_hitTestRegionTransformWithDisplayLayout:];
-[SBTouchRegionManager _queue_layoutHasClassicLetterboxedElement:];
-[SBTouchRegionManager _queue_setHitTestRegions:forLayout:];
-[SBTouchRegionManager _queue_shouldConsiderElementFullScreenModal:];
-[SBTouchRegionManager _queue_transformHitTestRegions:withDisplayLayout:];
-[SBTouchRegionManager _queue_transformRegionsIfNeeded:layout:];
-[SBTouchRegionManager _queue_updateHitTestRegionsForKnownLayouts];
-[SBTouchRegionManager debug_lastPublishedRegionsByDisplay];
-[SBTouchRegionManager edgeTouchRegionBuffer];
-[SBTouchRegionManager registerClassicLetterboxInnerFrame:forSceneIdentifier:];
-[SBTouchRegionManager setEdgeTouchRegionBuffer:];
-[SBTouchRegionManager setExclusiveBannerFrame:forDisplayIdentifier:];
-[SBTouchRegionManager setExclusivePictureInPictureFrame:forDisplayIdentifier:];
-[SBTouchRegionManager setTouchRegionBuffer:];
-[SBTouchRegionManager touchRegionBuffer];
```
