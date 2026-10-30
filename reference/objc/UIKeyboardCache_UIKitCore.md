# `UIKeyboardCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"TIImageCacheClient" _store;
@"NSSet" _layouts;
@"NSMutableSet" _activeRenderers;
d _persistenceDeferredUntil;
@"_UIActionWhenIdle" _idleAction;
```

## Properties

```
@property (T@"_UIActionWhenIdle",&,N,V_idleAction) idleAction;
```

## Class methods

```
+[UIKeyboardCache sharedInstance];
+[UIKeyboardCache enabled];
+[UIKeyboardCache enabledForTraitCollection:];
```

## Instance methods

```
-[UIKeyboardCache init];
-[UIKeyboardCache idleAction];
-[UIKeyboardCache dealloc];
-[UIKeyboardCache setIdleAction:];
-[UIKeyboardCache purge];
-[UIKeyboardCache _didIdle];
-[UIKeyboardCache _didIdleAndShouldWait];
-[UIKeyboardCache _isPersistenceDeferred];
-[UIKeyboardCache cachedCompositeImageForCacheKeys:fromLayout:opacities:];
-[UIKeyboardCache cachedImageForKey:fromLayout:];
-[UIKeyboardCache cachedImageForKey:fromLayout:traitCollection:];
-[UIKeyboardCache clearNonPersistentCache];
-[UIKeyboardCache commitTransaction];
-[UIKeyboardCache decrementExpectedRender:];
-[UIKeyboardCache deferPersistenceForTransitionFrame];
-[UIKeyboardCache displayImagesForView:fromLayout:imageFlags:];
-[UIKeyboardCache drawCachedImage:alpha:inContext:];
-[UIKeyboardCache endPersistenceDeferral];
-[UIKeyboardCache handleLocaleChange:];
-[UIKeyboardCache incrementExpectedRender:];
-[UIKeyboardCache uniqueLayoutsFromInputModes:];
-[UIKeyboardCache updateCacheForInputModes:];
```
