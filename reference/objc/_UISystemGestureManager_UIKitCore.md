# `_UISystemGestureManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `FBSDisplayObserving`
- 3 instance variables, 4 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _displayIdentityToManagerMap;
@"NSMapTable" _systemShellManagedDisplayIdentityToInvalidatableMap;
@"FBSDisplayMonitor" _displayMonitor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISystemGestureManager sharedInstance];
+[_UISystemGestureManager _cancelTouchesWithIdentifiers:forDisplayWithIdentity:];
+[_UISystemGestureManager _sharedInstanceIfExists];
```

## Instance methods

```
-[_UISystemGestureManager init];
-[_UISystemGestureManager dealloc];
-[_UISystemGestureManager description];
-[_UISystemGestureManager displayMonitor:willDisconnectIdentity:];
-[_UISystemGestureManager _displayIdentityForTrackingGestureManagers:];
-[_UISystemGestureManager _displayRequiresClientManagement:];
-[_UISystemGestureManager _systemGestureManagerForDisplayWithIdentityCreatingIfNeeded:];
-[_UISystemGestureManager addGestureRecognizer:recognitionEvent:toDisplayWithIdentity:];
-[_UISystemGestureManager addGestureRecognizer:toDisplayWithIdentity:];
-[_UISystemGestureManager allowGestureRecognizersOnDisplayWithIdentity:];
-[_UISystemGestureManager clearTransformFromDisplayWithIdentity:];
-[_UISystemGestureManager gestureRecognizersAllowedOnDisplayWithIdentity:];
-[_UISystemGestureManager removeGestureRecognizer:fromDisplayWithIdentity:];
-[_UISystemGestureManager setTransform:onDisplayWithIdentity:];
-[_UISystemGestureManager windowForSystemGesturesForDisplayWithIdentity:];
```
