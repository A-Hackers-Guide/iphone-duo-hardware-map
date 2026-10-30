# `SBDisplayHasBlankedNotificationPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightCoordinatorObserver`, `SBWindowSceneAttachmentObserving`
- 5 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightCoordinator" _backlightCoordinator;
B _hasPostedState;
B _lastPostedBlanked;
@"NSMapTable" _displayUUIDsByWindowScene;
@"NSSet" _lastSuppressedDisplayUUIDs;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayHasBlankedNotificationPolicy windowSceneDidDisconnect:];
-[SBDisplayHasBlankedNotificationPolicy dealloc];
-[SBDisplayHasBlankedNotificationPolicy backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBDisplayHasBlankedNotificationPolicy windowSceneDidConnect:];
-[SBDisplayHasBlankedNotificationPolicy backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBDisplayHasBlankedNotificationPolicy _postHasBlankedScreenState:];
-[SBDisplayHasBlankedNotificationPolicy _updateForAggregateBacklightState:];
-[SBDisplayHasBlankedNotificationPolicy _updateSuppressedDisplays];
-[SBDisplayHasBlankedNotificationPolicy initWithBacklightCoordinator:];
```
