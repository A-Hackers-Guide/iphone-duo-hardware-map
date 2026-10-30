# `_UIFocusMovementRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusUpdateRequesting`
- 7 instance variables, 20 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _shouldPerformHapticFeedback;
B _overridesDeferredFocusUpdate;
@"UIFocusSystem" _focusSystem;
@"_UIFocusInputDeviceInfo" _inputDeviceInfo;
@"_UIFocusItemInfo" _focusedItemInfo;
@"_UIFocusMovementInfo" _movementInfo;
@"_UIFocusSearchInfo" _searchInfo;
```

## Properties

```
@property (T@"_UIFocusMovementRequest",R,N) fallbackRequest;
@property (T@"_UIFocusItemInfo",&,N,V_focusedItemInfo) focusedItemInfo;
@property (T@"_UIFocusMovementInfo",&,N,V_movementInfo) movementInfo;
@property (T@"_UIFocusInputDeviceInfo",&,N,V_inputDeviceInfo) inputDeviceInfo;
@property (T@"_UIFocusSearchInfo",&,N,V_searchInfo) searchInfo;
@property (TB,N,V_shouldPerformHapticFeedback) shouldPerformHapticFeedback;
@property (TB,N,V_overridesDeferredFocusUpdate) overridesDeferredFocusUpdate;
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (TB,R,N,GisMovementRequest) movementRequest;
@property (TB,R,N,GshouldScrollIfNecessary) scrollIfNecessary;
@property (TB,R,N) shouldPlayFocusSound;
@property (TB,R,N) requiresNextFocusedItem;
@property (TB,R,N) requiresEnvironmentValidation;
@property (TB,R,N) allowsFocusingCurrentItem;
@property (TB,R,N) allowsDeferral;
@property (TB,R,N) allowsOverridingPreferedFocusEnvironments;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusMovementRequest init];
-[_UIFocusMovementRequest inputDeviceInfo];
-[_UIFocusMovementRequest focusSystem];
-[_UIFocusMovementRequest fallbackRequest];
-[_UIFocusMovementRequest focusedItemInfo];
-[_UIFocusMovementRequest setShouldPerformHapticFeedback:];
-[_UIFocusMovementRequest _requestByRedirectingRequestToFocusSystem:];
-[_UIFocusMovementRequest allowsDeferral];
-[_UIFocusMovementRequest allowsFocusingCurrentItem];
-[_UIFocusMovementRequest allowsOverridingPreferedFocusEnvironments];
-[_UIFocusMovementRequest initWithFocusSystem:];
-[_UIFocusMovementRequest isMovementRequest];
-[_UIFocusMovementRequest movementInfo];
-[_UIFocusMovementRequest overridesDeferredFocusUpdate];
-[_UIFocusMovementRequest requiresEnvironmentValidation];
-[_UIFocusMovementRequest requiresNextFocusedItem];
-[_UIFocusMovementRequest searchInfo];
-[_UIFocusMovementRequest setFocusedItemInfo:];
-[_UIFocusMovementRequest setInputDeviceInfo:];
-[_UIFocusMovementRequest setMovementInfo:];
-[_UIFocusMovementRequest setOverridesDeferredFocusUpdate:];
-[_UIFocusMovementRequest setSearchInfo:];
-[_UIFocusMovementRequest shouldPerformHapticFeedback];
-[_UIFocusMovementRequest shouldPlayFocusSound];
-[_UIFocusMovementRequest shouldScrollIfNecessary];
```
