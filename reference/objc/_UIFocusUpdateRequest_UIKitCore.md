# `_UIFocusUpdateRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusUpdateRequesting`, `NSCopying`
- 10 instance variables, 19 properties, 32 instance methods, 1 class methods

## Instance variables

```
B _scrollIfNecessary;
B _allowsDeferral;
B _isFocusRemovalRequest;
B _resetsUpdateThrottle;
B _allowsFocusingCurrentItem;
B _allowsOverridingPreferedFocusEnvironments;
B _shouldPlayFocusSound;
@"<UIFocusEnvironment>" _destinationEnvironment;
@"UIFocusSystem" _focusSystem;
@"<UIFocusEnvironment>" _environment;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",R,W,N,V_destinationEnvironment) destinationEnvironment;
@property (TB,R,N,V_isFocusRemovalRequest) isFocusRemovalRequest;
@property (TB,N,V_resetsUpdateThrottle) resetsUpdateThrottle;
@property (TB,N,V_allowsFocusingCurrentItem) allowsFocusingCurrentItem;
@property (TB,N,V_allowsOverridingPreferedFocusEnvironments) allowsOverridingPreferedFocusEnvironments;
@property (TB,N,V_shouldPlayFocusSound) shouldPlayFocusSound;
@property (T@"<UIFocusEnvironment>",R,W,N,V_environment) environment;
@property (TB,N,V_allowsDeferral) allowsDeferral;
@property (TB,N,GshouldScrollIfNecessary,V_scrollIfNecessary) scrollIfNecessary;
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (TB,R,N,GisMovementRequest) movementRequest;
@property (TB,R,N) shouldPerformHapticFeedback;
@property (TB,R,N) requiresNextFocusedItem;
@property (TB,R,N) requiresEnvironmentValidation;
@property (T@"_UIFocusInputDeviceInfo",R,N) inputDeviceInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFocusUpdateRequest requestForRemovingFocusInFocusSystem:];
```

## Instance methods

```
-[_UIFocusUpdateRequest initWithEnvironment:];
-[_UIFocusUpdateRequest init];
-[_UIFocusUpdateRequest inputDeviceInfo];
-[_UIFocusUpdateRequest focusSystem];
-[_UIFocusUpdateRequest copyWithZone:];
-[_UIFocusUpdateRequest environment];
-[_UIFocusUpdateRequest allowsDeferral];
-[_UIFocusUpdateRequest allowsFocusingCurrentItem];
-[_UIFocusUpdateRequest allowsOverridingPreferedFocusEnvironments];
-[_UIFocusUpdateRequest cacheCurrentFocusSystem];
-[_UIFocusUpdateRequest canMergeWithRequest:];
-[_UIFocusUpdateRequest destinationEnvironment];
-[_UIFocusUpdateRequest initWithFocusSystem:environment:];
-[_UIFocusUpdateRequest initWithFocusSystem:environment:destinationEnvironment:];
-[_UIFocusUpdateRequest isFocusRemovalRequest];
-[_UIFocusUpdateRequest isMovementRequest];
-[_UIFocusUpdateRequest isValidInFocusSystem:];
-[_UIFocusUpdateRequest requestByMergingWithRequest:];
-[_UIFocusUpdateRequest requestByRedirectingRequestToEnvironment:];
-[_UIFocusUpdateRequest requestByRedirectingRequestToNextContainerEnvironment];
-[_UIFocusUpdateRequest requiresEnvironmentValidation];
-[_UIFocusUpdateRequest requiresNextFocusedItem];
-[_UIFocusUpdateRequest resetsUpdateThrottle];
-[_UIFocusUpdateRequest setAllowsDeferral:];
-[_UIFocusUpdateRequest setAllowsFocusingCurrentItem:];
-[_UIFocusUpdateRequest setAllowsOverridingPreferedFocusEnvironments:];
-[_UIFocusUpdateRequest setResetsUpdateThrottle:];
-[_UIFocusUpdateRequest setScrollIfNecessary:];
-[_UIFocusUpdateRequest setShouldPlayFocusSound:];
-[_UIFocusUpdateRequest shouldPerformHapticFeedback];
-[_UIFocusUpdateRequest shouldPlayFocusSound];
-[_UIFocusUpdateRequest shouldScrollIfNecessary];
```
