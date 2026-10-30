# `BKTouchServiceClientManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_clients;
@"NSDictionary" _lock_sceneHostSettingsByContextID;
@"NSDictionary" _lock_contextIDToCategory;
@"NSMutableDictionary" _lock_contextIDsToFilterBySenderID;
@"NSDictionary" _lock_contextIDsToFilterPerStimulus;
```

## Instance methods

```
-[BKTouchServiceClientManager init];
-[BKTouchServiceClientManager _lock_updateContextIDCategoryMap];
-[BKTouchServiceClientManager _lock_updateHitTestFilterParameters];
-[BKTouchServiceClientManager _lock_updateSceneHostSettings];
```
